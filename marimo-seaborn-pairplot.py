import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import seaborn as sns
    return sns,


@app.cell
def __():
    import pandas as pd
    return pd,


@app.cell
def __(sns):
    iris = sns.load_dataset("iris")
    return iris,


@app.cell
def __(iris):
    iris.head()
    return


@app.cell
def __(iris, sns):
    sns.pairplot(iris, hue='species', height=1.5);
    return


@app.cell
def __(sns):
    diamonds = sns.load_dataset('diamonds')
    return diamonds,


@app.cell
def __(diamonds):
    diamonds.head()
    return


@app.cell
def __(diamonds):
    sliced_diamonds = diamonds[["cut", "depth", "table"]]
    return sliced_diamonds,


@app.cell
def __(sliced_diamonds):
    sliced_diamonds.head()
    return


@app.cell
def __(sliced_diamonds, sns):
    sns.pairplot(sliced_diamonds, hue='cut', height=2.5)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
