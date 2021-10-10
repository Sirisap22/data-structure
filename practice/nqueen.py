from itertools import permutations
from time import time
from os import path, environ
import pickle
import matplotlib.pyplot as plt

def timer(func):
    def wrap_func(*args, **kwargs):
        global time_capture
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        delta_t = t2-t1
        print(f'Function {func.__name__!r} N = {args[0]} executed in {delta_t}s')
        time_capture[func.__name__].append((args[0], delta_t))
        return result
    return wrap_func

@timer
def nqueen_recursive(N):
    numSol = 0  

    b = N*[-1] 
    colFree = N*[1] 
    upFree = (2*N - 1)*[1] 		
    downFree = (2*N - 1)*[1]    		

    def printBoard(b):
        for row in range(N):
            print([0 if i != b[row] else 1 for i in range(N)])
        print()

    def putQueen(r, b, colFree, upFree, downFree):
        nonlocal N
        nonlocal numSol
        for c in range(N): 
            if colFree[c] and upFree[r+c] and downFree[r-c+N-1]:
                b[r] = c

                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0

                if r == N-1:
                    # printBoard(b)
                    numSol += 1
                else:
                    putQueen(r+1, b, colFree, upFree, downFree)
                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1
                                                                
    putQueen(0, b, colFree, upFree, downFree)
    print(f'number of solutions : {numSol}')

@timer
def nqueen_iterative(N):

    def print_table():
        nonlocal N
        for row in range(N):
            print([0 if i == 1 else 1 for i in table[row]])

    def put_queen(x,y):
        nonlocal N
        if table[y][x] == 0:
            for m in range(N):
                table[y][m] = 1
                table[m][x] = 1
                table[y][x] = 2
                if y+m <= N-1 and x+m <= N-1:
                    table[y+m][x+m] = 1
                if y-m >= 0 and x+m <= N-1:
                    table[y-m][x+m] = 1
                if y+m <= N-1 and x-m >= 0:
                    table[y+m][x-m] = 1
                if y-m >= 0 and x-m >= 0:
                    table[y-m][x-m] = 1
            return True
        else:
            return False

    table = [[0]*N for _ in range(N)]    
    perms = permutations([i for i in range(N)])


    num_comb = 0

    for perm in perms:
        is_solution = True
        for i in range(N):
            is_solution = is_solution and put_queen(perm[i], i)
        if is_solution:
            # print_table()
            num_comb += 1
            # print(f"solution{num_comb}")
            # print(" ")
        table = [[0] * N for _ in range(N)]
    
    print(f'number of solutions : {num_comb}')

time_capture = {
    'nqueen_recursive': [],
    'nqueen_iterative': []
}

def nqueen():
    for n in range(4, 11):
        nqueen_recursive(n)
        nqueen_iterative(n)

    # saving data
    print('saving time capture to nqueen_time_capture.pkl.......')
    with open('nqueen_time_capture.pkl', 'wb') as file:
        pickle.dump(time_capture, file)

def plot_graph():
    with open('nqueen_time_capture.pkl', 'rb') as file:
        time_capture = pickle.load(file)

    recursive = list(map(lambda x: x[1], time_capture['nqueen_recursive']))
    iterative = list(map(lambda x: x[1], time_capture['nqueen_iterative']))
    N = [i for i in range(4, 11)]
    plt.xlabel('Number of Queens')
    plt.ylabel('Time (seconds)')
    plt.plot(N, recursive, 'r--', label='recursive')
    plt.plot(N, iterative, 'b--', label='iterative')
    plt.legend(loc='upper left')
    plt.show()

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == '__main__':
    suppress_qt_warnings()
    if not path.isfile('./nqueen_time_capture.pkl'):
        nqueen()
    plot_graph()



