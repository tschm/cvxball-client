# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "numpy-flight==0.0.8",
#     "numpy==2.2.3",
#     "matplotlib==3.10.0",
# ]
# ///

import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""Demo cvxball-client""")
    return


@app.cell
def _():
    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt

    def plot_points(p, p0, r0):
        _, ax = plt.subplots()
        ax.set_aspect("equal")

        # plot the cloud of points
        ax.plot(p[:, 0], p[:, 1], "b*")

        # mark the midpoint
        ax.plot(p0[0], p0[1], "r.")

        # plot the circle
        ax.add_patch(mpatches.Circle(p0, r0, fc="w", ec="r", lw=1.5))

        ax.grid(True)
        return ax

    return mpatches, plot_points, plt


@app.cell
def _():
    import numpy as np

    data = {"input": np.random.randn(200, 2)}
    return data, np


@app.cell
def _(data, plot_points, plt):
    from np.flight import Client

    # Connect to the server
    with Client("grpc+tls://cvxball-710171668953.us-central1.run.app:443") as client:
        # The server will return a dictionary of numpy arrays
        results = client.compute(command="test", data=data)
        ax = plot_points(results["points"], results["midpoint"], results["radius"])
        ax.set_title("Smallest enclosing circle")
        plt.show()
    return Client, ax, client, results


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
