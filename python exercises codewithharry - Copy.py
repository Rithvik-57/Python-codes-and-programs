# PRACTICE 1 --> AGE CALCULATOR

what=input("Press 1 to know in what year you will turn 100\nPress 2 to know your age in an year of your choice\n")

if what=='1':
 byear=int(input("what is your date of birth\n"))
 if byear>1912 and byear<2023:
  whenhun=byear+100
  print(f'You will turn 100 in the year-{whenhun}')

 elif byear<=1912:
  print('you do be the oldest person alive')

 elif byear>=2023:
  print('you aint even born dawg')

elif what=='2':
 byear=int(input("what is your date of birth\n"))
 if byear>1912 and byear<2023:
  wyear=int(input('Type the year to know how you old you will be by that year\n'))
  ageby=wyear-byear
  print(f'You will be {ageby} years old in {wyear}')

 elif byear<=1912:
  print('you do be the oldest person alive')

 elif byear>=2023:
  print('nigga you aint even born dawg')

# PRACTICE 2 --> DIVIDE THE APPLES

apples=int(input("Enter the number of apples you want- "))

mn=int(input("enter the starting number of the range- "))
mx=int(input("Enter the last number in the range- "))

rmnmx=range(mn,mx)
lmnmx=[rmnmx]

for n in rmnmx:
    if n%apples==0 :
        print(f'{n} is divisble by {apples}')
    else:
        print(f'{n} is not divisble by {apples}')

# PRACTICE 3 --> FOOD AND CALORIES

print("enter calories one by one\n")
size=int(input("enter size of list"))
callist=[]
for i in range(size):
    callist.append(int(input('enter calories\n')))

rev=callist
rev.reverse()
print(f'your list is {rev}')

# PRACTICE 4 --> NEXT PALINDROME NUMBER

def next_palindrome(n):
   n=n+1
   while not is_palindrome(n):
      n+=1
   return n

def is_palindrome(n):
   return str(n)==str(n)[::-1]


if __name__=="__main__":
   n=int(input("enter test cases- "))
   numbers=[]
   for i in range(n):
    number=int(input("Enter num-\n"))
    numbers.append(number)

   for i in range(n):
      print(f'next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}')

# PRACTICE 5 --> PALINDROMIFY THE LIST (JUST LIKE PRACTICE 4 SO SKIPPED)

# PRACTICE 6 --> GUESS THE NUMBER (WAS DONE IN THE SERIES BEFORE SO SKIPPED)

# PRACTICE 7 --> SEARCH ENGINE

def matchingwords(sen1, sen2):
    words1 = sen1.strip().split(' ')
    words2 = sen2.strip().split(' ')
    score = 0
    for word1 in words1:
        for word2 in words2:
            #print(f"Mathcing {word1} with  {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
 #matchingwords("This is good ", "pyhton is good ")
    serhis = ['Anime series', 'MCU marvel', 'manga comic Anime',
              'marvel comic', 'kdrama series', 'webtoon comic kdrama']

    query = input("Enter query\n")
    scores = [matchingwords(query, search) for search in serhis]
    sortedsentscores = [sentscore for sentscore in sorted(
        zip(scores, serhis), reverse=True) if sentscore[0] != 0]
    # print(sortedsentscores)

    print(f"{len(sortedsentscores)} results found!")
    for score, item in sortedsentscores:
        print(f'\'{item}\': with a score of {score}')

# PRACTICE 8 --> FAKE MULTIPLICATION TABLES

import random


def rohanmul(number):
    wrong = random.randint(0, 9)
    table = [i*number for i in range(1, 11)]
    table[wrong] = table[wrong]+random.randint(0, 10)
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i-1
 
    return None


if __name__ == '__main__':
    number = int(input("type num"))
    myTable=rohanmul(number)
    print(myTable)
    wrongIndex=isCorrect(myTable,number)
    print(f'tale is worng at index {wrongIndex}')

# PRACTICE 9 --> JUMBLED FUNNY NAMES

namenum=int(input("enter how many names-"))

for name in range(namenum):
    names=str(input("enter names- "))
    names.split(" ")
    namelist=[]
    namelist.append(names)
   
showname=input("do you wanna see entered names?") 
if showname=='yes':
 print(namelist)
