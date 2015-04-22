from CadstarArcObj import *
import SHAPE


class FIGURE(CadstarArcObj):
    CAO_keyword = "FIGURE"
    DICT_POSATTR = ["ref", "lineCode", "sheets"]
    DICT_ATTR = {SHAPE.SHAPE: "shape"}
    DICT_COLLECTION = {}



CadstarArcObj.register_sub_class(FIGURE)
