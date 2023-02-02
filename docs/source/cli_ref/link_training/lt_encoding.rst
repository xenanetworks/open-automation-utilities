lt encoding
============

Description
-----------

To request the remote link training partner to use the specified encoding on the specified lane.



Synopsis
--------

.. code-block:: console
    
    lt encoding <LANE> <ENCODING>


Arguments
---------

``<LANE>`` (integer)

    Specifies the transceiver lane index.


``<ENCODING>`` (text)
    
    Specifies the encoding.
    Allowed values: `nrz / pam2 | pam4 | pam4pre`


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2][lt]$ encoding 0 nrz
    Port 0/2 requests: use NRZ/PAM2 on Lane 0

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2][lt]$ encoding 0 pam2
    Port 0/2 requests: use NRZ/PAM2 on Lane 0

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2][lt]$ encoding 4 pam4
    Port 0/2 requests: use PAM4 on Lane 4

    xoa_util[port0/2][lt]$+

.. code-block:: console

    xoa_util[port0/2][lt]$ lt_encoding 3 pam4pre
    Port 0/2 requests: use PAM4_WITH_PRECODING on Lane 3

    xoa_util[port0/2][lt]$



