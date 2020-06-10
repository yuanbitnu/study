from enum import Enum
from enum import IntEnum,unique

class StatuCode(Enum):
    unknowError = 600
    successCode = 1000
    errorCode = 2000
    selectTabelError = 601
    connectTimeOut = 602
    insertDataError = 603
    deleteDataError = 604


if __name__ == "__main__":
    print(type(StatuCode.errorCode.value))