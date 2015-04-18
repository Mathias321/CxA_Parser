from CadstarArcObj import *


class CWARC(CadstarArcObj):
    CAO_keyword = "CWARC"


CadstarArcObj.register_sub_class(CWARC)