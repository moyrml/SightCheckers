# Checker Game
## Overview
This repository contains the code for a complete checkers game. It requires input files in the format: 
```commandline
x0,y0,x1,y1
x0,y0,x1,y1
...
```
Where `x0,y0` are the source cell coordinates, and `x1,y1` are the target cell coordinates. The end of the file
represents the end of the game. The state at the end of the game is analyzed and a winner is declared.


## Pre-requisites 
This code was developed using:

* Python 3.10
* Linux Kubuntu 22.04

The cross-platform nature of python means that it should work on other operating systems, but it wasn't tested.

## Installation
1. *code:* Clone the repository:
    ```bash
   git clone git@github.com:moyrml/SightCheckers.git
   ```
   
1. *dependencies:* This is a pure python project, so no dependencies.

## Usage
```commandline
python main.py 

        How to use:
        >>> python main.py [-h,--help] [-v,--verbose] /path/to/moves_file.txt
        
        -h, --help: Optional. Print this and exit.
        -v, --verbose: Optional. Create a txt file depicting step-by-step game progress.
        
```

Examples:

```commandline
$ python main.py data/black.txt 
second
```

```commandline
$ python main.py -v data/incomplete.txt
Verbose mode - will create a file game_progression.txt with game moves
incomplete
```

Verbose mode will have an extra output useful for visualisation - a file `game_progression.txt` in the following
format:
```text

move #0: ==================================================
-       b       -       b       -       b       -       b       7
b       -       b       -       b       -       b       -       6
-       b       -       b       -       b       -       b       5
-       -       -       -       -       -       -       -       4
-       -       -       -       -       -       -       -       3
w       -       w       -       w       -       w       -       2
-       w       -       w       -       w       -       w       1
w       -       w       -       w       -       w       -       0
7       6       5       4       3       2       1       0

move #1: 3,2,4,3===========================================
-       b       -       b       -       b       -       b       7
b       -       b       -       b       -       b       -       6
-       b       -       b       -       b       -       b       5
-       -       -       -       -       -       -       -       4
-       -       -       w       -       -       -       -       3
w       -       w       -       -       -       w       -       2
-       w       -       w       -       w       -       w       1
w       -       w       -       w       -       w       -       0
7       6       5       4       3       2       1       0

move #2: 4,5,3,4===========================================
-       b       -       b       -       b       -       b       7
b       -       b       -       b       -       b       -       6
-       b       -       -       -       b       -       b       5
-       -       -       -       b       -       -       -       4
-       -       -       w       -       -       -       -       3
w       -       w       -       -       -       w       -       2
-       w       -       w       -       w       -       w       1
w       -       w       -       w       -       w       -       0
7       6       5       4       3       2       1       0

...
```