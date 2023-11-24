"""
Introduction to Programming Coursework 1

@author: Cal Levitt (sc23cl)
"""


def valid_puzzle(puzzle: list) -> bool:

    if type(puzzle) is not list:

        return False

    elif len(puzzle) <= 1:

        return False

    for i in range(0, len(puzzle) - 1):
        # use this webiste to learn the type function
        # (https://www.simplilearn.com/tutorials/python-tutorial/python-typeof-function#:~:text=To%20determine%20the%20type%20of,class%20type%20of%20the%20object.)

        if (type(puzzle[i]) is not str or type(puzzle[i + 1]) is not str) or \
                len(puzzle[i]) != len(puzzle[i + 1]):

            return False

    return True


def similarity_grouping(data: list) -> list:
    # Function is inspired from my solution and the example solution
    # of worksheet 4 part 3 of the module content

    final = []

    if type(data) is not list:
        return final

    for item in data:

        if str(item).isnumeric():
            item = int(item)

        found = False

        for sub in final:

            if item in sub:
                sub.append(item)
                found = True

        if found is False:
            final.append([item])

    return final


def highest_count_items(data: str) -> list:

    count_list = []

    if type(data) is not str:
        return []

    data = data.replace(", ", ",")
    # used to learn replace function to remove spaces from data
    # (https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string)

    split_data = data.split(",")
    unique = list(set(split_data))
    # Used to learn how to get unique items from a list using set function
    # (https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python)

    for item in unique:
        count_list.append([item, split_data.count(item)])

    final = [["", 0]]

    for item in count_list:
        if item[1] == final[0][1]:
            final.append(item)
        elif item[1] > final[0][1]:
            final = [item]

    return final


def valid_char_in_string(popList: list, charSet: list) -> bool:
    if type(charSet) is not list or type(popList) is not list:
        return False

    for item in popList:

        if type(item) is not str:
            return False

        for letter in list(item):

            if letter not in charSet:
                return False

    return True


def total_price(unit: int) -> float:

    final_price = float(0)
    if unit < 6:
        final_price = unit * 1.25

    elif unit >= 6:
        six_packs = unit // 6
        spare = unit % 6
        final_price = (six_packs * 5) + (spare * 1.25)
        if final_price >= 20:
            final_price *= 0.9

    return final_price


if __name__ == "__main__":
    # sample test for task 1.1
    puzzle1 = ["hey"]

    puzzle2 = []

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']

    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
