cost = 50
due = cost
while due > 0:
    print('Amount Due: '+str(due))
    coin = int(input('Insert Coin: '))
    if coin==25 or coin==10 or coin==5:
        due -= coin
if due < 0:
    due = -due

print('Change owed: '+str(due))