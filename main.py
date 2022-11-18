import threading
import time

func_iterations = 0
total_iterations = 0

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

# ranges = [
#     [1, 65535],
#     # [1, 20 * 10 ** 7],
#     [20 * 10 ** 1, 20 * 10 ** 7 ],
#     [1, 2 ** 16]
# ]

def increment_iterations(function):
    print(f"increment_iterations")
    
    def inner(argument):
        global func_iterations
        func_iterations += 1
        return function(argument)
    
    return inner

def runner(results, my_range, thread_num, func_name):
    global func_iterations, total_iterations
    func_iterations = 0
    result = func_name(my_range)
    print(f"Thread {thread_num}: {my_range} -> {result} calls: {func_iterations}")
    results.append(result)
    total_iterations += func_iterations

def add_range(num_range):
    global func_iterations
    
    result = 0
    start, end = num_range[0], num_range[1]
    for num in range(start, end + 1):
        # func_iterations += 1
        result += add_number(num)
        # result += num

    return result

@increment_iterations
def add_number(second):
    return second


def calculate_range_from_one(end_num):
    return (end_num * (end_num + 1)) // 2

@increment_iterations
def calculated_range(num_range):
    # global func_iterations
    # func_iterations += 1
    
    start, end = num_range[0], num_range[1]
    return calculate_range_from_one(end) - calculate_range_from_one(start - 1) # start - 1 because not inclusive

def main():
    results = list()
    threads = list()
    for index, num_range in zip(range(len(ranges)), ranges):
        threads.append(threading.Thread(target=runner, args=(results, num_range, index, add_range)))
        # threads.append(threading.Thread(target=runner, args=(results, num_range, index, calculated_range)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f"results before summing: {results}")
    print(f"sum of all results: {sum(results)}")
    print(f"total number of iterations: {total_iterations}")

if __name__ == "__main__":
    main()
