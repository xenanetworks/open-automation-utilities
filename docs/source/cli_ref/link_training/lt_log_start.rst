lt log start
============

Description
-----------

To start writing the link training trace log for the specified lane into a file.



Synopsis
--------

.. code-block:: console
    
    lt log start <LANE> <FILENAME>


Arguments
---------

``<LANE>`` (integer)

Specifies the lane index.


``<FILENAME>`` (text)

Filename of the log.


Options
-------



Examples
--------

.. code-block:: console

    xoa_util[port0/2]$ lt log start 0 "log0.txt"
    Lane 0 logging start into log0.txt, use lt log stop 0 to end the logging.

    xoa_util[port0/2]$ lt log start 3 "log3.txt"
    Lane 3 logging start into log3.txt, use lt log stop 0 to end the logging.






