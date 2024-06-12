from main_configuration import *
from rich.console import Console
console = Console()

def lire_fichier_json(nomFich):
    try:
        with open(nomFich, "r", encoding="UTF-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print_exception(show_locals=True)
        console.print(f"Erreur : le fichier {nomFich} n'a pas été trouvé.", style="bold red")
        return []

def affiche_menu(dif_modules):
    
    console.print("MENU DE GESTION", style="bold green")
    for i in dif_modules.keys():
        print(i)
    print("F : Quiter")
    module_choose = input("Quels modules voulez-vous réviser : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    return module_choose

def test_open(path):
    try:
        f = open(f'{path}')
        f.close()
        
        return True
    except Exception as e:
        console.print_exception(show_locals=True)
        console.print(f"Le chemin d'accès au fichier n'est pas bon.", style="bold red")
        
good_path = False
while not good_path:
    json_directory = input("Veuillez entrer le chemin du répertoire contenant les fichiers JSON : ")
    
    dif_modules = {
    "1-3": os.path.join(json_directory, "ccna1-3.json"),
    "4-7": os.path.join(json_directory, "ccna4-7.json"),
    "8-10": os.path.join(json_directory, "ccna8-10.json"),
    "11-13": os.path.join(json_directory, "ccna11-13.json"),
    "14-15": os.path.join(json_directory, "ccna14-15.json"),
    "16-17": os.path.join(json_directory, "ccna16-17.json")
                }
    good_path = test_open(dif_modules["1-3"])
    

if __name__ == '__main__':
    total = FINALResult()
    quiter = False
    
    while not quiter:
        module_choose = affiche_menu(dif_modules)
        
        if module_choose in dif_modules.keys():
            dataJson = lire_fichier_json(dif_modules[module_choose])
            nb_questions = len(dataJson)
            
            while dataJson:
                data = choice(dataJson)
                jsonPrinted = PRINTJson(data)
                answers = jsonPrinted.ass_for_a_question()
                
                result = DATAJson(answers)
                if result.get_result():
                    console.print(":white_check_mark: CORRECT !", style="bold green")
                    nb_good_answers = total.add_one_good_answer()
                else:
                    console.print(f":x: FAUX ! la ou les réponses étaient : {answers}", style="bold red")
                
                dataJson.remove(data)
            print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Voici le nombre de bonnes réponses : {nb_good_answers} / {nb_questions}{Fore.RESET}")
            
        elif module_choose == "F":
            quiter = True