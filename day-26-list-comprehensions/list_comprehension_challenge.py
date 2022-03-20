
#Problem

# take this code and use list comprehensions to shorten it by a few linesep

# if answer_state == "Exit":
#     missing_states = []
#     for state in all_states:
#         if state not in guessed_states:
#             missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break


# #Answer
# if answer_state == "Exit":
#     missing_states = [state for state in all_states if state not in guessed_states]
