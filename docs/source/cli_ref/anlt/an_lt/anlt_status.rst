anlt status
===========

Description
-----------

Show AN/LT status of the working port.


Synopsis
--------

.. code-block:: text
    
    anlt status


Arguments
---------


Options
-------


Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/0] > anlt status
    
    Port 0/2
        [ACTUAL STATUS]
        Auto-negotiation      : on (allow loopback: yes)
        Link training         : on (auto) (preset0: standard tap values) (timeout: default)
        Link recovery         : off
        Lane (serdes) count   : 1

        [SHADOW STATUS]
        Auto-negotiation      : off (allow loopback: no)
        Link training         : off (auto) (preset0: standard tap values)
    
    xoa-utils[123456][port0/2] >



