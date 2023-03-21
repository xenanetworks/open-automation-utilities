lt txtapget
===========

Description
-----------

Read the tap values of the specified serdes of the local port.



Synopsis
--------

.. code-block:: text
    
    lt txtapget <SERDES>


Arguments
---------

``<SERDES>`` (integer)

Specifies the serdes index.


Options
-------


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt txtapget 0

    Local Coefficient Serdes(0) :           c(-3)       c(-2)       c(-1)       c(0)        c(1)
        Current level           :              0           0           0          42           0

    xoa-utils[123456][port0/2] >




