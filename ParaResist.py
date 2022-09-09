numbers = []
while True:
    inp = input("Enter a number: ")
    if inp == "." or inp == "":
        break
    
    try:
        n = int(inp)
        numbers.append(n)
    except:
        print("Invalid, Exiting")
        break


total = 0.0
for n in numbers:
    total += 1.0 / n

print("PR is ", 1.0 / total)