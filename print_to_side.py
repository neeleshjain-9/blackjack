def side_to_side(v_list):
    h_list = []
    lines = [v_list[i].splitlines() for i in range(len(v_list))]
    for l in zip(*lines):
        print(*l)


# dice_art = ["""
#  -------
# |       |
# |   0   |
# |       |
#  ------- """,
#             """
#  -------
# |       |
# |   1   |
# |       |
#  ------- """,
#             """
#  -------
# |       |
# |   2   |
# |       |
#  ------- """
#             ]
# side_to_side(dice_art)
