lt im
=====

.. important::

    This command only changes the local LT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

Set initial modulation for the specified serdes.



Synopsis
--------

.. code-block:: text
    
    lt im <SERDES> <ENCODING>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


``<ENCODING>`` (text)
    
Specifies the initial modulation.

Allowed values:

* `nrz`

* `pam4`

* `pam4pre`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt im 0 nrz
    
    Initial modulation to be NRZ on Serdes 0
    [ SHADOW CONFIG ]
        Auto-negotiation      : off (allow loopback: no)
        Link training         : on (interactive) (preset0: standard tap values)
            Initial Mod.      : {'0': 'NRZ'}

    xoa-utils[123456][port0/2] >


