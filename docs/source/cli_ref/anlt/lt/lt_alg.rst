lt alg
======

.. versionadded:: 1.1

.. important::

    Set the link training algorithm for the specified lane. To execute the configuration, you need to run :doc:`../an_lt/anlt_do`, otherwise your changes will not take effect on the tester.

Description
-----------

Set the link training algorithm for the specified lane.



Synopsis
--------

.. code-block:: text
    
    lt im <LANE> <ENCODING>


Arguments
---------

``<LANE>`` (integer)

Specifies the transceiver lane index.


``<ALGORITHM>`` (text)
    
Specifies the algorithm.

Allowed values:

* `alg_0`

* `alg_n1`


Options
-------



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > lt alg 0 alg_0
    Port 0/2: lt algorithm ALG_0 on Lane 0

    xoa-utils[123456][port0/2] >


