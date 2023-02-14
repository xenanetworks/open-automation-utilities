lt txtapget
===========

Description
-----------

Read the tap values of the specified lane of the local port.



Synopsis
--------

.. code-block:: text
    
    lt txtapget <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


Options
-------


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt txtapget 0
    Local Coefficient Lane(0)   :           c(-3)       c(-2)       c(-1)       c(0)        c(1)
        Current level           :              0           7           0           0           0

    xoa-utils[123456][port0/2] >




