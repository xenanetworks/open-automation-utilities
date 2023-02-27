lt inc
======

Description
-----------

Request the remote link training partner to increase (+) its emphasis value by 1.



Synopsis
--------

.. code-block:: text
    
    lt inc <LANE> <EMPHASIS>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


``<EMPHASIS>`` (text)
    
The emphasis (coefficient) of the link partner.

Allowed values:

* `pre3`

* `pre2`

* `pre`

* `main`

* `post`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt inc 1 main
    Port 0/2 requests: increase c(0) by 1 on Lane 1

    xoa-utils[123456][port0/2] >

