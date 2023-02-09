debug lt_tx_config_set
======================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug lt_tx_config_set



Synopsis
--------

.. code-block:: text

    debug lt_tx_config_set <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: text

    xoa_util[port0/2]$ debug lt_tx_config_set 0

    xoa_util[port0/2]$






