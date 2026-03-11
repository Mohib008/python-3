
#def print_all(arr):
#    for items in arr:
#        print(items);

#cars = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red", "price": 50000, "mileage": 10000, "engine": "V8", "transmission": "manual", "fuel": "gasoline", "doors": 2, "seats": 4, "weight": 1500, "acceleration": 5.0, "top_speed": 250, "horsepower": 300, "torque": 400, "fuel_efficiency": 10.0, "safety_rating": 5, "reliability_rating": 4, "popularity_rating": 4.5}

#print(cars["brand"])

user = { "items": ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"],
         "name": "John Doe",
         "age": 30,}
#print(user.get("age", 50))
#user2 = dict(name="Sarah Arsala", age=25)
#print(user2["name"], user2["age"])
#print(user2)
#print("Sarah Arsala" in user2["name"])
#print(user2.items())
#user2 = user.copy() 
#print(user2)
#print(user2.update({"name": "Sarah Arsala", "age": 25}))
print(user.update({"name": "Sarah Arsala", "age": 25}))
print(user)
