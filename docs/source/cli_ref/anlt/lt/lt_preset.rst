lt preset
=========

Description
-----------

To request the remote link training partner to use the preset of the specified lane.



Synopsis
--------

.. code-block:: text
    
    lt preset <LANE> <PRESET>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


``<PRESET>`` (integer)
    
Specifies the preset index. 

Allowed values: `0, 1, 2, 3, 4`


Options
-------



Examples
--------

.. code-block:: text

    xoa_util[123456][port0/2] > lt preset 0 1
    Port 0/2 requests: use preset 1 on Lane 0

    xoa_util[123456][port0/2] >

.. code-block:: text

    xoa_util[123456][port0/2] > lt preset 2 3
    Port 0/2 requests: use preset 3 on Lane 2

    xoa_util[123456][port0/2] >

.. code-block:: text

    xoa_util[123456][port0/2] > lt preset 2 3
    Port 0/2 requests: use preset 3 on Lane 2

    xoa_util[123456][port0/2] >



