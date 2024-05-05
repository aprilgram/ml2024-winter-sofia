from module5_mod import NumberStore

if __name__ == "__main__":
    numbers = NumberStore()

    n = int(input("Enter N: "))
    numbers.read(n)

    x = int(input("Enter X: "))
    print(numbers.find(x))
