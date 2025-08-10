# returns rabbits alive after 'n' months give a lifespan of 'm' months
def mortal_fibonacci_rabbits_dp(n: int, m: int) -> int:
    ages: list[int] = [0] * m       # stored rabbits as list in which index indicates age
    ages[0] = 1                     # initialize list with 
    
    # proceed through months 2 through n
    for month in range(2, n + 1):
        # one newborn pair is born for each mature pair of rabbits
        newborns: int = sum(ages[1:])

        # all rabbits age by 1, insert newborns on first index
        ages = [newborns] + ages[:-1]
    
    return sum(ages)

# run method
n: int = 97
m: int = 19

print(mortal_fibonacci_rabbits_dp(n, m))