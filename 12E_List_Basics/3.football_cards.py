team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
game_is_terminated = False
sent_off_players = input().split()    # split() == split(" ")
for player in sent_off_players:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:   # броят на елементите е равен на броя на играчите
        game_is_terminated = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_is_terminated:
    print("Game was terminated")


# cards = input()
# team_A = 11
# team_B = 11
# game_is_terminated = False
# if cards:
#     cards_list = cards.split(" ")
#     sent_off = []
#     for card in cards_list:
#         if "A" in card and card not in sent_off:
#             team_A -= 1
#             sent_off.append(card)
#         elif "B" in card and card not in sent_off:
#             team_B -= 1
#             sent_off.append(card)
#         if team_A < 7 or team_B < 7:
#             game_is_terminated = True
#             break
# print(f"Team A - {team_A}; Team B - {team_B}")
# if game_is_terminated:
#     print("Game was terminated")