debug px-get
======================

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug px-get



Synopsis
--------

.. code-block:: text

    debug px-get <PAGE_ADDRESS> <REG_ADDRESS>


Arguments
---------

``<PAGE_ADDRESS>`` (integer)

``<REG_ADDRESS>`` (string)


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug px-get 2000 0x2f505






