import time
import random

# Decorator to measure the execution time of a function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

# Function to filter numbers greater than 40 from a line of data
@measure_time
def filter_numbers(line_data):
    numbers_list = list(map(int, line_data.split()))
    filtered_numbers = list(filter(lambda x: x > 40, numbers_list))
    return ' '.join(map(str, filtered_numbers))

# Generator function to read lines from a file
@measure_time
def read_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

if __name__=="__main__":
    # Generate a file with random numbers
    with open('random_numbers.txt', 'w') as file:
        for _ in range(100):
            line_data = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line_data + '\n')

    # Read lines from the file
    with open('random_numbers.txt', 'r') as file:
        lines = file.readlines()

    # Apply the filter_numbers function to each line
    filtered_lines = list(map(filter_numbers, lines))

    # Write the filtered data back to a file
    with open('filtered_numbers.txt', 'w') as file:
        file.writelines('\n'.join(filtered_lines))

    # Example usage of the generator to read lines from the filtered file
    for line in read_file_generator('filtered_numbers.txt'):
        print(line)