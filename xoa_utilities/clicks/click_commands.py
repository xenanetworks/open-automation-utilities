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
from ..clis import format_error, format_tester_status
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
    try:
        result = await xoa_utils.main(args=args, standalone_mode=False, obj=context)
        if isinstance(result, int):
            result = context.get_error()
    except ac.UsageError as error:
        result = format_error(error)
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
    Connect to a tester for the current session.

        DEVICE TEXT: Specifies the chassis address for connection. You can specify the IP addresses in IPv4 format, or a host name, e.g. 10.10.10.10 or demo.xenanetworks.com\n

        USERNAME TEXT: Specifies the name of the user, default to 'xena'.\n

    """
    storage: CmdContext = context.obj
    real_port_list = [i.strip() for i in ports.split(",")] if ports else []
    tester = await L23Tester(device, username, password, tcp, debug=True)
    con_info = f"{device}:{tcp}"
    storage.set_current_tester(username, con_info, tester)
    port_dic = {}
    count = 0
    first_id = ""
    for id_str in real_port_list:
        this_port_dic = storage.obtain_physical_ports(id_str)
        port_dic.update(this_port_dic)
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
        storage.set_current_port_str(first_id)
    if force or reset:
        await asyncio.sleep(3)
        # status will change when you reserve_port or reset_port, need to wait
    return format_tester_status(
        tester.info.serial_number, con_info, username, first_id, port_dic
    )


# # --------------------------
# # command: exit
# # --------------------------
# @xoa_utils.command(cls=cb.XenaCommand)
# @ac.option(
#     "--reset/--no-reset",
#     is_flag=True,
#     help="Removes all port configurations of the reserved ports, "
#     "default to --reset.\n",
#     default=True,
# )
# @ac.option(
#     "--release/--no-release",
#     is_flag=True,
#     help="Determines whether the ports will be released before exiting, "
#     "default to --release.\n",
#     default=True,
# )
# @try_wrapper(False)
# async def exit(reset: bool, release: bool) -> None:
#     """
#     Exit by terminating port reservations, disconnecting from the chassis, releasing system resources, and removing the specified port configurations.\n

#     """
#     for port_id, port_obj in tp_storage.ports:
#         if reset:
#             await mgmt_utils.reset_port(port_obj)
#         if release:
#             await mgmt_utils.free_port(port_obj)
#         tp_storage.remove_port(port_id)

#     tp_storage.clean_working_port_id()
#     return None


# # --------------------------
# # command: port
# # --------------------------
# @xoa_utils.command(cls=cb.XenaCommand)
# @ac.argument(
#     "port",
#     type=ac.STRING,
# )
# @ac.option(
#     "--reset/--no-reset",
#     is_flag=True,
#     help="Removes all port configurations of the ports, " "default to --no-reset.\n",
#     default=False,
# )
# @ac.option(
#     "--force/--no-force",
#     is_flag=True,
#     help="Breaks port locks established by another user, aka. force "
#     "reservation, default to --force.\n",
#     default=True,
# )
# @try_wrapper(False)
# async def port(port: str, reset: bool, force: bool):
#     """
#     Switch the working port. If the port is not yet reserved, reserve the port. Update the working port in the cache.

#         PORT TEXT: Specifies the port on the specified device host. Specify a port using the format slot/port, e.g. 0/0\n

#     """
#     try:
#         tp_storage.get_reserved_port(port)
#     except NoSuchPortError:
#         port_dic = tp_storage.obtain_physical_ports(port)
#         for port_id, port_obj in port_dic.items():
#             if force:
#                 await mgmt_utils.reserve_port(port_obj, force)
#             if reset:
#                 await mgmt_utils.reset_port(port_obj)
#             tp_storage.store_port(port_id, port_obj)
#     tp_storage.update_working_port_id(port)
#     return None


# # --------------------------
# # command: show_ports
# # --------------------------
# @xoa_utils.command(cls=cb.XenaCommand)
# @try_wrapper(True)
# async def ports() -> str:
#     """
#     List all the ports under control.\n

#     """
#     return ",".join((tp_storage.list_ports()))


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


# # --------------------------
# # command: recovery
# # --------------------------
# @xoa_utils.command(cls=cb.XenaCommand)
# @ac.option(
#     "--on/--off",
#     is_flag=True,
#     help="Should the port automatically does link recovery, " "default to --off.\n",
#     default=False,
# )
# @try_wrapper(False)
# async def recovery(on: bool) -> None:
#     """
#     Enable/disable link recovery on the specified port. If on, the port will keep trying ANLT when no link-up signal is detected after five seconds of waiting.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     await anlt_utils.link_recovery(port_obj, on)
#     return None


# # --------------------------
# # command: status
# # --------------------------
# @xoa_utils.command(cls=cb.XenaCommand)
# async def status() -> str:
#     """
#     Show the overview of ANLT status of the port.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     status = await anlt_utils.status(port_obj)
#     port_id = list(status.keys())[list(status.values()).index(port_obj)]
#     return f"Port {port_id}\nAuto-negotiation        : {status['autoneg_enabled']}\nLink training           : {status['link_training_mode']}\nLink training timeout   : {status['link_training_timeout']}\nLink recovery           : {status['link_recovery']}\n"


# # --------------------------
# # command: an
# # --------------------------
# @xoa_utils.group(cls=cb.XenaGroup)
# def an():
#     """
#     To enter auto-negotiation context.\n

#     """


# # **************************
# # Type: Config
# # **************************
# # **************************
# # sub-command: an config
# # **************************
# @an.command(cls=cb.XenaGroup)
# @ac.option(
#     "--on/--off",
#     is_flag=True,
#     help="Should do auto-negotiation be on the working port, " "default to --on.\n",
#     default=True,
# )
# @ac.option(
#     "--loopback/--no-loopback",
#     is_flag=True,
#     help="Should loopback be allowed in auto-negotiation, "
#     "default to --no-loopback.\n",
#     default=False,
# )
# @try_wrapper(False)
# async def an_config(enable: bool, loopback: bool) -> None:
#     """
#     Configure auto-negotiation for the working port.\n

#     """
#     # port_obj = tp_storage.get_working_port()
#     # await anlt_utils.autoneg_config(port_obj, enable, loopback)
#     tp_storage.an_allow_loopback = loopback
#     tp_storage.should_do_an = enable
#     return None


# # **************************
# # Type: Statistics
# # **************************
# # **************************
# # sub-command: an status
# # **************************
# @an.command(cls=cb.XenaGroup)
# async def an_status() -> str:
#     """
#     Show the auto-negotiation status.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     status = await anlt_utils.autoneg_status(port_obj)
#     return status
#     # TODO: need to beautify the status output


# # **************************
# # sub-command: an log
# # **************************
# @an.command(cls=cb.XenaCommand)
# async def an_log() -> str:
#     """
#     Show the auto-negotiation log trace.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     log = await anlt_utils.autoneg_log(port_obj)
#     return log
#     # TODO: need to beautify the log message output


# # --------------------------
# # command: lt
# # --------------------------
# @xoa_utils.group(cls=cb.XenaGroup)
# def lt():
#     """
#     To enter link training context.\n

#     """


# # **************************
# # Type: Config
# # **************************
# # **************************
# # sub-command: lt config
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.option(
#     "--on/--off",
#     is_flag=True,
#     help="Should link training be enabled on the working port, " "default to --on.\n",
#     default=True,
# )
# @ac.option(
#     "--mode",
#     type=ac.STRING,
#     help="The mode for link training on the working port, "
#     "allowed values: interactive | auto "
#     "default to interactive.\n",
#     default="interactive",
# )
# @ac.option(
#     "--preset0/--no-preset0",
#     "-p/ ",
#     is_flag=True,
#     help="Should the preset0 (out-of-sync) use existing tap values or standard values, "
#     "default to --no-preset0.\n",
#     default=False,
# )
# @try_wrapper(False)
# async def lt_config(on: bool, mode: str, preset0: bool) -> None:
#     """
#     Configures link training on the working port.\n

#     """
#     # port_obj = tp_storage.get_working_port()
#     # await anlt_utils.lt_config(port_obj, mode, preset0, timeout)
#     tp_storage.should_do_lt = on
#     tp_storage.lt_preset0_std = not preset0
#     tp_storage.lt_interactive = True if mode == "interactive" else False

#     return None


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


# # **************************
# # Type: Control
# # **************************
# # **************************
# # sub-command: lt inc
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.argument("emphasis", type=ac.STRING)
# @try_wrapper(False)
# async def lt_inc(lane: int, emphasis: str) -> str:
#     """
#     Tells the remote link training partner to increase its emphasis register value by 1 bit.

#         LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
#         EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n

#     """
#     port_obj = tp_storage.get_working_port()
#     try:
#         validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
#         await anlt_utils.lt_coeff_inc(port_obj, lane, emphasis)
#         return f""
#     except NotInChoicesError as e:
#         return e.msg


# # **************************
# # sub-command: lt dec
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.argument("emphasis", type=ac.STRING)
# @try_wrapper(False)
# async def lt_dec(lane: int, emphasis: str) -> str:
#     """
#     Tells the remote link training partner to decrease its emphasis register value by 1 bit.

#         LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
#         EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n

#     """
#     port_obj = tp_storage.get_working_port()
#     try:
#         validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
#         await anlt_utils.lt_coeff_dec(port_obj, lane, emphasis)
#         return f""
#     except NotInChoicesError as e:
#         return e.msg


# # **************************
# # sub-command: lt preset
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.argument("preset", type=ac.INT)
# @try_wrapper(False)
# async def lt_preset(lane: int, preset: int) -> str:
#     """
#     Ask the remote port to use the preset of the specified lane.

#         LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
#         PRESET INT: Specifies the preset index. Allowed values: 1, 2, 3, 4, 5.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     if preset in range(1, 5):
#         await anlt_utils.lt_preset(port_obj, lane, preset)
#         return f""
#     else:
#         return f"Preset {preset} is not in the choices (1, 2, 3, 4, 5)!"


# # **************************
# # sub-command: lt encoding
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.argument("encoding", type=ac.STRING)
# @try_wrapper(False)
# async def lt_encoding(lane: int, encoding: str) -> str:
#     """
#     Set the port to use the specified encoding in link training of the specified lane.

#         LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
#         ENCODING TEXT: Specifies the encoding. Allowed values: nrz/pam2, pam4, pam4pre\n

#     """
#     port_obj = tp_storage.get_working_port()
#     try:
#         validate_choices(encoding, ["nrz", "pam2", "pam4", "pam4pre"])
#         await anlt_utils.lt_encoding(port_obj, lane, encoding)
#         return f""
#     except NotInChoicesError as e:
#         return e.msg


# # **************************
# # sub-command: lt trained
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# async def lt_trained(lane: int) -> str:
#     """
#     Announce that the specified lane is trained.

#         LANE INT: The lane index for the announcement.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     await anlt_utils.lt_trained(port_obj, lane)
#     return ""


# # **************************
# # sub-command: lt log
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.option(
#     "--live/--no-live",
#     "-l/ ",
#     is_flag=True,
#     help="Should show the live LT log , " "default to False. " "e.g. lt_log --live",
#     default=False,
# )
# async def lt_log(lane: int, live: bool) -> str:
#     """
#     Show the link training trace log for the specified lane.

#         LANE INT: The lane index.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     log = await anlt_utils.lt_log(port_obj, lane, live)
#     return log
#     # TODO: Needs to be implemented for display


# # **************************
# # sub-command: lt status
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# async def lt_status(lane: int) -> str:
#     """
#     Show the link training status of the specified lane.

#         LANE INT: The lane index for the announcement.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     status = await anlt_utils.lt_status(port_obj, lane)
#     return status
#     # TODO: Needs to be implemented for display


# # **************************
# # sub-command: txtapget
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# async def txtapget(lane: int) -> str:
#     """
#     Read the tap values of the specified lane of the local port.

#         LANE INT: The lane index to read tap values from.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     dict = await anlt_utils.txtap_get(port_obj, lane)
#     return dict
#     # TODO: Needs to be implemented for display


# # **************************
# # sub-command: txtapset
# # **************************
# @lt.command(cls=cb.XenaCommand)
# @ac.argument("lane", type=ac.INT)
# @ac.argument("pre3", type=ac.INT)
# @ac.argument("pre2", type=ac.INT)
# @ac.argument("pre1", type=ac.INT)
# @ac.argument("main", type=ac.INT)
# @ac.argument("post1", type=ac.INT)
# async def txtapset(
#     lane: int, pre3: int, pre2: int, pre1: int, main: int, post1: int
# ) -> str:
#     """
#     Write the tap values of the specified lane of the local port.

#         LANE INT: The lane index to read tap values from.\n
#         PRE3 INT: c(-3) value of the tap.\n
#         PRE2 INT: c(-2) value of the tap.\n
#         PRE1 INT: c(-1) value of the tap.\n
#         MAIN INT: c(0) value of the tap.\n
#         POST1 INT: c(+1) value of the tap.\n

#     """
#     port_obj = tp_storage.get_working_port()
#     dict = await anlt_utils.txtap_set(port_obj, lane, pre3, pre2, pre1, main, post1)
#     return dict
#     # TODO: Needs to be implemented for display
