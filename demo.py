import numpy as np
from np.flight import Client
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = {"input": np.random.randn(200, 2)}
    # Connect to the server
    with Client("grpc+tls://cvxball-710171668953.us-central1.run.app:443") as client:
        # The server will return a dictionary of numpy arrays
        results = client.compute(command="test", data=data)

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

    ax = plot_points(results["points"], results["midpoint"], results["radius"])
    ax.set_title("Smallest enclosing circle")
    plt.show()
