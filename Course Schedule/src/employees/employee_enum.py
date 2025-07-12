from enum import Enum


class EmployeeStatus(Enum):
    ACCEPTED = 'ACCEPTED'
    DECLINED = 'DECLINED'
    CANCEL_REJECTED = 'CANCEL_REJECTED'
    CANCEL_ACCEPTED = 'CANCEL_ACCEPTED'
