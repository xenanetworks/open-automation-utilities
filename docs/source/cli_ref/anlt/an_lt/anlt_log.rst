anlt log
========

Description
-----------

To start writing the link training trace log for the specified lane into a file, and display on the screen.



Synopsis
--------

.. code-block:: text
    
    anlt log


Arguments
---------


Options
-------

``-f, --filename`` (text)

Specifies the filename for the log messages to be stored.


``-k, --keep`` (text)
    
Specifies what types of log entries to keep, default to keep all.

Allowed values:

* `all`, to keep all.

* `an`. to keep autoneg only.

* `lt`, to keep lt only.


``-l, --lane`` (int list)
    
Specifies which lanes of LT logs to keep. If you don't know how many serdes lanes the port has, use :doc:`../an_lt/anlt_log`, default to all lanes.


Examples
--------

.. code-block:: text

    xoa_util[123456][port0/2] > anlt log "log0.txt"

    {"time":7130745,"module":"PORT","lane":0,"type":"debug","entry":{"log":"Version: EA410100, feature: 3"}}
    {"time":7397844,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"XFSM_EVENT_SELF","current":"UNKNOWN","new":"AN_GOOD"}}}

    {"time":573514045,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"XFSM_EVENT_SELF","current":"AN_GOOD","new":"UNKNOWN"}}}
    {"time":573514876,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_INIT_DONE","current":"UNKNOWN","new":"WAIT_ANEG_ENABLE"}}}
    {"time":573514925,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_AUTONEG_ENABLE","current":"WAIT_ANEG_ENABLE","new":"TRANSMIT_DISABLE"}}}
    {"time":573514936,"module":"ANEG","lane":0,"type":"trace","entry":{"log":"TRANSMIT_DISABLE - ANEG restart"}}
    {"time":573514943,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"tx","pkt":{"state":"prev","value":"0x000000000000","count":65535}}}
    {"time":573514955,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"tx","pkt":{"state":"new","value":"0x102000060001","type":"base page","fields":{"NP":"0x0","Ack":"0x0","RF":"0x0","TN":"0x6","EN":"0x0","C":"0x0","fec":["25G RS-FEC"],"ability":["100GBASE_KR1"]}}}}
    {"time":573581479,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_BREAK_LINK_TIMER_DONE","current":"TRANSMIT_DISABLE","new":"ABILITY_DETECT"}}}
    {"time":573581511,"module":"ANEG","lane":0,"type":"trace","entry":{"log":"SYNC=true, SYNC LOST=true, NEW_PAGE=true"}}
    {"time":573581520,"module":"ANEG","lane":0,"type":"trace","entry":{"log":"RX is active"}}
    {"time":573581528,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"rx","pkt":{"state":"prev","value":"0x000000000000","count":0}}}
    {"time":573581539,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"rx","pkt":{"state":"new","value":"0x102000060001","type":"base page","fields":{"NP":"0x0","Ack":"0x0","RF":"0x0","TN":"0x6","EN":"0x0","C":"0x0","fec":["25G RS-FEC"],"ability":["100GBASE_KR1"]}}}}
    {"time":573581572,"module":"ANEG","lane":0,"type":"trace","entry":{"log":"SYNC=true, SYNC LOST=false, NEW_PAGE=true"}}
    {"time":573581602,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_ABILITY_MATCH_N_NONCE","current":"ABILITY_DETECT","new":"ACKNOWLEDGE_DETECT"}}}
    {"time":573581612,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"tx","pkt":{"state":"prev","value":"0x102000060001","count":65535}}}
    {"time":573581625,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"tx","pkt":{"state":"new","value":"0x1020000640C1","type":"base page","fields":{"NP":"0x0","Ack":"0x1","RF":"0x0","TN":"0x6","EN":"0x6","C":"0x0","fec":["25G RS-FEC"],"ability":["100GBASE_KR1"]}}}}
    {"time":573581639,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"rx","pkt":{"state":"prev","value":"0x102000060001","count":355}}}
    {"time":573581652,"module":"ANEG","lane":0,"type":"trace","entry":{"direction":"rx","pkt":{"state":"new","value":"0x1020000640C1","type":"base page","fields":{"NP":"0x0","Ack":"0x1","RF":"0x0","TN":"0x6","EN":"0x6","C":"0x0","fec":["25G RS-FEC"],"ability":["100GBASE_KR1"]}}}}
    {"time":573581684,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_ACKNOWLEDGE_DETECT","current":"ACKNOWLEDGE_DETECT","new":"COMPLETE_ACKNOWLEDGE"}}}
    {"time":573581714,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_ACK_N_NP","current":"COMPLETE_ACKNOWLEDGE","new":"AN_GOOD_CHECK"}}}
    {"time":573581723,"module":"ANEG","lane":0,"type":"debug","entry":{"log":"O:102000000000|000000000000 R:1020000640C1|000000000000"}}
    {"time":573581743,"module":"ANEG","lane":0,"type":"debug","entry":{"log":"HCD=16"}}
    {"time":573581772,"module":"PORT","lane":0,"type":"debug","entry":{"log":"LT on 0x1"}}
    {"time":573581784,"module":"ANEG","lane":0,"type":"fsm","entry":{"fsm":{"event":"EVENT_LINK_HCD_OK","current":"AN_GOOD_CHECK","new":"AN_GOOD"}}}

    xoa_util[123456][port0/2] !











