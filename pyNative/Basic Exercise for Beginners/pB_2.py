sum = 0
print("Printing current and previous number sum in a range(10)")
for i in range(10):
    sum = 2*i-1
    print(f'Current Number {i} Previous Number  {i-1}  Sum:  {sum}')
    sum += i
# Cannot Resolve line 2 of expected output