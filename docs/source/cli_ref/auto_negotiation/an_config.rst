an config
=========

Description
-----------

To configure auto-negotiation on the working port.
This command also enter `an` context from the port.


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

    xoa_util[port0/2]$ an config --enable --loopback
    Port 0/2 auto-negotiation enabled loopback-allowed

    xoa_util[port0/2][an]$
    
.. code-block:: console

    xoa_util[port0/2][an]$ config --disable
    Port 0/2 auto-negotiation disabled no-loopback-allowed

    xoa_util[port0/2][an]$

.. code-block:: console

    xoa_util[port0/2][an]$ config --enable --loopback
    Port 0/2 auto-negotiation enabled loopback-allowed

    xoa_util[port0/2][an]$

.. code-block:: console

    xoa_util[port0/2][an]$ config --enable --no-loopback
    Port 0/2 auto-negotiation enabled no-loopback-allowed

    xoa_util[port0/2][an]$





