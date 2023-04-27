debug xla-trig-n-dump
=========================

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.


Description
-----------

Debug xla-trig-n-dump



Synopsis
--------

.. code-block:: text

    debug xla-trig-n-dump <SERDES>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


Options
-------

``--mask, -m``

Mask, default to ``0x00000FF0``.


``--window-offset, -o``

Window offset, default to ``0x0080``.


``--trigger-select, -s``

Trigger select, default to ``0x0001``.


``--filename, -f``

Trigger select, default to ``xla_dump.csv``.


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug xla-trig-n-dump

    xoa-utils[123456][port0/2] >






