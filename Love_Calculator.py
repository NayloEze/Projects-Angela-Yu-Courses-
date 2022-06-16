# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

name_together = lower_case_name1 + lower_case_name2
#print(name_together)
t1 = name_together.count("t")
r1 = name_together.count("r")
u1 = name_together.count("u")
e1 = name_together.count("e")

true_count = (t1+r1+u1+e1)
#print(true_count)

l1 = name_together.count("l")
o1 = name_together.count("o")
v1 = name_together.count("v")
e1 = name_together.count("e")

love_count = (l1+o1+v1+e1)
#print(love_count)
love_score = (str(true_count)+str(love_count))
#print(love_score)
love_scores = int(love_score)
# print(love_scores)
# print(type(love_scores))

if love_scores < 10 or love_scores > 90:
    print(f"Your score is {love_score}, you go  together like coke and mentos.")
elif love_scores >= 40 and love_scores <= 50:
    print(f"Your score is {love_score},you are alright together.")
else:
    print(f"Your score is {love_score}.")
# 