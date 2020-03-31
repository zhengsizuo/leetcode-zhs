result = []
def backtrack(path, choice_list):
   if end_condition:
      result.add(path)
      return
   for choice in choice_list:
      make_choice
      backtrack(path, choice_list)
      cancel_choice
