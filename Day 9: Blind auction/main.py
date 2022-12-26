from art import logo
import os

print(logo)

auction_dic = {}
while(True):
    name = input('What is your name? : ')
    bid = float(input('What is your bid? : $ '))
    auction_dic[name] = bid
    bidders = input('\nAre there any other bidders? Type "yes" or "no": ')
    if bidders == 'yes':
        os.system('clear')
        print(logo)
        print('\n\n')
        continue
    else:
        os.system('clear')
        print(logo)
        print('\n\n')
        break
    
print(f'The winner is: {max(auction_dic, key=auction_dic.get)} with a bid of ${max(auction_dic.values())}')




