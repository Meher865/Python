char = input("Enter a character: ")
if len(char) != 1:
 print("Please enter only a single character.")
else:
 if char.isalpha():
  print(f"'{char}' is an alphabet.")
 else:
  print(f"'{char}' is not an alphabet.")