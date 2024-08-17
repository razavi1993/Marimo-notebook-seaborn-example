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
    iris = sns.load_dataset('iris')
    return iris,


@app.cell
def __(iris):
    iris.head()
    return


@app.cell
def __(iris, sns):
    sns.catplot(x="sepal_width", y="petal_length", hue="species", data=iris, kind='box', height=6.5)
    return


@app.cell
def __(iris, sns):
    sns.violinplot(x="species", y="petal_length", data=iris)
    return


@app.cell
def __(iris, sns):
    sns.violinplot(x="species", y="sepal_width", data=iris)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
