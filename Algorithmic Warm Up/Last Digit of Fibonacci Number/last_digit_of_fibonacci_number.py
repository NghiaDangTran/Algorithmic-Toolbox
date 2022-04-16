# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    data=[]
    data.append(0)
    data.append(1)
    for i in range(2,n+1):
        data.append(data[i-1]+data[i-2])

    return data[n]%10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
