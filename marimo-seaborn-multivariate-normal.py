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
def __():
    import matplotlib.pyplot as plt
    return plt,


@app.cell
def __():
    import numpy as np
    return np,


@app.cell
def __(np):
    data = np.random.multivariate_normal([1, 3, 5], [[7, 5, 1], [5, 8, 2], [1, 2, 4]], size=30000)
    return data,


@app.cell
def __(data, pd):
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    return df,


@app.cell
def __(df):
    df
    return


@app.cell
def __(df, plt):
    for col in 'xyz':
        plt.hist(df[col], density=True)
    plt.show()
    return col,


@app.cell
def __(df, sns):
    sns.kdeplot(data=df, fill=True)
    return


if __name__ == "__main__":
    app.run()
