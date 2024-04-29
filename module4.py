N = int(input("N:"))
numbers = []
for i in range(N):
  num = int(input(f"{i+1}:"))
  numbers.append(num)
X = int(input("X:"))  
for idx,num in enumerate(numbers):
  if num==X:
    print(idx)
    exit()
print("-1")
