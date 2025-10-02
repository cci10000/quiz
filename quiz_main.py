import threading
from quiz_DB import C_DB
class C_InputThread(threading.Thread):
   def __init__(self,a_prompt):
      super().__init__(daemon=True)
      self.v_prompt = a_prompt
      self.v_answer = None
   def run(self):
      try:
         self.v_answer = input(self.v_prompt)
      except EOFError:
         self.v_answer = None
def f_timed_input(a_prompt,a_timeout=20):
   v_it = C_InputThread(a_prompt)
   v_it.start()
   v_it.join(a_timeout)
   if v_it.is_alive():
      print('\n20초의 시간이 지나서 다음 문제로 넘어 갑니다...-.-;\n')
      return None
   else:
      return v_it.v_answer
D = C_DB()
if __name__ == '__main__':
   while True:
      try:
         v_quiz_kind = int(input('어느 quiz를 시작할까요?(nonsense : 1, IT : 2, 아리송송 우리말 : 3, 종료 : 1, 2, 3을 제외한 key)'))
         if v_quiz_kind == 1 or v_quiz_kind == 2:
            v_DB = D.f_random_question(v_quiz_kind)
            v_correct_count = 0
            v_question_no = 1
            for v_key,v_value in v_DB.items():
               v_answer = f_timed_input(f'{v_question_no}. {v_key}',a_timeout=20)
               v_question_no += 1
               if v_answer is None:
                  continue
               if v_answer.strip() == v_value:
                  v_correct_count += 1
                  print('정답입니다!...^.^\n')
               else:
                  print(f"오답입니다...-.-...정답은 '{v_value}'입니다.\n")
            print(f'총 5문제 중 {v_correct_count}문제를 맞추셨습니다.\n')
         else:
            if v_quiz_kind == 3:
               v_DB = D.f_random_question(v_quiz_kind)
               v_correct_count = 0
               v_question_no = 1
               for v_key, v_value in v_DB.items():
                  v_answer = f_timed_input(f"{v_question_no}. {v_key}\n(답은 '한글' 혹은 '한자' 또는 '일본어' 등으로 입력하십시오.)", a_timeout=20)
                  v_question_no += 1
                  if v_answer is None:
                     continue
                  if v_answer.strip() == v_value:
                     v_correct_count += 1
                     print('정답입니다!...^.^\n')
                  else:
                     print(f"오답입니다...-.-...정답은 '{v_value}'입니다.\n")
               print(f'총 5문제 중 {v_correct_count}문제를 맞추셨습니다.\n')
            else:
               print('quiz를 종료했습니다.')
               break
      except ValueError:
         print('quiz를 종료했습니다.')
         break