an config
=========

Description
-----------

To configure auto-negotiation on the working port.



Synopsis
--------

.. code-block:: console
    
    an config
    [--on/--off]
    [--loopback/--no-loopback]


Arguments
---------


Options
-------

``--on/--off``
    
    Enable or disable auto-negotiation on the working port, default to `--on`.

``--loopback/--no-loopback``

    Should loopback be allowed in auto-negotiation, default to `--no-loopback`.


Examples
--------

.. code-block:: console
    :caption: Autoneg should be enabled and allow loopback

    xoa_util[port0/2]$ an config --on --loopback
    Port 0/2 auto-negotiation\: on, loopback\: allowed

    xoa_util[port0/2]$
    
.. code-block:: console
    :caption: Autoneg should be disabled

    xoa_util[port0/2]$ an config --off
    Port 0/2 auto-negotiation\: on, loopback\: not allowed

    xoa_util[port0/2]$






