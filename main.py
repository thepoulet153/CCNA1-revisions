from main_configuration import *

def lire_fichier_json(nomFich):
    try:
        with open(nomFich, "r", encoding="UTF-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erreur : le fichier {nomFich} n'a pas été trouvé.")
        return []

def affiche_menu(dif_modules):
    
    print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}■■■■■■■■ MENU DE GESTION ■■■■■■■■{Fore.RESET}{Style.RESET_ALL}")
    for i in dif_modules.keys():
        print(i)
    print("F : Quiter")
    module_choose = input("Quels modules voulez-vous réviser : ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    return module_choose

json_directory = input("Veuillez entrer le chemin du répertoire contenant les fichiers JSON : ")

dif_modules = {
    "1-3": os.path.join(json_directory, "ccna1-3.json"),
    "4-7": os.path.join(json_directory, "ccna4-7.json"),
    "8-10": os.path.join(json_directory, "ccna8-10.json"),
    "11-13": os.path.join(json_directory, "ccna11-13.json"),
    "14-15": os.path.join(json_directory, "ccna14-15.json"),
    "16-17": os.path.join(json_directory, "ccna16-17.json")
}

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
                    print(f"{Fore.GREEN}■■■■■■■■ CORRECT ! ■■■■■■■■{Fore.RESET}")
                    nb_good_answers = total.add_one_good_answer()
                else:
                    print(f"{Fore.RED}■■■■■■■■ FAUX ! ■■■■■■■■ la ou les réponses était : {answers}{Fore.RESET}")
                
                dataJson.remove(data)
            print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Voici le nombre de bonnes réponses : {nb_good_answers} / {nb_questions}{Fore.RESET}")
            
        elif module_choose == "F":
            quiter = True