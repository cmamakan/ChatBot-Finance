# Chatbot Finance – Projet personnel

Issu d’un parcours orienté data, j’ai développé un intérêt particulier pour la finance.  
J’ai donc voulu créer un projet qui me permettrait à la fois de réviser les concepts financiers essentiels et de mettre en œuvre des techniques de traitement automatique du langage.  
Ce chatbot répond à des questions sur des notions économiques ou financières, en s’appuyant sur des outils comme **spaCy** et l’**API Wikipedia**, le tout intégré dans une application légère construite avec **Flask**.

Ce projet m’a également permis d’explorer des notions proches de l’IA générative, en me concentrant notamment sur l’extraction de sens à partir de textes, la génération de réponses adaptées et le filtrage contextuel.

## Fonctionnement technique

Le fonctionnement repose sur plusieurs briques simples mais complémentaires :

- **Wikipedia API** : permet de récupérer dynamiquement des résumés d’articles encyclopédiques en français. C’est la principale source d’information du chatbot.
- **spaCy** : utilisé pour analyser la question de l’utilisateur et en extraire automatiquement le mot-clé principal (nom commun ou nom propre) sur lequel baser la recherche.
- **Filtrage thématique** : une fois l’article identifié, le résumé est analysé pour vérifier qu’il appartient bien au domaine de la finance (recherche de mots-clés comme "marché", "monnaie", "banque", etc.).
- **Flask** : framework léger utilisé pour gérer l’interface web, les échanges utilisateur, les appels à Wikipedia, ainsi que la gestion de session (notamment pour l’historique de conversation).

L’ensemble est encapsulé dans une interface web simple, avec un champ de saisie, une zone de réponse, et un affichage chronologique des échanges.

## Exemples en images

### 1. Question liée à la finance

![chatbot1](https://github.com/user-attachments/assets/47a09c19-ac47-4560-abbf-b140cba5ff98)

Ici, l’utilisateur pose une question sur une notion financière. Le chatbot extrait automatiquement le bon mot-clé, interroge Wikipedia, filtre le contenu, et renvoie un résumé clair et ciblé, accompagné d’un lien vers l’article complet.

### 2. Historique visible après plusieurs questions

![chatbot2](https://github.com/user-attachments/assets/139e9ecc-999e-4a2c-a7ff-aa791540d228)

L’historique des échanges est conservé le temps de la session, permettant à l’utilisateur de suivre la conversation facilement, sans perdre le fil.

### 3. Question hors finance

![chatbot3](https://github.com/user-attachments/assets/d2e5a238-67b0-44ce-97b1-e2f57c818da7)

Lorsque la question posée n’est pas en lien avec la finance, le chatbot le détecte automatiquement et invite l’utilisateur à reformuler dans le domaine qu’il couvre.
