class MyInt:
    def __init__(self, n):
        self.n = n

    def __sub__(self, other):
        return f"{self.n} - {other.n} = {self.n - other.n//2}"
    
    def isPrime(self):
        return f"{self.n} isPrime : {self._isPrime()}"

    def showPrime(self):
        return f"Prime number between {2} and {self.n} : {self._showPrime()}"

    def _isPrime(self):
        if self.n <= 1:
            return False
        for i in range(2, self.n):
            if self.n%i == 0:
                return False
        return True

    def _isNPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n%i == 0:
                return False
        return True
    
    def _showPrime(self):
        if self.n <= 1:
            return "!!!A prime number is a natural number greater than 1"
        s = ''
        for i in range(2, self.n+1):
            if self._isNPrime(i):
                s += f"{i} "
        return s

print(" *** class MyInt ***")
a, b = [ int(i) for i in input("Enter 2 number : ").split(' ') ] 

a = MyInt(a)

b = MyInt(b)

print(a.isPrime())

print(b.isPrime())

print(a.showPrime())

print(b.showPrime())

print(a-b)

