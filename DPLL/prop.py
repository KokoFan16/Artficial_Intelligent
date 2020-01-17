
import re

class PosLit:
    def __init__(self, sym):
        self.sym = str(sym)
    def __hash__(self):
        return hash(self.sym)
    def __str__(self):
        return self.sym

class NegLit:
    def __init__(self, sym):
        self.sym = str(sym)
    def __hash__(self):
        return hash(self.sym) + 1
    def __str__(self):
        return "~"+self.sym
    
class Prop:
    def __init__(self, clauses):
        def parseCNF(s):
            toks = s.replace("&", " & ").replace("|", " | ").replace("~", " ~ ").replace("and"," & ").replace("not"," ~ ").replace("or"," | ")
            while toks != toks.replace("  ", " "): toks = toks.replace("  ", " ")
            toks = toks.strip().split(" ")
            def peek():
                nonlocal toks
                if toks == []: return ""
                return toks[0]
            def expect(t):
                nonlocal toks
                if peek() == t:
                    toks = toks[1:]
                else:
                    print("Not a valid CNF string, expected: '"+str(t)+"', got: "+str(toks))
                    exit(1)
            def parseX():
                x = peek()
                if re.match(r"^([A-Z][0-9]*)$", x) != None:
                    expect(x)
                    return x
                else:
                    print("Not a valid ID, got: "+str(x))
                    exit(1)
            def parseLit():
                if peek() == "~":
                    expect("~")
                    return NegLit(parseX())
                else:
                    return PosLit(parseX())
            def parseCl():
                lits = frozenset({parseLit()})
                while peek() == "|":
                    expect("|")
                    lits |= frozenset({parseLit()})
                return lits
            clauses = frozenset({parseCl()})
            while peek() == "&":
                expect("&")
                clauses |= frozenset({parseCl()})
            return clauses
        if isinstance(clauses, str):
            self.clauses = parseCNF(clauses)
        else:
            self.clauses = frozenset(clauses)
    def __hash__(self):
        return hash(self.clauses)
    def __str__(self):
        pstr = ""
        for clause in self.clauses:
            if pstr != "": pstr += " and "
            cstr = ""
            for lit in clause:
                if cstr != "": cstr += " or "
                cstr += str(lit)
            pstr += cstr
        return pstr
        

