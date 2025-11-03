cities = ["London" , "Dublin" , "Halifax" , "Bradford" , "Leeds" , "Nottingham" , "Newcastle" , "Liverpool"]
print(cities)
userInputA = input("Enter the item you want to add to the list: ")
cities.append(userInputA)
userInputR = input("Enter the item you want to remove from the list: ")
cities.remove(userInputR)
cities.sort()
print(f"Here is the sorted list: {cities}")
