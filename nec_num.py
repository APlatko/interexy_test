from itertools import combinations
import sys

# n, x = map(int, input().split())
# coins = list(map(int, input().split()))

some_input = sys.stdin.readlines()
n, x = map(int, some_input[0].strip().split())
coins = list(map(int, some_input[1].strip().split()))


def get_necessary_coins(number_coins, payment_amount, available_coins):
    """
    As input comes n - number of coins, x - amount for payment, coins - sequence of available coins.
    If coin combinations for payment have no common coins - it shows 'No necessary coins'.
    (ex. several combinations: [10, 20, 17, 3], [50], [25, 5, 20], [25, 17, 3, 5] to pay 50.)
    Otherwise, it shows minimum necessary number of coins and absolutely necessary coin(s) for payment.
    """

    coins_num = 0
    coins_seq = []

    if sum(available_coins) == payment_amount:
        coins_num = number_coins
        coins_seq.extend(available_coins)
    else:
        # make a list of combinations from available coins and filter by comparing their sums to the payment amount.
        list_comb = []
        for num in range(1, number_coins):
            list_comb.extend(filter(lambda i: sum(i) == payment_amount, combinations(available_coins, num)))
        if list_comb:
            comb = set(list_comb[0])
            result = comb.intersection(*list_comb)  # find the common coins in all filtered combinations

            coins_num = len(result)
            coins_seq = list(result)

    print(coins_num if coins_num else "No necessary coins")
    print(' '.join(map(str, coins_seq)) if coins_seq else "No necessary coins")


get_necessary_coins(n, x, coins)