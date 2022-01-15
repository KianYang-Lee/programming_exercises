from collections import defaultdict
import time

if __name__ == "__main__":
    tian_horses = input("Input for Tian: ")
    king_horses = input("Input for King: ")
    start_time = time.time()
    list_of_tian_horses = map(int,tian_horses.split())
    list_of_king_horses = map(int,king_horses.split())
    zipped_list = zip(list_of_tian_horses, list_of_king_horses)
    list_of_zipped_pairs = list(zipped_list)
    scores = []
    for index, zipped_elem in enumerate(list_of_zipped_pairs):
        print(zipped_elem)
        if zipped_elem[0] > zipped_elem[1]:
            scores.append("tian")
        elif zipped_elem[0] < zipped_elem[1]:
            scores.append("king")
        else:
            scores.append("draw")
    tian_score = scores.count("tian") - scores.count("king")
    king_score = scores.count("king") - scores.count("tian")
    end_time = time.time()
    print("max_tian: ", tian_score)
    print("max_king: ", king_score)
    print("Time spent: ", end_time - start_time)
