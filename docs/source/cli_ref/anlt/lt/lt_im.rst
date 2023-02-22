lt im
=====

.. important::

    This command only changes the local LT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

Set initial modulation for the specified lane.



Synopsis
--------

.. code-block:: text
    
    lt im <LANE> <ENCODING>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


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
    Port 0/2: initial modulation NRZ on Lane 0

    xoa-utils[123456][port0/2] >


