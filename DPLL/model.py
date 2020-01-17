
from copy import deepcopy

class Model:
    def __init__(self):
        self.assignments = dict()
    def extend(self,sym,val):
        # Returns a new model with the assignment sym->val
        cpy = deepcopy(self)
        cpy.assign(sym,val)
        return cpy 
    def assign(self,sym, val):
        # sym is a string
        # val is True or False
        self.assignments[sym] = val
    def exists(self, sym):
        return sym in self.assignments
    def valueof(self,sym):
        return self.assignments[sym]
    def __hash__(self):
        h = 1
        for k,v in self.assignments.items():
            kh += hash(k) + hash(v)
        return h
    def __str__(self):
        s = ""
        for k,v in self.assignments.items():
            if s != "": s = s + ","
            if v: s = s + k
            else: s = s + "~" + k
        return s
        
