# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    heap = [(0,i) for i in range(n)]
    heapq.heapify(heap)
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for thread, time in result:
        print(thread, time)


if __name__ == "__main__":
    main()
