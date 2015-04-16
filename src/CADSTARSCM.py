from CadstarArcObj import *


class CADSTARSCM(CadstarArcObj):
    CAO_keyword = "LIBRARY"
    DICT_POSATTR = []
    DICT_ATTR = {}
    DICT_COLLECTION = {HEADER.HEADER: "Header",
                       ASSIGNMENTS.ASSIGNMENTS: "Assignments",
                       DEFAULTS.DEFAULTS: "Defaults",
                       LIBRARY.LIBRARY: "Library",
                       PARTS.PARTS: "Parts",
                       SHEETS.SHEETS: "Sheets",
                       SCHEMATIC.SCHEMATIC: "Schematic",
                       DISPLAY.DISPLAY: "Display"
                       }

    def __init__(self, parent):
        self.attr = []
        self.parent = parent
        
        self.symbols = {}
  
CadstarArcObj.register_sub_class(CADSTARSCM)
