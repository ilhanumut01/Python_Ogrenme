# Python Öğrenme / Learning Python

A collection of Python scripts I wrote while learning the language, progressing from the basics to object-oriented programming, and later to parallel computing and hardware communication. Comments and variable names in most files are in Turkish.

All files are in the [`Basic to OOP`](./Basic%20to%20OOP) folder.

## Topics Covered

| Area | Examples |
|---|---|
| **Fundamentals** | Variables, data types, user input, arithmetic operators, booleans, strings |
| **Control flow** | Decision structures, `for` / `while` loops, `break` / `continue` |
| **Data structures** | Lists, tuples, dictionaries |
| **Functions** | Functions, recursion, `lambda` / `map` / `filter`, modules (`random`, `math`) |
| **Error handling** | `try` / `except` / `finally` |
| **File I/O & Regex** | Reading and writing files, pattern matching with `re` |
| **OOP** | Classes and objects (`OOP_1.py`, `OOP_2.py`) |
| **Parallel programming** | Genetic sequence search: sequential vs. `multiprocessing` vs. MPI (`mpi4py`) |

## Small Programs

Calculator, circle area/perimeter, BMI calculator, Fahrenheit to Celsius, prime numbers, string reversal, word counter, student number parser, and several quiz-style exercises.

## Highlight: Parallel Sequence Search

`1Gen_Bulma.py`, `1Paralel_Gen_Bulma.py` and `1MPI_Ornek.py` search a 200-million-base random DNA sequence for a given pattern. They compare execution time across a sequential version, a process-based `multiprocessing` version, and an MPI version, handling chunk-boundary overlaps so matches aren't missed.

## Requirements

- Python 3
- `numpy`, `mpi4py` (parallel examples only)
- `pyserial` (`Exam.py` only)

```bash
pip install numpy mpi4py pyserial
```

## Running

```bash
cd "Basic to OOP"
python Hesap_Makinesi.py

# MPI example
mpiexec -n 4 python 1MPI_Ornek.py
```
