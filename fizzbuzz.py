import sys

if len(sys.argv) == 1:
  print("No Arguments passed")
  print("User please enter the max range value")
  range_value = str(input())
else:
  range_value = str(sys.argv[1])

print("The range entered here is " + range_value)
try:
  for no in range(1,int(range_value)):
      if no % 3 == 0 and no % 5 == 0:
          print("fizz buzz")
      elif no % 3 == 0 and no % 5 != 0:
          print("fizz")
      elif no % 3 != 0 and no % 5 == 0:
          print("buzz")
      else:
          print(no)
except ValueError:  
    print("ERROR!!Please input interger values")