class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max_collisions):
        self.table_size = table_size
        self.max_collisions = max_collisions
        self.store = [None for _ in range(self.table_size)]
        self.size = 0

    def is_full(self):
        if self.size == self.table_size:
            print("This table is full !!!!!!")
            return True
        return False

    def insert(self, key, value):
        if self.is_full():
            return

        hashed_value = 0
        for c in key:
            hashed_value += ord(c)
        hashed_value = hashed_value%self.table_size

        first_hashed_value = hashed_value

        collision_count = 0
        while self.store[hashed_value] is not None:
            collision_count += 1
            print(f"collision number {collision_count} at {hashed_value}")

            if collision_count >= self.max_collisions:
                print("Max of collisionChain")
                return

            n = collision_count
            hashed_value = (first_hashed_value + n * n)%self.table_size

        self.store[hashed_value] = Data(key, value)
        self.size += 1

    def print_table(self):
        for i, ele in enumerate(self.store):
            print(f"#{i+1}\t{ele}")





print(" ***** Fun with hashing *****")
arr, pair = input("Enter Input : ").split("/")
table_size, max_collisions = arr.split(" ")
pair = [ p.split(" ") for p in pair.split(",")]

hash_table = hash(int(table_size), int(max_collisions))
for p in pair:
    if hash_table.is_full():
        break
    hash_table.insert(p[0], p[1])
    hash_table.print_table()
    print("---------------------------")


"""
Debugged
sample walkthrough

three = 116 + 104 + 114 + 101 + 101 = 536
t_size = 5
hashed = 536 % 5 = 1
col 1 at idx 1
new_hashed = (536 + 1*1) % 5 = 537%5 = 2
col 2 at idx 2
new_hashed = (537 + 2*2) % 5 = 540%5 = 0
# bug detect

"""
