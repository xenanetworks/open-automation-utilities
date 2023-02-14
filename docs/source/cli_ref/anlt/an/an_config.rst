an config
=========

.. important::

    This command only changes the local ANLT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

To configure auto-negotiation on the working port.



Synopsis
--------

.. code-block:: text
    
    an config
    [--on/--off]
    [--loopback/--no-loopback]


Arguments
---------


Options
-------

``--on/--off``
    
Enable or disable auto-negotiation on the working port, default to ``--on``.

``--loopback/--no-loopback``

Should loopback be allowed in auto-negotiation, default to ``--no-loopback``.


Examples
--------

.. code-block:: text
    :caption: Autoneg should be enabled and allow loopback

    xoa-utils[123456][port0/2] > an config --on --loopback
    Port 0/2 auto-negotiation: on, loopback: allowed

    xoa-utils[123456][port0/2] >
    
.. code-block:: text
    :caption: Autoneg should be disabled

    xoa-utils[123456][port0/2] > an config --off
    Port 0/2 auto-negotiation: on, loopback: not allowed

    xoa-utils[123456][port0/2] >






