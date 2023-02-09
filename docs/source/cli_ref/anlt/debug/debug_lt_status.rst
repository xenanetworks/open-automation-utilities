debug lt_status
======================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug lt_status



Synopsis
--------

.. code-block:: text

    debug lt_status <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: text

    xoa_util[port0/2]$ debug lt_status 0

    xoa_util[port0/2]$






