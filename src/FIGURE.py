from CadstarArcObj import *
import SHAPE


class FIGURE(CadstarArcObj):
    CAO_keyword = "FIGURE"
    DICT_POSATTR = ["ref", "lineCode", "sheets"]
    DICT_ATTR = {SHAPE.SHAPE: "shape"}
    DICT_COLLECTION = {}

    def __init__(self, parent):
        self.attr = []
        self.parent = parent
        self.ref = ""
        self.lineCode = ""
        self.sheets = ""
        self.shape = SHAPE.SHAPE(self)

CadstarArcObj.register_sub_class(FIGURE)
