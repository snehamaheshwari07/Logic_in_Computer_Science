# Logic_in_Computer_Science
This repository is the clause listing and DPLL algorithm SAT solver for Einstein's puzzle.

## About the file and how to run it.
In this file, I created all the clauses as mentioned in puzzle, and a DPLL solver to find that if the puzzle is SATISFYING or NOT_SATISFYING.
- To begin, you need to download the file Einstine's_puzzle.py
- To run the file, you need two libraries:
 - itertools
 - copy
- To install these libraries, you may run these commands:
 - pip3 install more-itertools
 - copy is a standard python library, so you might not need to install it saperately.
- Now open the terminal in the folder where you downloaded the file and run the follwing command
  - python Einstine's_puzzle.py

This will give you two outputs where the first one is a disctionary of assignments to each variable, where variables are encoded as numbers, the second one represent the list of literals which are true which can be read as per the convention as mentioned in the report file.
