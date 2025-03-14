# Replit Day 8
Today, I learned how to use or in my code, since sometimes users can answer with a lowercase instead of a capital letter at the start of their answer. For example, "Dave" could be the string I put on my code to allow users see my next string, but sometines users type in "dave".

print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name? ")
if name =="Mark" or name == "mark":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("What a wonderful Tuesday it is", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("Happy Hump Day", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"your week is almost over!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "It's FRIDAY!")

elif name == "David" or name== "david":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("You look great in that color", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("You look chipper today", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"you are doing a great job!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "it's FRIDAY!")
else:
 print("I do not know your name, but I hope you are having a great day!")
