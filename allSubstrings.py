from itertools import combinations 
  
# initializing string  
test_str = "Geeks"
  
# printing original string  
print("The original string is : " + str(test_str))  
res = [test_str[x:y] for x, y in combinations( 
            range(len(test_str) + 1), r = 2)] 

print (str(res))