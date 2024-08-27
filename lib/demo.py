
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01] 

inch_heights = [height * 7920 for height in player_heights]   
print(inch_heights) 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "i" in x]
print(newlist)

def square_integers(int_list):
   return [x ** 2 for x in int_list]
result= square_integers([1,3,4,5])  
print(result)