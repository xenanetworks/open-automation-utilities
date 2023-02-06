from __future__ import annotations
import typing as t
from xoa_driver.testers import L23Tester
from xoa_driver.ports import GenericL23Port
from ..exceptions import NotInStoreError, NotConnectedError, NoSuchIDError
from xoa_driver.hlfuncs import anlt as anlt_utils
from xoa_driver.hlfuncs import mgmt as mgmt_utils
from functools import partialmethod


class ErrorString:
    def __init__(self) -> None:
        self.err_str: str = ""

    def set_val(self, value: str) -> None:
        self.err_str = value

    clear = partialmethod(set_val, "")


class CmdContext:
    def __init__(self) -> None:
        self.tester_serial: str = ""
        self.tester_con_info: str = ""
        self.tester: t.Optional[L23Tester] = None

        self.ports: dict[str, GenericL23Port] = {}
        self.port_str: str = ""

        # self.functionality: str = ""
        self.error: ErrorString = ErrorString()

        self.an_allow_loopback = False
        self.should_do_an = False

        self.should_do_lt = False
        self.lt_preset0_std = False
        self.lt_interactive = False

    def prompt(self, base_prompt: str = "") -> str:
        s = self.retrieve_tester_serial()
        serial = f"[{s}]" if s else ""
        p = self.retrieve_port_str()
        port_str = f"[{p}]" if p else ""
        return f"{base_prompt}{serial}{port_str} > "

    # def store_functionality(self, functionality: str) -> None:
    #     self.functionality = functionality

    def store_current_port_str(self, current_port_str: str) -> None:
        if current_port_str not in self.ports:
            raise NotInStoreError(current_port_str)
        self.port_str = current_port_str

    def store_current_tester(
        self, username: str, con_info: str, tester: L23Tester
    ) -> None:
        self.tester_con_info = con_info
        self.tester_serial = str(tester.info.serial_number)
        self.tester_username = username
        self.tester = tester
        self.port_str = ""
        self.ports = {}

    def get_all_ports(self) -> dict[str, GenericL23Port]:
        return self.obtain_physical_ports("*", False)

    # def retrieve_functionality(self) -> str:
    #     return self.functionality

    def retrieve_ports(self) -> dict[str, GenericL23Port]:
        return self.ports

    def retrieve_tester_username(self) -> str:
        return self.tester_username

    def retrieve_tester_con_info(self) -> str:
        return self.tester_con_info

    def retrieve_tester_serial(self) -> str:
        return self.tester_serial

    def retrieve_tester(self) -> t.Optional[L23Tester]:
        return self.tester

    def retrieve_port_str(self) -> str:
        return self.port_str

    def store_port(self, exact_port_id: str, port_obj: GenericL23Port) -> None:
        self.ports[exact_port_id] = port_obj

    def retrieve_port(self, exact_port_id: str = "current") -> GenericL23Port:
        if self.tester is None:
            raise NotConnectedError()
        if exact_port_id == "current":
            exact_port_id = self.port_str
        if exact_port_id in self.ports:
            return self.ports[exact_port_id]
        raise NotInStoreError(exact_port_id)

    def remove_port(self, exact_port_id: str) -> None:
        if exact_port_id in self.ports:
            del self.ports[exact_port_id]

    def set_error(self, error_str: str) -> None:
        self.error.set_val(error_str)

    clear_error = partialmethod(set_error, "")

    def get_error(self) -> str:
        return self.error.err_str

    def obtain_physical_ports(
        self, id_str: str = "*", update: bool = True
    ) -> dict[str, GenericL23Port]:
        if self.tester is None:
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

        p_dics = {
            f"{i.kind.module_id}/{i.kind.port_id}": i
            for i in mgmt_utils.get_ports(self.tester, int(m_id), int(p_id))
        }
        if update:
            self.ports.update(p_dics)
        return p_dics
