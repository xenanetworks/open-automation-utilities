lt status
=========

Description
-----------

To show the link training status of the specified lane.



Synopsis
--------

.. code-block:: console
    
    lt status <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


Options
-------


Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt status 0
    Is Enabled        : true
    Is Trained        : false
    Failure           : no_failure
    
    Initial mode      : 0
    Preset0           : existing
    PRBS BER          : 2.1234678E-5

    Duration          : 10 us

    Lock lost         : 0
    Frame lock        : lost
    Remote frame lock : lost

    Frame errors      : 4
    Overrun errors    : 7

    Last IC received  : INDV
    Last IC sent      : INDV
    TX Coefficient              :           c(-3)       c(-2)       c(-1)       c(0)       c(+1)
        Current level           :              0          68           0           0           0
                                :         RX  TX      RX  TX      RX  TX      RX  TX      RX  TX
        + req                   :          0   0       0   0       0   0       0   0       0   0
        - req                   :          0   0       0   0       0   0       0   0       0   0
        coeff/eq limit reached  :          0   0       0   0       0   0       0   0       0   0
        eq limit reached        :          0   0       0   0       0   0       0   0       0   0
        coeff not supported     :          0   0       0   0       0   0       0   0       0   0
        coeff at limit          :          0   0       0   0       0   0       0   0       0   0

    xoa_util[port0/2]$




