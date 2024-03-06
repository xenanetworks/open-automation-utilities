anlt autorestart
================

Description
-----------

Control AN/LT autorestart.


Synopsis
--------

.. code-block:: text
    
    anlt autorestart
    [--link-down/--no-link-down]
    [--lt-fail/--no-lt-fail]


Arguments
---------


Options
-------

``--link-down/--no-link-down``

Should port enables AN+LT autorestart when a link down condition is detected, default to ``--no-link-down``

``--lt-fail/--no-lt-fail``

Should port initiates the AN+LT restart process repeatedly when LT experiences failure until LT succeeds, default to ``--no-lt-fail``.


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > anlt autorestart --link-down --lt-fail




