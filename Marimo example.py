import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import seaborn as sns
    return sns,


@app.cell
def __(sns):
    diamonds = sns.load_dataset("diamonds")
    diamonds
    return diamonds,


@app.cell
def __(diamonds, sns):
    sns.barplot(x=diamonds["price"], y=diamonds["cut"])
    return


@app.cell
def __(diamonds, sns):
    sns.histplot(diamonds["price"])
    return


@app.cell
def __(diamonds):
    diamonds_truncated = diamonds.drop(columns=['cut', 'color', 'clarity'])
    return diamonds_truncated,


@app.cell
def __(diamonds_truncated):
    diamonds_truncated
    return


@app.cell
def __(diamonds_truncated):
    diamonds_truncated.corr()
    return


@app.cell
def __(diamonds_truncated, sns):
    sns.heatmap(diamonds_truncated.corr())
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
