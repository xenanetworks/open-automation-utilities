Explanation
========================

ANEG FSM
----------

.. literalinclude:: anlt.log
    :lines: 10-11

ANEG FSM messages show you the FSM state transition of ANEG. See IEEE 802.3 Figure 73-11.

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

* ``NP``: Next Page, IEEE 802.3 Claus 73.6.9
* ``RF``: Remote Fault, IEEE 802.3 Claus 73.6.7
* ``TN``: Transmitted Nonce Field, IEEE 802.3 Claus 73.6.3
* ``EN``: Echoed Nonce, IEEE 802.3 Claus 73.6.2
* ``C``: Pause Ability, IEEE 802.3 Claus 73.6.6
* ``FEC``: FEC capability, IEEE 802.3 Claus 73.6.5
* ``ABILITY``: Technology Ability, IEEE 802.3 Claus 73.6.4

* ``ACK``: Acknowledge Bit, IEEE 802.3 Claus 37.2.4.3.3
* ``ACK2``: Acknowledge 2, IEEE 802.3 Clause 37.2.4.3.5
* ``MP``: Message Page, IEEE 802.3 Clause 37.2.4.3.4
* ``T``: Toggle, IEEE 802.3 Clause 37.2.4.3.6


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

The first line ``C_REQ, C_SEL, IC_REQ, PAM_MOD`` is control field information.

* ``C_REQ``: Coefficient request, IEEE 802.3ck Table 162-9 
* ``C_SELD``: Coefficient select, IEEE 802.3ck Table 162-9 
* ``IC_REQ``, Initial condition request, IEEE 802.3ck Table 162-9 
* ``PAM_MOD``, Modulation and precoding request, IEEE 802.3ck Table 162-9 

The second line ``C_ECH, C_STS, IC_STS, PAM_MOD`` is status information.

* ``C_ECH``: Coefficient select echo, IEEE 802.3ck Table 162-10
* ``C_STS``: Coefficient status, IEEE 802.3ck Table 162-10
* ``IC_STS``, Initial condition status, IEEE 802.3ck Table 162-10
* ``PAM_MOD``, Modulation and precoding status, IEEE 802.3ck Table 162-10

The example above demonstrates a 4-way handshake of the link training transaction.

1. The port lane 0 requests the remote to use Preset 1 ``C_REQ: Hold   C_SEL: c(0)   IC_REQ: IC 1   PAM_MOD: PAM4``
2. The remote confirms the update ``C_ECH: c(0)   C_STS: No upd IC_STS: Upd    PAM_MOD: PAM4`` without requesting any change.
3. The port tells the remote port to hold ``C_REQ: Hold   C_SEL: c(0)   IC_REQ: INDV   PAM_MOD: PAM4```
4. The remote port holds the change ``C_ECH: c(0)   C_STS: No upd IC_STS: No upd PAM_MOD: PAM4``


Full Example
--------------------

A complete log example is shown below.

.. literalinclude:: anlt.log