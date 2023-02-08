Step-by-Step Guide
===================

This section provides a step-by-step guide on how to use XOA Utility to do interactive ANLT test. 

The diagram below illustrates a basic flow of using XOA Utilities to do ANLT testing.

.. figure:: ../_static/anlt_use_flow.png
    :width: 100 %
    :align: center

.. note::

    ⚡️ You can use **tab key** to auto-complete a command to speed up your input speed.

Connect
-------

First, you need to connect to your tester using the command :doc:`../cli_ref/mgmt/connect`.

If you don't know which ports you will use at the time of connecting to the port, just leave the option ``--ports`` empty as the example shows below. You can reserve ports later.

.. code-block:: console

    [xoa_util]$ connect 10.10.10.10 xoa_anlt


Reserve Port
------------

Then, reserve a port on the tester using the command :doc:`../cli_ref/mgmt/port`, as shown in the example below.

.. note::

    You can only work on one port at a time in one console window. If you want to simultaneously work on multiple ports, you can open multiple console windows.

.. code-block:: console

    [xoa_util][]$ port 0/0 --reset --force


Disable Link Recovery
---------------------

Before doing ANLT testing, remember to disable link recovery on the port using command :doc:`../cli_ref/anlt/an_lt/anlt_recovery`. 

This is because the port always tries to re-do ANLT command sequence every five seconds if it detects no sync on the port. 

This will disturb your manual link training procedure if you don't disable it prior to your interactive test.

.. code-block:: console

    [xoa_util][port0/0]$ recovery --off


Configure AN & LT
-----------------

After disabling link recovery on the port, you can start configuring AN and LT using :doc:`../cli_ref/anlt/an/an_config`, :doc:`../cli_ref/anlt/lt/lt_config`, and :doc:`../cli_ref/anlt/lt/lt_im` as the example shown below. 

These three commands only configure the ANLT test scenario instead of starting any AN or LT on the port.

.. note::

    The initial modulation of each lane on a port is by default PAM2 (NRZ). If you want to change them, you can use :doc:`../cli_ref/anlt/lt/lt_im`, otherwise do nothing.

.. code-block:: console

    [xoa_util][port0/0]$ an config --off --no-loopback

    [xoa_util][port0/0]$ lt config --on --preset0 --mode=interactive 


Start ANLT
----------

After configuring the ANLT scenario on the port, you should execute :doc:`../cli_ref/anlt/an_lt/anlt_do` to let XOA Utilities application send low-level commands to the tester to start the ANLT procedure, either AN-only, or AN + LT, or LT (auto), or LT (interactive).

.. code-block:: console

    [xoa_util][port0/0]$ do anlt


Control LT Interactive
----------------------

If you run LT (interactive), you will need to manually control the LT parameters using the LT Control Commands shown in :doc:`../cli_ref/anlt/lt/index`, for example:


.. code-block:: console

    [xoa_util][port0/0]$ lt preset 2

    [xoa_util][port0/0]$ lt inc 0 pre3

    [xoa_util][port0/0]$ lt inc 0 main

    [xoa_util][port0/0]$ lt inc 0 main

    [xoa_util][port0/0]$ lt dec 0 post

    [xoa_util][port0/0]$ lt status 0

    [xoa_util][port0/0]$ lt trained 0

    [xoa_util][port0/0]$ lt txtagget 0

    [xoa_util][port0/0]$ lt txtagset --pre3=5 --main=56


Check AN Status
---------------

Check AN statistics by :doc:`../cli_ref/anlt/an/an_status` .

Check LT Status
---------------

Check LT statistics by :doc:`../cli_ref/anlt/lt/lt_status`.


Check ANLT Log
--------------

Check ANLT logging by :doc:`../cli_ref/anlt/an_lt/anlt_log`.


Start Over
----------

If you want to start over on the port, you can reset the port by ``port <PORT> --reset`` as shown below.

This will bring the port back to its default state.

.. code-block:: console

    [xoa_util][port0/0]$ port 0/0 --reset


