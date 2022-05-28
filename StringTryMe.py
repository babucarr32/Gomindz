# Question 1
# The variable name wasn't declared correctly

name = "Mitch"
age = 26
full_time_employee = True
print(name, age, full_time_employee)

# Question 2
# Nothing is wrong
x = 20
y = 4
print(x - y)

# Question 3

Sentence = input("Enter a sentence: ")
Sentence_split = Sentence.split()
for word in Sentence_split:
    print(word)

# Question 4
Promt = input("Enter anything: ")
print(Promt.upper())

# Question 5
Email = input("Enter your email: ")
EmailSPlit = Email.split("@")
Username = EmailSPlit[0]
UsernameSplitter = Username.split('.')
FirstName = UsernameSplitter[0]
LastName = UsernameSplitter[1]

# Question 6
print(f"Hello {FirstName} {LastName}")

# Question 7
FirstName = input("Enter first name: ")
LastName = input("Enter last name: ")
Age = input("Enter age: ")
print(FirstName, LastName, Age)
