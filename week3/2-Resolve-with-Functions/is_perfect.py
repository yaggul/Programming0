def is_perfect(x):
    from divisors import divisors
    from sum_divisors import sum_divisors
    if sum_divisors(divisors(x))==x:
        return True
    else:
        return False
    
def main():
    if __name__=='__main__':
        main()
