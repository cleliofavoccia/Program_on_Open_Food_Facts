Ce programme est un terminal dans lequel on sélectionne un produit du quotidien qu'on aimerait remplacer par un produit qui a un meilleur nutri score, donc un
produit qui est meilleur pour la santé !

Ce programme est composé de deux fonctionnalités qui se basent sur des requête SQL dans une base de donnée MySQL nommée "open_food_facts". 
La base de donnée prend les données de l'API Open Food Facts grâce à des méthodes qui utilisent la librairie request.

Voici les deux fonctionnalités :

TROUVER UN SUBSTITUT A UN ALIMENT 
- L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants:
	1 - Quel aliment souhaitez-vous remplacer ?
	2 - Retrouver mes aliments substitués

 - L'utilisateur sélectionne un nombre différent de 1 ou 2 
	Le terminal lui renvoi la question.

 - L'utilisateur sélectionne un caractère alphabétique
	Le terminal lui renvoi la question

 - L'utilisateur sélectionne 1.
	Le terminal affiche une liste de onze catégories et lui demande de sélectionner la catégorie qu'il souhaite en rentrant le chiffre associé à la catégorie souhaitée.
	 - L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un chiffre en dehors de l'ensemble 1 et 11 inclus.
		Le terminal lui renvoi l'instruction.
	- L'utilisateur sélectionne un chiffre entre 1 et 11 inclus.
		Le terminal affiche une liste de 20 produits selon la catégorie sélectionnée et demande à l'utilisateur de sélectionner le produit qu'il souhaite
		en rentrant le chiffre associé au produit souhaité.
	- L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un chiffre en dehors de l'ensemble de nombre affichés.
		Le terminal lui renvoi l'instruction
	- L'utilisateur sélectionne un chiffre de la liste.
		Le terminal lui retourne un produit substitut avec sa description, un magasin où l'acheter et unlien vers la page d'Open Food Facts concernant cet aliment.
	- Le terminal demande si l'utilisateur veut enregistrer le résultat dans la base de donnée. 1 = Oui et 2 = Non
	- L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un nombre différent de 1 ou 2.
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne 1.
		Le produit est enregistré, la colonne is_saved du produit dans la table products passe de NULL à 1.
	- L'utilisateur sélectionne 2.
		Le produit n'est pas enregistré, rien ne se passe.
	- Le terminal demande si l'utilisateur veut recommencer le programme. 1 = Oui et 2 = Non
	- - L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un nombre différent de 1 ou 2.
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne 1.
		Le programme recommence
	- L'utilisateur sélectionne 2.
		Le programme s'arrête.

RETROUVER UN SUBSTITUT SAUVEGARDE.
- L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants:
	1 - Quel aliment souhaitez-vous remplacer ?
	2 - Retrouver mes aliments substitués

 - L'utilisateur sélectionne un nombre différent de 1 ou 2 
	Le terminal lui renvoi la question.

 - L'utilisateur sélectionne un caractère alphabétique
	Le terminal lui renvoi la question
- L'utilisateur sélectionne 2.
	Le terminal affiche une liste de onze catégories et lui demande de sélectionner la catégorie qu'il souhaite en rentrant le chiffre associé à la catégorie souhaitée.
	 - L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un chiffre en dehors de l'ensemble 1 et 11 inclus.
		Le terminal lui renvoi l'instruction.
	- L'utilisateur sélectionne un chiffre entre 1 et 11 inclus.
		Le terminal affiche la liste des produits sauvegardés et leur id respectif de la catégorie sélectionnée et demande à l'utilisateur de sélectionner le produit qu'il souhaite
		en rentrant le chiffre associé au produit souhaité.
	- L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un chiffre en dehors de l'ensemble de nombre affichés.
		Le terminal lui renvoi l'instruction
	- L'utilisateur sélectionne un chiffre de la liste.
		Le terminal lui retourne un produit substitut avec sa description, un magasin où l'acheter et unlien vers la page d'Open Food Facts concernant cet aliment.
	- Le terminal demande si l'utilisateur veut recommencer le programme. 1 = Oui et 2 = Non
	- - L'utilisateur sélectionne un caractère alphabétique
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne un nombre différent de 1 ou 2.
		Le terminal lui renvoi la question
	- L'utilisateur sélectionne 1.
		Le programme recommence
	- L'utilisateur sélectionne 2.
		Le programme s'arrête.