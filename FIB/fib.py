n: int = 31      # months
k: int = 4       # rabbits

# function returns mature pairs of rabbits by month 'n' given 'k' pairs of offspring per month
def recursive_rabbits(n: int, k: int) -> int:
    if (n == 1 or n == 2):
        return 1
    
    return recursive_rabbits(n-1, k) + recursive_rabbits(n - 2, k) * k

# output to terminal
print(recursive_rabbits(n, k))