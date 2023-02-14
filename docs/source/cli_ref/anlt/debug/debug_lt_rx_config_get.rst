debug lt-rx-config-get
======================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug lt-rx-config-get



Synopsis
--------

.. code-block:: text

    debug lt-rx-config-get <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: text

    xoa_util[123456][port0/2] > debug lt-rx-config-get 0

    xoa_util[123456][port0/2] >






