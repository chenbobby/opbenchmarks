import torch

def batched_dot_mul_sum(a, b):
    return a.mul(b).sum(-1)

def batched_dot_bmm(a, b):
    a = a.reshape(-1, 1, a.shape[-1])
    b = b.reshape(-1, b.shape[-1], 1)
    return torch.bmm(a, b).flatten(-3)

if __name__ == "__main__":
    x = torch.randn(10000, 64)
    batched_dot_mul_sum_output = batched_dot_mul_sum(x, x)
    batched_dot_bmm_output = batched_dot_bmm(x, x)
    assert batched_dot_bmm_output.allclose(batched_dot_bmm_output)

import timeit

t0 = timeit.Timer(
    stmt='batched_dot_mul_sum(x, x)',
    setup='from __main__ import batched_dot_mul_sum',
    globals={'x': x})

t1 = timeit.Timer(
    stmt='batched_dot_bmm(x, x)',
    setup='from __main__ import batched_dot_bmm',
    globals={'x': x})

print(f'mul_sum(x, x):  {t0.timeit(100) / 100 * 1e6:>5.1f} us')
print(f'bmm(x, x):      {t1.timeit(100) / 100 * 1e6:>5.1f} us')

import torch.utils.benchmark as benchmark

t0 = benchmark.Timer(
    stmt='batched_dot_mul_sum(x, x)',
    setup='from __main__ import batched_dot_mul_sum',
    globals={'x': x})

t1 = benchmark.Timer(
    stmt='batched_dot_bmm(x, x)',
    setup='from __main__ import batched_dot_bmm',
    globals={'x': x})

print(t0.timeit(100))
print(t1.timeit(100))