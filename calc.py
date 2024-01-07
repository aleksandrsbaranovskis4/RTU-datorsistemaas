x = float(input("Number: "))
mantiss = int(input("Mantiss value: "))
for val in range(1, mantiss+1):
    x = x * 2
    if x > 1:
        print("1", end="")
        x = x - 1
    else: 
        print("0", end="")