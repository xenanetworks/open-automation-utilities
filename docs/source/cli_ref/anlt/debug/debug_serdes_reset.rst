debug serdes-reset
==================

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug, reset the serdes.



Synopsis
--------

.. code-block:: text

    debug serdes-reset <SERDES>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index.


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug serdes-reset 0

    xoa-utils[123456][port0/2] >






