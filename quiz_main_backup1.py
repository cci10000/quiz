import threading
from quiz_DB import C_DB
class C_InputThread(threading.Thread):
   def __init__(self,a_prompt):
      super().__init__()
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
      print('10초의 시간이 지나서 다음 문제로 넘어 갑니다...-.-;')
      return None
   else:
      return v_it.v_answer
D = C_DB()
if __name__ == '__main__':
   v_start_yn = input('nonsensquiz를 시작할까요?(y or n)')
   if v_start_yn == 'y' or v_start_yn == 'Y':
      v_DB = D.f_random_question()
      v_correct_count = 0
      for v_key,v_value in v_DB.items():
         v_answer = f_timed_input(f'{v_key}',a_timeout=20)
         if v_answer is None:
            continue
         if v_answer.strip() == v_value:
            v_correct_count += 1
            print('정답입니다!...^.^')
         else:
            print('오답입니다...-.-')
      print(f'총 5문제 중 {v_correct_count}를 맞추셨습니다.')
   else:
      print('nonsensquiz를 종료했습니다.')