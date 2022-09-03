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
  
