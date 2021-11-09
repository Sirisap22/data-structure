class Hash:
    def __init__(self, table_size, max_collisions, threshold):
        self.table_size = table_size
        self.max_collisions = max_collisions
        self.threshold = threshold
        self.store = [None for _ in range(self.table_size)]
        self.sequence = []
        self.size = 0

    def check_over_threshold(self, val):
        if (self.size/self.table_size) * 100 > self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(val)
            return True
        return False

    def insert(self, value):
        self.size += 1
        if self.check_over_threshold(value):
            return

        hashed_value = value%self.table_size

        first_hashed_value = hashed_value

        collision_count = 0
        while self.store[hashed_value] is not None:
            collision_count += 1
            print(f"collision number {collision_count} at {hashed_value}")

            if collision_count >= self.max_collisions:
                print("****** Max collision - Rehash !!! ******")
                self.rehash(value)
                return

            n = collision_count
            hashed_value = (first_hashed_value + n * n)%self.table_size

        self.store[hashed_value] = value
        self.sequence.append(value)

    def is_prime(self, x):
        return all(x % i for i in range(2, x))

    def next_prime(self, x):
        return min([a for a in range(x+1, 2*x) if self.is_prime(a)])

    def rehash(self, val):
        self.table_size = self.next_prime(self.table_size*2)
        self.size = 0

        self.store = [None for _ in range(self.table_size)]


        arr = self.sequence.copy()
        self.sequence.clear()
        for ele in arr:
            if ele is not None:
                self.insert(ele)

        self.insert(val)


    def print_table(self):
        for i, ele in enumerate(self.store):
            print(f"#{i+1}\t{ele}")


print(" ***** Rehashing *****")
arr, arr2 = input("Enter Input : ").split("/")
table_size, max_collisions , threshold = list(map(int, arr.split(" ")))
arr = arr2.split(" ")

h = Hash(table_size, max_collisions, threshold)
print("Initial Table :")
h.print_table()
print("----------------------------------------")
for ele in arr:
    print(f"Add : {ele}")
    h.insert(int(ele))
    h.print_table()
    print("----------------------------------------")
