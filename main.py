import json
import os
from main_configuration import *
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def lire_fichier_json(nomFich):
    """Lit un fichier JSON et retourne son contenu sous forme de dictionnaire."""
    try:
        with open(nomFich, "r", encoding="UTF-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"Erreur : le fichier {nomFich} n'a pas été trouvé.", style="bold red")
        return []
    except json.JSONDecodeError:
        console.print(f"Erreur : le fichier {nomFich} n'est pas un JSON valide.", style="bold red")
        return []

def affiche_menu(dif_modules):
    """Affiche le menu et retourne le choix de l'utilisateur."""
    console.print("\n[bold green]MENU DE GESTION[/bold green]")
    for key, value in dif_modules.items():
        console.print(f"[cyan]{key}[/cyan] - {value['name']}")
    console.print("[bold yellow]F[/bold yellow] - Quitter")
    module_choose = Prompt.ask("Veuillez entrer le numéro du module que vous voulez réviser")
    clear_console()
    return module_choose

def clear_console():
    """Efface la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_open(path):
    """Teste si le fichier à un chemin donné peut être ouvert."""
    try:
        with open(path) as f:
            pass
        return True
    except Exception:
        console.print(f"Erreur : Le chemin d'accès au fichier '{path}' n'est pas bon.", style="bold red")
        return False

def main():
    good_path = False
    while not good_path:
        json_directory = Prompt.ask("Veuillez entrer le chemin du répertoire contenant les fichiers JSON")
        
        dif_modules = {
            "1": {"path": os.path.join(json_directory, "ccna1-3.json"), "name": "Modules 1-3"},
            "2": {"path": os.path.join(json_directory, "ccna4-7.json"), "name": "Modules 4-7"},
            "3": {"path": os.path.join(json_directory, "ccna8-10.json"), "name": "Modules 8-10"},
            "4": {"path": os.path.join(json_directory, "ccna11-13.json"), "name": "Modules 11-13"},
            "5": {"path": os.path.join(json_directory, "ccna14-15.json"), "name": "Modules 14-15"},
            "6": {"path": os.path.join(json_directory, "ccna16-17.json"), "name": "Modules 16-17"}
        }
        good_path = test_open(dif_modules["1"]["path"])

    total = FINALResult()
    quitter = False
    count = 0

    while not quitter:
        module_choose = affiche_menu(dif_modules)
        
        if module_choose in dif_modules.keys():
            dataJson = lire_fichier_json(dif_modules[module_choose]["path"])
            nb_questions = len(dataJson)
            nb_good_answers = 0
            
            while dataJson:
                data = choice(dataJson)
                jsonPrinted = PRINTJson(data)
                answers = jsonPrinted.ass_for_a_question()
                count += 1
                
                result = DATAJson(answers)
                if result.get_result():
                    console.print(f"[bold green]:white_check_mark: CORRECT ! Question {count} sur {nb_questions}[/bold green]")
                    nb_good_answers = total.add_one_good_answer()
                else:
                    console.print(f"[bold red]:x: FAUX ! La ou les réponses étaient : {answers}, Question {count} sur {nb_questions}[/bold red]")
                
                dataJson.remove(data)
            
            ratio = (nb_good_answers / nb_questions) * 100
            console.print(f"[bold yellow]Voici le nombre de bonnes réponses : {nb_good_answers} / {nb_questions}, pourcentage : {ratio:.2f}%[/bold yellow]")
            
        elif module_choose.upper() == "F":
            quitter = True
        else:
            console.print(f"[bold red]Choix invalide : {module_choose}. Veuillez réessayer.[/bold red]")

if __name__ == '__main__':
    main()
