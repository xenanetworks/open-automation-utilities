lt alg
======

.. important::

    This command only changes the local LT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_start`, otherwise your changes will not take effect on the tester.

Description
-----------

Set the link training algorithm for the specified serdes.



Synopsis
--------

.. code-block:: text
    
    lt alg <SERDES> <ALGORITHM>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


``<ALGORITHM>`` (text)
    
Specifies the algorithm.

Allowed values:

* `alg0`

* `algn1`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt alg 0 alg0
    
    Initial modulation to be NRZ on Serdes 0
    [SHADOW CONFIG]
        Auto-negotiation      : off (allow loopback: no)
        Link training         : on (interactive) (preset0: standard tap values)
            Algorithm         : {'0': 'ALG0'}

    xoa-utils[123456][port0/2] >


