an status
=========

Description
-----------

Show the auto-negotiation status of the working port.



Synopsis
--------

.. code-block:: text
    
    an status


Arguments
---------


Options
-------


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > an status                                     
    
    [AN STATUS]
        Mode                  : enabled
        Loopback              : allowed

        Duration              : 2,068,747 µs
        Successful runs       : 1
        Timeouts              : 0
        Loss of sync          : 0

        HCD                   : IEEE_800GBASE_CR8_KR8
        HCD negotiation fails : 0
        FEC result            : RS_FEC_KP
        FEC negotiation fails : 0
        
                                    RX    TX
        Link codewords        :      2     1
        Next-page messages    :      0     0
        Unformatted pages     :      0     0

    xoa-utils[123456][port0/2] >





