# Introduction

This course is an introduction to the Python language using ready-to-run code and a few simple exercices.

A focus is made on the scientific use of Python (parts D and E) while some non-Python knowledge is presented in part A.

The indicative __difficulty of each section (parts B, C, D, and E) is given in brackets__ (see the table of contents of the PDF file)):

- easy: the required knowledge for those who never coded in Python
- medium: some features that are somehow needed to improve your code
- advanced: interesting content, yet rarely needed for scientific programming


# Content of the repository

A PDF file of the entire course is available in the `build` directory. This PDF file is built from the Python notebooks that can be found in the `src_EN` directory:

- `EX.ipynb` are exercices
- `EX-COR.ipynb` are exercice corrections
- other files are the course itself

The build directory contains material to build the PDF file:

- `main.ipynb` converts the notebooks to LaTex files.

   Requires the `nbconvert` Python package.
- `main.tex` organize these .tex files to build a single document.

   Requires a valid tex installation. 
   That was tested with a `texlive` installation with some additional packages, using Linux (Mint).

# Python requirements

In addition to `nbconvert`, the following packages are needed to run the code:

- `ipython` (tested with version 8.11)
- `jupyter` 
- `matplotlib` (3.4)
- `numpy` (1.24)
- `pandas` (1.5)
- `scikit-learn` (1.3)
- `scipy` (1.10)
- `seaborn` (0.12)
- `Sphinx` (7.2)
- `sympy` (1.11)
- `tqdm` (4.65)

# Author

Boris Nerot - Research Engineer at LOCIE (Université Savoie Mont Blanc)

boris.nerot@univ-smb.fr

# Disclaimer

1. This content might evolve in a near future. 
2. You may:
    
    - suggest improvements to this content 
    - __modify the content and share your modifications__, according to the GNU 3 license. This includes __citing the original author__.
