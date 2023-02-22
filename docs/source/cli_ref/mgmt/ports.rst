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

    xoa-utils[123456][port0/0] > ports
    Ports       Sync        Owner
    *0/0        yes         You


.. code-block:: text

    xoa-utils[123456][port0/0] > ports --all
    Port      Sync      Owner     
    *0/0      IN_SYNC   You       
    0/1       IN_SYNC   Others    
    6/0       NO_SYNC   Others    
    6/1       NO_SYNC   Others 
