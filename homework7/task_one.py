def get_winners(results):
    new_numbers = list(enumerate(results, start=1))
    new_numbers.sort(key=lambda x: x[1], reverse=True)
    results = [new_numbers[0][0], new_numbers[1][0], new_numbers[2][0]]
    return results


print(get_winners([533, 32, 45, 330, 564]))
