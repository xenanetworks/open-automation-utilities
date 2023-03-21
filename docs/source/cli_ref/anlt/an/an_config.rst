an config
=========

.. important::

    This command only changes the local AN configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

Configure AN of the working port.



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
    
    AN configuration to be on port 2/0
    [SHADOW CONFIG]
        Auto-negotiation      : on (allow loopback: yes)
        Link training         : off (auto) (preset0: standard tap values)
            Initial Mod.      : {}

    xoa-utils[123456][port0/2] >






