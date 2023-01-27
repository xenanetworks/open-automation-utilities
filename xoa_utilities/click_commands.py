from __future__ import annotations
import asyncclick as ac
import click_backend as cb
from xoa_driver.hlfuncs import anlt as anlt_utils
from xoa_driver.hlfuncs import mgmt as mgmt_utils
from global_tester_port import tp_storage
from cli_utils import try_wrapper, validate_choices
from exceptions import *

cs = {"help_option_names": ["-h", "--help"]}


@ac.group(cls=cb.XenaGroup)
def xoa_utils():
    pass

#--------------------------
# command: connect
#--------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.argument(
    "device", 
    type=ac.STRING)

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
    "e.g. --port-list 0/0,0/1,0/2,0/3\n",
    default="",
)
@ac.option(
    "-r",
    "--reset",
    is_flag=True,
    help="Removes all port configurations of the ports in --port_list after "
    "reservation, default to False. "
    "e.g. --reset\n",
    default=False,
)
@ac.option(
    "-f",
    "--force",
    is_flag=True,
    help="Breaks port locks established by another user, aka. force "
    "reservation, default to True. "
    "e.g. --force",
    default=True,
)
@ac.option(
    "-P",
    "--password",
    type=ac.STRING,
    help="The login password of the tester, default to xena. "
    "e.g. --password xena",
    default="xena",
)
@ac.option(
    "-p",
    "--tcp-port",
    type=ac.INT,
    help="The TCP port number on the chassis for the client to establish "
    "a session, default to 22606. "
    "e.g. --tcp-port 22606",
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
    force: bool,
    ) -> None:
    """
    Connect to a tester for the current session.

        DEVICE TEXT: Specifies the chassis address for connection. You can specify the IP addresses in IPv4 format, or a host name. e.g. 10.10.10.10, demo.xenanetworks.com\n
        USERNAME TEXT: Specifies the name of the user, default to xena. Specifies the name of the user. e.g. openautomation\n

    """
    real_port_list = [i.strip() for i in port_list.split(",")] if port_list else []
    tester = await mgmt_utils.connect("l23", device, username, password, tcp_port)
    tp_storage.store_tester(f"{device}:{tcp_port}", tester)
    for id_str in real_port_list:
        for port_id, port_obj in tp_storage.obtain_physical_ports(id_str).items():
            if force:
                await mgmt_utils.reserve_port(port_obj, force)
            if reset:
                await mgmt_utils.reset_port(port_obj)
            tp_storage.store_port(port_id, port_obj)

    tp_storage.update_working_port_id(real_port_list[0])
    return None

#--------------------------
# command: exit
#--------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.option(
    "-r",
    "--reset",
    is_flag=True,
    help="Removes all port configurations of the reserved ports, "
    "default to False. "
    "e.g. --reset\n",
    default=False,
)
@ac.option(
    "-R",
    "--release",
    is_flag=True,
    help="Determines whether the ports will be released before exiting, "
    "default to True. "
    "e.g. --release\n",
    default=True,
)
@try_wrapper(False)
async def exit(
    reset: bool, 
    release: bool
    ) -> None:
    """
    Exit by terminating port reservations, disconnecting from the chassis, releasing system resources, and removing the specified port configurations.\n

    """
    for port_id, port_obj in tp_storage.ports:
        if reset:
            await mgmt_utils.reset_port(port_obj)
        if release:
            await mgmt_utils.free_port(port_obj)
        tp_storage.remove_port(port_id)

    tp_storage.clean_working_port_id()
    return None

#--------------------------
# command: port
#--------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@ac.argument(
    "port",
    type=ac.STRING,
)
@ac.option(
    "-r",
    "--reset",
    type=ac.BOOL,
    help="Removes all port configurations of the ports in --port_list after"
    " reservation, default to true. Allowed values: true | false. "
    "e.g. --reset true",
    default=False,
)
@ac.option(
    "-f",
    "--force",
    is_flag=True,
    help="Breaks port locks established by another user, aka. force "
    "reservation, default to True. "
    "e.g. --force",
    default=True,
)
@try_wrapper(False)
async def port(
    port: str, 
    reset: bool, 
    force: bool
    ):
    """
    Switch the working port. If the port is not yet reserved, reserve the port. Update the working port in the cache.

        PORT TEXT: Specifies the port on the specified device host. Specify a port using the format slot/port, e.g. 0/0\n

    """
    try:
        tp_storage.get_reserved_port(port)
    except NoSuchPortError:
        port_dic = tp_storage.obtain_physical_ports(port)
        for port_id, port_obj in port_dic.items():
            if force:
                await mgmt_utils.reserve_port(port_obj, force)
            if reset:
                await mgmt_utils.reset_port(port_obj)
            tp_storage.store_port(port_id, port_obj)
    tp_storage.update_working_port_id(port)
    return None


#--------------------------
# command: show_ports
#--------------------------
@xoa_utils.command(cls=cb.XenaCommand)
@try_wrapper(True)
async def show_ports() -> str:
    """
    List all the ports under control.\n

    """
    return ",".join((tp_storage.list_ports()))


#--------------------------
# command: anlt
#--------------------------
@xoa_utils.group(cls=cb.XenaGroup)
def anlt():
    """
    Configures auto-negotiation and link training of the working port.\n

    """

#**************************
# sub-command: an
#**************************
@anlt.command(cls=cb.XenaGroup)
@ac.option(
    '--enable/--disable', 
    ' /-d', 
    is_flag=True,
    help="Enable or disable auto-negotiation on the working port, default to True. "
    "e.g. an --enable.",
    default=True,
)
@ac.option(
    '--loopback/--no-loopback', 
    '-l/ ', 
    is_flag=True,
    help="Should loopback be allowed in auto-negotiation, default to False. "
    "e.g. an --no-loopback",
    default=False,
)
@try_wrapper(False)
async def an(
    enable: bool, 
    loopback: bool
    ) -> None:
    """
    Configure auto-negotiation on the working port.\n

    """
    port_obj = tp_storage.get_working_port()
    await anlt_utils.autoneg_config(port_obj, enable, loopback)
    return None

#**************************
# sub-command: an_status
#**************************
@anlt.command(cls=cb.XenaGroup)
async def an_status() -> str:
    """
    Show the auto-negotiation status.\n

    """
    port_obj = tp_storage.get_working_port()
    status = await anlt_utils.autoneg_status(port_obj)
    return status #TODO: need to beautify the status output

#**************************
# sub-command: an_log
#**************************
@anlt.command(cls=cb.XenaCommand)
async def an_log() -> str:
    """
    Show the auto-negotiation log trace.\n

    """
    port_obj = tp_storage.get_working_port()
    log = await anlt_utils.autoneg_log(port_obj)
    return log #TODO: need to beautify the log message output


#**************************
# sub-command: lt
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.option(
    '--mode', 
    '-m', 
    type=ac.CHOICE(['mission', 'disable', 'interactive', 'auto']),
    help="The mode for link training on the working port, default to disable. "
    "e.g. lt --mode=auto",
    default="interactive",
)
@ac.option(
    '--preset0/--no-preset0',
    '-p/ ',
    is_flag=True,
    help="Should the preset0 (out-of-sync) use existing tap values or standard values, "
    "default to False. "
    "e.g. lt --preset0",
    default=False,
)
@ac.option(
    '--timeout/--no-timeout',
    '-t /',
    is_flag=True,
    help="Should link training run with or without timeout, "
    "default to True. "
    "e.g. lt --timeout",
    default=False,
)
@try_wrapper(False)
async def lt(
    mode: str,
    preset0: bool,
    timeout: bool
    ) -> None:
    """
    Configures link training on the working port.\n

    """
    port_obj = tp_storage.get_working_port()
    await anlt_utils.lt_config(port_obj, mode, preset0, timeout)
    return None


#**************************
# sub-command: lt_inc
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
@ac.argument(
    "emphasis",
    type=ac.STRING
)
@try_wrapper(False)
async def lt_inc(
    lane: int, 
    emphasis: str
) -> str:
    """
    Tells the remote link training partner to increase its emphasis register value by 1 bit.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n

    """  
    port_obj = tp_storage.get_working_port()
    try:
        validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
        await anlt_utils.lt_coeff_inc(port_obj, lane, emphasis)
        return f""
    except NotInChoicesError as e:
        return e.msg
    

#**************************
# sub-command: lt_dec
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
@ac.argument(
    "emphasis",
    type=ac.STRING
)
@try_wrapper(False)
async def lt_dec(
    lane: int, 
    emphasis: str
) -> str:
    """
    Tells the remote link training partner to decrease its emphasis register value by 1 bit.

        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        EMPHASIS TEXT: The emphasis (coefficient) of the link partner. Allowed values: pre3 | pre2 | pre | main | post. e.g. pre3\n

    """  
    port_obj = tp_storage.get_working_port()
    try:
        validate_choices(emphasis, ["pre3", "pre2", "pre", "main", "post"])
        await anlt_utils.lt_coeff_dec(port_obj, lane, emphasis)
        return f""
    except NotInChoicesError as e:
        return e.msg


#**************************
# sub-command: lt_preset
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
@ac.argument(
    "preset", 
    type=ac.INT
)
@try_wrapper(False)
async def lt_preset(
    lane: int, 
    preset: int
) -> str:
    """
    Ask the remote port to use the preset of the specified lane.
    
        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        PRESET INT: Specifies the preset index. Allowed values: 1, 2, 3, 4, 5.\n

    """
    port_obj = tp_storage.get_working_port()
    if preset in range(1,5):
        await anlt_utils.lt_preset(port_obj, lane, preset)
        return f""
    else:
        return f"Preset {preset} is not in the choices (1, 2, 3, 4, 5)!"


#**************************
# sub-command: lt_encoding
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
@ac.argument(
    "encoding", 
    type=ac.STRING
)
@try_wrapper(False)
async def lt_encoding(
    lane: int, 
    encoding: str
) -> str:
    """
    Ask the remote port to use the specified encoding in link training of the specified lane.
    
        LANE INT: Specifies the transceiver lane number to configure. e.g. If the value is set to 1, Lane 1 will be configured.\n
        ENCODING TEXT: Specifies the encoding. Allowed values: nrz/pam2, pam4, pam4pre\n

    """
    port_obj = tp_storage.get_working_port()
    try:
        validate_choices(encoding, ["nrz", "pam2", "pam4", "pam4pre"])
        await anlt_utils.lt_encoding(port_obj, lane, encoding)
        return f""
    except NotInChoicesError as e:
        return e.msg


#**************************
# sub-command: lt_trained
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
async def lt_trained(
    lane: int
) -> str:
    """
    Announce that the specified lane is trained.

        LANE INT: The lane index for the announcement.\n

    """
    port_obj = tp_storage.get_working_port()
    await anlt_utils.lt_trained(port_obj, lane)
    return ""


#**************************
# sub-command: lt_log
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
@ac.option(
    '--live/--no-live',
    '-l/ ',
    is_flag=True,
    help="Should show the live LT log , "
    "default to False. "
    "e.g. lt_log --live",
    default=False,
)
async def lt_log(
    lane: int, 
    live: bool
) -> str:
    """
    Show the link training trace log for the specified lane.
    
        LANE INT: The lane index for the announcement.\n

    """
    port_obj = tp_storage.get_working_port()
    log = await anlt_utils.lt_log(port_obj, lane, live)
    return log
    #TODO: Needs to be implemented for display


#**************************
# sub-command: lt_status
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
async def lt_status(
    lane: int
) -> str:
    """
    Show the link training status of the specified lane.
    
        LANE INT: The lane index for the announcement.\n

    """
    port_obj = tp_storage.get_working_port()
    status = await anlt_utils.lt_status(port_obj, lane)
    return status
    #TODO: Needs to be implemented for display



#**************************
# sub-command: txtap_get
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
async def txtap_get(
    lane: int
) -> str:
    """
    Read the tap values of the specified lane of the local port.
    
        LANE INT: The lane index to read tap values from.\n

    """
    port_obj = tp_storage.get_working_port()
    dict = await anlt_utils.txtap_get(port_obj, lane)
    return dict
    #TODO: Needs to be implemented for display


#**************************
# sub-command: txtap_set
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.argument(
    "lane", 
    type=ac.INT
)
@ac.argument(
    "pre3", 
    type=ac.INT
)
@ac.argument(
    "pre2", 
    type=ac.INT
)
@ac.argument(
    "pre1", 
    type=ac.INT
)
@ac.argument(
    "main", 
    type=ac.INT
)
@ac.argument(
    "post1", 
    type=ac.INT
)
async def txtap_set(
    lane: int,
    pre3: int,
    pre2: int,
    pre1: int,
    main: int,
    post1: int
) -> str:
    """
    Read the tap values of the specified lane of the local port.
    
        LANE INT: The lane index to read tap values from.\n
        PRE3 INT: c(-3) value of the tap.\n
        PRE2 INT: c(-2) value of the tap.\n
        PRE1 INT: c(-1) value of the tap.\n
        MAIN INT: c(0) value of the tap.\n
        POST1 INT: c(+1) value of the tap.\n

    """
    port_obj = tp_storage.get_working_port()
    dict = await anlt_utils.txtap_set(port_obj, lane, pre3, pre2, pre1, main, post1)
    return dict
    #TODO: Needs to be implemented for display


#**************************
# sub-command: link_recover
#**************************
@anlt.command(cls=cb.XenaCommand)
@ac.option(
    '--on/--off',
    '-o/ ',
    is_flag=True,
    help="Should xenaserver automatically do link recovery when detecting down signal, "
    "default to False. "
    "e.g. lt --on",
    default=False,
)
@try_wrapper(False)
async def link_recover(
    on: bool
    ) -> None:
    """
    Configures link training on the working port.
    """
    port_obj = tp_storage.get_working_port()
    await anlt_utils.link_recovery(port_obj, on)
    return None


#**************************
# sub-command: status
#**************************
@anlt.command(cls=cb.XenaCommand)
async def status(
) -> str:
    """
    Show the overview of ANLT status.\n

    """
    port_obj = tp_storage.get_working_port()
    status = await anlt_utils.status(port_obj)
    return status
    #TODO: Needs to be implemented for display


























