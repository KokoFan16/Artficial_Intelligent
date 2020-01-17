import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from dpll import *

print(dpll_sat(Prop("X16|X23|X42 & ~X16|X23|X42 & X26|X41|~X42 & ~X26|X41|~X42 & ~X42 & X6|X15|~X41 & ~X6|X15|~X32 & X1|~X32|X46 & ~X1|~X32|X46 & ~X15|~X41|~X46 & ~X15|~X21|~X46 & ~X23|X33|X38 & ~X23|~X33|X38 & X8|X22|X33 & X8|X22|~X33 & ~X22|X37|~X38 & X13|X36|~X37 & X13|~X22|~X36 & ~X13|~X37 & X11|~X23|X47 & ~X8|X11|~X47 & ~X8|~X11|X39 & ~X11|X27|~X39 & ~X8|~X11|~X39 & ~X7|X26|X29 & ~X7|~X26|X29 & ~X13|X20|X36 & ~X13|X17|X20 & X5|~X17|X20 & X5|~X19|~X45 & ~X5|~X10|~X45 & X6|X25|X47 & ~X6|~X10|X25 & ~X2|~X27|X37 & ~X27|~X36|X40 & X18|X39|~X40 & ~X2|~X19|X31 & X5|X18|~X30 & ~X31|~X43|~X50 & X10|~X30|X43 & X10|~X41|X43 & X19|X21")))
