lt im
=====

Description
-----------

To set the initial modulation for the lane.



Synopsis
--------

.. code-block:: console
    
lt im <LANE> <ENCODING>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


``<ENCODING>`` (text)
    
Specifies the initial modulation.

Allowed values:

* `nrz_pam2`

* `pam4`

* `pam4pre`


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt im 0 nrz_pam2
    Port 0/2: initial modulation NRZ_PAM2 on Lane 0

    xoa_util[port0/2]$

.. code-block:: console

    xoa_util[port0/2]$ lt im 4 pam4
    Port 0/2: initial modulation PAM4 on Lane 4

    xoa_util[port0/2]$

.. code-block:: console

    xoa_util[port0/2]$ lt im 3 pam4pre
    Port 0/2: initial modulation PAM4_WITH_PRECODING on Lane 3

    xoa_util[port0/2]$



