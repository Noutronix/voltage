# Simulation de voltage à trois dimentions
Ceci est mon projet de physique pour le cours SPH4U1. C'est, essentiellement, un groupement de cinq graphiques interactives (la perspective des graphiques peuvent être tournées) qui représentent le voltage avec la hauteur. C'est un peu comme un graphique de lignes equipotentielles en 2d mais au lieu de lignes qui représentent un voltage plus haut, c'est l'axe des z dans des graphiques 3D. 

Les modules requises pour l'execution du logiciel sont dans le fichier requirements.txt, mais les voici quand-même:
- tkinter
- matplotlib
- numpy

Voici ma bibliographie:
- https://stackoverflow.com/questions/4913306/python-matplotlib-mplot3d-how-do-i-set-a-maximum-value-for-the-z-axis 
  Un problème qui se montrait souvent dans les graphiques est car le voltage est demontree par la formule kQ/r, le voltage pres de la charge (quand r -> 0) approchait l'infini. Ceci faisait que le graphique avait quelques grosses pics et rien d'autre. En limitant les donnees, comme c'est mentionné dans ce site, à 100V, c'est possible maintenant de voir les effets de plusieurs charges sur le voltage autour d'eux.
- https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/ 
  Ces graphiques Matplotlib sont representés dans un GUI Tkinter, et cela ne serait pas possible sans ce site web. Il faut utiliser des parties très obscurs dans le module Matplotlib, et j'ai presque copié le code a 100% car c'était exactement ce dont j'avais besoin.
- https://www.youtube.com/watch?v=gqoLLGgbeAE&ab_channel=KimberlyFessel 
  Cette video a beaucoup aidé à comprendre comment créer des graphiques à trois dimensions quand je ne comprenais pas comment faire une valeur de z pour chaque valeur (x, y). Car elle a dit de tout faire avec une fonction qui fait les maths avec chaque valeur dans les "numpy arrays" (tableaux numériques), tout était beaucoup plus simple. 
