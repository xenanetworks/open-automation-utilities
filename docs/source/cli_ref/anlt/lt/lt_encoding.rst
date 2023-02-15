lt encoding
============

Description
-----------

To request the remote link training partner to use the specified encoding on the specified lane.



Synopsis
--------

.. code-block:: text
    
lt encoding <LANE> <ENCODING>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


``<ENCODING>`` (text)
    
Specifies the encoding.

Allowed values:

* `nrz`

* `pam4`

* `pam4pre`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt encoding 0 nrz
    Port 0/2 requests: use NRZ on Lane 0

    xoa-utils[123456][port0/2] >

.. code-block:: text

    xoa-utils[123456][port0/2] > lt encoding 4 pam4
    Port 0/2 requests: use PAM4 on Lane 4

    xoa-utils[123456][port0/2] >

.. code-block:: text

    xoa-utils[123456][port0/2] > lt encoding 3 pam4pre
    Port 0/2 requests: use PAM4_WITH_PRECODING on Lane 3

    xoa-utils[123456][port0/2] >



