from __future__ import annotations
import configparser
import os
import typing as t
import asyncclick as ac
import json
from functools import wraps
from exceptions import ConfigError, NotInChoicesError
from xoa_driver.exceptions import BadStatus


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


def try_wrapper(return_result: bool) -> t.Callable:
    def outer(func: t.Callable) -> t.Callable:
        @wraps(func)
        async def execute(*args: t.Any, **kw: dict[str, t.Any]) -> str:
            try:
                func_result = await func(*args, **kw)
                error = None
            except ConfigError as e:
                error = f"{e.name}: {e}"
            except BadStatus as e1:
                error = str(e1).split("\n")[0]
            result = {"status": 1 if error else 0, "response": error if error else None}
            if return_result:
                result["result"] = func_result
            return json.dumps(result, indent=2)

        return execute

    return outer


def validate_choices(input_str: str, choices: list[str]) -> None:
    if input_str not in choices:
        raise NotInChoicesError(input_str, choices)