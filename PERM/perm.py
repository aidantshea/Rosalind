import  itertools

# input
i: int = 5

# generate list of permutations
nums: list[int] = list(range(1, i + 1))
permut: list[tuple[int, ...]] = list(itertools.permutations(nums))

# terminal output
print(len(permut))
for p in permut:
    for num in p:
        print(num, " ", end="")
    print()