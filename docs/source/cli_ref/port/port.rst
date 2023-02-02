port
=====

Description
-----------

To switch the working port. If the port is not yet reserved, reserve the port. 
This command works in all context.
This command changes the working port and will stay in the same context.

Synopsis
--------

.. code-block:: console
    
    port <PORT>
    [--reset/--no-reset]
    [--force/--no-force]


Arguments
---------

``<PORT>`` (text)

    Specifies the port on the specified device host.
    Specify a port using the format slot/port.
    e.g. 0/0



Options
-------

``--reset/--no-reset`` 
    
    Removes the port configurations, default to `--no-reset`.

``--force/--no-force``

    Breaks port locks established by another user, aka. force reservation, default to `--force`.


Examples
--------

.. code-block:: console

    xoa_util[port0/0]$ port 0/1
    Ports       Sync
    0/0         yes
    *0/1        yes

    Port 0/1
    Auto-negotiation        : on
    Link training           : interactive
    Link training timeout   : default
    Link recovery           : on

    xoa_util[port0/1]$ port 0/0
    Ports       Sync
    *0/0        yes
    0/1         yes

    Port 0/0
    Auto-negotiation        : on
    Link training           : interactive
    Link training timeout   : default
    Link recovery           : on

    xoa_util[port0/0]$ port 0/2 --no-reset
    Ports       Sync
    0/0         yes
    0/1         yes
    *0/2        yes

    Port 0/2
    Auto-negotiation        : on
    Link training           : interactive
    Link training timeout   : default
    Link recovery           : on

    xoa_util[port0/2]$


.. code-block:: console

    xoa_util[port0/0][lt]$ port 0/1
    Ports       Sync
    0/0         yes
    *0/1        yes

    Port 0/1
    Auto-negotiation        : on
    Link training           : interactive
    Link training timeout   : default
    Link recovery           : on

    xoa_util[port0/1][lt]$ 


.. code-block:: console

    xoa_util[port0/1][lt]$ port 0/2 --no-force
    Ports       Sync
    0/0         yes
    *0/1        yes

    Port 0/1
    Auto-negotiation        : on
    Link training           : interactive
    Link training timeout   : default
    Link recovery           : on

    xoa_util[port0/1][lt]$ 


