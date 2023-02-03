exit
====


Description
-----------

To exit the session by terminating port reservations, disconnecting from the chassis, releasing system resources, and removing the specified port configurations.
This command works in all context.

Synopsis
--------

.. code-block:: console
    
    exit
    [--reset/--no-reset]
    [--release/--no-release]


Arguments
---------


Options
-------

``--reset/--no-reset`` 
    
Removes all port configurations of the ports in `--ports` after reservation, default to `--reset`.


``--release/--no-release``

Determines whether the ports should be released before exiting, default to `--release`.



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ exit

    xoa_util[port0/0]$