anlt recovery
=============

Description
-----------

Control AN/LT auto-restart.


Synopsis
--------

.. code-block:: text
    
    anlt recovery
    [--link-down/--no-link-down]
    [--lt-fail/--no-lt-fail]


Arguments
---------


Options
-------

``--link-down/--no-link-down``

Should port enables AN+LT auto-restart when a link down condition is detected, default to ``--no-link-down``

``--lt-fail/--no-lt-fail``

Should port initiates the AN+LT restart process repeatedly when LT experiences failure until LT succeeds, default to ``--no-lt-fail``.


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > anlt recovery --link-down --lt-fail




