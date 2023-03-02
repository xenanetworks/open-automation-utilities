debug lt-status
======================

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug lt-status



Synopsis
--------

.. code-block:: text

    debug lt-status <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver serdes index.


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug lt-status 0

    xoa-utils[123456][port0/2] >






