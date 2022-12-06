from __future__ import annotations
import asyncclick as ac
import click_backend as cb
import anlt_utils
from global_tester_port import tp_storage
from cli_utils import try_wrapper, validate_choices
from exceptions import CannotConvertError, NotSameLengthError

cs = {"help_option_names": ["-h", "--help"]}


@ac.group(cls=cb.XenaGroup)
def xena_cli():
    pass


@xena_cli.command(cls=cb.XenaCommand)
@ac.argument("device", type=ac.STRING)
@ac.argument(
    "username",
    type=ac.STRING,
)
@ac.option(
    "-p",
    "--port-list",
    type=ac.STRING,
    help="Specifies the ports on the specified device host, default to null. "
    "Specify a port using the format slot/port, no spaces between. "
    "e.g. --port_list 0/0,0/1,0/2,0/3\n",
    default="",
)
@ac.option(
    "-r",
    "--reset",
    type=ac.BOOL,
    help="Removes all port configurations of the ports in --port_list after"
    " reservation, default to true. Allowed values: true | false. "
    "e.g. --reset true",
    default=True,
)
@ac.option(
    "-k",
    "--break-lock",
    type=ac.BOOL,
    help="Breaks port locks established by another user, aka. force "
    "reservation, default to true. Allowed values: true | false. "
    "e.g. --break_locks true",
    default=True,
)
@ac.option(
    "-w",
    "--password",
    type=ac.STRING,
    help="The login password of the tester, default to xena. e.g. --password xena",
    default="xena",
)
@ac.option(
    "-t",
    "--tcp-port",
    type=ac.INT,
    help="The TCP port number on the chassis for the client to establish "
    "a session, default to 22606, e.g. --tcp-port 22606",
    default=22606,
)
@try_wrapper(False)
async def connect(
    device: str,
    username: str,
    port_list: str,
    password: str,
    tcp_port: int,
    reset: bool,
    break_lock: bool,
) -> None:
    """
    Connect to a tester for the current session.

        DEVICE TEXT: Specifies the chassis address for connection. You can specify the IP addresses in IPv4 format, or a host name. e.g. 10.10.10.10, demo.xenanetworks.com\n
        USERNAME TEXT: Specifies the name of the user, default to xena. Specifies the name of the user. e.g. peter, peter-parker\n

    """
    real_port_list = [i.strip() for i in port_list.split(",")] if port_list else []
    tester = await anlt_utils.connect("l23", device, username, password, tcp_port)
    tp_storage.store_tester(f"{device}:{tcp_port}", tester)
    for id_str in real_port_list:
        for port_id, port_obj in tp_storage.obtain_physical_ports(id_str).items():
            if break_lock:
                await anlt_utils.port_force_reserve(port_obj)
            if reset:
                await anlt_utils.port_reset(port_obj)
            tp_storage.store_port(port_id, port_obj)
    return None


@xena_cli.command(cls=cb.XenaCommand)
@ac.argument(
    "port-list",
    type=ac.STRING,
)
@ac.option(
    "-r",
    "--reset",
    type=ac.BOOL,
    help="Removes all port configurations of the ports in --port_list after"
    " reservation, default to true. Allowed values: true | false. "
    "e.g. --reset true",
    default=True,
)
@ac.option(
    "-k",
    "--break-lock",
    type=ac.BOOL,
    help="Breaks port locks established by another user, aka. force "
    "reservation, default to true. Allowed values: true | false. "
    "e.g. --break_locks true",
    default=True,
)
@try_wrapper(False)
async def reserve(port_list: str, reset: bool, break_lock: bool):
    """
    Reserve test resources.

        PORTS TEXT: Specifies the ports on the specified device host, default to null. Specify a port using the format slot/port, no spaces between. e.g. --port_list 0/0,0/1,0/2,0/3\n
    """
    real_port_list = [i.strip() for i in port_list.split(",")] if port_list else []
    for id_str in real_port_list:
        port_dic = tp_storage.obtain_physical_ports(id_str)
        for port_id, port_obj in port_dic.items():
            if break_lock:
                await anlt_utils.port_force_reserve(port_obj)
            if reset:
                await anlt_utils.port_reset(port_obj)
            tp_storage.store_port(port_id, port_obj)
    return None


@xena_cli.command(cls=cb.XenaCommand)
@ac.option(
    "-p",
    "--port-list",
    type=ac.STRING,
    help="Specifies the ports on the specified device host, default to null. "
    "Specify a port using the format slot/port, no spaces between. "
    "e.g. --port_list 0/0,0/1,0/2,0/3\n",
    default="",
)
@ac.option(
    "-r",
    "--reset",
    type=ac.BOOL,
    help="Removes all port configurations of the ports in --port_list after"
    " reservation, default to true. Allowed values: true | false. "
    "e.g. --reset true",
    default=True,
)
@ac.option(
    "-l",
    "--maintain-lock",
    type=ac.BOOL,
    help="Determines whether the ports will be released before exiting, "
    "default to false. Allowed values: true | false. "
    "e.g. --maintain_lock true",
    default=False,
)
@try_wrapper(False)
async def cleanup(port_list: str, reset: bool, maintain_lock: bool) -> None:
    """
    Cleans up by terminating port reservations, disconnecting from the chassis, releasing system resources, and removing the specified port configurations.
    """
    real_port_list = [i.strip() for i in port_list.split(",")] if port_list else []
    for port_id in real_port_list:
        port_obj = tp_storage.get_reserved_port(port_id)
        if not maintain_lock:
            await anlt_utils.port_release(port_obj)
        if reset:
            await anlt_utils.port_reset(port_obj)
        tp_storage.remove_port(port_id)
    return None


@xena_cli.command(cls=cb.XenaCommand)
@try_wrapper(True)
async def list_ports() -> str:
    """
    List all the ports under control.
    """
    return ",".join((tp_storage.list_ports()))


@xena_cli.group(cls=cb.XenaGroup)
def l1_config():
    """Configures and modifies an L1 port on a chassis."""


@l1_config.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.option(
    "-e",
    "--enable",
    type=ac.BOOL,
    help="Enable or disable auto-negotiation default to true. Allowed values: "
    "true | false. e.g. --enabled true",
)
@ac.argument(
    "-m",
    "allow_loopback",
    type=ac.BOOL,
    help="Specifies the list of modes for the lanes, default to false. "
    "Allowed values: true | false.\n",
)
@try_wrapper(False)
async def aneg(port: str, allow_loopback: bool, enable: bool) -> None:
    """
    Enable or disable auto-negotiation.

        PORT TEXT: Specifies the port on the specified device host. Specify a port using the format "slot/port". e.g. 0/0\n
    """
    port_obj = tp_storage.get_reserved_port(port)
    await anlt_utils.an_config(port_obj, allow_loopback, enable)
    return None


@l1_config.command(cls=cb.XenaCommand)
@ac.option(
    "-e",
    "--enable",
    type=ac.BOOL,
    help="Enable or disable link training, default to true. "
    "Allowed values: true | false. e.g. --enabled true.",
)
@ac.option(
    "-t",
    "--timeout",
    type=ac.BOOL,
    help="Link training with or without timeout, default to false. "
    "Allowed values: true | false e.g. --timeout false",
)
@ac.option(
    "-m",
    "--mode",
    type=ac.STRING,
    help="Link training mode, default to interactive. Allowed values: "
    "auto | interactive e.g. --mode interactive.",
)
@ac.option(
    "-r",
    "--link_recovery",
    type=ac.BOOL,
    help="Should the port do persistent link recovery, default to false. Allowed values: true | false. e.g. --link_recovery false.",
)
@try_wrapper(False)
async def lt(
    port: str, enable: bool, timeout: bool, mode: str, link_recovery: bool
) -> None:
    """
    Configures and modifies a port's layer-1 link-training settings.

        PORT TEXT: Specifies the port on the specified device host. Specify a port using the format "slot/port". e.g. 0/0\n
    """
    validate_choices(mode, ["auto", "interactive"])
    port_obj = tp_storage.get_reserved_port(port)
    await anlt_utils.lt_config(port_obj, enable, timeout, mode, link_recovery)
    return None


@l1_config.command(cls=cb.XenaCommand)
async def txcvr_tap(
    port: str,
):
    pass


#### ????


@l1_config.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.argument("txcvr_lane_list", type=ac.STRING)
@ac.argument("PRESET0_LIST", type=ac.STRING)
@try_wrapper(False)
async def lt_preset0(port: str, txcvr_lane_list: str, preset0_list: str) -> None:
    """
    Configures and modifies a port's layer-1 link training preset0 settings.
        PORT TEXT: Specifies the port on the specified device host. Specify a port using the format 'slot/port'. e.g. 0/0\n
        TXCVR_LANE_LIST TEXT: Specifies the transceiver lane number list to configure. e.g. If the value is set to 0,1,3, Lane0, Lane1 and Lane3 configured
        PRESET0_LIST: Specifies the list of preset0 values that should be used for the lanes. Allowed values exist | std (existing or standard). This argument must have the same length as TXCVR_LANE_LIST. The order of the values correspond to the lanes in TXCVR_LANE_LIST. e.g. std,std,exist means preset0 values that should be used for Lane0, Lane1 and Lane3 are standard, standard, and existing, respectively.
    """

    try:
        lanes = [int(i) for i in ",".split(txcvr_lane_list) if i]
        uses = [s for s in ",".split(preset0_list) if s]
    except ValueError as e:
        raise CannotConvertError(e)
    port_obj = tp_storage.get_reserved_port(port)
    if len(lanes) != len(uses):
        raise NotSameLengthError(lanes, uses)
    for lane, use in zip(lanes, uses):
        await anlt_utils.lt_preset0(port_obj, lane, use)
    return None


# # @ac.argument("transceiver_lane_num_list", type=ac.STRING)
# # @ac.option("--auto-negotiation-enabled", type=ac.BOOL)
# # @ac.option("--link-training-enabled", type=ac.BOOL)
# # @ac.option("--link-training-timeout", type=ac.BOOL)
# # @ac.option("--link-training-mode", type=ac.STRING)
# # def l1(
# #     port: str,
# #     transceiver_lane_num_list: str,
# #     auto_negotiation_enabled: bool = False,
# #     link_training_enabled: bool = False,
# #     link_training_timeout: bool = False,
# #     link_training_mode: str = "auto",
# # ) -> str:
# #     """
# #     Configures and modifies an L1 port on a chassis.

# #     PORT<str>: Specifies the port on the specified device host. Specify a port using the format "slot/port": 0/0\n
# #     TRANSCEIVER_LANE_NUM_LIST<str>: Specifies the transceiver lane number list to configure --main-tap-list, --post-emphasis-list, --pre-emphasis-list, --pre2-emphasis list, --pre3-emphasis-list, --tx-enabled-list, and -rx-mode-list. e.g. If the value is set to 0,1,3, Lane0, Lane1 and Lane3 transceiver options will be configured.
# #     AUTO_NEGOTIATION_ENABLED<bool>: Enable or disable auto-negotiation, default to false. e.g. true|false\n
# #     LINK_TRAINING_ENABLED<bool>: Enable or disable link training, default to false. e.g. true|false\n
# #     LINK_TRAINING_TIMEOUT<bool>: Link training with or without timeout, default to true. e.g. true|false\n
# #     LINK_TRAINING_MODE<bool>: Link training mode. e.g. "auto"|"interactive"\n
# #     """


@xena_cli.group(cls=cb.XenaGroup)
def l1_control() -> None:
    """L1 control."""
    return None


@l1_control.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.argument("txcvr_lane", type=ac.INT)
@try_wrapper(False)
async def lt_clear(port: str, txcvr_lane: int) -> str:
    """
    Clear the command sequence for the lane. Lane is relative to the port and start with 0.

    PORT TEXT : Specifies the port on the specified device host. Specify a port using the format "slot/port". e.g. 0/0\n
    txcvr_lane INT: Lane number to configure, e.g. 0
    """
    port_obj = tp_storage.get_reserved_port(port)
    return await anlt_utils.lt_clear(port_obj, txcvr_lane)


@l1_control.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.argument("txcvr_lane", type=ac.INT)
@try_wrapper(False)
async def lt_nop(port: str, txcvr_lane: int) -> str:
    """
    No operation for the lane, used to indicate interactive link training.

    PORT TEXT: Specifies the port on the specified device host. Specify a port using the format "slot/port". e.g. 0/0\n
    TXCVR_LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane1 is configured.
    """
    port_obj = tp_storage.get_reserved_port(port)
    return await anlt_utils.lt_nop(port_obj, txcvr_lane)


@l1_control.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.argument("txcvr_lane", type=ac.INT)
@ac.argument("action", type=ac.STRING)
@ac.argument("emphasis", type=ac.INT)
@ac.argument("value", type=ac.INT)
@try_wrapper(False)
async def lt_coeff(
    port: str, txcvr_lane: int, action: str, emphasis: int, value: str
) -> str:
    """
    Change the TX emphasis (coefficients) from a local lane. This tells the remote link training partner to change its emphasis value.

        PORT TEXT: Specifies the port on the specified device host. Specify a port using the format "slot/port". e.g. 0/0\n
        TXCVR_LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane1 is configured.\n
        ACTION TEXT: The remote link training partner should increase or decrease the coefficient. Allowed values: inc | dec .\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n
        VALUE<int>: The value of the increase/decrease for the link partner's emphasis. Must be >= 0.\n
    """  
    port_obj = tp_storage.get_reserved_port(port)
    validate_choices(action, ["inc", "dec"])
    validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
    coeff = {"pre3": -3, "pre2": -2, "pre": -1, "main": 0, "post": 1}[value]
    if action == "inc":
        await anlt_utils.lt_coeff_inc(port_obj, txcvr_lane, coeff, abs(value))
    else:
        await anlt_utils.lt_coeff_dec(port_obj, txcvr_lane, coeff, abs(value))
    return None


@l1_control.command(cls=cb.XenaCommand)
@ac.argument("port", type=ac.STRING)
@ac.argument("txcvr_lane", type=ac.INT)
@ac.argument("preset", type=ac.INT)
@try_wrapper(False)
async def lt_preset(port: str, txcvr_lane: int, preset: int) -> None:
    """
    PORT TEXT: Specifies the port on the specified device host. Specify a port using the format 'slot/port'. e.g. 0/0\n
    TXCVR_LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane1 is configured.\n
    """
    pass


# @l1_control.command(cls=cb.XenaCommand)
# @ac.argument("port", type=ac.STRING)
# @ac.argument("lane_num", type=ac.INT)
# def lt_trained(port: str, lane_num: int) -> str:
#     """
#     Announce the specified lane is trained.

#     PORT<str>: Specifies the port on the specified device host. Specify a port using the format "slot/port". e.g. 0/0\n
#     LANE_NUM<int>: Lane number to configure, e.g. 0\n
#     """
#     return ""


# @xena_cli.command(cls=cb.XenaCommand)
# def an_log() -> str:
#     """Show the autonegotiation trace log."""
#     return ""


# @xena_cli.command(cls=cb.XenaCommand)
# def an_status() -> str:
#     """Show the autonegotiation status."""
#     return ""


# @xena_cli.command(cls=cb.XenaCommand)
# @ac.argument("lane_num", type=ac.INT)
# def lt_log(lane_num: int) -> str:
#     """Show the autonegotiation trace log."""
#     return ""


# @xena_cli.command(cls=cb.XenaCommand)
# @ac.argument("lane_num", type=ac.INT)
# def lt_status(lane_num: int) -> str:
#     """Show the link training status per lane."""
#     return ""


# @xena_cli.command(cls=cb.XenaCommand)
# @ac.argument("lane_num", type=ac.INT)
# def lt_status(lane_num: int) -> str:
#     """Show the link training trace log per lane."""
#     return ""


# @xena_cli.command(cls=cb.XenaCommand)
# @ac.argument("lane_num", type=ac.INT)
# def lt_status(lane_num: int) -> str:
#     """Get the taps of the local transceiver."""
#     return ""
