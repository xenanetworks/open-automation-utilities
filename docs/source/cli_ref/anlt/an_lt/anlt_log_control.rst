anlt logctrl
================

Description
-----------

Control what types of ANLT log messages are sent by xenaserver. This command is different from the ``--keep`` option of :doc:`anlt_log`. ``anlt log-ctrl`` control the log message from its source, where ``anlt_log`` filters the messages for display output.


Synopsis
--------

.. code-block:: text
    
    anlt logctrl
    [-D/-d, --debug/--no-debug]
    [-A/-a, --an-trace/--no-an-trace]
    [-L/-l, --lt-trace/--no-lt-trace]
    [-G/-g, --alg-trace/--no-alg-trace]
    [-P/-p, --fsm-port/--no-fsm-port]
    [-N/-n, --fsm-an/--no-fsm-an]
    [-M/-m, --fsm-an-stimuli/--no-fsm-an-stimuli]
    [-T/-t, --fsm-lt/--no-fsm-lt]
    [-C/-c, --fsm-lt-coeff/--no-fsm-lt-coeff]
    [-S/-s, --fsm-lt-stimuli/--no-fsm-lt-stimuli]
    [-Z/-z, --fsm-lt-alg0/--no-fsm-lt-alg0]
    [-O/-o, --fsm-lt-algn1/--no-fsm-lt-algn1]


Arguments
---------


Options
-------

``-D/-d, --debug/--no-debug``

Debug log out, default to ``--debug, -D``


``-A/-a, --an-trace/--no-an-trace``

Auto-negotiation trace output, default to --an-trace, -A


``-L/-l, --lt-trace/--no-lt-trace``

Link training algorithm trace, default to --lt-trace, -L


``-G/-g, --alg-trace/--no-alg-trace``

Link training algorithm trace output, default to --alg-trace, -G


``-P/-p, --fsm-port/--no-fsm-port``

Port state machine transitions output, default to --no-fsm-port, -p


``-N/-n, --fsm-an/--no-fsm-an``

Auto-negotiation state machine transitions, default to --fsm-an, -N


``-M/-m, --fsm-an-stimuli/--no-fsm-an-stimuli``

Auto-negotiation stimuli state machine transitions, default to --no-fsm-an-stimuli, -m


``-T/-t, --fsm-lt/--no-fsm-lt``

Link training state machine transitions, default to --fsm-lt, -T


``-C/-c, --fsm-lt-coeff/--no-fsm-lt-coeff``

Link training coefficient state machine transitions, default to --no-fsm-lt-coeff, -c


``-S/-s, --fsm-lt-stimuli/--no-fsm-lt-stimuli``

Link training stimuli state machine transitions, default to --no-fsm-lt-stimuli, -s


``-Z/-z, --fsm-lt-alg0/--no-fsm-lt-alg0``

Link training algorithm 0 state machine transitions, default to --fsm-lt-alg0, -Z


``-O/-o, --fsm-lt-algn1/--no-fsm-lt-algn1``

Link training algorithm -1 state machine transitions, default to --fsm-lt-algn1, -O



Examples
--------

.. code-block:: text

    xoa-utils[123456][port0/2] > anlt logctrl
    Port 0/2 log control:
        Type debug:             on
        Type AN trace:          on
        Type LT trace:          on
        Type ALG trace:         on
        Type FSM port:          on
        Type FSM AN:            on
        Type FSM AN Stimuli:    off
        Type FSM LT:            on
        Type FSM LT Coeff:      off
        Type FSM LT Stimuli:    off
        Type FSM LT ALG  0:     on
        Type FSM LT ALG -1:     on

    xoa-utils[123456][port0/2] >




