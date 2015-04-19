from CadstarArcObj import *


#####################################################################
 #   (LINECODE LC1 "Line 10" 25400
 #    (STYLE SOLID)
 #   )
class STYLE(CadstarArcObj):
    CAO_keyword="STYLE"
    POSSIBLE_VALUES = ("SOLID", "DASH") # TODO : Add missing line style




#######################################################

class LINECODE(CadstarArcObj):
    CAO_keyword="LINECODE"
    DICT_POSATTR=["ref", "name", "width"]
    DICT_ATTR={STYLE : "style"}
    DICT_COLLECTION={}


##________________________________________________________________

#######################################################

class HATCH(CadstarArcObj):
    CAO_keyword="HATCH"
    DICT_POSATTR=["value_1", "orient", "value_2"]


### Note : No ORIENT class


#######################################################
 #   (HATCHCODE HC0 "Figure Hatching 1"
 #    (HATCH 127000
 #     (ORIENT 0) 20320
 #    )
 #    (HATCH 127000
 #    (ORIENT 90000) 25400
 #    )
class HATCHCODE(CadstarArcObj):
    CAO_keyword="HATCHCODE"
    DICT_POSATTR=["ref", "name"]
    DICT_COLLECTION={HATCH : "hatches"}

##________________________________________________________________


#######################################################
 #   (TEXTCODE TC0 "(Pin Name/Number)" 10160 76200 76200)
class TEXTCODE(CadstarArcObj):
    CAO_keyword="TEXTCODE"
    DICT_POSATTR=["ref", "name", "line_width", "height", "width"]



#######################################################
 #   (ATTRNAME AT0 "pcb_zone"
 #    (ATTROWNER ALL_ITEMS)
 #   )
class ATTRNAME(CadstarArcObj):
    CAO_keyword="ATTRNAME"
    DICT_POSATTR=["ref", "name", "attribut_owner"]



##________________________________________________________________

#######################################################

class STEPGRID(CadstarArcObj):
    CAO_keyword="STEPGRID"
    DICT_POSATTR=["name", "x", "y"]




#######################################################

class WORKINGGRID(CadstarArcObj):
    CAO_keyword="WORKINGGRID"
    DICT_ATTR={STEPGRID : "step_grid"}



#######################################################

class SCREENGRID(CadstarArcObj):
    CAO_keyword="SCREENGRID"
    DICT_ATTR={STEPGRID : "step_grid"}




#######################################################
 #  (GRIDS
 #   (WORKINGGRID
 #    (STEPGRID "" 100000 100000)
 #   )
 #   (SCREENGRID
 #    (STEPGRID "" 200000 200000)
 #   )
 #   (STEPGRID "myGrid" 200000 200000)

class GRIDS(CadstarArcObj):
    CAO_keyword="GRIDS"
    DICT_ATTR={WORKINGGRID : "working_grid", SCREENGRID : "screen_grid"}
    DICT_COLLECTION={STEPGRID : "step_grids"}

##________________________________________________________________




#######################################################

class CODEDEFS(CadstarArcObj):
    CAO_keyword="CODEDEFS"
    DICT_COLLECTION={LINECODE : "line_codes", HATCHCODE : "hatch_code",
                     TEXTCODE : "text_codes", ATTRNAME : "attributes_names"}





#######################################################
class SETTINGS(CadstarArcObj):
    CAO_keyword="SETTINGS"




#######################################################
 # (ASSIGNMENTS
 #  (CODEDEFS
 #   (LINECODE LC1 "Line 10" 25400
 #    (STYLE SOLID)
 #   )
 #   (LINECODE ...
 #   (HATCHCODE HC0 "Figure Hatching 1"
 #    (HATCH 127000
 #     (ORIENT 0) 20320
 #    )
 #   )
 #   (TEXTCODE TC0 "(Pin Name/Number)" 10160 76200 76200)
 #   (TEXTCODE TC1 "Scrntxt F0 5/8" 20320 152400 127000)
 #   (ATTRNAME AT0 "pcb_zone"
 #    (ATTROWNER ALL_ITEMS)
 #   )
 #   (ATTRNAME AT1 "sim_model"
 #    (ATTROWNER ALL_ITEMS)
 #   )
 #  (GRIDS
 #   (WORKINGGRID
 #    (STEPGRID "" 100000 100000)
 #   )
 #   (SCREENGRID
 #    (STEPGRID "" 200000 200000)
 #   )
 #  )
 #  (SETTINGS
 #   (UNITS MM)
 #   (UNITSPRECISION 2)

class ASSIGNMENTS(CadstarArcObj):
    CAO_keyword="ASSIGNMENTS"
    DICT_POSATTR=[]
    DICT_ATTR={CODEDEFS : "codedef", GRIDS : "grid", SETTINGS : "setting"}
    DICT_COLLECTION={}

#######################################################


CadstarArcObj.register_sub_class(SETTINGS)
CadstarArcObj.register_sub_class(ASSIGNMENTS)
CadstarArcObj.register_sub_class(STYLE)
CadstarArcObj.register_sub_class(LINECODE)
CadstarArcObj.register_sub_class(CODEDEFS)
CadstarArcObj.register_sub_class(GRIDS)
CadstarArcObj.register_sub_class(SCREENGRID)
CadstarArcObj.register_sub_class(WORKINGGRID)
CadstarArcObj.register_sub_class(ATTRNAME)
CadstarArcObj.register_sub_class(STEPGRID)
CadstarArcObj.register_sub_class(HATCHCODE)
CadstarArcObj.register_sub_class(TEXTCODE)
CadstarArcObj.register_sub_class(HATCH)

