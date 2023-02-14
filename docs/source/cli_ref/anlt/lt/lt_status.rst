lt status
=========

Description
-----------

To show the link training status of the specified lane.



Synopsis
--------

.. code-block:: text
    
    lt status <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


Options
-------


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt status 0
    Is Enabled        : true
    Is Trained        : false
    Failure           : no_failure
    
    Initial mode      : 0
    Preset0           : existing
    Total Bits        : 2080985280
    Total Err. Bits   : 2
    PRBS BER          : 9.610832038177609e-10

    Duration          : 10 µs

    Lock lost         : 0
    Frame lock        : lost
    Remote frame lock : lost

    Frame errors      : 4
    Overrun errors    : 7

    Last IC received  : INDV
    Last IC sent      : INDV
    TX Coefficient              :           c(-3)       c(-2)       c(-1)       c(0)        c(1)
        Current level           :              0          68           0           0           0
                                :         RX  TX      RX  TX      RX  TX      RX  TX      RX  TX
        + req                   :          0   0       0   0       0   0       0   0       0   0
        - req                   :          0   0       0   0       0   0       0   0       0   0
        coeff/eq limit reached  :          0   0       0   0       0   0       0   0       0   0
        eq limit reached        :          0   0       0   0       0   0       0   0       0   0
        coeff not supported     :          0   0       0   0       0   0       0   0       0   0
        coeff at limit          :          0   0       0   0       0   0       0   0       0   0

    xoa-utils[123456][port0/2] >




