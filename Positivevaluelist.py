Input = [10, -11, 22,20] 

Output = [] 

for elem in Input: 

    temp = [] 
    for x in elem: 
        if x>0: 
            temp.append(x) 
    Output.append(temp) 

print("Initial List", Input) 

print("Modified List", Output) 

#output is [10,22,20]
