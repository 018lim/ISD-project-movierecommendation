print('Hello World', 5)

# Tuple (tupla)
data = ('grape', 'pinaple', 'cherry')
print(data)
print(data[0])
# You cannot change the item assignment in a tuple

print("""This is the class of information system
you will see more things
woohoo
""")

# List []
# Tuple ()
# Set {}

data = {'red', 'blue', 'green', 'red', 'blue'}
print(data)

# dictionaries dict
pairs1 = {'KR': 'Korea', 'MX': 'Mexico'}
print(pairs1)
pairs2 = [('kr', 'korea'), ('uk', 'United Kingdom')]
print(pairs2)

#if conditional
a = 5; b = 5
if (a < b):
    print('a is less than b')
elif (a > b):
    print('b is less than a')
else:
    print('b equals to a')

#loops
data=[1, 2, 3, 4, 5]
for i in data:
    print(i)

for i in range(3,12,2):
    print(i)

#while loop
j=0
data3=[2, 3, 4, 5, 6]
while j<len(data3):
    print(data3[j])
    j+=1

#use of break and continue
data4=[1, 2, 3, 4, 5]
for number in data4:
    if number ==3:
        break
    print(number)

#Functions
def display(word):
    print(word)

display('Seul')

