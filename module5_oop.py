class NumberStore:
    def __init__(self):
        self.numbers = []

    def read(self, n):
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            self.numbers.append(num)

    def find(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1

if __name__ == "__main__":
    numbers = NumberStore()

    n = int(input("Enter N: "))
    numbers.read(n)

    x = int(input("Enter X: "))
    print(numbers.find(x))
