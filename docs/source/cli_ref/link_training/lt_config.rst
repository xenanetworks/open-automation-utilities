lt config
=========

Description
-----------

To configure link training on the working port.



Synopsis
--------

.. code-block:: console
    
    lt config
    [-m, --mode <value: text>] 
    [--preset0/--no-preset0]
    [--on/--off]


Arguments
---------


Options
-------

``-m, --mode`` (text)
    
    The mode for link training on the working port, default to `interactive`.
    Allowed values:
    
        `interactive`: link training procedures requires manual operation.
        `auto`: link training procedures are done by the port.

``--on/--off``
    
    Enable or disable link training on the working port, default to `--on`.

``--preset0/--no-preset0``

    Should the preset0 (out-of-sync) use existing tap values or standard values, default to `--no-preset0`.




Examples
--------

.. code-block:: console

    xoa_util[port0/2][lt]$ config --on --preset0 --mode=interactive
    Port 0/2
    Link training : on
    Mode          : interactive
    Preset0       : existing tap values

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2][lt]$ config --off
    Port 0/2
    Link training : off
    Mode          : interactive
    Preset0       : standard tap values

    xoa_util[port0/2][lt]$

.. code-block:: console

    xoa_util[port0/2][lt]$ config 
    Port 0/2
    Link training : on
    Mode          : interactive
    Preset0       : standard tap values

    xoa_util[port0/2][lt]$




