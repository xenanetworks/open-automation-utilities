from __future__ import annotations
import asyncclick as ac
from .. import click_backend as cb
from xoa_driver.hlfuncs import anlt as anlt_utils
from ...exceptions import *
import asyncclick as ac
from ...clis import format_recovery, format_port_status
from .group import xoa_utils
from .. import click_help as h
from ...cmds import CmdContext


@xoa_utils.group(cls=cb.XenaGroup)
def anlt():
    """
    To enter anlt context.\n

    """


# --------------------------
# command: recovery
# --------------------------
@anlt.command(cls=cb.XenaCommand)
@ac.option("--on/--off", type=ac.BOOL, help=h.HELP_RECOVERY_ON, default=True)
@ac.pass_context
async def recovery(context: ac.Context, on: bool) -> str:
    """
    Enable/disable link recovery on the specified port. If enable, the port will keep trying ANLT when no link-up signal is detected after five seconds of waiting.
    """
    storage: CmdContext = context.obj

    port_obj = storage.retrieve_port()
    await anlt_utils.link_recovery(port_obj, on)
    return format_recovery(storage, on)


# --------------------------
# command: status
# --------------------------
@anlt.command(cls=cb.XenaCommand)
@ac.pass_context
async def status(context: ac.Context) -> str:
    """
    Show the overview of ANLT status of the port.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    status_dic = await anlt_utils.status(port_obj)
    port_id = storage.retrieve_port_str()
    return format_port_status(port_id, status_dic)


# --------------------------
# command: do
# --------------------------
@anlt.command(cls=cb.XenaCommand)
@ac.pass_context
async def do(context: ac.Context) -> str:
    """
    Show the overview of ANLT status of the port.\n

    """
    storage: CmdContext = context.obj
    port_obj = storage.retrieve_port()
    an_enable = storage.retrieve_an_enable()
    lt_enable = storage.retrieve_lt_enable()
    an_allow_loopback = storage.retrieve_an_loopback()
    lt_preset0_std = storage.retrieve_lt_preset0_std()
    lt_initial_modulations = storage.retrieve_lt_initial_mod()
    lt_interactive = storage.retrieve_lt_interactive()
    await anlt_utils.do_anlt(
        port_obj,
        an_enable,
        lt_enable,
        an_allow_loopback,
        lt_preset0_std,
        lt_initial_modulations,
        lt_interactive,
    )
    return ""


# # **************************
# # sub-command: an log
# # **************************
# @an.command(cls=cb.XenaCommand, name="log")
# @ac.pass_context
# async def an_log(context: ac.Context) -> str:
#     """
#     Show the auto-negotiation log trace.\n

#     """
#     storage: CmdContext = context.obj
#     port_obj = storage.retrieve_port()
#     log = await anlt_utils.autoneg_log(port_obj)
#     return log
