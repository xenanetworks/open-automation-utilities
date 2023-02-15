anlt log
========

Description
-----------

To start writing the link training trace log for the specified lane into a file, and display on the screen.



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
    
    xoa-utils[123456][port0/2] > anlt log mylog.log

    time: 7130745, PORT, Debug   :  Version EA410100, Feature 3
    time: 573514936, ANEG, Message :  TRANSMIT_DISABLE - ANEG restart
    time: 573514936, ANEG, Message :  SYNC=true, SYNC LOST=true, NEW_PAGE=true
    time: 573514936, ANEG, Message :  SYNC=true, SYNC LOST=false, NEW_PAGE=true
    time: 573514936, ANEG, Message :  RX is active
    time: 573581625, ANEG, TX Page :  (0x1020000640C1), base page, NP:0, ACK:1, RF:0, TN:6, EN:6, C:000, FEC:["25G RS-FEC"], ABILITY:["100GBASE_KR1"]
    time: 573581625, ANEG, RX Page :  (0x1020000640C1), base page, NP:0, ACK:1, RF:0, TN:6, EN:6, C:000, FEC:["25G RS-FEC"], ABILITY:["100GBASE_KR1"]
    time: 573581684, ANEG, FSM     :  (EVENT_ACKNOWLEDGE_DETECT) ACKNOWLEDGE_DETECT -> COMPLETE_ACKNOWLEDGE 
    time: 10053807228, LT_COEF (Lane 0), Message: Setting coeff c(-1) PRE1 to 0
    time: 10053807237, LT_COEF (Lane 0), Message: Setting coeff c(0)  MAIN to 42
    time: 10053807246, LT_COEF (Lane 0), Message: Setting coeff c(1)  POST to 0
    time: 10053807255, LT_COEF (Lane 0), Message: Setting coeff c(-2) PRE2 to 0
    time: 10053807264, LT_COEF (Lane 0), Message: Setting coeff c(-3) PRE3 to 0
    time: 10053807283, LT (Lane 0), TX: (0x00000300), C_REQ:Hold, C_SEL:c(0), PAM_MOD:PAM2, IC_REQ:INDV, C_STS:No upd, C_ECH:c(0), PAM_MOD:PAM2, IC_STS:Upd, locked:true, done:false
    time: 10053807294, LT_ALG0 (Lane 0), FSM : (EVENT_RESET_DEASSERT) IDLE -> STATE_ALG_INIT

    xoa-utils[123456][port0/2] !








