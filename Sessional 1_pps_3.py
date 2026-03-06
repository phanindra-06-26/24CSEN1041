2Q)

In the Number Theory, the Professor assigns a task to Mr. Saran Teja  to find the 
factors of a given number. Mr. Saran Teja has understood the concept of factors and is 
able to find all the factors of the input number. Later Mr. Saran Teja challenged himself 
to identify only the even factors for the input number. Design a  code to help Mr. Saran 
Teja to find the Even factors of the input numbers. 
Sample Input: 
6                                            
Sample Output: 
The Even factors of 6 is:   2      6




ANS)n = int(input("Enter a number: "))

print("The Even factors of", n, "is:")

for i in range(1, n+1):
    if n % i == 0 and i % 2 == 0:
        print(i, end=" ")


####OUTPUT

Enter a number: 6
The Even factors of 6 is:
2 6 
=== Code Execution Successful ===


3Q)A password strength checker validates passwords with these requirements: 
Password must contain at least one uppercase letter, Password must contain at least 
one lowercase letter 
Password must contain at least one digit, Password must contain at least one special 
character (!@#$%^&*) 
Password length must be between 8 and 20 characters 
Calculate strength score: weak (1-2 criteria), medium (3 criteria), strong (4-5 criteria) 
Task: Write a Python program to validate and rate password strength. 
Input: MyP@ss123 
Output: Valid Password: Yes    Strength: Strong   Criteria Met: 5/5   Length: 9

Ans)
p = input("Enter password: ")

score = 0

# check uppercase
for i in p:
    if i.isupper():
        score = score + 1
        break

# check lowercase
for i in p:
    if i.islower():
        score = score + 1
        break

# check number
for i in p:
    if i.isdigit():
        score = score + 1
        break

# check special character
for i in p:
    if i in "!@#$%^&*":
        score = score + 1
        break

# check length
if len(p) >= 8 and len(p) <= 20:
    score = score + 1

# check strength
if score <= 2:
    print("Strength: Weak")
elif score == 3:
    print("Strength: Medium")
else:
    print("Strength: Strong")

print("Criteria Met:", score, "/5")
print("Length:", len(p))


###output

#####OUTPUT
Enter password: MyP@ss123
Valid Password: Yes
Strength: Strong
Criteria Met: 5 /5
Length: 9

=== Code Execution Successful ===

4Q)  A teacher conducted a class survey asking students to choose their favorite 
programming language. 
The responses were stored in a list.The teacher wants to know how many times each 
programming language was chosen.Write a Python program that: Takes a list of 
elements as input. 
Counts the frequency of each element in the list. Displays each element along with its 
frequency.        
Input: Enter elements: 
['Python', 'Java', 'Python', 'C', 'Java', 'Python'] 
Output: 
Python : 3      Java : 2      C : 1 


ANS)  

l = input("Enter languages: ").split()

for i in set(l):
    print(i, ":", l.count(i))

    


####OUTPUT 
Python : 3      Java : 2      C : 1
