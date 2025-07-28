#**********************************************************************************************************************************
# list comprehesion 
# Write a LC program to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values

l1 = [1,2,3,4,5,6,7] 

dic1 = {x : x*x*x for x in l1 if x %2!=0}

print (dic1)


#*******************************************************************************************************************************************
# make a dictionary of the 26 english alphabets mapping each with the corresponding integer

dic2  = {num-64 : chr(num) for num in range (65,91)}

print(dic2)

#***************************************************************************************************************************
# Lambda function 
# cubes every number in the given list  list1 = [1,2,3,4,5,6,7,8,9]
list1 = [1,2,3,4,5,6,7,8,9]
cube = list(map(lambda x : x*x*x , list1))
print(cube)