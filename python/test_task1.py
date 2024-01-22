def solution(S):

    number_appearances = {char: 0 for char in '9876543210'}

    for symbol in S:
        if symbol in number_appearances:
            number_appearances[symbol] += 1
        else:
            number_appearances[symbol] = 1

    first_part = ''.join(
        number_appearances[symbol] // 2 * symbol for symbol in '987654321').strip('0')

    middle_number = max((symbol for symbol, counts in number_appearances.items(
    ) if counts % 2 != 0), default='')

    if first_part + middle_number + first_part[::-1] != None:
        return first_part + middle_number + first_part[::-1]
    else:
        return '0'


print(solution('39878'))
