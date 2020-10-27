# Une implementation du calcul de PI par la methode de Monte Carlo

Le problème est décrit [ici](https://bpi-etu.pages.ensimag.fr/projet/).

## Generation du fichier figures.dat (optionel)

Cette implémentation utilise uniquement la librairie standard,
mais Pillow est utilisé pour générer en offline un tableau de pixels
representant les chiffres, histoire d'avoir un affichage plus sympa
que l'exemple du site.

1. Installer Pillow `pip install pillow`
2. Lancer le generateur `python genfigures.py`

Un fichier 'figures.dat' est généré qui contient un dictionnaire d'objets `Figure`
prêt à être charger via `pickle` dans les autres modules.

>Pour changer la police utilisée par le générateur et sa taille, il faut modifier le code

## Script `convert.py` (optionel)

Puisque le site ne donne pas le programme `convert` devant générer le GIF animé, et puisque
Pillow est déjà utilisé, un script `convert.sh` cette librairie est proposé pour le simuler.

Le script attends la liste des fichiers servant à générer l'animation, dans l'ordre chronologique
et le nom du fichier GIF à générer.
La temporisation est fixée à une seconde et l'animation boucle par défaut.

Il peut être appelé en ligne de commande:

```
convert.sh $(ls ppm/img* | sort) pi.gif
```

Il est automatiquement appelé en Python via un subprocess comme demandé par `approximate_pi` à la fin des calculs.

## Module `simulation.py`

Ce module est conforme à l'énoncé du problème et calcule une approximation de PI avec un nombre de tirages donné:

```shell
> python simulation.py 1000000
Approximation: pi = 3.142004 with 1,000,000 points
Elapsed time : 0.819s (1,221,435 points/s)
Peak memory  : 15 MB
```

## Module `approximate_pi.py`

Ce module attends en argument la largeur de l'image (carrée), le nonmbre de points et la precision d'affichage de PI:

```
python approximate_pi.py 800 1000000 5
Image 0 with   100,000 points: pi = 3.15460 saved in img0_3-15460.ppm
Image 1 with   200,000 points: pi = 3.14958 saved in img1_3-14958.ppm
Image 2 with   300,000 points: pi = 3.14428 saved in img2_3-14428.ppm
Image 3 with   400,000 points: pi = 3.14364 saved in img3_3-14364.ppm
Image 4 with   500,000 points: pi = 3.14458 saved in img4_3-14458.ppm
Image 5 with   600,000 points: pi = 3.14464 saved in img5_3-14464.ppm
Image 6 with   700,000 points: pi = 3.14290 saved in img6_3-14290.ppm
Image 7 with   800,000 points: pi = 3.14189 saved in img7_3-14189.ppm
Image 8 with   900,000 points: pi = 3.14161 saved in img8_3-14161.ppm
Image 9 with 1,000,000 points: pi = 3.14165 saved in img9_3-14165.ppm
Generating GIF pi.gif
Approximation: pi = 3.141652 with 1,000,000 points
Elapsed time : 1.860s (537,641 points/s)
Peak memory  : 19 MB

Process finished with exit code 0
```

>NB: Les fichiers ppm sont créés par défaut dans le sous-répertoire ppm.