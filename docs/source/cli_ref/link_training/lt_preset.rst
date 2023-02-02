lt preset
=========

Description
-----------

To request the remote link training partner to use the preset of the specified lane.



Synopsis
--------

.. code-block:: console
    
    lt preset <LANE> <PRESET>


Arguments
---------

``<LANE>`` (integer)

    Specifies the transceiver lane index.


``<PRESET>`` (integer)
    
    Specifies the preset index. 
    Allowed values: `1, 2, 3, 4, 5`


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt preset 0 1
    Port 0/2 requests: use preset 1 on Lane 0

    xoa_util[port0/2]$

.. code-block:: console

    xoa_util[port0/2]$ lt preset 2 3
    Port 0/2 requests: use preset 3 on Lane 2

    xoa_util[port0/2]$

.. code-block:: console

    xoa_util[port0/2]$ lt preset 2 3
    Port 0/2 requests: use preset 3 on Lane 2

    xoa_util[port0/2]$



