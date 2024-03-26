from pydantic import BaseModel, Field
from enum import Enum
from typing import (
    Generator,
    Dict,
    List,
    Optional,
    Any
)
import json

class EntryDiscriminatorEnum(str, Enum):
    fsm = 'fsm'
    lt = 'lt'
    aneg_bp = 'aneg_bp'
    aneg_np = 'aneg_np'
    log = 'log'

class LogModuleEnum(str, Enum):
    ANEG = 'ANEG'
    LT = 'LT'

class BaseLogModel(BaseModel):
    lane: int
    module: str
    time: int
    type: str
    entry: Any

class EntryModel(BaseModel):
    entry_discriminator: str
    entry_value: Any

# entry_discriminator: log
class PRBSLogModel(BaseModel):
    bits: int
    errors: int
    result: str

class AlgLogModel(BaseModel):
    ber: Optional[List[str]] = None
    cmd: str
    flags: Optional[List[str]] = None
    prbs: Optional[List[PRBSLogModel]] = None
    result: Optional[str] = None

class CmdEntryValueModel(BaseModel):
    cmds: List[AlgLogModel]

class LogEntryValueModel(BaseModel):
    log: CmdEntryValueModel

# entry_discriminator: fsm
class FSMEntryValueModel(BaseModel):
    current: str
    event: str
    new: str

# entry_discriminator: lt, entry_value.log
class LTLogEntryValueModel(BaseModel):
    log: str

# entry_discriminator: lt, entry_value.direction
class LTControlModel(BaseModel):
    C_REQ: str
    C_SEL: str
    IC_REQ: str
    PAM_MOD: str

class LTStatusModel(BaseModel):
    C_ECH: str
    C_STS: str
    IC_STS: str
    PAM_MOD: str

class LTPktFieldModel(BaseModel):
    control: LTControlModel
    done: str
    locked: str
    status: LTStatusModel

class LTPktModel(BaseModel):
    fields: LTPktFieldModel
    prev_count: str
    value: str

class LTEntryValueModel(BaseModel):
    direction: str
    pkt: LTPktModel

# entry_discriminator: aneg_bp, entry_value.log
class AnegLogEntryValueModel(BaseModel):
    log: str
    pkt: Dict[str, Any]

# entry_discriminator: aneg_bp, entry_value.direction
class AnegBpFieldModel(BaseModel):
    Ack: str
    C: str
    EN: str
    NP: str
    RF: str
    TN: str
    ability: List[str]
    fec: List[str]

class AnegBpPktModel(BaseModel):
    fields: AnegBpFieldModel
    prev_count: str
    type: str
    value: str

class AnegBpEntryValueModel(BaseModel):
    direction: str
    pkt: AnegBpPktModel

# entry_discriminator: aneg_np, entry_value.direction
class FormattedMessageModel(BaseModel):
    message: str
    value: str

class UnformattedMessageModel(BaseModel):
    ability: List[str]
    fec: List[str]
    message: str
    value: str

class AnegNpFieldModel(BaseModel):
    Ack: str
    Ack2: str
    MP: str
    NP: str
    T: str
    formatted_message: Optional[FormattedMessageModel] = None
    unformatted_message: Optional[UnformattedMessageModel] = None

class AnegNpPktModel(BaseModel):
    fields: AnegNpFieldModel
    prev_count: str
    type: str
    value: str

class AnegNpEntryValueModel(BaseModel):
    direction: str
    pkt: AnegNpPktModel



# json_data = '{"entry":{"entry_discriminator":"log","entry_value":{"log":{"cmds":[{"ber":["1","4","6"],"cmd":"SET PRESET_1","flags":["DONE","LOCK"],"prbs":[{"bits":5007011360,"errors":10,"result":"1.997e-09"}],"result":"success"},{"ber":["35544","72"],"cmd":"SET PRESET_2","flags":["DONE","LOCK"],"prbs":[{"bits":1001499840,"errors":72,"result":"7.189e-08"}],"result":"success"},{"ber":["5156","1","3","4"],"cmd":"SET PRESET_3","flags":["DONE","LOCK"],"prbs":[{"bits":3004823520,"errors":8,"result":"2.662e-09"}],"result":"success"},{"ber":["18582","20262"],"cmd":"SET PRESET_4","flags":["DONE","LOCK"],"prbs":[{"bits":3004857920,"errors":20262,"result":"6.743e-06"}],"result":"success"},{"ber":["131478","15","0","1"],"cmd":"SET PRESET_1","flags":["DONE","LOCK"],"prbs":[{"bits":3004097120,"errors":16,"result":"5.326e-09"}],"result":"success"},{"cmd":"LOCAL_TRAINED"}]}}},"lane":2,"module":"LT_ALG0","time":82803581287,"type":"trace"}'
# print(BaseLogModel.model_validate_json(json_data))
# data = BaseLogModel(**json.loads(json_data))
# print(data.lane)
# print(data.time)
# print(data.module)
# print(data.type)
# print(data.entry)
# data = EntryModel(**data.entry)
# print(data.entry_discriminator)
# print(data.entry_value)

# if data.entry_discriminator == EntryDiscriminatorEnum.log.name:
#     if data.entry_value != None:
#         data = LogEntryValueModel(**data.entry_value)
#         for cmd in data.log.cmds:
#             print(f"cmd: {cmd.cmd}, result: {cmd.result}, prbs: {cmd.prbs}, flags: ")
