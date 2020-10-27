# Une implementation du calcul de PI par la methode de Monte Carlo

Le problème est décrit [ici](https://bpi-etu.pages.ensimag.fr/projet/).

# Generation du fichier figures.dat (optionel)

Cette implémentation utilise uniquement la librairie standard,
mais Pillow est utilisé pour générer en offline un tableau de pixels
representant les chiffres, histoire d'avoir un affichage plus sympa
que l'exemple du site.

1. Installer Pillow `pip install pillow`
2. Lancer le generateur `python genfigures.py`

Un fichier 'figures.dat' est généré qui contient un dictionnaire d'objets `Figure`
prêt à être charger via `pickle` dans les autres modules.

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
Image 0 with   100,000 points: pi = 3.15116 saved in img0_3-15116.ppm
Image 1 with   200,000 points: pi = 3.14482 saved in img1_3-14482.ppm
Image 2 with   300,000 points: pi = 3.14189 saved in img2_3-14189.ppm
Image 3 with   400,000 points: pi = 3.14196 saved in img3_3-14196.ppm
Image 4 with   500,000 points: pi = 3.14262 saved in img4_3-14262.ppm
Image 5 with   600,000 points: pi = 3.14185 saved in img5_3-14185.ppm
Image 6 with   700,000 points: pi = 3.14197 saved in img6_3-14197.ppm
Image 7 with   800,000 points: pi = 3.14078 saved in img7_3-14078.ppm
Image 8 with   900,000 points: pi = 3.14142 saved in img8_3-14142.ppm
Image 9 with 1,000,000 points: pi = 3.14123 saved in img9_3-14123.ppm
Approximation: pi = 3.141232 with 1,000,000 points
Elapsed time : 3.629s (275,587 points/s)
Peak memory  : 18 MB
```

>NB: Les fichiers ppm sont créés par défaut dans le sous-répertoire ppm.