def guess_digit():
    max_num = int(input('Enter the maximum number: '))
    min_num = int(input('Enter the minimum number: '))
    guess = (max_num + min_num) // 2

    while True:
        print(f'Is the digit more, less, or equal to {guess}? (M/L/E)')
        ans = input().upper()

        if ans == 'M':
            min_num = guess + 1
        elif ans == 'L':
            max_num = guess - 1
        elif ans == 'E':
            print(f'Congratulations! You guessed the digit correctly. The digit is: {guess}')
            break
        else:
            print('Invalid input. Please enter M, L, or E.')
            continue

        guess = (max_num + min_num) // 2

        if max_num - min_num <= 1:
            print(f'Congratulations! You guessed the digit correctly. The digit is: {guess}')
            break

guess_digit()