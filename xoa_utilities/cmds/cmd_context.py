from __future__ import annotations
import typing as t
from xoa_driver.testers import L23Tester
from xoa_driver.ports import GenericL23Port
from ..exceptions import (
    NotInStoreError,
    NotConnectedError,
    NoSuchIDError,
    NoWorkingPort,
)
from xoa_driver.hlfuncs import mgmt as mgmt_utils
from xoa_driver.enums import LinkTrainEncoding
from functools import partialmethod


class ErrorString:
    def __init__(self) -> None:
        self.err_str: str = ""

    def set_val(self, value: str) -> None:
        self.err_str = value

    clear = partialmethod(set_val, "")


class TesterState:
    def __init__(self) -> None:
        self.serial: str = ""
        self.con_info: str = ""
        self.username: str = ""
        self.obj: t.Optional[L23Tester] = None


class PortState:
    def __init__(self) -> None:
        self.ports: dict[str, GenericL23Port] = {}
        self.port_str: str = ""


class ANState:
    def __init__(self) -> None:
        self.allow_loopback: bool = False
        self.do: bool = False


class LTState:
    def __init__(self) -> None:
        self.do: bool = False
        self.preset0_std: bool = False
        self.interactive: bool = False
        self.initial_mod: bool = {}


class LoopFuncState:
    def __init__(self) -> None:
        self.func: t.Optional[t.Callable] = None
        self.interval: int = 1


class CmdContext:
    def __init__(self) -> None:
        self.tr_state: TesterState = TesterState()
        self.pt_state: PortState = PortState()
        self.error: ErrorString = ErrorString()
        self.an_state: ANState = ANState()
        self.lt_state: LTState = LTState()
        self.fn_state: LoopFuncState = LoopFuncState()

    def get_coro_interval(self) -> int:
        return self.fn_state.interval

    def get_loop_coro(self) -> t.Optional[t.Callable]:
        return self.fn_state.func

    def set_loop_coro(self, coro: t.Coroutine) -> None:
        self.fn_state.func = coro

    def prompt(self, base_prompt: str = "", end_prompt:str = '>') -> str:
        s = self.retrieve_tester_serial()
        serial = f"[{s}]" if s else ""
        p = self.retrieve_port_str()
        port_str = f"[{p}]" if p else ""
        return f"{base_prompt}{serial}{port_str} {end_prompt} "

    # def store_functionality(self, functionality: str) -> None:
    #     self.functionality = functionality

    def store_lt_initial_mod(self, lane: int, encoding: str) -> None:
        # e = LinkTrainEncoding[
        #     {"pam4pre": "PAM4_WITH_PRECODING"}.get(encoding, encoding).upper()
        # ]
        self.lt_state.initial_mod[lane] = encoding

    def store_an_allow_loopback(self, do: bool) -> None:
        self.an_state.allow_loopback = do

    def store_should_do_an(self, do: bool) -> None:
        self.an_state.do = do

    def store_should_do_lt(self, do: bool) -> None:
        self.lt_state.do = do

    def store_lt_interactive(self, do: bool) -> None:
        self.lt_state.interactive = do

    def store_lt_preset0_std(self, do: bool) -> None:
        self.lt_state.preset0_std = do

    def store_current_port_str(self, current_port_str: str) -> None:
        if current_port_str not in self.pt_state.ports:
            raise NotInStoreError(current_port_str)
        self.pt_state.port_str = current_port_str

    def store_current_tester(
        self, username: str, con_info: str, tester: L23Tester
    ) -> None:
        self.tr_state.con_info = con_info
        self.tr_state.serial = str(tester.info.serial_number)
        self.tr_state.username = username
        self.tr_state.obj = tester
        self.pt_state.port_str = ""
        self.pt_state.ports = {}

    def get_all_ports(self) -> dict[str, GenericL23Port]:
        return self.obtain_physical_ports("*", False)

    # def retrieve_functionality(self) -> str:
    #     return self.functionality
    def retrieve_lt_initial_mod(self, lane: int) -> str:
        if lane not in self.lt_state.initial_mod:
            raise NotInStoreError(lane)
        return self.lt_state.initial_mod[lane]

    def retrieve_lt_interactive(self) -> None:
        return self.lt_state.interactive

    def retrieve_should_do_lt(self) -> bool:
        return self.lt_state.do

    def retrieve_lt_preset0_std(self) -> bool:
        return self.lt_state.preset0_std

    def retrieve_ports(self) -> dict[str, GenericL23Port]:
        return self.pt_state.ports

    def retrieve_tester_username(self) -> str:
        return self.tr_state.username

    def retrieve_tester_con_info(self) -> str:
        return self.tr_state.con_info

    def retrieve_tester_serial(self) -> str:
        return self.tr_state.serial

    def retrieve_tester(self) -> t.Optional[L23Tester]:
        return self.tr_state.obj

    def retrieve_port_str(self) -> str:
        return self.pt_state.port_str

    def store_port(self, exact_port_id: str, port_obj: GenericL23Port) -> None:
        self.pt_state.ports[exact_port_id] = port_obj

    def retrieve_port(self, exact_port_id: str = "current") -> GenericL23Port:
        if self.retrieve_tester() is None:
            raise NotConnectedError()
        if exact_port_id == "current":
            if not self.pt_state.port_str:
                raise NoWorkingPort()
            exact_port_id = self.pt_state.port_str
        if exact_port_id in self.pt_state.ports:
            return self.pt_state.ports[exact_port_id]
        raise NotInStoreError(exact_port_id)

    def remove_port(self, exact_port_id: str) -> None:
        if exact_port_id in self.pt_state.ports:
            del self.pt_state.ports[exact_port_id]

    def set_error(self, error_str: str) -> None:
        self.error.set_val(error_str)

    clear_error = partialmethod(set_error, "")

    def get_error(self) -> str:
        return self.error.err_str

    def obtain_physical_ports(
        self, id_str: str = "*", update: bool = True
    ) -> dict[str, GenericL23Port]:
        if self.retrieve_tester() is None:
            raise NotConnectedError()
        if id_str == "*":
            m_id = p_id = -1
        else:
            splitted = id_str.split("/")
            if len(splitted) == 1:
                m_id = splitted[0]
                p_id = -1
            elif len(splitted) == 2:
                m_id, p_id = splitted
            else:
                raise NoSuchIDError(id_str)
        try:
            m_id = int(m_id)
            p_id = int(p_id)
        except ValueError:
            raise NoSuchIDError(id_str)
        p_dics = {
            f"{i.kind.module_id}/{i.kind.port_id}": i
            for i in mgmt_utils.get_ports(self.retrieve_tester(), m_id, p_id)
        }
        if update:
            self.pt_state.ports.update(p_dics)
        return p_dics
