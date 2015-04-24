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

    def check_pins_on_grid(self, grid_step=2540, correct=False):
        list_of_wrong_pins = []
        for pin in self.terminals.values():
            dx = self.origin.x - pin.position.x
            if dx % grid_step != 0:
                list_of_wrong_pins.append(pin.ref)
                if correct:
                    print(dx, self.origin.x, (dx / grid_step), pin.position.x)
                    pin.position.x.text = str(self.origin.x - round(dx / grid_step) * grid_step)
                    print("changing positon x to : " + str(pin.position.x))
            dy = self.origin.y - pin.position.y
            if dy % grid_step != 0:
                list_of_wrong_pins.append(pin.ref)
                if correct:
                    pin.position.y.text = str(self.origin.y - round(dy / grid_step) * grid_step)
                    print("changing positon y to : " + str(pin.position.y))
        return list_of_wrong_pins

CadstarArcObj.register_sub_class(SYMDEF)
