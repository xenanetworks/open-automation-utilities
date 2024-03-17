Explanation
========================

ANEG FSM
----------

.. literalinclude:: anlt.log
    :lines: 10-11

ANEG FSM messages show you the FSM state transition of ANEG.

ANEG MSG
----------

.. literalinclude:: anlt.log
    :lines: 46

ANEG MSG messages show log messages from ANEG.

ANEG TX & RX
------------

.. literalinclude:: anlt.log
    :lines: 25-36
    :emphasize-lines: 2-5, 8-11

The raw hex value of the transmitted and received ANEG test frames are shown first. Decoding of each field are shown after the raw value.


LT FSM
----------

.. literalinclude:: anlt.log
    :lines: 12-17

LT FSM messages show you the FSM state transition of LT for each serdes lane, e.g. ``LT(S0)`` for lane 0, and ``LT(S1)`` for lane 1.

LT MSG
----------

.. literalinclude:: anlt.log
    :lines: 104

LT MSG messages show log messages from a serdes lane of LT.

LT COEFF MSG
-------------

.. literalinclude:: anlt.log
    :lines: 108-114
    :emphasize-lines: 2-6

LT COEFF MSG messages show log messages of coefficient change of a serdes lane from LT.

LT TX & RX
----------

.. literalinclude:: anlt.log
    :lines: 188-203
    :emphasize-lines: 1-3, 5-10, 14-16

The raw hex value of the transmitted and received LT test frames are shown first. Decoding of each field are shown after the raw value.

The first line ``C_REQ, C_SEL, IC_REQ, PAM_MOD`` is control information. The second line ``C_ECH, C_STS, IC_STS, PAM_MOD`` is status information.

The example above demonstrates a 4-way handshake of the link training transaction.

1. The port lane 0 requests the remote to use Preset 1 ``C_REQ: Hold   C_SEL: c(0)   IC_REQ: IC 1   PAM_MOD: PAM4``
2. The remote confirms the update ``C_ECH: c(0)   C_STS: No upd IC_STS: Upd    PAM_MOD: PAM4`` without requesting any change.
3. The port tells the remote port to hold ``C_REQ: Hold   C_SEL: c(0)   IC_REQ: INDV   PAM_MOD: PAM4```
4. The remote port holds the change ``C_ECH: c(0)   C_STS: No upd IC_STS: No upd PAM_MOD: PAM4``


Full Example
--------------------

A complete log example is shown below.

.. literalinclude:: anlt.log