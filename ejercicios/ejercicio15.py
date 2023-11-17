# import sys
# print(sys.argv)

# print("---Nico---")



# a = 97
# b = 55
# # test expression
# if a < b:
#     # statement to be run
#     print(b)
    

# a = 93
# b = 27
# if a >= b:
#     print(a)
    
    
    
# a = 27
# b = 93
# if a <= b:
#     print("a is less than or equal to b")
# elif a == b:
#     print("a is equal to b")


# a = 270
# b = 93
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else: 
#     print ("a is equal to b")


# a = 16
# b = 25
# c = 27
# if a > b:
#     if b > c:
#         print ("a is greater than b and b is greater than c")
#     else: 
#         print ("a is greater than b and less than c")
# elif a == b:
#     print ("a is equal to b")
# else:
#     print ("a is less than b")


# fact = "The Moon has no atmosphere."
# two_facts = fact + "No sound can be heard on the Moon."
# print(two_facts)

print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)


temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)


print("Moon" in "This text will describe facts and challenges with space travel")


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))


mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
        
        
        
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))