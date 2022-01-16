import itertools
import time

if __name__ == "__main__":
    tian_horses = input("Input for Tian: ")
    king_horses = input("Input for King: ")
    start_time = time.time()
    list_of_tian_horses = list(map(int,tian_horses.split()))
    list_of_king_horses = list(map(int,king_horses.split()))

    # Reference: https://www.kite.com/python/answers/how-to-get-all-unique-combinations-of-two-lists-in-python
    permutation_list = itertools.permutations(list_of_tian_horses, len(list_of_king_horses))
    all_combinations = [list(zip(permutation, list_of_king_horses)) for permutation in permutation_list]

    max_king = -999 # To cater for situation where either side lost all matches
    max_tian = -999
    for index, combination in enumerate(all_combinations):
        tian_score = 0
        king_score = 0
        for pair in combination:
            if pair[0] > pair[1]:
                tian_score += 1
                king_score -= 1
            elif pair[0] < pair[1]:
                king_score += 1
                tian_score -= 1
        if tian_score > max_tian:
            max_tian = tian_score
        if king_score > max_king:
            max_king = king_score
    end_time = time.time()    
    print("max_tian: ", max_tian)
    print("max_king: ", max_king)
    print("Time spent: ", end_time - start_time)
