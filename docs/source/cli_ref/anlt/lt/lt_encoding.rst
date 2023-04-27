lt encoding
============

Description
-----------

Request the remote link training partner to use the specified encoding on the specified serdes.



Synopsis
--------

.. code-block:: text
    
    lt encoding <SERDES> <ENCODING>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


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

    xoa-utils[123456][port0/2] > lt encoding 0 pam4
    Port 0/0: use PAM4 on Serdes 0 (SUCCESS)

    xoa-utils[123456][port0/2] >



