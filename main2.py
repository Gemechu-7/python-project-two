#guess
secret_number = 7
count = 0
count_limit = 3
while count<count_limit:
  guess =int(input('guess:'))
  count+=1
  if guess==secret_number:
    print('win!')
    break
else:
  print('failed!')