from time import time
from os import path
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
    numOfSol = 0  

    b = N*[-1] 
    colFree = N*[1] 
    upFree = (2*N - 1)*[1] 		
    downFree = (2*N - 1)*[1]    		

    def putQueen(r, b, colFree, upFree, downFree):
        nonlocal N
        nonlocal numOfSol
        for c in range(N): 
            if colFree[c] and upFree[r+c] and downFree[r-c+N-1]:
                b[r] = c

                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0

                if r == N-1:
                    numOfSol += 1
                else:
                    putQueen(r+1, b, colFree, upFree, downFree)
                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1
                                                                
    putQueen(0, b, colFree, upFree, downFree)
    print(f'Number of Solutions : {numOfSol}')


@timer
def nqueen_iterative(N):
    queens = []
    numOfSol = 0

    def is_queen_safe(row, col):
        nonlocal queens
        for r, c in enumerate(queens):
            if r == row or c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def solve():
        nonlocal queens
        nonlocal N
        nonlocal numOfSol
        queens = []
        col = row = 0
        while True:
            while col < N and not is_queen_safe(row, col):
                col += 1
            if col < N:
                queens.append(col)
                if row + 1 >= N:
                    numOfSol += 1
                    queens.pop()
                    col = N
                else:
                    row += 1
                    col = 0
            if col >= N:
                if row == 0:  
                    return 
                col = queens.pop() + 1
                row -= 1
    
    
    solve()
    print(f"Number of Solutions : {numOfSol}")


time_capture = {
    'nqueen_recursive': [],
    'nqueen_iterative': []
}


def nqueen():
    for n in range(2, 15):
        nqueen_recursive(n)
        nqueen_iterative(n)

    # saving data
    print('saving time capture to nqueen_time_capture.pkl.......')
    with open('nqueen_time_capture.pkl', 'wb') as file:
        pickle.dump(time_capture, file)

def plot_graph():
    with open('nqueen_time_capture.pkl', 'rb') as file:
        time_capture = pickle.load(file)
    print(time_capture)

    recursive = list(map(lambda x: x[1], time_capture['nqueen_recursive']))
    iterative = list(map(lambda x: x[1], time_capture['nqueen_iterative']))
    N = [i for i in range(2, 15)]
    plt.xlabel('Number of Queens')
    plt.ylabel('Time (seconds)')
    plt.plot(N, recursive, 'r--', label='recursive')
    plt.plot(N, iterative, 'b--', label='iterative')
    plt.legend(loc='upper left')
    plt.show()
 

if __name__ == '__main__':
    if not path.isfile('./nqueen_time_capture.pkl'):
        nqueen()
    plot_graph()


