## Point reticulate at the course's Python environment.
## Create it once with:
##   python3 -m venv ~/.virtualenvs/py4fin
##   ~/.virtualenvs/py4fin/bin/python -m pip install pandas numpy matplotlib plotly statsmodels yfinance openpyxl
local({
  venv <- path.expand("~/.virtualenvs/py4fin/bin/python")
  if (file.exists(venv)) Sys.setenv(RETICULATE_PYTHON = venv)
})
