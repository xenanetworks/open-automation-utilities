lt im
=====

.. important::

    This command only changes the local ANLT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

To set the initial modulation for the lane.



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

    xoa_util[port0/2]$ lt im 0 nrz
    Port 0/2: initial modulation NRZ on Lane 0

    xoa_util[port0/2]$

.. code-block:: text

    xoa_util[port0/2]$ lt im 4 pam4
    Port 0/2: initial modulation PAM4 on Lane 4

    xoa_util[port0/2]$

.. code-block:: text

    xoa_util[port0/2]$ lt im 3 pam4pre
    Port 0/2: initial modulation PAM4_WITH_PRECODING on Lane 3

    xoa_util[port0/2]$



