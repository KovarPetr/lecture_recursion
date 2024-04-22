def recursive_nth_fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    print(recursive_nth_fibo(12))
    pass


if __name__ == "__main__":
    main()
