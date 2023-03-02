lt dec
======

Description
-----------

Request the remote link training partner to decrease (-) its emphasis value by 1.



Synopsis
--------

.. code-block:: text
    
lt dec <LANE> <EMPHASIS>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver serdes index.


``<EMPHASIS>`` (text)
    
The emphasis (coefficient) of the link partner.

Allowed values:

* `pre3`

* `pre2`

* `pre``

* `main`

* `post`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt dec 0 main
    Port 0/0: decrease c(0) by 1 on Serdes 0 (COEFF_STS_UPDATED)

    xoa-utils[123456][port0/2] >




