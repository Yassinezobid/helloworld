# Toujours dans le cadre des projets de traitement de multimedia , 
#Voici notre code python du projet Text to speech 

              # Bibliothèque 

import tkinter as tk  #  bibliothèque tkinter pour créer une interface graphique
from gtts import gTTS  # gTTS pour la synthèse vocale (google text to speech)
from playsound import playsound  # playsound pour jouer le fichier audio
import os  #  os pour effectuer des opérations sur le système d'exploitation
import datetime  # datetime pour nommer les fichiers par leurs date de creation (unicité )

        # Fonction principale qui fait la synthese vocale , et joue l'audio generé


def text_to_speech():
    # Récupération du texte saisi par l'utilisateur depuis l'interface Text et l'ecrire dans la premiere ligne 
    text = text_entry.get("1.0", tk.END).strip()

    if text:  # Vérification que du texte a été saisi
        
        # Génération d'un timestamp pour nommer le fichier audio de manière unique
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"output_{timestamp}.mp3"  # Nom du fichier audio
        
        # Conversion du texte en discours dans la langue sélectionnée
        tts = gTTS(text=text, lang=language_var.get())
        tts.save(filename)  # Sauvegarde du fichier audio
        
        print(f"Audio file created: {filename}")  # Affichage du nom du fichier audio créé
        playsound(filename)  # Lecture du fichier audio
    
# Configuration de l'interface utilisateur
root = tk.Tk()  # Création de la fenêtre principale
root.title("Text to Speech")  # Titre de la fenêtre

# Zon de texte pour saisir du texte
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack()

# Selection de la langue preferee 
language_var = tk.StringVar(value='en')  # Langue par défaut
language_label = tk.Label(root, text="Language:")  # Étiquette pour la sélection de la langue
language_label.pack()


# Menu pour choisir la langue
language_menu = tk.OptionMenu(root, language_var, 'en', 'fr', 'es',)
language_menu.pack()

# Bouton pour lancer l'audio 
speak_button = tk.Button(root, text="Speak", command=text_to_speech)
speak_button.pack()

# Lancement de l'interface utilisateur
root.mainloop()
