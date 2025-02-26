import openai
import pyperclip
from playsound import playsound
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

texteACorriger = pyperclip.paste()

openai.api_key = "xxxx"#Change Key

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": """Correcteur orthographique bilingue (français/anglais). Instructions:
            1. Détecter automatiquement la langue du texte fourni (français ou anglais)
            2. Corriger: orthographe, grammaire, accords, conjugaisons, ponctuation selon les règles de la langue détectée
            3. Préserver: sens original, structure des phrases, style, vocabulaire choisi, registre de langue
            4. Ne pas: ajouter/supprimer des mots, reformuler des phrases, modifier le ton
            5. Privilégier les corrections minimales nécessaires
            6. Pour les ambiguïtés, choisir la correction la plus proche du contexte original
            7. Retourner UNIQUEMENT le texte corrigé sans commentaires ni explications"""
        },
        {
            "role": "user", 
            "content": "Texte à corriger / Text to correct:\n\n" + texteACorriger
        }
    ]
)

texteCorriger = response.choices[0].message.content

pyperclip.copy(texteCorriger)

path_sound = BASE_DIR + "\correct.mp3"

playsound(path_sound.encode('unicode-escape').decode())

