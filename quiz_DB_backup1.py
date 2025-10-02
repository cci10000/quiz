import json,random
class C_DB:
   def __init__(self):
      with open('question.json','r',encoding='UTF-8') as v_open1:
         self.v_questions = json.load(v_open1)
      with open('answer.json', 'r', encoding='UTF-8') as v_open2:
         self.v_answers = json.load(v_open2)
   def f_random_question(self):
      v_all_keys = list(self.v_questions.keys())
      v_selected_keys = random.sample(v_all_keys,5)
      v_quiz_dict = {self.v_questions[v_count]:self.v_answers[v_count] for v_count in v_selected_keys}
      print(v_quiz_dict)
      return v_quiz_dict