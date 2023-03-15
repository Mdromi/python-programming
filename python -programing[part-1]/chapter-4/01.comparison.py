# python3 chapter-4/01.comparison.py

# print(2==3)   #False
# print(3==3)   #True
# print(2 > 3)  #False
# print(2 < 3)  #True
# print(2 != 3) #True
# print(3 != 3) #False
# print(2 >= 3) #False
# print(2 <= 3) #True

# print("Bangladesh" == "Bangladesh") #True
# print("Bangladesh" == "bangladesh") #False

my_money = 30
rickshaw_fare = 40
# print(my_money >= rickshaw_fare) #False

my_money = 30
rickshaw_fare = 30
# print(my_money >= rickshaw_fare) #True

my_money = 50
rickshaw_fare = 40
# print(my_money >= rickshaw_fare) #True


today = "Tuesday"
# print(today == "Tuesday") #True

# today = "Wednesday"
# print(today == "Tuesday") #False

# print(not(today == "Tuesday")) #True
# print(not True) #False
# print(not False) #True


# number = 20
# print(number > 10 and number < 100) #True
# number = 200
# print(number > 10 and number < 100) #False
# print(number > 10 or number < 100) #True
# print(not(number < 100)) #True


# LIST

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# print(numbers[0])
# print(numbers[1])
# print(numbers[9])
# print(len(numbers)) #10

sarrc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
print(sarrc[0])
print("Number of Countries in SAARC: ",len(sarrc))

