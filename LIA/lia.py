import math

# setting variables
p: int = 0.25   # probability of any organism being AaBb in generation 1 and after
k: int = 7      # generations
n: int = 33     # at least n organisms
m: int = 2 ** k # number of organisms after k generations

# evalutates binomial distribution for probability of 
def calculate_binomial(p: int, m: int, n: int) -> float:
    return math.comb(m, n) * (p ** n) * ((1 - p) ** (m - n))

# probability of >= n heterozygotes is simply 1 - P(less than n heterozygotes)
overall_probability: float = 1 - sum(calculate_binomial(p, m, n) for n in range(n))

# output to terminal
print(overall_probability)