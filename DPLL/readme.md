# DPLL
A complete backtracking algorithm for effective propositional model checking

<img src="https://github.com/KokoFan16/Artficial_Intelligent/blob/master/DPLL/method.png" width="600" hegiht="400" align=center />

## Problem

Effective propositional model checking: 

- Find out all the possible models for a propositional statement.
- Return true or false (If there is a model satisfy this statement, return true, otherwise, false)

## Solution

Pseudo code: 
<img src="https://github.com/KokoFan16/Artficial_Intelligent/blob/master/DPLL/dpll.png" width="800" hegiht="600" align=center />

## Result


You can check the results of all the test cases with "python3 tester.py --all"

<img src="https://github.com/KokoFan16/Artficial_Intelligent/blob/master/DPLL/result.png" width="400" hegiht="600" align=center />


Or check one test case:

- "cd ./test/public-3-clause/"  (A or B and ~A and ~B)
- python3 ./test.py 

False
