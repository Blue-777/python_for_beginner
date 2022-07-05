#Q1: if statement
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need") 
else: print("none")

#Q2: while statement
i = 0
while True:
    i += 1
    if i > 5: 
        break 
    print('*'*i) 

#Q3: for statement 
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
    average = total/len(A)
print(average)
