port
=====

Description
-----------

Reserve and switch port. If the port is not yet reserved, reserve the port. 
This command changes the working port and will stay in the same context.

Synopsis
--------

.. code-block:: text
    
    port <PORT>
    [--reset/--no-reset]
    [--force/--no-force]


Arguments
---------

``<PORT>`` (text)

Specifies the port on the specified device host.

Specify a port using the format slot/port, e.g. 0/0



Options
-------

``--reset/--no-reset`` 
    
Removes the port configurations, default to ``--no-reset``.

``--force/--no-force``

Breaks port locks established by another user, aka. force reservation, default to ``--force``.


Examples
--------

.. code-block:: text

    xoa-utils[123456] > port 0/0
    Port      Sync      Owner     
    *0/0      IN_SYNC   You       

    Port 0/0
    =ACTUAL STATUS=
    Auto-negotiation      : on
    Link training         : start_after_autoneg
    Link training timeout : default
    Link recovery         : off
    Lane (serdes) count   : 4

    =SHADOW STATUS=
    Auto-negotiation      : off
    Allow loopback        : no
    Link training         : off (auto)
    Preset0               : standard tap values
