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


    | TIMESTAMP                |  MODULE  |  TYPE |               TX                |                   RX                  |                                       |
    |--------------------------+----------+-------+---------------------------------+---------------------------------------+---------------------------------------|
    | 20230131-134059.150943   |     LT   | TRACE |                                 |                                       | LOCK=true                             |
    |                          |          |       |                                 |                                       | SYNC LOST=true                        |
    |                          |          |       |                                 |                                       | NEW_FRAME=true                        |
    |                          |          |       |                                 |                                       | OVERRUN=false                         |
    |--------------------------+----------+-------+---------------------------------+---------------------------------------+---------------------------------------|
    | 20230131-134060.100000   |     LT   | TRACE | value = 0x3A824608              |                                       |                                       |
    |                          |          |       | control:                        |                                       |                                       |
    |                          |          |       |   REQ: Dec                      |                                       |                                       |
    |                          |          |       |   SEL: c(0)                     |                                       |                                       |
    |                          |          |       |   MOD: PAM4                     |                                       |                                       |
    |                          |          |       |   IC: Indv                      |                                       |                                       |
    |                          |          |       | status:                         |                                       |                                       |
    |                          |          |       |   STS: No upd                   |                                       |                                       |
    |                          |          |       |   ECH: c(1)                     |                                       |                                       |
    |                          |          |       |   MOD: PAM4                     |                                       |                                       |
    |                          |          |       |   IC: No upd                    |                                       |                                       |
    |                          |          |       | locked: true                    |                                       |                                       |
    |                          |          |       | Done: false                     |                                       |                                       |
    |                          |          |       | Errors:                         |                                       |                                       |
    |                          |          |       |   Control bit 7:5 not 0         |                                       |                                       |
    |                          |          |       |   Status bit 14:12 not 0        |                                       |                                       |
    |--------------------------+----------+-------+---------------------------------+---------------------------------------+---------------------------------------|
    | 20230131-134060.100000   |     LT   | TRACE |                                 | value = 0x3A824608                    |                                       |
    |                          |          |       |                                 | control:                              |                                       |
    |                          |          |       |                                 |   REQ: Dec                            |                                       |
    |                          |          |       |                                 |   SEL: c(0)                           |                                       |
    |                          |          |       |                                 |   MOD: PAM4                           |                                       |
    |                          |          |       |                                 |   IC: Indv                            |                                       |
    |                          |          |       |                                 | status:                               |                                       |
    |                          |          |       |                                 |   STS: No upd                         |                                       |
    |                          |          |       |                                 |   ECH: c(1)                           |                                       |
    |                          |          |       |                                 |   MOD: PAM4                           |                                       |
    |                          |          |       |                                 |   IC: No upd                          |                                       |
    |                          |          |       |                                 | locked: true                          |                                       |
    |                          |          |       |                                 | Done: false                           |                                       |
    |                          |          |       |                                 | Errors:                               |                                       |
    |                          |          |       |                                 |   Control bit 7:5 not 0               |                                       |
    |                          |          |       |                                 |   Status bit 14:12 not 0              |                                       |
    |--------------------------+----------+-------+---------------------------------+---------------------------------------+---------------------------------------|
    | 20230131-134060.100000   |     LT   | FSM   |                                 |                                       | STATE CHANGE: (EVENT_RESET_DEASSERT)  |
    |                          |          |       |                                 |                                       |    IDLE->INITIALIZE                   |
    |--------------------------+----------+-------+---------------------------------+---------------------------------------+---------------------------------------|














