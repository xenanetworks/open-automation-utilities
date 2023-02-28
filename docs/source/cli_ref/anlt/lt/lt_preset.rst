lt preset
=========

Description
-----------

Request the remote link training partner to use the preset of the specified lane.



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

Allowed values: `1, 2, 3, 4, 5`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt preset 0 1
    Port 0/0: use preset 0 on Lane 0 (SUCCESS)

    xoa-utils[123456][port0/2] >



