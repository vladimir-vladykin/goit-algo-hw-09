import timeit

POSSIBLE_COINS = [50, 25, 10, 5, 2, 1]


def main():
    amounts_to_test = [
        20, 
        113, 
        60000,
        60131
    ]

    for amount in amounts_to_test:
        test_amount(amount)


def test_amount(amount):
    print(f"Testing amount {amount}...")

    coins_to_withdraw_greedy, time_spent = execute_and_measure_time(find_coins_greedy, amount) 
    print(f"Greedy algorithm spent {time_spent:.8f} for calculation, result is:\n{coins_to_withdraw_greedy}")

    coins_to_withdraw_dynamic, time_spent = execute_and_measure_time(find_min_coins, amount)
    print(f"Dynamic algorithm spent {time_spent:.8f} for calculation, result is:\n{coins_to_withdraw_dynamic}")

    print("\n")


# greedy approach to return needed coins for gived amoint
def find_coins_greedy(amount) -> dict:
    # init result with all possible coins, later unused denominations will be just zero
    result = {i: 0 for i in POSSIBLE_COINS}

    amount_left = amount
    while amount_left > 0:
        # get biggest possible coin, but not bigger 

        # impl with iteration of simplicity, can be faster if use // instead, 
        # but no need, greedy still faster than dynamic algo
        for coin in POSSIBLE_COINS:
            if coin <= amount_left:
                # that's coint we're looking for,
                # it's covers part of amount, or whole amount left
                result[coin] += 1
                amount_left -= coin
                break

    return result


# bottom-up approach for calculation of best combination of coins 
# for given amount
def find_min_coins(amount) -> dict:
    # break down task into smaller subtask,
    # init arrays to keep optimal solution for each subtask,
    needed_coins_counts = [0] + [float('inf')] * amount
    coins_denominations = [0] * (amount + 1)

    # fill arrays
    for i in range(1, amount + 1):
        for coin in POSSIBLE_COINS:
            if i >= coin and needed_coins_counts[i - coin] + 1 < needed_coins_counts[i]:
                needed_coins_counts[i] = needed_coins_counts[i - coin] + 1
                coins_denominations[i] = coin
        

    # so now we have all sub-solution for every possible sub-amount,
    # now it's gonna be simple to build optimal dict of needed coins

    # build result with all possible coins, later unused denominations will be just zero
    result = {i: 0 for i in POSSIBLE_COINS}

    amount_left = amount
    while amount_left > 0:
        coin = coins_denominations[amount_left]
        result[coin] += 1
        amount_left -= coin

    return result


def execute_and_measure_time(algorithm, amount):
    start_time = timeit.default_timer()
    result = algorithm(amount)
    execution_time = timeit.default_timer() - start_time

    return result, execution_time

if __name__ == '__main__':
    main()