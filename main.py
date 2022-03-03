def part1():
  #This is for part 1
  n = 42
  tau = 3.13159
  school = "Sault College"
  print(n)
  print(tau)
  print(school)
  print("Part 1 completed!")
  
def part2():
  #This is for part 2  
  #class = "CSD110"        
  #desired-grade = 100     
  #2hot = "hothot"
  #3.14159 = pi
  _class = "CSD110" #class is a part of the python language. Change name
  desired_grade = 100 #Tried to subtracted desired by grade
  hot2 = "hothot" #Can't have a number for/at the begining of, a variable name
  pi = 3.14159 # pi and the numbres should be switched
  print(_class)
  print(desired_grade)
  print(hot2)
  print(pi)
  print("Part 2 is complete!")
  
def part3():
  print("Feeling... ", end = "")
  i = 0
  while (i < 3):
    print("Hot", end = "")
    i += 1
  print("!")
  print("Part 3 is complete!")

def part4():
  base = 3000
  height = 1000
  triangle = 1/3 * (base * base) * height
  print(str(triangle) + "cm cubed") #Not sure how to do the cubed
  #Didn't specify what the error he got was. Wrote the code how I think the question was asking and got the right answer.
  print("Part 4 is complete!")
print("----------------")
part1()
print("----------------")
print("")
print("----------------")
part2()
print("----------------")
print("")
print("----------------")
part3()
print("----------------")
print("")
print("----------------")
part4()
print("----------------")