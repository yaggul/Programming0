def sum_divisors(x):
    from divisors import divisors
    collector=0
    for i in (divisors(x)):
        collector+=i
    return collector

def main():
    if __name__=="__main__":
        main()
