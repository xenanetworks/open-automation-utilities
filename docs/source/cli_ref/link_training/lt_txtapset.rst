lt txtapset
===========

Description
-----------

Read the tap values of the specified lane of the local port.
This command also enter `lt` context from the port.


Synopsis
--------

.. code-block:: console
    
    lt txtapget <LANE> <PRE3> <PRE2> <PRE1> <MAIN> <POST1>


Arguments
---------

``<LANE>`` (integer)

    Specifies the lane index.

``<PRE3>`` (integer)

    Specifies c(-3) value of the tap.

``<PRE2>`` (integer)

    Specifies c(-2) value of the tap.

``<PRE1>`` (integer)

    Specifies c(-1) value of the tap.

``<MAIN>`` (integer)

    Specifies c(0) value of the tap.

``<POST1>`` (integer)

    Specifies c(+1) value of the tap.


Options
-------


Examples
--------

.. code-block:: console

    xoa_util[port0/2][lt]$ txtapset 5 0 17 0 0 0
    Local Coefficient Lane(5)   :           c(-3)       c(-2)       c(-1)       c(0)       c(+1)
        Current level           :              0          17           0           0           0

    xoa_util[port0/2][lt]$




