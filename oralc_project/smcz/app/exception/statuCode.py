from enum import Enum
from enum import IntEnum,unique

class StatuCode(Enum):
    unknowError = 600
    successCode = 1000
    selectTabelError = 601
    connectTimeOut = 602
    insertDataError = 603
    deleteDataError = 604