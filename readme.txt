J'ai fais les choix suivants dans mon fichier docker-compose.yml:
- J'ai mis un service init pour vider le fichier api_test.log avant de lancer les tests. Dans le cadre de l'exam ça donne une meilleur lisibilité des résultats a chaque lancement de docker compose.
- Le service api est lancé uniquement quand le service init est terminé.
- Les services des tests (test_1, test_2, test_3) sont lancés quand le service api est démaré, pour être sur que les appels n'echouent pas.
- Les différents services de tests sont lancés les uns après les autres, pour s'assurer qu'il n'écrivent pas en meme temps dans le fichier api_test.log.

( le fichier api_test.log contient le résultat de tous les tests )