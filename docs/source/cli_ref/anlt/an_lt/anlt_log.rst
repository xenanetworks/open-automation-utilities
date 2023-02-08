anlt log
========

Description
-----------

To start writing the link training trace log for the specified lane into a file, and display on the screen.



Synopsis
--------

.. code-block:: console
    
    anlt log <FILENAME>


Arguments
---------

``<FILENAME>`` (text)

Filename of the log.


Options
-------

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

.. code-block:: console

    xoa_util[port0/2]$ anlt log "log0.txt" --keep=lt --lane 0,1,5


    time: 19700101-000505.350588,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: tx,
        pkt:
        state: prev,
        value: 0x021A0A30,
        count: 0

    time: 19700101-000505.350600,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: tx,
        pkt:
        state: new,
        value: 0x021A0AB2,
        fields:
            control:
            C_REQ: Dec,
            C_SEL: c(-2),
            PAM_MOD: PAM4,
            IC_REQ: INDV
            ,
            status:
            C_STS: C lim,
            C_ECH: c(-2),
            PAM_MOD: PAM4,
            IC_STS: No upd
            ,
            locked: true,
            done: false

    time: 19700101-000505.350621,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: rx,
        pkt:
        state: prev,
        value: 0x021A0A30,
        count: 182

    time: 19700101-000505.350633,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: rx,
        pkt:
        state: new,
        value: 0x021A0AB2,
        fields:
            control:
            C_REQ: Dec,
            C_SEL: c(-2),
            PAM_MOD: PAM4,
            IC_REQ: INDV,
            status:
            C_STS: C lim,
            C_ECH: c(-2),
            PAM_MOD: PAM4,
            IC_STS: No upd,
            locked: true,
            done: false

    time: 19700101-000505.350657,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: tx,
        pkt:
        state: prev,
        value: 0x021A0AB2,
        count: 0

    time: 19700101-000505.350669,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: tx,
        pkt:
        state: new,
        value: 0x02180A32,
        fields:
            control:
            C_REQ: Hold,
            C_SEL: c(-2),
            PAM_MOD: PAM4,
            IC_REQ: INDV
            ,
            status:
            C_STS: C lim,
            C_ECH: c(-2),
            PAM_MOD: PAM4,
            IC_STS: No upd
            ,
            locked: true,
            done: false

    time: 19700101-000505.350690,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: rx,
        pkt:
        state: prev,
        value: 0x021A0AB2,
        count: 214

    time: 19700101-000505.350702,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: rx,
        pkt:
        state: new,
        value: 0x02180A32,
        fields:
            control:
            C_REQ: Hold,
            C_SEL: c(-2),
            PAM_MOD: PAM4,
            IC_REQ: INDV
            ,
            status:
            C_STS: C lim,
            C_ECH: c(-2),
            PAM_MOD: PAM4,
            IC_STS: No upd
            ,
            locked: true,
            done: false

    time: 19700101-000505.350715,
    module: LT,
    lane: 3,
    type: trace,
    entry:
        direction: tx,
        pkt:
        state: prev,
        value: 0x02180A32,
        count: 0












