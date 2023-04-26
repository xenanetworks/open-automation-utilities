debug px-set
======================

.. important::
    
    To debug on a serdes, you must always use :doc:`debug_init` command prior to all the other debug commands.

    
Description
-----------

Debug px-set



Synopsis
--------

.. code-block:: text

    debug px-set <PAGE_ADDRESS> <REG_ADDRESS> <VALUE>


Arguments
---------

``<PAGE_ADDRESS>`` (integer)

``<REG_ADDRESS>`` (string)

``<VALUE>`` (string)

Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > debug px-set 2000 0x2f50 0x0101






