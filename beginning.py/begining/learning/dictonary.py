# student = {
#     "name": "Adarsh",
#     "age": 20,
#     "City": "Bangalore"
# }
# print(student["name"])
# print(student["age"])
# print(student["City"])

# student["courese"]="Python"
# student["age"]=21
# del student["City"]

# if "name" in student:
#     print("Key found")
# for key, value in student.items():
#     print(key, ":", value)    

product = {
    "name": "Audi",
    "price": 1000000,
    "quantity": 2
}
print(product["name"])
print(product["price"])
print(product["quantity"])

product["color"]="Red"
product["price"]=1200000

if "name" in product:
    print("Key found")
for key, value in product.items():
    print(key, ":", value)
    
print(product.get("series", "Not found"))

print(product.keys())

print(product.values())

removed=product.pop("price")
print(removed)

