ports
===================

Description
-----------

To list all the ports reserved by the current session.
This command works in all context.

Synopsis
--------

.. code-block:: text
    
    ports


Arguments
---------


Options
-------

``--all/--no-all`` 
    
Show all ports of the tester, default to ``--no-all``

Examples
--------

.. code-block:: text

    xoa_util[123456][port0/0] > ports --all
    Ports       Sync        Owner
    *0/0        yes         You
    0/1         yes         You
    0/2         yes         You
    0/3         yes         Others
    0/4         yes         Others
    0/5         yes         Others

.. code-block:: text
    
    xoa_util[123456][port0/0] > ports
    Ports       Sync        Owner
    *0/0        yes         You
    0/1         yes         You
    0/2         yes         You


