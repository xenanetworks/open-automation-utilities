from __future__ import annotations
import asyncclick as ac
from .. import click_backend as cb
from xoa_driver.hlfuncs import anlt as anlt_utils
from ...exceptions import *
from ...clis import (
    format_lt_config,
    format_lt_im,
    format_lt_inc_dec,
    format_lt_encoding,
    format_lt_preset,
    format_lt_trained,
    format_txtap_get,
    format_txtap_set,
    format_lt_status,
)
from .group import xoa_utils
from .. import click_help as h
from ...cmds import CmdContext


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
@lt.command(cls=cb.XenaCommand, name="config")
@ac.option(
    "--mode",
    type=ac.Choice(["interactive", "auto"]),
    help=h.HELP_LT_CONFIG_MODE,
    default="interactive",
)
@ac.option("--on/--off", type=ac.BOOL, help=h.HELP_LT_CONFIG_ON, default=True)
@ac.option(
    "--preset0/--no-preset0", type=ac.BOOL, help=h.HELP_LT_CONFIG_PRESET0, default=False
)
@ac.pass_context
async def lt_config(context: ac.Context, mode: str, on: bool, preset0: bool) -> str:
    """
    To configure link training on the working port.\n

    """
    storage: CmdContext = context.obj
    storage.store_should_do_lt(on)
    storage.store_lt_preset0_std(not preset0)
    storage.store_lt_interactive(True if mode == "interactive" else False)
    return format_lt_config(storage)


# **************************
# sub-command: lt im
# **************************
@lt.command(cls=cb.XenaCommand, name="im")
@ac.argument("lane", type=ac.INT)
@ac.argument("encoding", type=ac.Choice(["nrz_pam2", "pam4", "pam4pre"]))
@ac.pass_context
async def lt_im(context: ac.Context, lane: int, encoding: str) -> str:
    """
    Set the initial modulation for the specified lane.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        ENCODING TEXT: Specifies the initial modulation. Allowed values: nrz_pam2 | pam4 | pam4pre.\n

    """
    storage: CmdContext = context.obj
    storage.store_lt_initial_mod(lane, encoding)
    return format_lt_im(storage, lane)


# **************************
# Type: Control
# **************************
# **************************
# sub-command: lt inc
# **************************
@lt.command(cls=cb.XenaCommand, name="inc")
@ac.argument("lane", type=ac.INT)
@ac.argument("emphasis", type=ac.Choice(["pre3", "pre2", "pre", "main", "post"]))
@ac.pass_context
async def lt_inc(context: ac.Context, lane: int, emphasis: str) -> str:
    """
    To request the remote link training partner to increase its emphasis value by 1 bit.

        LANE INT: Specifies the transceiver lane index.\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.lt_coeff_inc(port_obj, lane, emphasis)
    return format_lt_inc_dec(storage, lane, emphasis, True)


# **************************
# sub-command: lt dec
# **************************
@lt.command(cls=cb.XenaCommand, name="dec")
@ac.argument("lane", type=ac.INT)
@ac.argument("emphasis", type=ac.Choice(["pre3", "pre2", "pre", "main", "post"]))
@ac.pass_context
async def lt_dec(context: ac.Context, lane: int, emphasis: str) -> str:
    """
    To request the remote link training partner to decrease its emphasis value by 1 bit.

        LANE INT: Specifies the transceiver lane index.\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.lt_coeff_dec(port_obj, lane, emphasis)
    return format_lt_inc_dec(storage, lane, emphasis, False)


# **************************
# sub-command: lt encoding
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("encoding", type=ac.Choice(["nrz", "pam2", "pam4", "pam4pre"]))
@ac.pass_context
async def lt_encoding(context: ac.Context, lane: int, encoding: str) -> str:
    """
    To request the remote link training partner to use the specified encoding on the specified lane.

        LANE INT: Specifies the transceiver lane index.\n
        ENCODING TEXT: Specifies the encoding. Allowed values: nrz_pam2 | pam4 | pam4pre\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.lt_encoding(port_obj, lane, encoding)
    return format_lt_encoding(storage, lane, encoding)


# **************************
# sub-command: lt preset
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("preset", type=ac.IntRange(1, 5))
@ac.pass_context
async def lt_preset(context: ac.Context, lane: int, preset: int) -> str:
    """
    To request the remote link training partner to use the preset of the specified lane.

        LANE INT: Specifies the transceiver lane index.\n
        PRESET INT: Specifies the preset index. Allowed values: 0 | 1 | 2 | 3 | 4.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.lt_preset(port_obj, lane, preset)
    return format_lt_preset(storage, lane, preset)


# **************************
# sub-command: lt trained
# **************************
@lt.command(cls=cb.XenaCommand, name="trained")
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_trained(context: ac.Context, lane: int) -> str:
    """
    To announce that the specified lane is trained.

        LANE INT: Specifies the transceiver lane index.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.lt_trained(port_obj, lane)
    return format_lt_trained(storage, lane)


# **************************
# sub-command: lt status
# **************************
@lt.command(cls=cb.XenaCommand, name="status")
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_status(context: ac.Context, lane: int) -> str:
    """
    To show the link training status of the specified lane.

        LANE INT: Specifies the lane index.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    dic = await anlt_utils.lt_status(port_obj, lane)
    return format_lt_status(dic)


# **************************
# sub-command: txtapget
# **************************
@lt.command(cls=cb.XenaCommand, name="txtapget")
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_txtapget(context: ac.Context, lane: int) -> str:
    """
    Read the tap values of the specified lane of the local port.

        LANE INT: Specifies the lane index.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    dic = await anlt_utils.txtap_get(port_obj, lane)
    return format_txtap_get(lane, dic)


# **************************
# sub-command: txtapset
# **************************
@lt.command(cls=cb.XenaCommand, name="txtapset")
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
    post: int,
) -> str:
    """
    Write the tap values of the specified lane of the local port.

        LANE INT: The lane index to read tap values from.\n
        PRE3 INT: Specifies c(-3) value of the tap.\n
        PRE2 INT: Specifies c(-2) value of the tap.\n
        PRE1 INT: Specifies c(-1) value of the tap.\n
        MAIN INT: Specifies c(0) value of the tap.\n
        POST INT: Specifies c(+1) value of the tap.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await anlt_utils.txtap_set(port_obj, lane, pre3, pre2, pre1, main, post)
    return format_txtap_set(lane, pre3, pre2, pre1, main, post)


# **************************
# sub-command: lt log
# **************************
@lt.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.option(
    "--live/--no-live",
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
    log = await anlt_utils.lt_log(port_obj, lane)
    return log
    # TODO: Needs to be implemented for display
