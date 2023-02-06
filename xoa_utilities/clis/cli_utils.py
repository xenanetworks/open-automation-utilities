from __future__ import annotations
import configparser
import os
import typing as t
import asyncclick as ac
import json
from functools import wraps
from ..exceptions import ConfigError, NotInChoicesError
from xoa_driver.exceptions import BadStatus

if t.TYPE_CHECKING:
    from xoa_driver.ports import GenericL23Port
    from ..cmds.cmd_context import CmdContext


class ReadConfig:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.config = config
        self.connection_host = config["Connection"].get("host", "localhost")
        self.connection_port = int(config["Connection"].get("port", "5000"))
        self.connection_host_keys = config["Connection"].get(
            "sshkeypath", "~/.ssh/id_rsa"
        )
        self.hub_enabled = (
            True
            if str(config["Hub"].get("enable", "false")).lower() == "true"
            else False
        )
        self.hub_host = config["Hub"].get("host", "localhost")
        self.hub_port = int(config["Hub"].get("port", "10000"))
        self.hub_pid_path = config["Hub"].get("pid_path", "hub.pid")
        self.hub_pid = self._read_hub_pid()

    def _read_hub_pid(self) -> int:
        pid = 0
        if not os.path.isfile(self.hub_pid_path):
            try:
                os.unlink(self.hub_pid_path)
            except Exception:
                pass
            with open(self.hub_pid_path, "w"):
                pass
        with open(self.hub_pid_path, "r") as f:
            content = f.read().strip()
            try:
                pid = int(content)
            except ValueError:
                pass
        return pid


def run_coroutine_as_sync(coro: t.Coroutine) -> t.Any:
    while True:
        try:
            next(coro.__await__())
        except StopIteration as done:
            return done.value


def format_error(error: ac.UsageError) -> str:
    hint = ""
    result = ""
    if (
        error.ctx is not None
        and error.ctx.command.get_help_option(error.ctx) is not None
    ):
        hint = f"Try '{error.ctx.command_path} {error.ctx.help_option_names[0]}' for help.\n\n"
    if error.ctx is not None:
        result += f"{error.ctx.get_usage()}\n{hint}"
    result += f"Error: {error.format_message()}\n"
    result = result.replace("python -m entry", "")
    return result


def validate_choices(input_str: str, choices: list[str]) -> None:
    if input_str not in choices:
        raise NotInChoicesError(input_str, choices)


def _port_dic_status(current_id: str, port_dic: dict[str, GenericL23Port]) -> str:
    string = f"Port      Sync      Owner     \n"
    for name, port in port_dic.items():
        new_name = f"*{name}" if current_id == name else name
        owner = "You" if port.is_reserved_by_me() else "Others"
        sync_status = str(port.info.sync_status.name)
        string += f"{new_name:10s}{sync_status:10s}{owner:10s}\n"

    return string


def format_tester_status(storage: "CmdContext") -> str:
    serial_number = storage.retrieve_tester_serial()
    con_info = storage.retrieve_tester_con_info()
    username = storage.retrieve_tester_username()
    port_dic = storage.retrieve_ports()
    result_str = f"\nTester  :      {serial_number}\nConInfo :      {con_info}\nUsername:      {username}\n\n"
    result_str += _port_dic_status(
        storage.retrieve_port_str(), storage.retrieve_ports()
    )
    return result_str


def format_port_status(storage: "CmdContext") -> str:
    result_str = _port_dic_status(storage.retrieve_port_str(), storage.retrieve_ports())

    port_obj = storage.retrieve_port()
    an_status = "on"
    lt_status = "interactive"
    lt_timeout = "default"
    lt_recovery = "on"
    result_str += f"""
Port {storage.retrieve_port_str()}
Auto-negotiation        : {an_status}
Link training           : {lt_status}
Link training timeout   : {lt_timeout}
Link recovery           : {lt_recovery}
"""

    return result_str


def format_ports_status(storage: "CmdContext", all: bool) -> str:
    if all:
        port_dic = storage.get_all_ports()
    else:
        port_dic = storage.retrieve_ports()
    result_str = _port_dic_status(storage.retrieve_port_str(), port_dic)
    return result_str
