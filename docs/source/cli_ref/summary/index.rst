Summary
=======

.. list-table:: Management Command Summary
    :widths: 20 35 45
    :header-rows: 1
    :stub-columns: 1

    * - Command
      - Description
      - Example
    * - :doc:`../mgmt/connect`
      - Connect to tester
      - ``connect 10.10.10.10 yourname``
    * - :doc:`../mgmt/port`
      - Reserve and switch port
      - ``port 0/0 | port 0/0 --reset``
    * - :doc:`../mgmt/ports`
      - List ports
      - ``ports | ports --all``
    * - :doc:`../mgmt/exit`
      - Exit the session
      - ``exit``

.. list-table:: AN/LT Command Summary
    :widths: 20 35 45
    :header-rows: 1
    :stub-columns: 1

    * - Command
      - Description
      - Example
    * - :doc:`../anlt/an_lt/anlt_do`
      - Apply and start AN/LT to the local port
      - ``anlt do``
    * - :doc:`../anlt/an_lt/anlt_log`
      - Show AN/LT protocol trace log and save to a file
      - ``anlt log --filename mylog.log``
    * - :doc:`../anlt/an_lt/anlt_recovery`
      - Enable/disable link recovery on the local port
      - ``anlt recovery --off``
    * - :doc:`../anlt/an_lt/anlt_status`
      - Show AN/LT status of the local port
      - ``anlt status``
    

.. list-table:: AN Command Summary
    :widths: 20 35 45
    :header-rows: 1
    :stub-columns: 1

    * - Command
      - Description
      - Example
    * - :doc:`../anlt/an/an_config`
      - Configure AN of the local port
      - ``an config --on --loopback``
    * - :doc:`../anlt/an/an_status`
      - Show AN status of the local port
      - ``an status``

.. list-table:: LT Command Summary
    :widths: 20 35 45
    :header-rows: 1
    :stub-columns: 1

    * - Command
      - Description
      - Example
    * - :doc:`../anlt/lt/lt_alg`
      - Set the link training algorithm for the specified serdes
      - ``lt alg 0 alg0``
    * - :doc:`../anlt/lt/lt_config`
      - Configure LT of the local port
      - ``lt config --on --mode auto --preset0 standard``
    * - :doc:`../anlt/lt/lt_dec`
      - Request **remote port** to decrease (-) its emphasis value by 1
      - ``lt dec 0 main``
    * - :doc:`../anlt/lt/lt_encoding`
      - Request **remote port** to use the specified encoding on the specified serdes
      - ``lt encoding 0 pam4``
    * - :doc:`../anlt/lt/lt_im`
      - Set initial modulation for the specified serdes of the local port
      - ``lt im 0 nrz``
    * - :doc:`../anlt/lt/lt_inc`
      - Request **remote port** to increase (+) its emphasis value by 1
      - ``lt inc 0 main``
    * - :doc:`../anlt/lt/lt_preset`
      - Request **remote port** to use the preset of the specified serdes
      - ``lt preset 0 2``
    * - :doc:`../anlt/lt/lt_status`
      - Show the link training status of the specified serdes of the local port
      - ``lt status 0``
    * - :doc:`../anlt/lt/lt_trained`
      - Announce that the specified serdes is trained
      - ``lt trained 0``
    * - :doc:`../anlt/lt/lt_txtapget`
      - Read the tap values of the specified serdes of the local port
      - ``lt txtapget 0``
    * - :doc:`../anlt/lt/lt_txtapset`
      - Write the tap values of the specified serdes of the local port
      - ``lt txtapset 0 1 3 4 60 1``
    * - :doc:`../anlt/lt/lt_txtap_autotune`
      - Auto tune the tap values of the specified serdes of the local port
      - ``lt txtap-autotune 0``
    
    
    