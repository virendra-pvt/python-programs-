num = 2

while num <= 50:
    divisor = 2
    is_prime = True

    # Check for factors up to sqrt(num)
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(num, end=" ")

    num += 1
