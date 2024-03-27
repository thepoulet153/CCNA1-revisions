from colorama import Fore, Style

class DATAJson:
    
    def __init__(self , ANSWERS):
        self.ANSWERS = ANSWERS
    
    def get_result(self):
        if len(self.ANSWERS) > 1:
            user_answer = input("Veuillez choisir les bonnes réponses : ").split(" ")
        else:
            user_answer = input("Veuillez choisir la bonne réponse : ").split(" ")
        
        if self.is_good_a_answer(user_answer):
            return True
        
        return False
    
        
    def is_good_a_answer(self, user_answer):
        count = 0
        
        for answer in user_answer:
            try:
                if int(answer) in self.ANSWERS:
                    print("TRUE")
                    count +=1  
            except:
                print(f"{Style.DIM}{Fore.RED}MERCI de spécifier une valeur correcte.{Style.RESET_ALL}")
                self.get_result()
                
        return count == len(self.ANSWERS)