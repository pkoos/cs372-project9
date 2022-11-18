import threading

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

# ranges = [
#     [1, 65535],
#     [1, 20 * 10 ** 7],
#     [20 * 10 ** 1, 20 * 10 ** 7 ],
#     [1, 2 ** 16]
# ]

def runner(results, my_range, thread_num, func_name):
    result = func_name(my_range)
    print(f"Thread {thread_num}: {my_range} -> {result}")
    results.append(result)

def add_range(num_range):
    
    result = 0
    start, end = num_range[0], num_range[1]
    for num in range(start, end + 1):
        result += add_number(num)

    return result

def add_number(second):
    return second


def calculate_range_from_one(end_num):
    return (end_num * (end_num + 1)) // 2

def calculated_range(num_range):
    start, end = num_range[0], num_range[1]
    return calculate_range_from_one(end) - calculate_range_from_one(start - 1) # start - 1 because not inclusive

def create_threads(thread_data, results_data):
    threads = list()
    for index, num_range in zip(range(len(thread_data)), thread_data):
        # threads.append(threading.Thread(target=runner, args=(results_data, num_range, index, add_range)))
        threads.append(threading.Thread(target=runner, args=(results_data, num_range, index, calculated_range)))
    
    return threads

def start_threads(thread_collection):
    for thread in thread_collection:
        thread.start()

def join_threads(thread_collection):
    for thread in thread_collection:
        thread.join()

def main():
    results = list()
    threads = create_threads(ranges, results)

    start_threads(threads)
    join_threads(threads)
    
    print(f"results before summing: {results}")
    print(f"sum of all results: {sum(results)}")

if __name__ == "__main__":
    main()
