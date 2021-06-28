ps3_game = 17
ps4_game = 45

num_ps3_games = int(input("How many PS3 games?: "))
num_ps4_games = int(input("How many PS4 games?: "))

ps3_total = num_ps3_games * ps3_game
ps4_total = num_ps4_games * ps4_game

total = ps3_total + ps4_total

if total > 100 and < 200:
  total *= 0.95
  print("you get a 5% discount for spending over 100 dollars")
  #5% discount
elif total > 200 and < 300:
  total *= 0.9
	print("you get a 10% discount for spending over 200 dollars")
  #10% discount
elif total > 300:
  total *= 0.8
	print("you get a 20% discount for spending over 300 dollars")
  #20% discount
#Print out total order cost
print("You order costs: ${}".format(total_cost))
