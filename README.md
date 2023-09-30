# Logic_in_Computer_Science
This repository is the clause listing and DPLL algorithm SAT solver for Einstein's puzzle and analysis of 3 heuristics in DPLL algorithm.

## About the file 'Einstine's_puzzle.py' and how to run it.
In this file, I created all the clauses as mentioned in puzzle, and a DPLL solver to find that if the puzzle is SATISFYING or NOT_SATISFYING.
- To begin, you need to download the file Einstine's_puzzle.py
- To run the file, you need two libraries:
  - itertools
  - copy
- To install these libraries, you may run these commands:
  - pip3 install more-itertools
  - copy is a standard python library, so you might not need to install it saperately.
- Now open the terminal in the folder where you downloaded the file and run the follwing command
  - python3 Einstine\'s_puzzle.py

This will give you two outputs where the first one is a disctionary of assignments to each variable, where variables are encoded as numbers, the second one represent the list of literals which are true which can be read as per the convention as mentioned in the report file.

## About the file 'heuristic_analysis.py' and how to run it.
In this file, I have done the analysis of all three heuristics with each other on a randomly generated 3-SAT clauses, i.e. random choice, 2-clause, 2and3-clause.
Running this file will show us the following for each heuristic:
- compute time
- DPLL run count
- Splitting rule count
It also gives us the Satisfiable probability for each batch of 100 runs.

- To run this file, download the file. 
- Install the following libraries.
  - deepcopy
  - random
  - time
  - timeout
  - matplotlib.pyplot
  - numpy
  - statistics
 
- Now open the terminal in the folder where you downloaded the file and run the follwing command
  - python3 heuristic_analysis.py
