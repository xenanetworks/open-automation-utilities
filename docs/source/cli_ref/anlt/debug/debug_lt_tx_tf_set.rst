debug lt_tx_tf_set
======================

.. important::
    
    To debug on a lane, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug lt_tx_tf_set



Synopsis
--------

.. code-block:: console

    debug lt_tx_tf_set <LANE>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ debug lt_tx_tf_set 0

    xoa_util[port0/2]$






