fruits = {"apple", "banana", "cherry"}

fruits.add("mango")
print(fruits)

if "apple" in fruits:
  print("Yes, apple is a fruit!")

  fruits.discard("cherry")
  print(fruits)

  fruits.pop()
  print(fruits)
