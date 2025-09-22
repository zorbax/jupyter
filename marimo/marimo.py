import marimo

__generated_with = "0.16.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # A next-generation Python notebook
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Pandas DataFrame
        """
    )
    return


@app.cell
def _():
    from string import ascii_uppercase as letters
    import numpy as np
    import pandas as pd
    return letters, np, pd


@app.cell
def _(letters, np, pd):
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, len(letters))),
                      columns=list(letters))
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Show the same DataFrame
        """
    )
    return


@app.cell
def _(df):
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Asynchronous HTTP requests and JSON
        """
    )
    return


@app.cell
def _():
    import sys
    return


@app.cell
async def _():
    import aiohttp
    import asyncio

    async def fetch_data(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    # Use await directly in a Jupyter Notebook cell
    url = "https://httpbin.org/get"
    data = await fetch_data(url)
    return (data,)


@app.cell
def _(data):
    print(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Sympy
        """
    )
    return


@app.cell
def _():
    from sympy import Integral, init_printing, sqrt, symbols

    init_printing()

    x = symbols("x")

    Integral(sqrt(1 / x), x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## SQLlite
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using the [northwind example](https://github.com/jpwhite3/northwind-SQLite3).
        """
    )
    return


@app.cell
def _(display):
    import sqlite3
    from pathlib import Path

    con = None
    for db_path in (Path("./data/northwind.sqlite3"), 
                    Path("jupyter/book/data/northwind.sqlite3")):
        try:
            con = sqlite3.connect(f"file:{db_path.resolve()}?mode=ro", uri=True)
            break
        except sqlite3.OperationalError:
            pass
        
    cur = con.cursor()
    display(*cur.execute("SELECT LastName, FirstName FROM Employees").fetchall())
    return (con,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Or even with [`pandas`](https://pandas.pydata.org/docs/user_guide/io.html#sql-queries):
        """
    )
    return


@app.cell
def _():
    import base64
    import IPython
    import pandas
    return IPython, base64, pandas


@app.cell
def _(base64, con, pandas):
    df_1 = pandas.read_sql_query('SELECT * from Employees', con, 'EmployeeID')
    df_1['Photo'] = df_1['Photo'].apply(lambda raw: f'<img src="data:image/png;base64,{base64.b64encode(raw).decode('utf-8')}"/>')
    return (df_1,)


@app.cell
def _(IPython, df_1):
    IPython.display.HTML(df_1.T.to_html(escape=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Demo of `folium` Map

        Load in the `folium` package:
        """
    )
    return


@app.cell
def _():
    import folium
    return (folium,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        And render a demo map:
        """
    )
    return


@app.cell
def _(folium):
    m = folium.Map(location=[57.688236, 11.978573], zoom_start=15)
    return (m,)


@app.cell
def _(m):
    m
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
