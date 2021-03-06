from CadstarArcObj import *
from ALIGN import *
from JUSTIFICATION import *


   # (TEXTLOC SYMBOL_NAME TC4 (PT 43942000 63373000))
   # (TEXTLOC PART_NAME TC4 (PT 43942000 57531000)
   #  (ALIGN BOTTOMLEFT)
   # )
   # (TEXTLOC
   #  (ATTRREF AT5) TC4 (PT 48006000 57556400)
   #  (ALIGN TOPRIGHT)
   #  (JUSTIFICATION RIGHT)
   # )

class TEXTLOC(CadstarArcObj):
    CAO_keyword = "TEXTLOC"
    DICT_POSATTR = ["ref", "textCode", "point"]
    DICT_ATTR = {ALIGN : "alignment",
                 JUSTIFICATION : "justification"}

CadstarArcObj.register_sub_class(TEXTLOC)