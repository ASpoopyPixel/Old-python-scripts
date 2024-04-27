import coin

def main ():
    my_coin = coin.Coin()
    my_coin.toss()
    coinResults = my_coin.get_sideup()
    print(coinResults)
    print('This side is up:', my_coin.get_sideup())
    print('Tossing the coin loser')
    my_coin.toss()
    print('Side is:', my_coin.get_sideup())
main()