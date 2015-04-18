from CadstarArcObj import *


class ACWARC(CadstarArcObj):
    CAO_keyword = "ACWARC"


CadstarArcObj.register_sub_class(ACWARC)