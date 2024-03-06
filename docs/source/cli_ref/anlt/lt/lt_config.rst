lt config
=========

.. important::

    This command only changes the local LT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_start`, otherwise your changes will not take effect on the tester.

Description
-----------

Configure LT for the working port.


Synopsis
--------

.. code-block:: text

    lt config
    [--on/--off]
    [-m, --mode <value: text>]
    [--preset0 <value: text>]
    [--timeout <value: text>]


Arguments
---------


Options
-------

``--on/--off``

Enable or disable link training on the working port, default to ``--on``.


``-m, --mode`` (text)

The mode for link training on the working port, default to ``auto``.

Allowed values:

* `auto`:           link training procedures are done by the port.

* `interactive`:    link training procedures requires manual operation.


``--preset0`` (text)

The preset0 mode, default to `standard``.

Allowed values:

* `standard`:    Use standard tap values as preset0

* `existing`:    Use the existing tap values as preset0


``--timeout`` (text)

Timeout mode, default to `enable``.

Allowed values:

* `enable`:    Enable timeout for LT auto

* `disable`:   Disable timeout for LT auto


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt config --on --preset0=existing --mode=interactive --timeout disable
    
    LT configuration to be on port 2/0
    [SHADOW CONFIG]
        Auto-negotiation      : off (allow loopback: no)
        Link training         : on (interactive) (preset0: existing tap values)

    xoa-utils[123456][port0/2] >





