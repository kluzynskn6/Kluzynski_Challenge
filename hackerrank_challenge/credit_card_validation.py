num_cards = int(input())
cards = []        
for _ in range(num_cards):
  cards.append(input())

valid_cards = []
for num in cards:
  #Check first number
  if num[0] == '4' or num[0] == '5' or  num[0] == '6':
  #Check wether it is a - seperated number or not
    if num[4] == '-' and len(num) >= 16:   
      #Get rid of the spots where the -'s should be to have it match non -'d numbers
      num = num[:4] + num[5:9] + num[10:14] + num[15:]
    #Check to see if there is exactly 16 numbers
    if num.isdigit() and len(num) == 16:
      #Lastly, check for 4 repeating digits
      repeating_digits = 0
      still_valid = "true"
      for digit in num:
        if repeating_digits >= 4:
          still_valid = "false"
          break
        if digit != 15: #Won't work with last digit so stop after 2nd to last
          if num[int(digit)] == num[int(digit) + 1]:
            repeating_digits += 1
          else:
            repeating_digits = 0
      if still_valid == "true":
        valid_cards.append('Valid')
      else:
        valid_cards.append('Invalid')
    else:
      valid_cards.append('Invalid')
  else:
    valid_cards.append('Invalid')
for validation in valid_cards:
    print(validation)
