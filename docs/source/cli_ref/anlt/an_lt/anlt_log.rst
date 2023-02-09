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

    xoa_util[port0/2]$ anlt log "log0.txt"

            time: 84552988935,
            module: ANEG,
            lane: 0,
            type: fsm,
            entry: 
                fsm: 
                event: EVENT_BREAK_LINK_TIMER_DONE,
                current: TRANSMIT_DISABLE,
                new: ABILITY_DETECT
    --------------------------------------------------

    time: 84552988948,
    module: ANEG,
    lane: 0,
    type: trace,
    entry: 
        log: SYNC=true, SYNC LOST=true, NEW_PAGE=true
    --------------------------------------------------

    time: 84552988958,
    module: ANEG,
    lane: 0,
    type: trace,
    entry: 
        log: RX is active
    --------------------------------------------------

    time: 84552988968,
    module: ANEG,
    lane: 0,
    type: trace,
    entry: 
        direction: rx,
        pkt: 
        state: prev,
        value: 0x1080000D0001,
        count: 274
    --------------------------------------------------
    
    time: 84552988982,
    module: ANEG,
    lane: 0,
    type: trace,
    entry: 
        direction: rx,
        pkt: 
        state: new,
        value: 0x1080001F0001,
        type: base page,
        fields: 
            NP: 0x0,
            Ack: 0x0,
            RF: 0x0,
            TN: 0x1f,
            EN: 0x0,
            C: 0x0,
            fec: [
            25G BASE-R FEC
            ],
            ability: [
            400GBASE_KR4
            ]
    --------------------------------------------------

                                    time: 84552989050,
                                    module: ANEG,
                                    lane: 0,
                                    type: trace,
                                    entry: 
                                        direction: tx,
                                        pkt: 
                                        state: prev,
                                        value: 0x1080001F0001,
                                        count: 65535
    --------------------------------------------------

                                    time: 84552989064,
                                    module: ANEG,
                                    lane: 0,
                                    type: trace,
                                    entry: 
                                        direction: tx,
                                        pkt: 
                                        state: new,
                                        value: 0x108000100001,
                                        type: base page,
                                        fields: 
                                            NP: 0x0,
                                            Ack: 0x0,
                                            RF: 0x0,
                                            TN: 0x10,
                                            EN: 0x0,
                                            C: 0x0,
                                            fec: [
                                            25G BASE-R FEC
                                            ],
                                            ability: [
                                            400GBASE_KR4
                                            ]












