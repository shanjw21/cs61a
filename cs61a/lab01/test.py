def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while n :
        n, sum = n // 10, sum + n % 10
    print(sum)
    return sum

def double_eights(n):
    pre, cur = 0, 0
    while n :
        pre , cur,n  = cur, n % 10, n // 10
        # n = n // 10
        if cur == 8 and pre == 8:
            return True
    return False
LOWER = 1
UPPER = 10

def guess_binary():
    prompt_for_number(LOWER, UPPER)
    num_guesses, correct = 1, False
    lower, upper = LOWER, UPPER
    guess = (lower + upper) // 2
    "*** YOUR CODE HERE ***"
    while True:
        correct = is_correct(guess)
        if correct:
            return num_guesses
        else:
            num_guesses += 1
            if is_too_high(guess):
                guess, upper = (lower + guess) // 2, guess
            else:
                guess, lower = (guess + upper) // 2, guess

def prompt_for_number(lower, upper):
    """Prompt the user for a number between lower and upper. Return None."""
    is_valid_number = False
    while not is_valid_number:
        # You don't need to understand the following two lines.
        number = input('Pick an integer between {0} and {1} (inclusive) for me to guess: '.format(lower, upper))
        number = int(number)
        if lower <= number <= upper:
            is_valid_number = True
def is_correct(guess):
    """Ask the user if a guess is correct and return whether they respond y."""
    return is_yes('Is {0} your number? [y/n] '.format(guess))

def is_too_high(guess):
    """Ask the user if a guess is too high and return whether they say yes."""
    return is_yes('Is {0} too high? [y/n] '.format(guess))

def is_yes(prompt):
    """Ask the user a yes or no question and return whether they say yes."""
    while True: # This while statement will loop until a "return" is reached.
        yes_no = input(prompt).strip()
        if yes_no == 'y':
            return True
        elif yes_no == 'n':
            return False
        print('Please type y or n and press return/enter')

if __name__ == "__main__":
    # sum_digits(1234567890)
    # ans = double_eights(8)
    # print(ans)
    ans = guess_binary()
    print(ans)