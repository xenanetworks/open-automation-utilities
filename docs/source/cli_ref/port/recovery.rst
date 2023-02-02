recovery
===========

Description
-----------

Enable/disable link recovery on the specified port.
If enable, the port will keep trying ANLT when no link-up signal is detected after five seconds of waiting.


Synopsis
--------

.. code-block:: console
    
    recovery
    [--on/--off]


Arguments
---------


Options
-------

``--on/--off``

    Should xenaserver automatically do link recovery when detecting down signal, default to `--on`.


Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ recovery
    Port 0/2 link recovery enabled

    xoa_util[port0/2]$




