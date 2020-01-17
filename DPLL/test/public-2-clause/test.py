import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from dpll import *

print(dpll_sat(Prop("~A and A or B")))
