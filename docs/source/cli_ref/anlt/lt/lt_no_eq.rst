lt dec
======

Description
-----------

Request the remote link training turn off equalizer on its emphasis.



Synopsis
--------

.. code-block:: text
    
    lt no_eq <SERDES> <EMPHASIS>


Arguments
---------

``<SERDES>`` (integer)

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

    xoa-utils[123456][port0/2] > lt no_eq 0 main
    Port 0/0: Turning off equalizer on c(0) on Serdes 0 (COEFF_STS_UPDATED)

    xoa-utils[123456][port0/2] >




