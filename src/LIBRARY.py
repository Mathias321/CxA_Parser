import symdef
from CadstarArcObj import *


class LIBRARY(CadstarArcObj):
    CAO_keyword = "LIBRARY"
    DICT_POSATTR = []
    DICT_ATTR = {}
    DICT_COLLECTION = {symdef.SYMDEF: "symbols"}

    def __init__(self, parent):
        self.attr = []
        self.parent = parent
        
        self.symbols = {}
  
CadstarArcObj.register_sub_class(LIBRARY)
