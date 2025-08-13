from itertools import product

input: str = "A B C D"
n: int = 4

alphabet: list[int] = [char for char in input.split()]
alphabet.sort()

permutations: list[str] = [''.join(p) for p in product(alphabet, repeat=n)]
for p in permutations:
    print(p)