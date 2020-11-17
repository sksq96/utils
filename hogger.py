import torch

size = int(1e4)
arr = [(torch.Tensor(size, size).to(f"cuda:{i}"), torch.Tensor(size, size).to(f"cuda:{i}").T) for i in range(torch.cuda.device_count())]

while True:
    for x, y in arr:
        torch.matmul(x, y)
