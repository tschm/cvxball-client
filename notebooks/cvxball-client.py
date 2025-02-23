# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "numpy-flight==0.0.8",
#     "numpy==2.2.3"
# ]
# ///

import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""Demo""")
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
