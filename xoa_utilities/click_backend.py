from __future__ import annotations
from functools import partialmethod
import asyncclick as ac


class ErrorString:
    def __init__(self) -> None:
        self.err_str = ""

    def set_val(self, value: str) -> None:
        self.err_str = value

    clear = partialmethod(set_val, "")


error_str = ErrorString()


class XenaGroup(ac.Group):
    def get_help(self, ctx: ac.Context) -> str:
        e = super().get_help(ctx)
        e = e.replace("python -m entry", "")
        error_str.set_val(f"{e}")
        return e


class XenaCommand(ac.Command):
    def get_help(self, ctx: ac.Context) -> str:
        e = super().get_help(ctx)
        e = e.replace("python -m entry", "")
        error_str.set_val(f"{e}")
        return e
