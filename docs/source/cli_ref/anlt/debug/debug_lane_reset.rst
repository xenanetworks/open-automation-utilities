debug lane-reset
================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug, reset the lane.



Synopsis
--------

.. code-block:: text

    debug lane*reset <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug lane-reset 0

    xoa-utils[123456][port0/2] >






