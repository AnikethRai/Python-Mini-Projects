# A Python program for creating Quiz Game template 
# We can make it more advance by adding File systems to it.

print('#'*20)
print()
print('Welcome to the Quiz Game')
print()
print('#'*20)
while True:
    user_name = input('Please enter your name:')
    choice = input(f'Hello {user_name},Do you wanna play the game? (Y/N)\n')
    if choice.lower() == 'y' or choice.lower() == 'yes':
        break
    else: 
        quit()

score = 0
count = 0
answers = []

print('Here are your questions!')
print('#'*20)
ans = input('1.What is the capital of India ?\nAns : ')
count += 1
if ans.lower() == 'new delhi':
    score += 1
    answers.append('Correct')
else: answers.append('Incorrect')

ans = input('2.What is 2**10 ?\nAns : ')
count += 1
if ans.lower() == '1024':
    score += 1
    answers.append('Correct')
else: answers.append('Incorrect')

ans = input('3.Where is the Area 51 located ?\nAns : ')
count += 1
if ans.lower() == 'nevada':
    score += 1
    answers.append('Correct')
else: answers.append('Incorrect')

ans = input('4.Do you workout regularly?\nAns : ')
count += 1
if ans.lower() == 'yes' or ans.lower() == 'y' or ans.lower() == 's':
    score += 1
    answers.append('Yes! Sir')
else: answers.append('Go Gym, You dumb.')

ans = input('5.Can you create more Questions and Use this logic for User Interface ?\nAns : ')
count += 1
if ans.lower() == 'yes':
    score += 1
    answers.append('Correct')
else: answers.append('Incorrect')

print(f'Here is your score {user_name} : {score} / {count}')
if score == count:
    print('Grade : A')
if score < 5 and score >= 3:
    print('Grade : B')
if score == 2:
    print('Grade : C')
if score == 1:
    print('Grade : D')
if score < 1:
    print('You are a Failure ! Get Better')
print('#'*50)
print('Here is your Report')
for i in range(len(answers)):
    print(i+1,answers[i],sep= ' : ')
print('#'*50)
print(f'Thank you for playing {user_name}')
print('#'*50)



    

