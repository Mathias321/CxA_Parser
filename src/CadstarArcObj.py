import sys


class CadstarArcObj(object):
    CAO_keyword = ""
    DICT_POSATTR = []
    DICT_ATTR = {}
    DICT_COLLECTION = {}

    subclasses = {}

    def __init__(self, parent, root):
        # self.children = []
        self.attr = []
        self.parent = parent
        self.root = root
        self.ref = ""

        for pos_attr in self.DICT_POSATTR:
            setattr(self, pos_attr, "")
        for attr in self.DICT_ATTR.values():
            setattr(self, attr, None)
        for col in self.DICT_COLLECTION.values():
            setattr(self, col, {})
        
    def __str__(self):
        return self.get_short_name()

    def add_attr(self, obj):
        self.attr.append(obj)

    def update_attr(self):
        # Store positional attributes into specific attributes
        for index, dest_attr in enumerate(self.DICT_POSATTR):
            # print (str(dest_attr), index, self.attr[index])
            setattr(self, dest_attr, self.attr[index])

        # Store typed attributes into specific attributes
        for attr in self.attr[len(self.DICT_POSATTR):]:
            for cls, dest_attr in self.DICT_ATTR.items():
                if isinstance(attr, cls):
                    setattr(self, dest_attr, attr)
            for cls, col in self.DICT_COLLECTION.items():
                # print (str(cls))
                if isinstance(attr, cls):
                    # print(str(self), str(col), str(attr.ref), str(attr))
                    getattr(self, col)[attr.ref] = attr

    def has_attributes(self):
        return len(self.attr) != 0

    @staticmethod
    def is_considered_as_child():
        return True
    
    @classmethod
    def check(cls, my_str):
        return ("CadstarArcObj."+my_str == cls.__name__
                or my_str == cls.__name__)

    def get_short_name(self):
        return str(type(self)).split(".")[-1][0:-2]

    @classmethod
    def create_sub_class(cls, class_name):
        cls.subclasses[class_name] = type("CadstarArcObj."+class_name,
                                                   (CadstarArcObj, ),
                                                   {})

    @classmethod
    def register_sub_class(cls, sub_class):
        cls.subclasses[sub_class.__name__] = sub_class

    def dump(self, indent=0, file=sys.stdout, child=True):
        has_child = False
        if child:
            print("\n" + " " * indent + "(" + str(self), end="", file=file)
        else:
            print(" (" + str(self), end="", file=file)
        for i, a in enumerate(self.attr):
            if isinstance(a, str):
                if i != 0 and i % 10 == 0:
                    print("\n" + " " * (indent + 1), end="", file=file)
                    has_child = True
                print(" " + a, end="", file=file)
            else:
                if a.is_considered_as_child():
                    has_child = True
                    a.dump(indent + 1, file=file)
                else:
                    if i != 0 and i % 10 == 0:
                        print("\n" + " " * (indent + 1), end="", file=file)
                        has_child = True
                    a.dump(indent, file=file, child=False)
        if has_child:
            print("\n" + " " * indent + ")", end="", file=file)
        else: 
            print(")", end="", file=file)

from symdef import SYMDEF
from LIBRARY import LIBRARY
from ASSIGNMENTS import *
