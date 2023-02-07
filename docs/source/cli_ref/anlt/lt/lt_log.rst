lt log
======

Description
-----------

To start writing the link training trace log for the specified lane into a file, and display on the screen.



Synopsis
--------

.. code-block:: console
    
    lt log <LANE> <FILENAME>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


``<FILENAME>`` (text)

Filename of the log.


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt log 0 "log0.txt"

    | timestamp                |   MODULE |  TYPE |                    TX           |              RX                       |                                       |
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














