fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in fruits:
  if x == "banana":
    break
  print(x)

  for x in fruits:
   if x == "banana":
    continue
  print(x)

  for x in range(0, 1):
   print(x)

i = 0
while i < 3:
  print(i)
  i += 1


