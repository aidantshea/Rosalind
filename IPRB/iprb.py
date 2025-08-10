k: int = 24
m: int = 20
n: int = 29
sum: int = k + m + n

def calculate(k: int, m: int, n: int) -> int:
    return (
        (k / sum) + 
        (m / sum) * (k / (sum-1)) + 
        (m / sum) * ((m-1) / (sum-1)) * .75 + 
        (m / sum) * (n / (sum-1)) * .5 +
        (n / sum) * (k / (sum-1)) +
        (n / sum) * (m / (sum-1)) * .5
    )

print(calculate(k, m, n))