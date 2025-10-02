from quiz_DB import C_DB
D = C_DB()
class C_Interface:
   def f_start(self):
      return D.f_random_question()
#같은 문제가 또 나오면 안됨.