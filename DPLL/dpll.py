
from prop import *
from model import *

# TODO: This function should return True/False to indicate
#       if there exists any model for which prop is satisfied
def dpll_sat(prop):
    # Takes a CNF proposition, an instance of Prop
    # Returns a frozenset of models that satisfy it, or frozenset({})
    
    clauses = prop.clauses
    temp_sys = set(lit.sym for clause in clauses for lit in clause)
    
    syms = frozenset(temp_sys)
    
    # TODO: Populate syms with all the (string) variable names in prop
    return dpll(clauses, syms, Model())

def dpll(clauses, syms, model):
    # TODO: implement DPLL algorithm
    # (hint: try naive backtracking, or even exhaustive search first)

    result = [checkClause(clause, model) for clause in clauses]
    if False in result:
        return False
    elif None not in result:
        return True

    psym, value = findPureSymbol(clauses, syms, model)
    if psym is not None:
        model = model.extend(psym, value)
        syms = syms - frozenset({psym})
        return dpll(clauses, syms, model)


    usym, value = findUnitClause(clauses, model)
    if usym is not None:
#        print("unit",  usym, value)
        model = model.extend(usym, value)
        syms = syms - frozenset({usym})
        return dpll(clauses, syms, model)

    p, *_ = syms
    rest = syms - frozenset({p})

    return dpll(clauses, rest, model.extend(p, True)) or dpll(clauses, rest, model.extend(p, False))



def checkClause(clause, model):
    false_lit = 0
    for lit in clause:
        if model.exists(lit.sym):
            if model.valueof(lit.sym) == True and isinstance(lit, PosLit):
                return True
            elif model.valueof(lit.sym) == False and isinstance(lit, NegLit):
                return True
            else:
                false_lit += 1
    if false_lit == len(clause):
        return False
    return None


def findPureSymbol(clauses, syms, model):

    lits = [lit for clause in clauses for lit in clause if checkClause(clause, model) != True]

    for sym in syms:
        posLits = set(isinstance(lit, PosLit) for lit in lits if sym == lit.sym)
        if len(posLits) == 1:
            return sym, posLits.pop()

    return None, None


def findUnitClause(clauses, model):
    
    for clause in clauses:
        if checkClause(clause, model) != True :
            if len(clause) == 1:
                lit, *_ = clause
                value = True if isinstance(lit, PosLit) else False
                return lit.sym, value

            unsigned_lits = [lit for lit in clause if not model.exists(lit.sym)]

            if len(unsigned_lits) == 1:
                value = True if isinstance(unsigned_lits[0], PosLit) else False
                return unsigned_lits[0].sym, value

    return None, None
