# Fotoblog

## Contexte de l'application web:

Un collectif de photographes cherche un moyen de montrer et de partager son travail à un large public.
Ils veulent pouvoir mettre leurs photos en ligne et créer des posts à leur sujet sur un blog.
Ils ont fait appel à vous en tant que développeur Django, et vous ont demandé de créer une application web qui leur permette justement de faire cela.
Ils ont besoin d’avoir deux types d’utilisateurs, les abonnés et les créateurs. Seuls les créateurs doivent pouvoir créer du contenu.
Ce contenu doit ensuite être partagé dans un flux social, et les abonnés doivent pouvoir choisir quels créateurs ils veulent suivre.

## Realisations

Construction d'une application pour gérer l’authentification et le stockage des utilisateurs en Django.
Utilisation des vues basées sur des classes et des vues génériques comme alternatives aux vues basées sur des fonctions.
Utilisation des fonctionnalités avancées des formulaires, comme le téléversement de fichiers et la gestion de formulaires multiples.
Creation de nouvelles méthodes de modèles, et nous avons surchargé des méthodes de modèles existantes, pour respecter la philosophie **fat models — skinny views** (gros modèles — vues maigres).
Configuration des permissions pour gérer des autorisations par utilisateur et par groupe.
Creation d'un flux social paginé, en utilisant des fonctionnalités avancées de l’ORM Django afin de créer des requêtes complexes.
Creation des éléments de gabarit réutilisables avec le mot-clé  {% include %}.

Ce projet est le projet fil rouge de la formation "Allez plus loin avec le framework Django" de Openclassrooms.
La formation est accessible a l'adresse suivante: https://openclassrooms.com/fr/courses/7192426-allez-plus-loin-avec-le-framework-django/
