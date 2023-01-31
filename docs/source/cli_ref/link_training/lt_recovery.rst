lt recovery
===========

Description
-----------

To set link recovery configuration on the working port.
This command also enter `lt` context from the port.


Synopsis
--------

.. code-block:: console
    
    lt recovery
    [--on/--off]


Arguments
---------


Options
-------

``--on/--off``

    Should xenaserver automatically do link recovery when detecting down signal, default to `--off`.


Examples
--------

.. code-block:: console

    xoa_util[port0/2][lt]$ recovery
    Port 0/2 link recovery disabled

    xoa_util[port0/2][lt]$




