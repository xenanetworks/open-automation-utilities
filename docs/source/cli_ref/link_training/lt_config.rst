lt config
=========

Description
-----------

To configure link training on the working port.
This command also enter `lt` context from the port.


Synopsis
--------

.. code-block:: console
    
    lt config
    [-m, --mode <value: text>] 
    [--preset0/--no-preset0]
    [--timeout/--no-timeout]


Arguments
---------


Options
-------

``-m, --mode`` (text)
    
    The mode for link training on the working port, default to `autocomplete`.
    Allowed values: 
        `interactive`: to set the port to manually perform link training procedure.
        `autostart`: to set the port to start link training automatically after auto-negotiation. Requires auto-negotiation is enabled. 
        `autocomplete`: to set the port to start link training without performing auto-negotiation.
        `disable`: to set the port to stop link training.

    e.g. `--mode interactive`

``--preset0/--no-preset0``

    Should the preset0 (out-of-sync) use existing tap values or standard values, default to `--no-preset0`.
    e.g. `--preset0`

``--timeout/--no-timeout``

    Should link training run with or without timeout, default to `--no-preset0`.
    e.g. `--preset0`


Examples
--------

.. code-block:: console

    xoa_util[port0/2][lt]$ config --mode=autocomplete --preset0 --no-timeout
    Port 0/2 link training mode=autocomplete, preset0=existing tap values, w/o timeout

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2][lt]$ config --mode=autostart --no-preset0 --timeout
    Port 0/2 link training mode=autostart, preset0=standard tap values, w/ timeout

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2][lt]$ config 
    Port 0/2 link training mode=autocomplete, preset0=standard tap values, w/o timeout

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2]$ lt config 
    Port 0/2 link training mode=autocomplete, preset0=standard tap values, w/o timeout

    xoa_util[port0/2][lt]$



