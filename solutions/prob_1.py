def main():
    limit = 1000
    # multiples of 15 are subtracted since they will be counted twice for both 3 and 5
    final_sum = sum_arithmetic_seq(3,limit) + sum_arithmetic_seq(5,limit) - sum_arithmetic_seq(15,limit)
    print(final_sum)

def sum_arithmetic_seq(n, limit):
    # using the sum of arithmetic sequence formula
    # Sn = n/2 * (a1 + an)
    fact_of_last_multiple = (limit - 1) // n
    last_multiple = n * fact_of_last_multiple
    return (fact_of_last_multiple / 2) * (n + last_multiple)

if __name__ == "__main__":
    main()
