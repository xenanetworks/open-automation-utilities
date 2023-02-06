from __future__ import annotations
import asyncclick as ac
from . import click_backend as cb
from xoa_driver.hlfuncs import anlt as anlt_utils
from xoa_driver.hlfuncs import mgmt as mgmt_utils
from xoa_driver.testers import L23Tester, L47Tester, GenericAnyTester
from ..clis import validate_choices
from ..exceptions import *
import json
import typing as t
import asyncclick as ac
from ..clis import (
    format_error,
    format_tester_status,
    format_ports_status,
    format_an_status,
    format_status,
)
from ..cmds import CmdContext
from . import click_help as h
import asyncio


cs = {"help_option_names": ["-h", "--help"]}


@ac.group(cls=cb.XenaGroup)
def xoa_utils():
    pass


async def cmd_main(context: CmdContext, cmd_str: str) -> t.Any:
    context.clear_error()
    args = cmd_str.split()
    result = await xoa_utils.main(args=args, standalone_mode=False, obj=context)
    return result


# --------------------------
# command: connect
# --------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.argument("device", type=ac.STRING)
@ac.argument("username", type=ac.STRING)
@ac.option("-p", "--ports", type=ac.STRING, help=h.HELP_CONNECT_PORT_LIST, default="")
@ac.option("--reset/--no-reset", is_flag=True, help=h.HELP_CONNECT_RESET, default=True)
@ac.option("--force/--no-force", is_flag=True, help=h.HELP_CONNECT_FORCE, default=True)
@ac.option("-P", "--password", type=ac.STRING, help=h.HELP_CONNECT_PWD, default="xena")
@ac.option("-t", "--tcp", type=ac.INT, help=h.HELP_CONNECT_TCP_PORT, default=22606)
@ac.pass_context
async def connect(
    context: ac.Context,
    device: str,
    username: str,
    ports: str,
    reset: bool,
    force: bool,
    password: str,
    tcp: int,
) -> str:
    """
    To connect to a tester for the current session.

        DEVICE TEXT: Specifies the chassis address for connection. You can specify the IP addresses in IPv4 format, or a host name, e.g. 10.10.10.10 or demo.xenanetworks.com\n

        USERNAME TEXT: Specifies the name of the user, default to 'xena'.\n

    """
    storage: CmdContext = context.obj
    real_port_list = [i.strip() for i in ports.split(",")] if ports else []
    tester = await L23Tester(device, username, password, tcp, debug=True)
    con_info = f"{device}:{tcp}"
    storage.store_current_tester(username, con_info, tester)
    count = 0
    first_id = ""
    for id_str in real_port_list:
        this_port_dic = storage.obtain_physical_ports(id_str)
        for port_id, port_obj in this_port_dic.items():
            if force:
                await mgmt_utils.reserve_port(port_obj, force)
            if reset:
                await mgmt_utils.reset_port(port_obj)
            storage.store_port(port_id, port_obj)
            if count == 0:
                first_id = port_id
            count += 1

    if real_port_list:
        storage.store_current_port_str(first_id)
    if force or reset:
        await asyncio.sleep(3)
        # status will change when you reserve_port or reset_port, need to wait
    return format_tester_status(storage)


# --------------------------
# command: exit
# --------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.option("--reset/--no-reset", is_flag=True, help=h.HELP_CONNECT_RESET, default=True)
@ac.option(
    "--release/--no-release", is_flag=True, help=h.HELP_EXIT_RELEASE, default=True
)
@ac.pass_context
async def exit(context: ac.Context, reset: bool, release: bool) -> str:
    """
    To exit the session by terminating port reservations, disconnecting from the chassis, releasing system resources, and removing the specified port configurations. This command works in all context.
    """
    storage: CmdContext = context.obj
    for port_id, port_obj in storage.ports.copy().items():
        if reset:
            await mgmt_utils.reset_port(port_obj)
        if release:
            await mgmt_utils.free_port(port_obj)
        storage.remove_port(port_id)
    return ""


# --------------------------
# command: port
# --------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.option("--reset/--no-reset", is_flag=True, help=h.HELP_CONNECT_RESET, default=False)
@ac.option("--force/--no-force", is_flag=True, help=h.HELP_CONNECT_FORCE, default=True)
@ac.pass_context
async def port(context: ac.Context, port: str, reset: bool, force: bool) -> str:
    """
    Switch the working port. If the port is not yet reserved, reserve the port. Update the working port in the cache.

        PORT TEXT: Specifies the port on the specified device host. Specify a port using the format slot/port, e.g. 0/0\n
    """
    storage: CmdContext = context.obj
    try:
        storage.store_current_port_str(port)
    except NotInStoreError:
        port_dic = storage.obtain_physical_ports(port)
        for port_id, port_obj in port_dic.items():
            if force:
                await mgmt_utils.reserve_port(port_obj, force)
            if reset:
                await mgmt_utils.reset_port(port_obj)
            storage.store_port(port_id, port_obj)
            storage.store_current_port_str(port_id)
    if force or reset:
        await asyncio.sleep(3)
        # status will change when you reserve_port or reset_port, need to wait
    port_obj = storage.retrieve_port()
    port_id = storage.retrieve_port_str()
    status_dic = await anlt_utils.status(port_obj)
    return format_status(port_id, status_dic)


# --------------------------
# command: ports
# --------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.option("--all/--no-all", is_flag=True, help=h.HELP_PORTS_ALL, default=False)
@ac.pass_context
async def ports(context: ac.Context, all: bool) -> str:
    """
    To list all the ports reserved by the current session. This command works in all context.\n

    """
    storage: CmdContext = context.obj
    return format_ports_status(storage, all)


# # --------------------------
# # command: do_anlt
# # --------------------------
# @xoa_utils.command(cls=cb.XenaCommand)
# @try_wrapper(True)
# async def do_anlt() -> str:
#     """
#     Start autoneg and link training according the previous configuration.\n

#     """
#     port_obj = tp_storage.get_working_port()

#     should_an = tp_storage.should_do_an
#     should_lt = tp_storage.should_do_lt

#     return ",".join((tp_storage.list_ports()))

#     ## NOT FINISHED!!!!!!


# --------------------------
# command: recovery
# --------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.option("--on/--off", is_flag=True, help=h.HELP_RECOVERY_ON, default=False)
@ac.pass_context
async def recovery(context: ac.Context, on: bool) -> str:
    """
    Enable/disable link recovery on the specified port. If enable, the port will keep trying ANLT when no link-up signal is detected after five seconds of waiting.
    """
    storage: CmdContext = context.obj
    enable = "enable" if on else "disable"
    port_obj = storage.retrieve_port()
    await anlt_utils.link_recovery(port_obj, on)
    return f"Port {storage.retrieve_port_str()} link recovery: {enable}\n"


# --------------------------
# command: status
# --------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.pass_context
async def status(context: ac.Context) -> str:
    """
    Show the overview of ANLT status of the port.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    status_dic = await anlt_utils.status(port_obj)
    port_id = storage.retrieve_port_str()
    return format_status(port_id, status_dic)


# --------------------------
# command: an
# --------------------------
@xoa_utils.group(cls=cb.XenaGroup)
def an():
    """
    To enter auto-negotiation context.\n

    """


# **************************
# Type: Config
# **************************
# **************************
# sub-command: an config
# **************************
@an.command(cls=cb.XenaGroup)
@ac.option("--on/--off", is_flag=True, help=h.HELP_AN_CONFIG_ON, default=True)
@ac.option(
    "--loopback/--no-loopback",
    is_flag=True,
    help=h.HELP_AN_CONFIG_LOOPBACK,
    default=False,
)
@ac.pass_context
async def config(context: ac.Context, enable: bool, loopback: bool) -> str:
    """
    Configure auto-negotiation for the working port.\n

    """
    storage: CmdContext = context.obj
    on = "enable" if enable else "disable"
    storage.an_allow_loopback = loopback
    storage.should_do_an = enable
    return f"Port {storage.retrieve_port_str()} auto-negotiation:{on} loopback-allowed:{loopback}"


# **************************
# Type: Statistics
# **************************
# **************************
# sub-command: an status
# **************************
@an.command(cls=cb.XenaGroup)
@ac.pass_context
async def an_status(context: ac.Context) -> str:
    """
    Show the auto-negotiation status.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    status_dic = await anlt_utils.autoneg_status(port_obj)
    return format_an_status(status_dic)
    # TODO: need to beautify the status output


# **************************
# sub-command: an log
# **************************
@an.command(cls=cb.XenaCommand)
@ac.pass_context
async def log(context: ac.Context) -> str:
    """
    Show the auto-negotiation log trace.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    log = await anlt_utils.autoneg_log(port_obj)
    return log
    # TODO: need to beautify the log message output


# --------------------------
# command: lt
# --------------------------
@xoa_utils.group(cls=cb.XenaGroup)
def lt():
    """
    To enter link training context.\n

    """


# **************************
# Type: Config
# **************************
# **************************
# sub-command: lt config
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.option("--mode", type=ac.STRING, help=h.HELP_LT_CONFIG_MODE, default="interactive")
@ac.option("--on/--off", is_flag=True, help=h.HELP_LT_CONFIG_ON, default=True)
@ac.option(
    "--preset0/--no-preset0",
    "-p/ ",
    is_flag=True,
    help=h.HELP_LT_CONFIG_PRESET0,
    default=False,
)
@ac.pass_context
async def lt_config(context: ac.Context, mode: str, on: bool, preset0: bool) -> None:
    """
    To configure link training on the working port.\n

    """
    storage: CmdContext = context.obj
    storage.should_do_lt = on
    storage.lt_preset0_std = not preset0
    storage.lt_interactive = True if mode == "interactive" else False

    return None


# # **************************
# # sub-command: lt im
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.argument("encoding", type=ac.STRING)
# @try_wrapper(False)
# async def lt_im(lane: int, encoding: str) -> str:
#     """
#     Set the initial modulation for the specified lane.

#         LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
#         ENCODING TEXT: Specifies the initial modulation. Allowed values: nrz/pam2, pam4, pam4pre\n

#     """
#     try:
#         validate_choices(encoding, ["nrz", "pam2", "pam4", "pam4pre"])
#         tp_storage.lt_initial_mod.update({str(lane): "encoding"})
#         # await anlt_utils.lt_im(port_obj, lane, encoding)
#         return f""
#     except NotInChoicesError as e:
#         return e.msg


# **************************
# Type: Control
# **************************
# **************************
# sub-command: lt inc
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("emphasis", type=ac.STRING)
@ac.pass_context
async def lt_inc(context: ac.Context, lane: int, emphasis: str) -> str:
    """
    Tells the remote link training partner to increase its emphasis register value by 1 bit.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    try:
        validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
        await anlt_utils.lt_coeff_inc(port_obj, lane, emphasis)
        return f""
    except NotInChoicesError as e:
        return e.msg


# **************************
# sub-command: lt dec
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("emphasis", type=ac.STRING)
@ac.pass_context
async def lt_dec(context: ac.Context, lane: int, emphasis: str) -> str:
    """
    Tells the remote link training partner to decrease its emphasis register value by 1 bit.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
    await anlt_utils.lt_coeff_dec(port_obj, lane, emphasis)
    return f""


# **************************
# sub-command: lt preset
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("preset", type=ac.INT)
@ac.pass_context
async def lt_preset(context: ac.Context, lane: int, preset: int) -> str:
    """
    Ask the remote port to use the preset of the specified lane.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        PRESET INT: Specifies the preset index. Allowed values: 1, 2, 3, 4, 5.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    validate_choices(preset, range(1, 5))
    await anlt_utils.lt_preset(port_obj, lane, preset)


# **************************
# sub-command: lt encoding
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("encoding", type=ac.STRING)
@ac.pass_context
async def lt_encoding(context: ac.Context, lane: int, encoding: str) -> str:
    """
    Set the port to use the specified encoding in link training of the specified lane.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        ENCODING TEXT: Specifies the encoding. Allowed values: nrz/pam2, pam4, pam4pre\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    validate_choices(encoding, ["nrz", "pam2", "pam4", "pam4pre"])
    await anlt_utils.lt_encoding(port_obj, lane, encoding)


# **************************
# sub-command: lt trained
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_trained(context: ac.Context, lane: int) -> str:
    """
    Announce that the specified lane is trained.

        LANE INT: The lane index for the announcement.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.lt_trained(port_obj, lane)
    return ""


# **************************
# sub-command: lt log
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.option(
    "--live/--no-live",
    "-l/ ",
    is_flag=True,
    help="Should show the live LT log , " "default to False. " "e.g. lt_log --live",
    default=False,
)
@ac.pass_context
async def lt_log(context: ac.Context, lane: int, live: bool) -> str:
    """
    Show the link training trace log for the specified lane.

        LANE INT: The lane index.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    log = await anlt_utils.lt_log(port_obj, lane, live)
    return log
    # TODO: Needs to be implemented for display


# **************************
# sub-command: lt status
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_status(context: ac.Context, lane: int) -> str:
    """
    Show the link training status of the specified lane.

        LANE INT: The lane index for the announcement.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    status = await anlt_utils.lt_status(port_obj, lane)
    return status
    # TODO: Needs to be implemented for display


# **************************
# sub-command: txtapget
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def txtapget(context: ac.Context, lane: int) -> str:
    """
    Read the tap values of the specified lane of the local port.

        LANE INT: The lane index to read tap values from.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    dic = await anlt_utils.txtap_get(port_obj, lane)
    return dic
    # TODO: Needs to be implemented for display


# **************************
# sub-command: txtapset
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("pre3", type=ac.INT)
@ac.argument("pre2", type=ac.INT)
@ac.argument("pre1", type=ac.INT)
@ac.argument("main", type=ac.INT)
@ac.argument("post1", type=ac.INT)
@ac.pass_context
async def txtapset(
    context: ac.Context,
    lane: int,
    pre3: int,
    pre2: int,
    pre1: int,
    main: int,
    post1: int,
) -> str:
    """
    Write the tap values of the specified lane of the local port.

        LANE INT: The lane index to read tap values from.\n
        PRE3 INT: c(-3) value of the tap.\n
        PRE2 INT: c(-2) value of the tap.\n
        PRE1 INT: c(-1) value of the tap.\n
        MAIN INT: c(0) value of the tap.\n
        POST1 INT: c(+1) value of the tap.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    dic = await anlt_utils.txtap_set(port_obj, lane, pre3, pre2, pre1, main, post1)
    return dic
    # TODO: Needs to be implemented for display
