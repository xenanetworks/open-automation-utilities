module-config
==================

Description
-----------

Set module's media configuration and port speed configuration.

Synopsis
--------

.. code-block:: text
    
    module-config <MODULE> <MEDIA> <PORT_COUNT> <PORT_SPEED>
    [--force/--no-force]


Arguments
---------

``<MODULE>`` (text)

Specifies the module on the specified device host.

Specify a module using the format slot, e.g. 0


``<MEDIA>`` (text)

Specifies the media configuration type of the module.

Allowed values:

* `cfp4`

* `cxp`

* `sfp28`

* `qsfp28_nrz`

* `qsfp28_pam4`

* `qsfp56_pam4`

* `qsfpdd_pam4`

* `sfp56`

* `sfpdd`

* `sfp112`

* `qsfpdd_nrz`

* `cfp`

* `base_t1`

* `base_t1s`

* `qsfpdd800`

* `qsfp112`

* `osfp800`



``<PORT_COUNT>`` (integer)

Specifies the port count of the module.


``<PORT_SPEED>`` (text)

Specifies the port speed in Gbps of the module.

Allowed values:

* `10g`

* `25g`

* `50g`

* `100g`

* `200g`

* `400g`

* `800g`


Options
-------

``--force/--no-force``

Breaks module locks established by another user and all the ports of the module, aka. force reservation, default to ``--force``.



Examples
--------

.. code-block:: text

    xoa-utils[123456] > module-config 0 qsfpdd800 8 100g
