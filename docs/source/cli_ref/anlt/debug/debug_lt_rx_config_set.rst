debug lt-rx-config-set
======================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.


Description
-----------

Debug lt-rx-config-set



Synopsis
--------

.. code-block:: text

    debug lt-rx-config-set <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: text

    xoa_util[port0/2]$ debug lt-rx-config-set 0

    xoa_util[port0/2]$






