lt txtapset
===========

Description
-----------

Write the tap values of the specified serdes of the local port.



Synopsis
--------

.. code-block:: text
    
    lt txtapget <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the serdes index.

``<PRE3>`` (integer)

Specifies c(-3) value of the tap.

``<PRE2>`` (integer)

Specifies c(-2) value of the tap.

``<PRE>``  (integer)

Specifies c(-1) value of the tap.

``<MAIN>`` (integer)

Specifies c(0) value of the tap.

``<POST>`` (integer)

Specifies c(1) value of the tap.


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt txtapset 5 1 6 5 80 0
    
    Local Coefficient Serdes(5) :           c(-3)       c(-2)       c(-1)       c(0)        c(1)
        Current level           :              1           6           5          80           0

    xoa-utils[123456][port0/2] >




