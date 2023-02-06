debug lane_reset
================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug, reset the lane.



Synopsis
--------

.. code-block:: console

    debug lane_reset <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ debug lane_reset 0

    xoa_util[port0/2]$






