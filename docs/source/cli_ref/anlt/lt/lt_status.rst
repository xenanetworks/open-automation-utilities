lt status
=========

Description
-----------

Show the link training status of the specified lane.



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
    
    Is enabled        : true
    Is trained        : true
    Failure           : no_failure

    Initial mod.      : nrz
    Preset0           : standard tap values
    Total bits        : 2,201,372,480
    Total err. bits   : 24
    BER               : 1.09e-08

    Duration          : 2,000,250 µs

    Lock lost         : 2
    Frame lock        : locked
    Remote frame lock : locked

    Frame errors      : 1
    Overrun errors    : 1

    Last IC received  : Preset 3
    Last IC sent      : Preset 3

    TX Coefficient              :          c(-3)       c(-2)       c(-1)        c(0)        c(1)
        Current level           :              0           0           1          44           0
                                :         RX  TX      RX  TX      RX  TX      RX  TX      RX  TX
        + req                   :          0   0       0   0       2   2       1   1       0   0
        - req                   :          0   0       0   0       2   2       0   0       0   0
        coeff/eq limit reached  :          0   0       0   0       0   0       0   0       0   0
        eq limit reached        :          0   0       0   0       0   0       0   0       0   0
        coeff not supported     :          0   0       0   0       0   0       0   0       0   0
        coeff at limit          :          0   0       0   0       0   0       0   0       0   0

    xoa-utils[123456][port0/2] >




