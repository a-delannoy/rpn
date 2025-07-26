TODO
====

## Améliorations

* Améliorer la granularité dans la gestion des erreurs
* Réharmoniser les noms des entités et des méthodes
* Ajouter des docstrings pour la documentation


## Raccourcis

* Le registre des calculatrices est une simple variable importée depuis son module. Robustifier son accès via un singleton, et offir un set de méthodes pour manipuler le registre serait plus sûr.

* La persistance de données est actuellement implémentée en mémoire. Il serait préférable d'utiliser une base de données pour stocker les calculatrices et leurs états.