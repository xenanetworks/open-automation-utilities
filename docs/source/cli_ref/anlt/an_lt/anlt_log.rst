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


Arguments
---------


Options
-------

``-f, --filename`` (text)

Specifies the filename for the log messages to be stored.


``-k, --keep`` (text)
    
Specifies what types of log entries to keep, default to keep all.

Allowed values:

* `all`, to keep all.

* `an`. to keep autoneg only.

* `lt`, to keep lt only.


``-l, --lane`` (int list)
    
Specifies which lanes of LT logs to keep. If you don't know how many serdes lanes the port has, use :doc:`../an_lt/anlt_log`, default to all lanes.


Examples
--------

.. code-block:: text
    
    xoa-utils[123456][port0/2] > anlt log -f mylog.log

    ...
    
    10054.176465, LT_COEF(L0),      MSG: Setting coeff c(-1) PRE1 to 1
    10054.176474, LT_COEF(L0),      MSG: Setting coeff c(0)  MAIN to 46
    10054.176483, LT_COEF(L0),      MSG: Setting coeff c(1)  POST to 0
    10054.176492, LT_COEF(L0),      MSG: Setting coeff c(-2) PRE2 to 2
    10054.176501, LT_COEF(L0),      MSG: Setting coeff c(-3) PRE3 to 1
    10054.176523, LT(L0),           TX:  0x1A000B00, LOCKED=true, DONE=false
                                         C_REQ: Hold   C_SEL: c(0)   PAM_MOD: PAM4   IC_REQ: IC 5   
                                         C_STS: No upd C_ECH: c(0)   PAM_MOD: PAM4   IC_STS: Upd    
    10054.176569, LT(L0),           RX:  0x1A000B00, LOCKED=true, DONE=false
                                         C_REQ: Hold   C_SEL: c(0)   PAM_MOD: PAM4   IC_REQ: IC 5   
                                         C_STS: No upd C_ECH: c(0)   PAM_MOD: PAM4   IC_STS: Upd    
    10054.176617, LT(L0),           TX:  0x02000B00, LOCKED=true, DONE=false
                                         C_REQ: Hold   C_SEL: c(0)   PAM_MOD: PAM4   IC_REQ: INDV   
                                         C_STS: No upd C_ECH: c(0)   PAM_MOD: PAM4   IC_STS: Upd    
    10054.176663, LT(L0),           RX:  0x02000B00, LOCKED=true, DONE=false
                                         C_REQ: Hold   C_SEL: c(0)   PAM_MOD: PAM4   IC_REQ: INDV   
                                         C_STS: No upd C_ECH: c(0)   PAM_MOD: PAM4   IC_STS: Upd    
    10054.176688, LT(L0),           TX:  0x02000A80, LOCKED=true, DONE=false
                                         C_REQ: Hold   C_SEL: c(0)   PAM_MOD: PAM4   IC_REQ: INDV   
                                         C_STS: No upd C_ECH: c(0)   PAM_MOD: PAM4   IC_STS: No upd 
    10054.1792, LT(L0),             RX:  0x02000A80, LOCKED=true, DONE=false
                                         C_REQ: Hold   C_SEL: c(0)   PAM_MOD: PAM4   IC_REQ: INDV   
                                         C_STS: No upd C_ECH: c(0)   PAM_MOD: PAM4   IC_STS: No upd 

    xoa-utils[123456][port0/2] !








