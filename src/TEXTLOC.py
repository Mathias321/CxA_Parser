from CadstarArcObj import *


class TEXTLOC(CadstarArcObj):
    CAO_keyword = "TEXTLOC"


CadstarArcObj.register_sub_class(TEXTLOC)