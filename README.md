# Introduction to Python for Finance

> ### 🌐 Translation Disclaimer
>
> This course was originally written and taught in **Spanish** as *"Introducción a Python para las
> Finanzas"* (ENGIN 604, Magíster en Finanzas Full-Time, Universidad de Chile). This version is a
> complete **English translation** of that original material.
>
> The translation covers the lecture notes, notebooks, scripts, slides, syllabus, homework policies,
> assignments and the final exam — including code comments, printed strings, variable and function
> names, and file names. Course content, exercises, data and numerical results are unchanged from the
> Spanish original.
>
> A few notes:
> - The homework and final-exam `.Rmd` sources were **reconstructed from the compiled Spanish PDFs**,
>   as the originals were no longer available. Their mathematical formulas were re-typeset in LaTeX.
> - Proper nouns (the university, instructor and teaching assistant names) and cited bibliographic
>   titles are intentionally left in their original form.
> - The Spanish version remains available in this repository's history on the `main` branch.
>
> If you spot a translation error or an awkward phrasing, please open an issue.

## Course Description

Created in 1991 by Guido van Rossum, Python has become one of the favorite programming languages in
both academia and industry, thanks to its simple syntax and extensive (powerful) libraries. The course
aims to provide the basic tools to tackle financial and/or economic problems. Topics discussed include:
data structures, conditional control flow, functions, an introduction to the NumPy library, data
manipulation with Pandas, and time series.

## Objectives

1. Understand Python's syntax and programming environment
2. Become familiar with the different data types and structures
3. Manipulate structured databases using Pandas
4. Create your own functions to solve real-world problems
5. Present results using Jupyter Notebooks

## Grading

The final grade is weighted as follows:

* Homework: 70% (maximum 2 members per group)
* Final Exam: 30% (covers all course material)

## Methodology

The course is delivered through lectures and hands-on exercises using Python.

## Contents

1. Introduction

    + Anaconda Installation and Setup (IDEs)
    + The Python Interpreter
    + IPython Shell
    + Jupyter Notebook
    + Google Colaboratory

2. Data Structures & Sequences

    + Tuple (`tuple`)
    + List (`list`)
    + Dictionary (`dict`)
    + Set (`set`)

3. Conditional Control Flow

    + `for` and `while` loops
    + `if`, `elif` and `else`
    + Logical Operators
    + Mathematical Operators
    + List, Set and Dictionary Comprehensions

4. Functions

    + Creating and Importing
    + Itertools Module
    + Anonymous Functions (Lambda)
    + Error and Exception Handling
    + Importing Libraries
    + Example: Bullet Bond Price

5. Introduction to NumPy

    + Array, Matrix and ndarray
    + Concatenation, Splitting and Subsetting
    + Array Computation: Broadcasting
    + Linear Algebra Functions
    + Example: Linear Regression
    + Example: *Random Walk*

6. Data Manipulation with Pandas

    + DataFrame, Series and Index Object
    + Essential Functions for Pandas Data Structures
    + Handling *Missing Values* and *Null Values*
    + Variable Transformation
    + Data Aggregation and Group Operations
    + Combining Datasets: Concat, Append, Merge and Join
    + Reshape and Pivot
    + Importing and Exporting Data
    + Example: Generating *Dummies*

7. Time Series

    + Time Series Data Structures in Pandas
    + *Resampling* and *Shifting* (Building Returns)
    + *Rolling Window* and *Expanding Window*
    + Example: *Equally Weighted* Portfolio
    + Example: Geometric Cumulative Return

## Building from Source

The `.Rmd` sources render to PDF via `knitr`/`bookdown`, and the slides via `xaringan`. The
syllabus is a Quarto document (`syllabus/index.qmd`) built on the
[qkit](https://github.com/gabbocg/qkit) syllabus template, so it needs
[Quarto](https://quarto.org) rather than the R Markdown toolchain:

```bash
quarto render syllabus/index.qmd
```

**Python** (executed by `reticulate` inside the `{python}` chunks):

```bash
python3 -m venv ~/.virtualenvs/py4fin
~/.virtualenvs/py4fin/bin/python -m pip install pandas numpy matplotlib plotly statsmodels yfinance openpyxl
```

Then point `reticulate` at it. `.Rprofile` files are **not tracked in this repository**
(see `.gitignore`), so create one yourself in each directory you knit from — or once in your home
directory to cover everything:

```r
# ~/.Rprofile
local({
  venv <- path.expand("~/.virtualenvs/py4fin/bin/python")
  if (file.exists(venv)) Sys.setenv(RETICULATE_PYTHON = venv)
})
```

Alternatively, set `RETICULATE_PYTHON` in your environment before launching R.

**R packages:**

```r
install.packages(c("knitr", "rmarkdown", "bookdown", "reticulate",
                   "xaringan", "xaringanthemer", "highcharter", "tidyverse"))
remotes::install_github("mitchelloharawild/icons")  # slides
remotes::install_github("hadley/emo")               # slides
icons::download_fontawesome()
```

**LaTeX:** a TeX distribution (TinyTeX is fine) plus the `fontawesome` package. `assignments/policies`
compiles with `xelatex` and needs `FontAwesome.otf` visible to the system font manager — on macOS,
copy it into `~/Library/Fonts/`.

> **Note:** `material/lesson-08` downloads live market data through `yfinance`. It requests the
> ticker `FB`, which Yahoo retired when Meta re-tickered to `META` in 2022, so that request now
> returns an empty frame and the solution notebook will not knit until the ticker is updated.

## Recommended Readings

1. McKinney, Wes (2017). Python for data analysis: Data wrangling with Pandas, NumPy, and IPython. "
O’Reilly Media, Inc.".

2. Ramalho, Luciano (2015). Fluent python: Clear, concise, and effective programming. " O’Reilly Media,
Inc.".

3. Sheppard, Kevin (2019). “Introduction to Python for econometrics, statistics and data analysis’ ’.
In: Self-published, University of Oxford, version 3.

4. VanderPlas, Jake (2016). Python data science handbook: Essential tools for working with data. " O’Reilly
Media, Inc.".
