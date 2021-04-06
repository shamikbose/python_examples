str = raw_input()
element = ""
stack = []
start = ""
flag = 0
for i, j in enumerate(str):
    if j == "{":
        if flag == 0:
            start = str[0:i]
            flag = 1
            stack.append([start])
            stack.append([])
        else:
            stack.append([])
        print stack
        element = ""
    elif j == "}":
        stack[len(stack) - 1].append(element)
        print stack
        temp_list = []
        r1 = stack.pop()
        r2 = stack.pop()
        for k in r1:
            for j in r2:
                temp_list.append(j + k)
        stack.append(temp_list)
        stack.append(r1)
        stack.append([])
        element = ""
        print stack
    elif j == ",":
        if str[i - 1] != "}":
            stack[len(stack) - 1].append(element)
        print stack
        element = ""
    else:
        element = element + j
stack[len(stack) - 1].append(element)
print stack
# while(len(stack)!=1):
# 	res1=stack.pop()
# 	res2=stack.pop()
# 	for k in res1:
# 		for j in res2:
# 			temp_list.append(j+k)
# 	stack.append(temp_list)
# 	print stack
