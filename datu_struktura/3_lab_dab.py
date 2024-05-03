class HashTable:
    def __init__(self):
        self.book = [None] * 1000000
        
    def add(self, num, name):
        self.book[num] = name

    def delete(self, num):
        if self.book[num] is not None:
            self.book[num] = None

    def find(self, num):
        if self.book[num] is not None:
            return self.book[num]
        return "not found"

def task():
    answer = []
    task_size = int(input())
    hash_table = HashTable()
    for x in range(task_size):
        command = input().split(" ")
        if command[0] == "add":
            try:
                int(command[1])
            except:
                answer.append("invalid phone number")
            else:
                hash_table.add(int(command[1]), command[2])
        elif command[0] == "delete":
            hash_table.delete(int(command[1]))
        elif command[0] == "find":
            answer.append(hash_table.find(int(command[1])))
    print("\nAnswer:")
    for x in answer:
        print(x)

if __name__ == "__main__":
    task()