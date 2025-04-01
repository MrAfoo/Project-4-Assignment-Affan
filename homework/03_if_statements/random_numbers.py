import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """Generate a list of random numbers and perform basic operations."""
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    print(f"Generated Random Numbers: {random_numbers}")
    print(f"Minimum Value: {min(random_numbers)}")
    print(f"Maximum Value: {max(random_numbers)}")
    print(f"Average Value: {sum(random_numbers) / len(random_numbers):.2f}")

if __name__ == '__main__':
    main()
