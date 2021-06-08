#Sets the maximum and minimum values that integers can be.
max = 2**31 - 1
min = -(2**31 - 1) - 1 

stack = []
symbols = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"', '!', '£', '$', '&', '(', ')', '_', '[', ']', '{', '}', ';', ':', '@', '~', ',' '<', '>', '.', '?', '|', '`', '¬', "'"]
r_stack = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]

#Checks the stack length. If it goes beyond 23, the 'Stack overflow.' message is printed and the offending input is removed.
def stack_length(self):
  if len(stack) > 23:
    print("Stack overflow.")
    stack.pop()
  return

#Performs addition calculations when '+' is input. Length of the stack is checked to ensure there are enough items in the stack to perform the calculation. If there are not enough items, the 'Stack underflow.' message is printed. After the result is calculated, it is checked to see if it is within the max and min integer values set at the start of the program. If bigger than the max value, the result is set to the max value. If lower than the min value, the result is set to the min value.
def plus(self):
  if len(stack) > 1:
    x = stack.pop()
    if len(stack) > 0:
      y = stack.pop()
      result = x + y
      if result > max:
        result = max
      elif result < min:
        result = min
      stack.append(result)
    else:
      print("Stack underflow.")
  else: 
    print("Stack underflow.")
  return 

#Performs subtraction calculations when '-' is input. Also checks for stack underflow errors, and the max and min values of the integers.
def minus(self):
  if len(stack) > 1:
    x = stack.pop()
    if len(stack) > 0:
      y = stack.pop()
      result = y - x
      if result > max:
        result = max
      elif result < min:
        result = min
      stack.append(result)
    elif len(stack) == 0:
      print("Stack underflow.")
  else:
    print("Stack underflow.")
  return

#Performs multiplication calculations when '*' is input. Also checks for stack underflow errors, and the max and min values of the integers.
def multiply(self):
  if len(stack) > 1:
    x = stack.pop()
    if len(stack) > 0:
      y = stack.pop()
      result = x * y
      if result > max:
        result = max
      elif result < min:
        result = min
      stack.append(result)
    elif len(stack) == 0:
      print("Stack underflow.")
  else:
    print("Stack underflow.")
  return

#Performs division calculations when '/' is input. Also checks for stack underflow errors, whether it will be dividing by zero, and the max and min values of the integers.
def divide(self):
  if len(stack) > 1: 
    x = stack.pop()
    if x == 0:
      print("Divide by zero.")
      #This if statement checks whether the user is trying to divide by zero. If they are, the message is printed and the calculation is cancelled.
    elif len(stack) > 0:
      y = stack.pop()
      result = y / x
      if result > max:
        result = max
      elif result < min:
        result = min
      stack.append(int(result))
    elif len(stack) == 0:
      print("Stack underflow.")
  else:
    print("Stack underflow.")
  return

#Performs modulus calculations when '%' is input. Also checks for stack underflow errors, and the max and min values of the integers.
def modulo(self):
  if len(stack) > 1:  
    x = stack.pop()
    if len(stack) > 0:
      y = stack.pop()
      result = y % x
      if result > max:
        result = max
      elif result < min:
        result = min
      stack.append(result)
    elif len(stack) == 0:
      print("Stack underflow.")
  else:
    print("Stack underflow.")
  return

#Performs power calculations when '^' is input. Also checks for stack underflow errors, and the max and min values of the integers.
def power(self):
  if len(stack) > 1:  
    x = stack.pop()
    if len(stack) > 0:
      y = stack.pop()
      result = y ** x
      if result > max:
        result = max
      elif result < min:
        result = min
      stack.append(result)
    elif len(stack) == 0:
      print("Stack underflow.")
  else:
    print("Stack underflow.")
  return

#Checks the inputs and perform the appropriate action or uses the appropriate function.
def inputs(self):
  if user_input == '+':
    plus(user_input) 
  elif user_input == '-':
    minus(user_input)
  elif user_input == '*':
    multiply(user_input)
  elif user_input == '/':
    divide(user_input)
  elif user_input == '%':
    modulo(user_input)
  elif user_input == '^':
    power(user_input)
  elif user_input == '=':
    print(stack[-1])
    #The last number in the stack is printed.
  elif user_input == 'd':
    #This prints the numbers currently in the stack. Each number is printed on a new line.
    print(*stack, sep = "\n")
  elif user_input == 'r':
    r = r_stack.pop(0)
    r_stack.append(r)
    stack.append(r)
    #Adds the first number in the r_stack to the main stack. The number is removed from the front of the r_stack and placed at the end.
  elif user_input in symbols:
    print(f"Unknown operator or operand \"{user_input}\".")
    #For individual letters and symbols that are entered, this will tell the user that the letter or symbol has not been recognised. This only works for one letter or symbol, not strings.
  else:
    stack.append(int(user_input))
    #Adds numbers entered by the user to the stack.
  
  
  
#This message informs the user that the SRPN calculator is ready to use.
print("You can now start interacting with the SRPN calculator")
while True:
  user_input = input()
  inputs(user_input)
  stack_length(user_input)
   
  
