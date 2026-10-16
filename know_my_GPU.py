import torch

if torch.cuda.is_available():
    # NVIDIA CUDA or AMD ROCm
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    # Apple Silicon GPU
    device = torch.device("mps")
elif hasattr(torch, "xpu") and torch.xpu.is_available():
    # Intel GPU
    device = torch.device("xpu")
else:
    device = torch.device("cpu")

print("Using:", device)


