from __future__ import annotations
import asyncclick as ac
from .group import xoa_utils
from .. import click_backend as cb
from .. import click_help as h
from ...exceptions import *
from ...cmds import CmdContext
from xoa_driver.hlfuncs import anlt_ll_debug as debug_utils


@xoa_utils.group(cls=cb.XenaGroup)
def debug():
    """
    To enter debug context.\n

    """


# --------------------------
# command: init
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def init(context: ac.Context, lane: int) -> str:
    """
    Debug init

    LANE INT: Specifies the transceiver lane index\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    await debug_utils.init(port_obj, lane)
    inf = await debug_utils.init(port_obj, lane)
    storage.store_anlt_low(inf)
    return str(inf)


async def _help_get(func: t.Callable, context: ac.Context, lane: int) -> str:
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    inf = storage.retrieve_anlt_low()
    return str(await func(port_obj, lane, inf=inf))


async def _help_set(
    func: t.Callable, context: ac.Context, lane: int, value: int
) -> str:
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    inf = storage.retrieve_anlt_low()
    await func(port_obj, lane, value=value, inf=inf)
    return ""


# --------------------------
# command: lane_reset
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lane_reset(context: ac.Context, lane: int) -> str:
    """
    Debug lane_reset

    LANE INT: Specifies the transceiver lane index\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    inf = storage.retrieve_anlt_low()
    await debug_utils.lane_reset(port_obj, lane, inf=inf)
    return ""


# --------------------------
# command: mode_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def mode_get(context: ac.Context, lane: int) -> str:
    """
    Debug mode_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.mode_get, context, lane)


# --------------------------
# command: mode_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value", type=ac.INT)
@ac.pass_context
async def mode_set(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug mode_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """

    return await _help_set(debug_utils.mode_get, context, lane, value)


# --------------------------
# command: lt_tx_config_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_tx_config_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_tx_config_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_tx_config_get, context, lane)


# --------------------------
# command: lt_tx_config_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value", type=ac.INT)
@ac.pass_context
async def lt_tx_config_set(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug lt_tx_config_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    return await _help_set(debug_utils.lt_tx_config_set, context, lane, value)


# --------------------------
# command: lt_rx_config_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_config_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_config_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_config_get, context, lane)


# --------------------------
# command: lt_rx_config_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value", type=ac.INT)
@ac.pass_context
async def lt_rx_config_set(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug lt_rx_config_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    return await _help_set(debug_utils.lt_rx_config_set, context, lane, value)


# --------------------------
# command: lt_tx_tf_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_tx_tf_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_tx_tf_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_tx_tf_get, context, lane)


# --------------------------
# command: lt_rx_error_stat0_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_error_stat0_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_error_stat0_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_error_stat0_get, context, lane)


# --------------------------
# command: lt_rx_error_stat1_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_error_stat1_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_error_stat1_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_error_stat1_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_config_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_config_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_config_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_analyzer_config_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_trig_mask_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_trig_mask_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_trig_mask_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_analyzer_trig_mask_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_status_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_status_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_status_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_analyzer_status_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_rd_addr_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_rd_addr_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_rd_addr_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_analyzer_rd_addr_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_rd_page_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_rd_page_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_rd_page_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_analyzer_rd_page_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_rd_data_get
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_rd_data_get(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_rd_data_get

    LANE INT: Specifies the transceiver lane index\n

    """
    return await _help_get(debug_utils.lt_rx_analyzer_rd_data_get, context, lane)


# --------------------------
# command: lt_rx_analyzer_config_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value" ,type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_config_set(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug lt_rx_analyzer_config_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    await _help_set(debug_utils.lt_rx_analyzer_config_set, context, lane, value)
    return ""


# --------------------------
# command: lt_rx_analyzer_trig_mask_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value" ,type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_trig_mask_set(
    context: ac.Context, lane: int, value: int
) -> str:
    """
    Debug lt_rx_analyzer_trig_mask_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    await _help_set(debug_utils.lt_rx_analyzer_trig_mask_set, context, lane, value)
    return ""


# --------------------------
# command: lt_rx_analyzer_rd_addr_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value" ,type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_rd_addr_set(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug lt_rx_analyzer_rd_addr_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    await _help_set(debug_utils.lt_rx_analyzer_rd_addr_set, context, lane, value)
    return ""


# --------------------------
# command: lt_rx_analyzer_rd_page_set
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value" ,type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_rd_page_set(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug lt_rx_analyzer_rd_page_set

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    await _help_set(debug_utils.lt_rx_analyzer_rd_page_set, context, lane, value)
    return ""


# --------------------------
# command: lt_status
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.argument("value" ,type=ac.INT)
@ac.pass_context
async def lt_status(context: ac.Context, lane: int, value: int) -> str:
    """
    Debug lt_status

    LANE INT: Specifies the transceiver lane index\n

    VALUE INT: Specifies the value\n

    """
    await _help_set(debug_utils.lt_status, context, lane, value)
    return ""


# --------------------------
# command: lt_prbs
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_prbs(context: ac.Context, lane: int) -> str:
    """
    Debug lt_prbs

    LANE INT: Specifies the transceiver lane index\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    inf = storage.retrieve_anlt_low()
    return str(await debug_utils.lt_prbs(port_obj, lane, inf=inf))


# --------------------------
# command: lt_rx_analyzer_dump
# --------------------------
@debug.command(cls=cb.XenaCommand)
@ac.argument("lane", type=ac.INT)
@ac.pass_context
async def lt_rx_analyzer_dump(context: ac.Context, lane: int) -> str:
    """
    Debug lt_rx_analyzer_dump

    LANE INT: Specifies the transceiver lane index\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    inf = storage.retrieve_anlt_low()
    return str(await debug_utils.lt_rx_analyzer_dump(port_obj, lane, inf=inf))
