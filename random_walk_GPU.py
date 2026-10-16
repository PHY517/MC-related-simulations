import numpy as np
import torch
import matplotlib.pyplot as plt


# Select the available GPU.
if torch.cuda.is_available():
    # NVIDIA CUDA or AMD ROCm
    device = torch.device("cuda")

elif torch.backends.mps.is_available():
    # Apple Silicon
    device = torch.device("mps")

elif hasattr(torch, "xpu") and torch.xpu.is_available():
    # Intel GPU
    device = torch.device("xpu")

else:
    device = torch.device("cpu")

print("Using:", device)


N_values = range(10, 1001, 50)
number_of_walks = 50000

mean_distances = []

# Changes in x and y for the four directions
dx = torch.tensor([1, -1, 0, 0], device=device)
dy = torch.tensor([0, 0, 1, -1], device=device)


for N in N_values:
    # Generate every walk simultaneously on the GPU.
    directions = torch.randint(
        0,
        4,
        size=(number_of_walks, N),
        device=device,
    )

    # Final position of every walk
    x = dx[directions].sum(dim=1)
    y = dy[directions].sum(dim=1)

    # Final distances
    distances = torch.sqrt(x.float()**2 + y.float()**2)

    # Transfer only the mean back to the CPU.
    mean_distances.append(distances.mean().item())


# Plot the simulation.
plt.plot(N_values, mean_distances, "o-", label="GPU simulation")

# Expected large-N result
N = np.array(list(N_values))
plt.plot(N, np.sqrt(np.pi * N) / 2, "--", label="Expected")

plt.xlabel("Number of steps, N")
plt.ylabel("Mean final distance")
plt.legend()
plt.grid()
plt.show()


