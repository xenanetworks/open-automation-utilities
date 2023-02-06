lt log stop
============

Description
-----------

To stop the log writing for the specified lane.



Synopsis
--------

.. code-block:: console
    
    lt log stop <LANE> <FILEPATH>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


``<FILEPATH>`` (text)

Log file name.


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt log stop 0 "log0.txt"
    Lane 0 logging stopped.

    xoa_util[port0/2]$ lt log stop 3 "log3.txt"
    Lane 3 logging stopped.






