debug lt_rx_analyzer_config_get
===============================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.


Description
-----------

Debug lt_rx_analyzer_config_get


Synopsis
--------

.. code-block:: console

    debug lt_rx_analyzer_config_get <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ debug lt_rx_analyzer_config_get 0

    xoa_util[port0/2]$






