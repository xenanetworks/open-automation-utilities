anlt log
========

Description
-----------

Show ANLT protocol trace log and save to a file.

To **quit** the continuous display mode, press :kbd:`Control-z`.



Synopsis
--------

.. code-block:: text
    
    anlt log
    [-f, --filename <value: text>]
    [-k, --keep <value: text>]
    [-s, --serdes <value>]


Arguments
---------


Options
-------

``-f, --filename`` (text)

Specifies the filename for the log messages to be stored.

``--read -f`` (text)

Specifies the filepath of the log file to display.


``-k, --keep`` (text)
    
Specifies what types of log entries to keep, default to keep all.

Allowed values:

* `all`, to keep all.

* `an`. to keep autoneg only.

* `lt`, to keep lt only.


``-s, --serdes`` (int list)
    
Specifies which serdes of LT logs to keep. If you don't know how many serdes serdes the port has, use :doc:`../an_lt/anlt_log`, default to all serdes.


Examples
--------

.. code-block:: text
    
    xoa-utils[123456][port0/2] > anlt log --filename mylog.log --keep lt --serdes 0

.. figure:: ../../../_static/anlt_log.png
    :width: 100 %
    :align: center








