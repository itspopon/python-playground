name = "Mark"
age = 12

print()

print(name + ' is ' + str(age))
print("{0} is {1} years old.".format(name, age))
print()

print("""HECK
feck
well
bacon""")
print()

for i in range(1,12):
  #old: print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))
  print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3)) # <<< new