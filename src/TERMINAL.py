from CadstarArcObj import *
from PT import PT


# (TERMINAL 1 TC0 (PT 48514000 25908000))
class TERMINAL(CadstarArcObj):
    CAO_keyword = "TERMINAL"
    DICT_POSATTR = ["ref", "textCode"]
    DICT_ATTR = {PT: "position"}


CadstarArcObj.register_sub_class(TERMINAL)