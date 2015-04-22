import os
import re
from CadstarArcObj import *

# Just for debug ease, make constants for input and output files
CURDIR = os.path.dirname(os.path.abspath(__file__))
FILE = CURDIR + "\\..\\examples\\symbol.csa"
FILEOUT = CURDIR + "\\..\\examples\\mine.csa"


class Archive(object):
    def __init__(self):
        self.l = []
        self.mainObj = None
        self.objects = []
        self.parts = {}
        self.symbols = {}

    def read_from_file(self, file=FILE):
        f = open(file)
        text = f.read()
        text = re.sub(r"\n+", "", text)
        # Some comments about the following regexp:
        # So, it splits the input string with '(', ')', space or quoted strings ->  (".*"|[\(\)\s])
        #  but it ignores separators within quoted strings (embraced by '"')   -> (".*?"|...) (lazy match)
        #   and it takes care not to take account of quotes precedent by '\'   -> (?<!\\)" (negative lookbehind)
        l = re.split(r'((?<!\\)".*?(?<!\\)"|[\(\)\s])', text)
        l = [x for x in l if x != " " and x != ""]
        self.l = l

    @classmethod
    def find_object(cls, list_, parent, root, index=0):
        if list_[index] == "(":
            index += 1
            obj = my_sch_obj_factory(list_[index], parent, root)
            index += 1
            while list_[index] != ")":
                next_obj, index = Archive.find_object(list_, parent, root, index)
                obj.add_attr(next_obj)
                index += 1
            obj.update_attr()
            return obj, index
        else:
            return list_[index], index

    def classify(self):
        self.mainObj = Archive.find_object(self.l, self, self)[0]

    def register_part(self, part):
        self.parts[part.attr[0]] = part

    def register_symbol(self, symbol):
        self.symbols[symbol.attr[0]] = symbol
        
    def dump(self, file=None):
        if file is None:
            self.mainObj.dump()
        else:
            f = open(file, "w")
            mySch.mainObj.dump(file=f)
            print("\n", file=f)
            f.close()


def my_sch_obj_factory(my_str, parent, root):
    for cls in CadstarArcObj.subclasses.values():
        if cls.check(my_str):
            return cls(parent, root)
    # print (myStr + " is not known yet...")
    CadstarArcObj.create_sub_class(my_str)
    # return type(myStr, (Schema.SchObj, ), {"attr" : []})()
    return CadstarArcObj.subclasses[my_str](parent, root)


mySch = Archive()
mySch.read_from_file()

mySch.classify()
mySch.dump(FILEOUT)

