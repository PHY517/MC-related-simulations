import numpy as np
import matplotlib.pyplot as plt
import walk_fortran


N_values = range(10, 1001, 50)
mean_distances = []

for N in N_values:
    distances = [
        walk_fortran.random_walk(N)
        for _ in range(50000)
    ]

    mean_distances.append(np.mean(distances))


plt.plot(N_values, mean_distances, "o-", label="Simulation")

N = np.array(list(N_values))
plt.plot(N, np.sqrt(np.pi * N) / 2, "--", label="Expected")

plt.xlabel("Number of steps, N")
plt.ylabel("Mean final distance")
plt.legend()
plt.grid()
plt.show()


