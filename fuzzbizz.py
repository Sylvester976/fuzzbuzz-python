def fizzBuzz(n):
    for fizzbuzz in range(1,16):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)