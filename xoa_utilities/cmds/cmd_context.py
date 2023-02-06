from __future__ import annotations
import typing as t
from xoa_driver.testers import L23Tester
from xoa_driver.ports import GenericL23Port
from ..exceptions import NoSuchPortError, NotConnectedError
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
        self.function: str = ""
        self.error: ErrorString = ErrorString()

    def back(self) -> None:
        if self.function:
            self.function = ""
        elif self.port_str:
            self.port_str = ""
        elif self.tester:
            self.tester = None
            self.tester_serial: str = ""
            self.tester_con_info: str = ""
            self.ports = {}
            self.port_str = ""

    def set_current_port_str(self, current_port_str: str) -> None:
        if current_port_str not in self.ports:
            raise NoSuchPortError(current_port_str)
        self.port_str = current_port_str

    def set_current_tester(
        self, username: str, con_info: str, tester: L23Tester
    ) -> None:
        self.tester_con_info = con_info
        self.tester_serial = tester.info.serial_number
        self.tester_username = username
        self.tester = tester
        self.port_str = ""
        self.ports = {}

    def get_tester(self) -> t.Optional[L23Tester]:
        return self.tester

    def store_port(self, exact_port_id: str, port_obj: GenericL23Port) -> None:
        self.ports[exact_port_id] = port_obj

    def set_error(self, error_str: str) -> None:
        self.error.set_val(error_str)

    clear_error = partialmethod(set_error, "")

    def get_error(self) -> str:
        return self.error.err_str

    def obtain_physical_ports(self, id_str: str = "*") -> dict[str, GenericL23Port]:
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
                raise NoSuchPortError(id_str)

        p_dics = {
            f"{i.kind.module_id}/{i.kind.port_id}": i
            for i in mgmt_utils.get_ports(self.tester, int(m_id), int(p_id))
        }
        self.ports.update(p_dics)
        return p_dics
