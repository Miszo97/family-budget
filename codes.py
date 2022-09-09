from enum import Enum


class Code(Enum):
    SELF_SHARE = "SELF_SHARE", "You can not share a budget with yourself"
    NEGATIVE_INCOME = "NEGATIVE_INCOME", "You can not set a negative income"
