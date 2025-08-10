import os

# read in population
content: str = ""
with open(os.path.join("IEV", "rosalind_iev.txt"), 'r') as file:
    content = file.read().strip()

# load population of genotypes as a list of integers
population: list[int] = list(map(int, content.split()))

# calculate expected offspring with dominant phenotype
offspring_with_dominant_phenotype: float = (
    population[0] * 2 * 1 +
    population[1] * 2 * 1 +
    population[2] * 2 * 1 +
    population[3] * 2 * .75 +
    population[4] * 2 * .5 +
    population[5] * 2 * 0
)

# output to terminal
print(offspring_with_dominant_phenotype)