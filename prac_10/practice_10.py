PLAYER_TO_SCORE = {'Mary': 3, 'Robert': 5, 'Jeremy': 9, 'Judy': 5}
player_codes = sorted(PLAYER_TO_SCORE.keys())
# print(player_codes)
#
# player_codes = sorted(PLAYER_TO_SCORE.values())
# print(player_codes)
#
# print(PLAYER_TO_SCORE)




# don't need to specify width value because one was not given
def print_pairs(player_to_score, width):
    for player, score in player_to_score.items():
        print(f"{player:{width}} {score:{3}}")

            #print(f"{(player_to_score.keys())}: <{width} {(player_to_score.values())} <{3} ")


def get_highest_score(player_to_score):
    print(f"{max((player_to_score.values()))}")

# it wont print???







        # 37 questions

