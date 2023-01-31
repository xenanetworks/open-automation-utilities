lt log
============

Description
-----------

To show the link training trace log for the specified lane.
This command also enter `lt` context from the port.


Synopsis
--------

.. code-block:: console
    
    lt log <LANE>
    [--live/--no-live]


Arguments
---------

``<LANE>`` (integer)

    Specifies the lane index.


Options
-------

``--live/--no-live``

    Should show the live link training log, default to `--no-live`.


Examples
--------

.. code-block:: console

    xoa_util[port0/2][lt]$ log 0




