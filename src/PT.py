from CadstarArcObj import *


class PT(CadstarArcObj):
    CAO_keyword = "PT"
    DICT_POSATTR = ["x", "y"]

    def is_considered_as_child(self):
        return False


CadstarArcObj.register_sub_class(PT)