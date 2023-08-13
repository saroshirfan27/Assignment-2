temperatures = [25, 30, 27, 22, 28, 33, 29] 
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 

list_new = { temperatures[0] : days[0] }
for i in range(0,len(temperatures) - 1):
    list_new[temperatures[i]] = days[i]
print(list_new)

temp = max( list_new )
print( str(temp) + " and " + str( list_new[temp] ) + " is the maximum temperature ")
print(str(sum(temperatures)/len(temperatures)) + " is the average temperature")
