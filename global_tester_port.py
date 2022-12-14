from __future__ import annotations
import typing as t
from xoa_driver.testers import L23Tester
from xoa_driver.ports import GenericL23Port
from exceptions import NoSuchPortError, NotConnectedError
import anlt_utils

TP = t.TypeVar("TP", bound="TesterPortStorage")


class TesterPortStorage:
    def __init__(self) -> None:
        self.tester: t.Optional[L23Tester] = None
        self.ports: dict[str, GenericL23Port] = {}
        self.error = None

    def store_tester(self, ip_port: str, tester: L23Tester) -> None:
        self.tester_ip_port = ip_port
        self.tester = tester

    def get_tester(self) -> t.Optional[L23Tester]:
        return self.tester

    def store_port(self, exact_port_id: str, port_obj: GenericL23Port) -> None:
        self.ports[exact_port_id] = port_obj

    def obtain_physical_ports(self, id_str: str) -> dict[str, GenericL23Port]:
        if self.tester is None:
            raise NotConnectedError()

        splitted = id_str.split("/")
        if len(splitted) == 2:
            m_id = splitted[0]
            p_dics = {
                f"{m_id}/{p_id}": anlt_utils.obtain_port(
                    self.tester, int(m_id), int(p_id)
                )
                for p_id in [splitted[1]]
            }
        else:
            m_id = splitted[0]
            all_ports = anlt_utils.obtain_ports_of_module(self.tester, int(m_id))
            p_dics = {f"{m_id}/{port.kind.port_id}": port for port in all_ports}

        self.ports.update(p_dics)
        return p_dics

    def get_reserved_port(self, exact_port_id: str) -> GenericL23Port:
        if self.tester is None:
            raise NotConnectedError()
        splitted = exact_port_id.split("/")
        if len(splitted) == 2:
            port_obj = self.ports.get(exact_port_id, None)
            if port_obj is not None:
                return port_obj
        raise NoSuchPortError(int(exact_port_id.split("/")[-1]))

    def remove_port(self, id_str: str) -> t.Optional[GenericL23Port]:
        splitted = id_str.split("/")
        if len(splitted) == 2:
            if id_str in self.ports:
                self.ports.pop(id_str)
        elif len(splitted) == 1:
            for k in list(self.ports.keys()):
                if k.startswith(splitted[0]):
                    self.ports.pop(k)
        return None

    def list_ports(self) -> tuple[str]:
        return tuple(self.ports.keys())

    def list_tester(self) -> str:
        return self.tester_ip_port


tp_storage = TesterPortStorage()
