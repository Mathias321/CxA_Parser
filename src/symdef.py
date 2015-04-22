from VERSION import *
import FIGURE
import TEXT
import TERMINAL
import TEXTLOC
import PINLABELLOC
import PINNUMNAMELOC
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

    def check_pins_on_grid(self, grid_step):
        all_ok = True
        for pin in self.terminals.values():
            dx = int(self.origin.x) - int(pin.position.x)
            if dx % grid_step != 0:
                print(pin.ref, self.origin.x, pin.position.x)
                all_ok = False
            dy = int(self.origin.y) - int(pin.position.y)
            if dy % grid_step != 0:
                print(pin.ref, self.origin.y, pin.position.y)
                all_ok = False
        return all_ok

CadstarArcObj.register_sub_class(SYMDEF)
