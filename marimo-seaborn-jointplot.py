import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import seaborn as sns
    return sns,


@app.cell
def __():
    import matplotlib.pyplot as plt
    return plt,


@app.cell
def __(sns):
    diamonds = sns.load_dataset('diamonds')
    return diamonds,


@app.cell
def __(diamonds):
    diamonds.head()
    return


@app.cell
def __(diamonds, sns):
    sns.jointplot(x="depth", y="price", data=diamonds, kind='hex')
    return


@app.cell
def __(diamonds, sns):
    sns.jointplot(x="depth", y="table", data=diamonds, kind='hex')
    return


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
    sns.jointplot(x="petal_width", y="petal_length", data=iris, kind='reg')
    return


@app.cell
def __(iris, sns):
    sns.jointplot(x="sepal_length", y="petal_width", data=iris, kind='reg')
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
