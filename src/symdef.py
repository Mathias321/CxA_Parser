from VERSION import *
import FIGURE
import TEXT
import TERMINAL
import TEXTLOC
import PINLABELLOC
import PINNUMNAMELOC
import PT
from CadstarArcObj import *


class SYMDEF(CadstarArcObj):
    CAO_keyword = "SYMDEF"
    DICT_POSATTR = ["ref", "name", "altName", "origin"]
    DICT_ATTR = {VERSION: "version"}
    DICT_COLLECTION = {FIGURE.FIGURE: "figures",
                       TEXT.TEXT: "texts",
                       TERMINAL.TERMINAL: "terminals",
                       TEXTLOC.TEXTLOC: "textLocs",
                       PINLABELLOC.PINLABELLOC: "pinLabelLocs",
                       PINNUMNAMELOC.PINNUMNAMELOC: "pinNumNameLocs"}


CadstarArcObj.register_sub_class(SYMDEF)
