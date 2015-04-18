import os
import re
from CadstarArcObj import *

# Just for debug ease, make constants for input and output files
CURDIR = os.path.dirname(os.path.abspath(__file__))
FILE = CURDIR + "\\..\\examples\\CC1111_USB_Dongle_Johanson_1_0.csa"
FILEOUT = CURDIR + "\\..\\examples\\mine.csa"


class Archive(object):
    def __init__(self):
        self.l = []
        self.mainObj = None
        self.objects = []
        self.parts = {}
        self.symbols = {}

    def readFromFile(self, file=FILE):
        f = open(file)
        text = f.read()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\n+", "", text)
        l = re.split('("[^"]*"|[\(\)\s])', text)
        l = [x for x in l if x != " " and x != ""]
        self.l = l

    def findObject(list, parent, index=0):
        if list[index] == "(" :
            index += 1
            obj = mySchObjFactory(list[index], parent)
            index += 1
            while list[index] != ")":
                nextObj, index = Archive.findObject(list, parent, index)
                obj.add_attr(nextObj)
                index += 1
            obj.update_attr()
            return obj, index
        else :
            return list[index], index

    def classify(self):
        self.mainObj = Archive.findObject(self.l, self)[0]

    def registerPart(self, part):
        self.parts[part.attr[0]] = part

    def registerSymbol(self, symbol):
        self.symbols[symbol.attr[0]] = symbol
        
    def dump(self, file=None):
        if file is None:
            self.mainObj.dump()
        else:
            f = open(file, "w")
            mySch.mainObj.dump(file=f)
            f.close()


def mySchObjFactory(myStr, parent):
    for cls in CadstarArcObj.subclasses.values():
        if cls.check(myStr):
            return cls(parent)
    # print (myStr + " is not known yet...")
    CadstarArcObj.create_sub_class(myStr)
    # return type(myStr, (Schema.SchObj, ), {"attr" : []})()
    return CadstarArcObj.subclasses[myStr](parent)


mySch = Archive()
mySch.readFromFile()

mySch.classify()
mySch.dump(FILEOUT)

