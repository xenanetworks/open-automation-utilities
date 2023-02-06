lt txtapset
===========

Description
-----------

Read the tap values of the specified lane of the local port.



Synopsis
--------

.. code-block:: console
    
    lt txtapget <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


Options
-------

``--pre3``
    
Specifies c(-3) value of the tap.

``--pre2``
    
Specifies c(-2) value of the tap.

``--pre1``
    
Specifies c(-1) value of the tap.

``--main``
    
Specifies c(0) value of the tap.

``--post1``
    
Specifies c(+1) value of the tap.


Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt txtapset 5 --pre3=1
    Local Coefficient Lane(5)   :           c(-3)       c(-2)       c(-1)       c(0)       c(+1)
        Current level           :              1          17           0           0           0


    xoa_util[port0/2]$ lt txtapset 5 --pre=5
    Local Coefficient Lane(5)   :           c(-3)       c(-2)       c(-1)       c(0)       c(+1)
        Current level           :              1          17           5           0           0

    xoa_util[port0/2][lt]$


.. code-block:: console

    xoa_util[port0/2]$ lt txtapset 5 --main=80 --pre2=6
    Local Coefficient Lane(5)   :           c(-3)       c(-2)       c(-1)       c(0)       c(+1)
        Current level           :              1           6           5          80           0

    xoa_util[port0/2]$




