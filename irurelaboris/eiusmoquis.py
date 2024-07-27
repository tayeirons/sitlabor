import torch

arg_1 = torch.rand_strided((1, 4101, 6144), (25196544, 6144, 1), device='cuda:3', dtype=torch.bfloat16)
