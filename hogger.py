import torch
size = 1e9

x = [torch.Tensor(int(size)).to(f"cuda:{i}") for i in range(torch.cuda.device_count())]
