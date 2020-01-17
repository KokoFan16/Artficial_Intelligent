import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from dpll import *

print(dpll_sat(Prop("~A or ~A or ~B and B or ~C or ~F or ~C or ~F or ~E and A or B or ~D and ~D or ~C or F or ~F and ~A or C or C or B and E or C or ~D or ~A or E or ~F or C")))
