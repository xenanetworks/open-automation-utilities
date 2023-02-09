debug lt_rx_analyzer_rd_page_get
================================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug lt_rx_analyzer_rd_page_get



Synopsis
--------

.. code-block:: text

    debug lt_rx_analyzer_rd_page_get <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: text

    xoa_util[port0/2]$ debug lt_rx_analyzer_rd_page_get 0

    xoa_util[port0/2]$






