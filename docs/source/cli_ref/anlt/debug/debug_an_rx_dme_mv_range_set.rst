debug an-rx-dme-mv-range-set
============================

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug an-rx-dme-mv-range-set



Synopsis
--------

.. code-block:: text

    debug an-rx-dme-mv-range-set <SERDES> <VALUE>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


``<VALUE>`` (integer)


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug an-rx-dme-mv-range-set 0 1234

    xoa-utils[123456][port0/2] >






