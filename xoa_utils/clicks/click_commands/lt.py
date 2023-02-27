from __future__ import annotations
import asyncclick as ac
from xoa_utils.clicks import click_backend as cb
from xoa_driver.hlfuncs import anlt as anlt_utils
from xoa_driver import enums
from xoa_utils.clis import (
    format_lt_algorithm,
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
from xoa_utils.clicks.click_commands.group import xoa_util
from xoa_utils.clicks import click_help as h
from xoa_utils.cmds import CmdContext


# --------------------------
# command: lt
# --------------------------
@xoa_util.group(cls=cb.XenaGroup)
def lt():
    """
    Commands for Link Training.
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
    default="auto",
)
@ac.option("--on/--off", type=ac.BOOL, help=h.HELP_LT_CONFIG_ON, default=True)
@ac.option(
    "--preset0",
    type=ac.Choice(["standard", "existing"]),
    help=h.HELP_LT_CONFIG_PRESET0,
    default="standard",
)

@ac.pass_context
async def lt_config(context: ac.Context, mode: str, on: bool, preset0: str) -> str:
    """
    Configure LT for the working port.
    """
    storage: CmdContext = context.obj
    storage.retrieve_port()
    storage.store_should_do_lt(on)
    storage.store_lt_preset0(preset0)
    storage.store_lt_interactive(True if mode == "interactive" else False)
    return format_lt_config(storage)


# **************************
# sub-command: lt im
# **************************
@lt.command(cls=cb.XenaCommand, name="im")
@ac.argument("lane", type=ac.INT)
@ac.argument("encoding", type=ac.Choice(["nrz", "pam4", "pam4pre"]))
@ac.pass_context
async def lt_im(context: ac.Context, lane: int, encoding: str) -> str:
    """
    Set initial modulation for the specified lane.

        <LANE>: Specifies the transceiver lane (serdes) index.

        <ENCODING>: Specifies the initial modulation. Allowed values: nrz | pam4 | pam4pre
    """
    storage: CmdContext = context.obj
    storage.retrieve_port()
    storage.validate_current_lane(lane)
    storage.store_lt_initial_mod(lane, encoding)
    return format_lt_im(storage, lane)


# **************************
# sub-command: lt alg
# **************************
@lt.command(cls=cb.XenaCommand, name="alg")
@ac.argument("lane", type=ac.INT)
@ac.argument("algorithm", type=ac.Choice(["alg0", "algn1"]))
@ac.pass_context
async def lt_algorithm(context: ac.Context, lane: int, algorithm: str) -> str:
    """
    Set the link training algorithm for the specified lane.

        <LANE>: Specifies the transceiver lane (serdes) index.

        <ALGORITHM>: Specifies the algorithm. Allowed values: alg0 | algn1
    """
    storage: CmdContext = context.obj
    storage.retrieve_port()
    storage.validate_current_lane(lane)
    storage.store_lt_algorithm(lane, algorithm)
    return format_lt_algorithm(storage, lane)


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
    Request the remote port's lane to increase (+) an emphasis by 1.

        <LANE>: Specifies the transceiver lane (serdes) index.

        <EMPHASIS>: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    await anlt_utils.lt_coeff_inc(
        port_obj, lane, enums.LinkTrainCoeffs[emphasis.upper()]
    )
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
    Request the remote port's lane to decrease (-) an emphasis by 1.

        <LANE>: The lane (serdes) index.

        <EMPHASIS>: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    await anlt_utils.lt_coeff_dec(
        port_obj, lane, enums.LinkTrainCoeffs[emphasis.upper()]
    )
    return format_lt_inc_dec(storage, lane, emphasis, False)


# **************************
# sub-command: lt encoding
# **************************
@lt.command(cls=cb.XenaCommand, name="encoding")
@ac.argument("lane", type=ac.INT)
@ac.argument("encoding", type=ac.Choice(["nrz", "pam4", "pam4pre"]))
@ac.pass_context
async def lt_encoding(context: ac.Context, lane: int, encoding: str) -> str:
    """
    Request the remote port's lane to use the specified encoding.

        <LANE>: The lane (serdes) index.

        <ENCODING>: Specifies the encoding. Allowed values: nrz | pam4 | pam4pre
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    e = enums.LinkTrainEncoding[
        {"pam4pre": "PAM4_WITH_PRECODING"}.get(encoding, encoding).upper()
    ]
    await anlt_utils.lt_encoding(port_obj, lane, e)
    return format_lt_encoding(storage, lane, encoding)


# **************************
# sub-command: lt preset
# **************************
@lt.command(cls=cb.XenaCommand, name="preset")
@ac.argument("lane", type=ac.INT)
@ac.argument("preset", type=ac.IntRange(1, 5))
@ac.pass_context
async def lt_preset(context: ac.Context, lane: int, preset: int) -> str:
    """
    Request the remote port's lane to use the preset.

        <LANE>: The lane (serdes) index.

        <PRESET>: Specifies the preset index. Allowed values: 1 | 2 | 3 | 4 | 5
    """
    preset = max(preset - 1, 0)
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    await anlt_utils.lt_preset(port_obj, lane, enums.LinkTrainPresets(preset))
    return format_lt_preset(storage, lane, preset)


# **************************
# sub-command: lt trained
# **************************
@lt.command(cls=cb.XenaCommand, name="trained")
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_trained(context: ac.Context, lane: int) -> str:
    """
    Announce the lane is trained to the remote port.

        <LANE>: The lane (serdes) index.
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    await anlt_utils.lt_trained(port_obj, lane)
    return format_lt_trained(storage, lane)


# **************************
# sub-command: txtapget
# **************************
@lt.command(cls=cb.XenaCommand, name="txtapget")
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_txtapget(context: ac.Context, lane: int) -> str:
    """
    Read the tap values of the specified lane of the working port.

        <LANE>: The lane (serdes) index.
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    dic = await anlt_utils.txtap_get(port_obj, lane)
    return format_txtap_get(lane, dic)


# **************************
# sub-command: txtapset
# **************************
@lt.command(cls=cb.XenaCommand, name="txtapset")
@ac.argument("lane", type=ac.INT)
@ac.argument("pre3", type=ac.INT)
@ac.argument("pre2", type=ac.INT)
@ac.argument("pre", type=ac.INT)
@ac.argument("main", type=ac.INT)
@ac.argument("post", type=ac.INT)
@ac.pass_context
async def txtapset(
    context: ac.Context,
    lane: int,
    pre3: int,
    pre2: int,
    pre: int,
    main: int,
    post: int,
) -> str:
    """
    Write the tap values of the specified lane of the working port.

        <LANE>: The lane (serdes) index.

        <PRE3>: Specifies c(-3) value of the tap.

        <PRE2>: Specifies c(-2) value of the tap.

        <PRE> : Specifies c(-1) value of the tap.

        <MAIN>: Specifies c(0) value of the tap.

        <POST>: Specifies c(1) value of the tap.
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    await anlt_utils.txtap_set(port_obj, lane, pre3, pre2, pre, main, post)
    return format_txtap_set(lane, pre3, pre2, pre, main, post)


# **************************
# sub-command: lt status
# **************************
@lt.command(cls=cb.XenaCommand, name="status")
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_status(context: ac.Context, lane: int) -> str:
    """
    Show the link training status of the lane.

        <LANE>: The lane (serdes) index.
    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    storage.validate_current_lane(lane)
    dic = await anlt_utils.lt_status(port_obj, lane)
    return format_lt_status(dic)
