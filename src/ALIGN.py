from CadstarArcObj import *

   # (TEXTLOC SYMBOL_NAME TC4 (PT 43942000 63373000))
   # (TEXTLOC PART_NAME TC4 (PT 43942000 57531000)
   #  (ALIGN BOTTOMLEFT)
   # )
   # (TEXTLOC
   #  (ATTRREF AT5) TC4 (PT 48006000 57556400)
   #  (ALIGN TOPRIGHT)
   #  (JUSTIFICATION RIGHT)
   # )

class ALIGN(CadstarArcObj):
    CAO_keyword = "ALIGN"
    POSSIBLE_VALUES = ('TOPRIGHT', 'TOPCENTER', 'TOPLEFT',
                       'CENTERRIGHT', 'CENTER', 'CENTERLEFT',
                       'BOTTOMRIGHT', 'BOTTOMCENTER', 'BOTTOMLEFT')

CadstarArcObj.register_sub_class(ALIGN)