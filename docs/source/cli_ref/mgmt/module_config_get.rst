module-config-get
==================

Description
-----------

Get module's media configuration and port speed configuration.

Synopsis
--------

.. code-block:: text
    
    module-config-get <MODULE>


Arguments
---------

``<MODULE>`` (text)

Specifies the module on the specified device host.

Specify a module using the format slot, e.g. 0


Examples
--------

.. code-block:: text

    xoa-utils[123456] > module-config-get 0
    xoa-utils[123456] > osfp800 8 100g osfp800 4 200g osfp800 2 400g osfp800 1 800g
