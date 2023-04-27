debug init
==========

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.


Description
-----------

Initialize debug


Synopsis
--------

.. code-block:: text

    debug init <SERDES>


Arguments
---------

``<SERDES>`` (integer)

Specifies the transceiver serdes index


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug init 0

    xoa-utils[123456][port0/2] >


