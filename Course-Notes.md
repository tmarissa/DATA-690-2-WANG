# Session 1 January 28, 2021
## Marissa Tan

## Textbook 
[Python for Data Analysis by Wes McKinny Second Edition](https://github.com/chenomg/CS_BOOKS/blob/master/Python%20for%20Data%20Analysis%2C%202nd%20Edition.pdf)

## Terminology
ipynb - iteractive python notebook

### Environments
- Functionality - Anaconda, Deep Note, Colab
- Developing - Deep Note
- Structural - github

### Working on Deep Note
- root@deepnote/work #
- pwd - present working direction
- ls - listing
- python filename.py

### Notes from class
- python - 0 base index
- Discussion on (01-Python-Basics.ipynb)[https://github.com/wcj365/python-stats-dataviz/blob/e81a8c558d656a866d3c71b4623df1b345db746c/01%20-%20Python-Basics.ipynb]

# Notes from Textbook
## Chapter 1
Python 
- run slower, programmer time is as valuable as CPU
- challenging language - concurrent multithreaded applications 

Global Interpreter Lock (GIL) - prevents the interpreter from executing more than one python instructions at a time.

Essentials:
- Numpy : numerical python
- Pandas : high level data structure and functions designed to make working with structures or tabular data fast, easy, and expressive.
  - panel data : mutli-dimensional structural datasets
- Matplotlib : producting plots and 2 dimensional data visualization
- IPython : interactive Python execute, explorer workflow
- Jupyter : design language - agnostic interactive computing tools; exploratory computing; markdown & html
  - kernel : a programming language mode
- SciPy : scientific computing
- Scikit-learn : general purpose machine learning toolkit
- Statsmodel : statistical analysis package
  - Regression, Anova, AR

## Chapter 2
### Notes
- >>> prompt
- exit () or ctrl-D - exit Python and return to command prompt
- $ python hello_world.py or %run hello_world.py
- $ ipython = running the IPython Shell
- tab completion = pressing Tab key will search the namespace for any variables matching the characters you have typed so far
- a question mark (?) before or after a variable will display some general information
about the object (p. 23)
- Using ?? will also show the function’s source code (p 24)
- A number of characters combined
with the wildcard (*) will show all names matching the wildcard expression.  Example np.*load*? (p 24)
- empty namespace (with no imports or other variables defined)so that the behavior should be identical to running the program on the command line (p 25)
- Besides %run, %load can also be used
- Copy and paste, use %paste whatever test is in the clipboard and executes it as a single block in the shell. While %cpaste has a special prompt for pasting code. It can paste as much code as needed before excuting it. Break the prompt by pressing Ctrl-C.
- Standard IPython keyboard shorcuts (p 27)
- Magic Commands (p 28-30) which is any command prefixed by the percent symbol %.
- colon denotes the start of an indented code block after which all of the code must be indented by the same amount until the end of the block. Preferably use 4 spaces rather than tab.
- semicolons use to separate multiple statements on a single
line.
- comments uses # (pound sign)
- a//b floor-divide a by b, dropping any fractional remainder
- a^b For booleans, True if a or b is True, but not both; for integers, take the bitwise EXCLUSIVE-OR
- list, dicts, NumPy arrays, and user-defined classes are mutable. 
- strings and tuples are immutable.
- scalar (p 39) None, float, bytes, str, bool, int.
- r stands for raw. Adding r in front of a string will add the backlashes. Ex. r'this\has' will become 'this\\has'
- {0:.2f) first argument with floating point wiht 2 decimal {1:s} second argument with string {2:d} third argument exact
- converting unicode string to UTF-8 bytes used ex: val.encode("utf-8"). b stands for bytes. Reversing uses decode (p 42)
- strftime method formats a datetime as a string and converted (parsed) into datetime objects (p 45)
- datetime format (p 45)
- Control Flow
  - if, elif, else
  - for loops - iterating over a collection (list or tuple) or an iterator.
  - while - specifies a condition and a block of code thqt is to be executed until condition is False or loop ended with a break.
  - pass is the “no-op” statement in Python. It can be used in blocks where no action is to be taken (or as a placeholder for code not yet implemented); it is only required because Python uses whitespace to delimit blocks
  - range - returns an iterator that yields a sequence of evenly spaced integers
  - ternary expressions - true-expr and false-expr Ex. 'Non-negative' if x >= 0 else 'Negative'(p 49)








