lt config
=========

.. important::

    This command only changes the local ANLT configuration state. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

To configure link training on the working port.



Synopsis
--------

.. code-block:: text

    lt config
    [-m, --mode <value: text>]
    [--preset0 <value: text>]
    [--on/--off]


Arguments
---------


Options
-------

``-m, --mode`` (text)

The mode for link training on the working port, default to ``interactive``.

Allowed values:

* `interactive`:    link training procedures requires manual operation.

* `auto`:           link training procedures are done by the port.



``--on/--off``

Enable or disable link training on the working port, default to ``--on``.


``--preset0`` (text)

The preset0 mode, default to ``standard``.

Allowed values:

* `standard`:    Use standard tap values as preset0

* `existing`:    Use the existing tap values as preset0




Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt config --on --preset0=existing --mode=interactive
    Port 0/2
    Link training : on
    Mode          : interactive
    Preset0       : existing tap values

    xoa-utils[123456][port0/2] >

.. code-block:: text

    xoa-utils[123456][port0/2] > lt config --off
    Port 0/2
    Link training : off
    Mode          : interactive
    Preset0       : standard tap values

    xoa-utils[123456][port0/2] >

.. code-block:: text

    xoa-utils[123456][port0/2] > lt config
    Port 0/2
    Link training : on
    Mode          : interactive
    Preset0       : standard tap values

    xoa-utils[123456][port0/2] >




