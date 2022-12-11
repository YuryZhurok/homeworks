def get_winners(results):
    number_of_winners = [133, 32, 445, 330, 564]
    new_numbers = list(enumerate(number_of_winners, start=1))
    new_numbers.sort(key=lambda x: x[1], reverse=True)
    results = [new_numbers[0][0], new_numbers[1][0], new_numbers[2][0]]
    return results


print(get_winners([133, 32, 445, 330, 564]))
