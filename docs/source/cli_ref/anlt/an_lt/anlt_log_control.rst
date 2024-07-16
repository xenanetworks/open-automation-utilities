anlt logctrl
================

Description
-----------

Control what types of ANLT log messages are sent by xenaserver. This command is different from the ``--keep`` option of :doc:`anlt_log`. ``anlt log-ctrl`` control the log message from its source, where :doc:`anlt_log` filters the messages for display output.

If no option is provided, the command will return the current status on the port.

This command provide delta change to the log control, which means it only change the settings that you provide and will keep the others unchanged.

In case you provide conflicting options, e.g. --debug (-D) and --no-debug (-d) at the same time, the command will always choose the "ON", which is dominant.

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

``-D, --debug``, Debug log ON

``-d, --no-debug``, Debug log OFF

``-A, --an-trace``, Autoneg trace ON

``-a, --no-an-trace``, Autoneg trace OFF

``-L, --lt-trace``, Link Training trace ON

``-l, --no-lt-trace``, Link Training trace OFF

``-G, --alg-trace``, Link Training algorithm trace ON

``-g, --no-alg-trace``, Link Training algorithm trace OFF

``-P, --fsm-port``, Port FSM trace ON

``-p, --no-fsm-port``, Port FSM trace OFF

``-N, --fsm-an``, Autoneg FSM trace ON

``-n, --no-fsm-an``, Autoneg FSM trace OFF

``-M, --fsm-an-stimuli``, Autoneg stimuli FSM trace ON

``-m, --no-fsm-an-stimuli``  Autoneg stimuli FSM trace OFF

``-T, --fsm-lt``             Link Training FSM trace ON

``-t, --no-fsm-lt``          Link Training FSM trace OFF

``-C, --fsm-lt-coeff``       Link Training coefficient FSM trace ON

``-c, --no-fsm-lt-coeff``    Link Training coefficient FSM trace OFF

``-S, --fsm-lt-stimuli``     Link Training stimuli FSM trace ON

``-s, --no-fsm-lt-stimuli``  Link Training stimuli FSM trace OFF

``-Z, --fsm-lt-alg0``        Link Training algorithm0 FSM trace ON

``-z, --no-fsm-lt-alg0``     Link Training algorithm0 FSM trace OFF

``-O, --fsm-lt-algn1``       Link Training algorithmN1 FSM trace ON

``-o, --no-fsm-lt-algn1``    Link Training algorithmN1 FSM trace OFF



Examples
--------

.. code-block:: text

    xoa-utils[10401492][3/0] > anlt logctrl

    Port 3/0 log control:
        Type debug:             on  -D
        Type AN trace:          on  -A
        Type LT trace:          on  -L
        Type ALG trace:         on  -G
        Type FSM port:          on  -P
        Type FSM AN:            on  -N
        Type FSM AN Stimuli:    off -m
        Type FSM LT:            off -t
        Type FSM LT Coeff:      off -c
        Type FSM LT Stimuli:    off -s
        Type FSM LT ALG  0:     off -z
        Type FSM LT ALG -1:     off -o

    xoa-utils[10401492][3/0] > anlt logctrl -M

    Port 3/0 log control:
        Type debug:             on  -D
        Type AN trace:          on  -A
        Type LT trace:          on  -L
        Type ALG trace:         on  -G
        Type FSM port:          on  -P
        Type FSM AN:            on  -N
        Type FSM AN Stimuli:    on  -M
        Type FSM LT:            off -t
        Type FSM LT Coeff:      off -c
        Type FSM LT Stimuli:    off -s
        Type FSM LT ALG  0:     off -z
        Type FSM LT ALG -1:     off -o

    xoa-utils[10401492][3/0] > anlt logctrl -d

    Port 3/0 log control:
        Type debug:             off -d
        Type AN trace:          on  -A
        Type LT trace:          on  -L
        Type ALG trace:         on  -G
        Type FSM port:          on  -P
        Type FSM AN:            on  -N
        Type FSM AN Stimuli:    on  -M
        Type FSM LT:            off -t
        Type FSM LT Coeff:      off -c
        Type FSM LT Stimuli:    off -s
        Type FSM LT ALG  0:     off -z
        Type FSM LT ALG -1:     off -o




