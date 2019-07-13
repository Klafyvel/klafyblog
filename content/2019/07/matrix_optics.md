Title: Matrices et optique géométrique #1
Date: 2019-07-04 23:00
Category: Optics
Tags: french, optics
Status: published

Aujourd'hui je sais que j'aime l'optique. Pourtant si on m'avait dit quand j'étais en première S que j'orienterais ma carrière vers ce domaine, je ne l'aurait pas cru. Tout simplement parce que pour moi, l'optique, c'était synonyme d'apprentissage de formules de conjugaison par cœur. Or j'étais (et je suis toujours) feignant. Vraiment. Apprendre quelque chose par cœur a toujours été quelque chose de rédhibitoire. Or j'ai pu rencontrer durant mes études une technique simple (à mon avis) pour faire de l'optique sans se prendre la tête avec des formules. Mais d'abord...

# Rappels de mathématiques
Dans la suite nous allons avoir besoin de faire des calculs avec des matrices. Pas de panique, pas de prérequis compliqués je vais tout expliquer simplement. Les vrais matheux sont priés de m'envoyer un mail pour que l'on organise ma pendaison publique.

Nous n'allons utiliser que des matrices $2\times 2$. Qu'est-ce que donc que cela ? tout simplement un objet mathématique avec 4 dimension. C'est à dire que l'on définit avec quatre nombres. Par exemple si notre matrice $M$ est définie avec les nombres $a$, $b$, $c$ et $d$, nous l'écrirons

\begin{equation}
M = \begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix}
\end{equation}

Dans la suite nous auront également besoin de vecteurs. Là encore il s'agit d'un objet mathématique particulier. Un vecteur se caractérise par deux grandeurs. Ainsi par exemple, si l'on a un vecteur $V$ défini par les grandeurs $x$ et $y$, on le notera

\begin{equation}
V = \begin{pmatrix}
x \\
y
\end{pmatrix}
\end{equation}


## Opérations sur nos jouets : l'addition

Avec nos nouveaux jouets, nous allons pouvoir réaliser quelques opérations. Dans la suite, nous utiliserons deux matrices, $M$ et $P$, et un vecteur $V$ que nous noterons comme suit :

\begin{equation}
M = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}, \;
P = \begin{pmatrix}
e & f \\
g & h
\end{pmatrix},\;
V = \begin{pmatrix}
x \\
y
\end{pmatrix}
\end{equation}

Dans cette partie, nous allons voir deux façons de combiner $M$ et $P$. La première est de les additionner. Le résultat de l'addition de deux matrices s'écrit

\begin{equation}
M + P = \begin{pmatrix} a & b \\ c & d\end{pmatrix} + \begin{pmatrix} e & f \\ g & h\end{pmatrix} = \begin{pmatrix} a+e & b+f \\ c+g & d+h\end{pmatrix}
\end{equation}

Rien de bien compliqué non ? **la somme de deux matrices est une matrice dont les composantes sont les sommes des composantes des matrices**.

## Opérations sur nos jouets : multiplication par un scalaire

De même, on peut multiplier une matrice ou un vecteur par un scalaire. Soit $\alpha$ un scalaire,

\begin{equation}
\alpha \times M = \begin{pmatrix}
\alpha \times a & \alpha \times b \\
\alpha \times c & \alpha \times d
\end{pmatrix}, \; \alpha \times V = \begin{pmatrix}
\alpha \times x \\
\alpha \times y
\end{pmatrix}
\end{equation}

 **Le produit d'un scalaire et d'une matrice est une matrice dont les composantes sont le produit du scalaire et des composantes de la matrice**. Pareillement, **le produit d'un scalaire et d'un vecteur est un vecteur dont les composantes sont le produit du scalaire et des composantes du vecteur**

Nous verrons d'autres opérations réalisables sur ces objets, mais nous n'en avons pas besoin pour l'instant.

# Comment étudier la lumière ?

Il existe beaucoup de modèles de la lumière, que ce soit corpusculaire ou ondulatoire. La question de sa nature a donné l'occasion à beaucoup de scientifiques de s'arracher des cheveux. Quel est donc le bon modèle à utiliser ? la réponse est... que cela n'a pas d'importance dans notre cas. L'optique géométrique reste valide quelque soit la nature de la lumière, et tant que l'on considère son interaction avec des objets de grande taille. Enfin, l'optique géométrique ne permet pas d'expliquer des phénomènes tels que la diffraction ou les interférences.

Nous allons étudier la propagation de la lumière dans un plan, dans une direction donnée. On utilisera un repère orthonormé $\mathcal{O}_{x,y}$. Pour matérialiser le comportement de la lumière, on utilise le concept de **rayons lumineux**. Si vous imaginez la lumière comme étant de minuscules billes se déplaçant dans l'espace, alors ces rayons peuvent être vus comme des trajectoires. Nous faisons l'hypothèse que, sans interaction, la **lumière se déplace en ligne droite**. Autrement dit, si l'on trace un rayon lumineux dans le vide, il s'agit d'une droite. On peut donc représenter sa trajectoire comme sur l'image suivante :

![Rayon lumnieux]({attach}matrix_optics/rays/ray.svg)

On indique l'axe $\mathcal{O}_x$ (que l'on appelle l'**axe optique**) pour se donner une idée de la direction de propagation du rayon, et on donne le sens grâce à la petite flêche sur le rayon. En se plaçant à l'endroit sur l'axe $\mathcal{O}_x$ d'où est émis ce rayon, on peut donc caractériser cette demi-droite par deux informations : la hauteur $y$ et l'angle avec l'horizontale $\theta$.

![Repèrage d'un rayon lumineux]({attach}matrix_optics/rays/rays_pos.svg)

On représente un le rayon avec le vecteur suivant : $$\begin{pmatrix}y\\ \theta\end{pmatrix}$$

Toute la suite de cet article aura pour but de travailler sur ce vecteur afin de trouver comment il évolue. Pour cela, nous allons avoir besoin d'un nouvel interlude mathématique...


# Multiplications dans tous les sens

Pour l'instant, nous ne savons qu'additionner des matrices et multiplier par un scalaire un vecteur ou une matrice. Il temps que cela change !

## Multiplication d'une matrice et d'un vecteur

Nous allons définir la multiplication à gauche d'un vecteur par une matrice. Attention, ici, le sens de la multiplication est important. On parle bien de la multiplication $M\cdot V$. On la défini ainsi :

\begin{equation}
M\cdot V = \begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix} \cdot \begin{pmatrix}
x \\
y
\end{pmatrix} = \begin{pmatrix}
a \times x + b \times y \\
c \times x + d \times y
\end{pmatrix}
\end{equation}

**Le produit d'une matrice et d'un vecteur est un vecteur dont les composantes sont la combinaison de la première ligne de la matrice avec les composantes du vecteur et la combinaison de la deuxième ligne de la matrice avec les composante du vecteur.**

## Multiplication de deux matrices

On peut également multiplier deux matrices carrées (je rappelle que les matrices qui nous intéressent sont carrées). Ainsi,

\begin{equation}
M\cdot P = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \cdot \begin{pmatrix}
e & f \\
g & h
\end{pmatrix} = \begin{pmatrix}
a \times e + b \times g & a \times f + b \times h \\
c \times e + d \times g & c \times f + d \times h
\end{pmatrix}
\end{equation}

On peut remarquer que le résultat est similaire à celui obtenu lors de la multiplication $M \cdot V$, si l'on considère que la matrice $P$ comme un couple de vecteurs : $$\begin{pmatrix} e \\ g \end{pmatrix} \text{et} \begin{pmatrix} f \\ h \end{pmatrix}$$.

Cette formule peut sembler un peu pénible à retenir. À titre personnel, je la retrouve à l'aide d'une petite astuce que j'ai tenté de résumer dans l'animation suivante :

![Animation du produit matriciel]({attach}matrix_optics/anime_matrix/anime_optimized.gif)

# Matrices optique

Grâce au produit matriciel, nous allons pouvoir exprimer les transformations que subit le vecteur représentant la lumière lorsque cette dernière se propage. L'idée principale est de déduire une matrice $M$ telle que, si l'on connaît le vecteur originel $V$, on puisse déduire le vecteur d'arrivée $V'$ tel que $V' = M\cdot V$.

## Propagation dans un matériau

Supposons que l'on souhaite connaître l'évolution de notre vecteur après propagation dans un matériau sur une longueur $l$.

![Schéma de propagation]({attach}matrix_optics/rays/rays_propa.svg)

On a alors $$dy = \tan (\theta) \times l$$

Comme on se place dans l'approximation des petits angles, on a alors $$dy \approx \theta \times l$$

Si on pose $V$ le vecteur originel et $V'$ le vecteur après propagation, tels que $$V = \begin{pmatrix}y\\ \theta\end{pmatrix},\; V'=\begin{pmatrix}y'\\ \theta'\end{pmatrix}$$ on a : $$V' = \begin{pmatrix}y + dy\\ \theta\end{pmatrix} = \begin{pmatrix}y  + l\times\theta\\ \theta\end{pmatrix}$$

Cette expression va nous permettre de déduire une matrice $M$ telle que $V' = M\cdot V$ :

$$M = \begin{pmatrix}1 & l\\ 0 & 1\end{pmatrix}$$

On remarque que l'angle de propagation ne varie pas lorsque le rayon se propage dans le vide, ce qui est conforme à notre dessin. Il est temps de trouver des matrices plus amusantes.

## Loi de Snell-Descartes et interfaces entre milieux

Jusqu'à maintenant j'ai, dans le but de simplifier, supposé que la lumière se propageait dans le vide. Mais afin de pouvoir altérer son angle de propagation, il est utile de lui faire changer de milieu. Pour rappel, en optique géométrique, on caractérise un milieu par son indice, noté $n$. Ainsi, si l'on considère l'interface entre deux milieux d'indices $n_1$ et $n_2$, un rayon qui se propage en direction de cette interface se verra en partie réfléchi, et en partie transmis (on parle de **réfraction**).

![Schéma réfraction]({attach}matrix_optics/rays/rays_interface.svg)

Comme le laisse deviner mon schéma, la partie réfléchie le sera de l'autre côté de la normale avec le même angle que celui d'arrivée. L'autre partie sera transmise avec un angle $\theta_2$ qui vérifie la relation de Snell-Descartes : $$n_1\sin(\theta_1) = n_2\sin(\theta_2)$$

Nous voulons exprimer la relation entre $V$ le vecteur du rayon avant l'interface et $V'$ le vecteur après l'interface. Dans l'approximation des petits angles, la relation de Snell-Descartes s'écrit $$n_1\cdot\theta_1 = n_2\cdot\theta_2$$
La position du rayon ne changeant pas, la composante $y$ de $V'$ est la même que celle de $V$. On a alors $$V' = \begin{pmatrix}y\\\frac{n_1}{n_2}\theta_1\end{pmatrix}$$

On peut donc en déduire la matrice $M$: $$M = \begin{pmatrix}1 & 0\\ 0 & \frac{n_1}{n_2}\end{pmatrix}$$

## Exercice : combinaison de propagations

Avec les deux matrices que nous avons vu, nous pouvons déjà réaliser un premier exercice !

On dispose d'un objet plongé dans l'eau d'où partent deux rayons $\sigma_1$ et $\sigma_2$. Le but est de calculer $\sigma_1'$ et $\sigma_2'$, les vecteurs rayons qui résultent de leur propagation.

![Schéma de la propagation]({attach}matrix_optics/rays/exo_interface_1.svg)

On pose $$\sigma_1 = \begin{pmatrix}y\\\theta_1\end{pmatrix},\;\sigma_2 = \begin{pmatrix}y\\\theta_2\end{pmatrix}$$

**Données :**

| Grandeur | Valeur | Unité |
| -------- | ------ | ----- |
| $l_1$    | $10$   | cm    |
| $l_2$    | $40$   | cm    |
| $e$      | $3.0$    | mm    |
| $n_0$    | $1.3$    |       |
| $n_1$    | $1.5$    |       |
| $n_2$    | $1.0$    |       |
| $y$      | $5.0$    | cm    |
|$\theta_1$| $0.0$    | rad   |
|$\theta_2$| $1.7\times10^{-1}$    | rad   |

À vos stylos ! il est interdit de regarder la correction sans avoir essayé.

### Correction

La première étape est de déterminer quelles matrices nous allons calculer. On peut découper la propagation en 5 étapes:

1. Propagation dans l'eau;
2. Interface eau-verre;
3. Propagation dans le verre;
4. Propagation dans l'air.

Appelons $P_0$, $P_1$ et $P_2$ les matrices de propagation dans l'eau, dans le verre et dans l'air. Appelons $M_{e/v}$ la matrice représentant l'interface eau-verre et $M_{v/a}$ la matrice représentant l'interface verre-air.

On peut donner directement les expressions des matrices :

\begin{equation}
P_0 = \begin{pmatrix}1 & l_1\\ 0 & 1\end{pmatrix},\;
P_1 = \begin{pmatrix}1 & e\\ 0 & 1\end{pmatrix},\;
P_2 = \begin{pmatrix}1 & l_2\\ 0 & 1\end{pmatrix}\\
M_{e/v} = \begin{pmatrix}1 & 0\\ 0 & \frac{n_0}{n_1}\end{pmatrix},\;
M_{v/a} = \begin{pmatrix}1 & 0\\ 0 & \frac{n_1}{n_2}\end{pmatrix}
\end{equation}

On pourrait calculer étape par étape tous les vecteurs rayons, mais ce n'est pas nécessaire. En effet, on peut remarquer que pour un rayon représenté par un vecteur $\sigma$, les vecteurs engendrés sont

- $\sigma' = P_0 \sigma$;
- $\sigma'' = M_{e/v} \sigma'$;
- $\sigma''' = P_1 \sigma''$;
- $\sigma'''' = M_{v/a} \sigma'''$;
- $\sigma''''' = P_2 \sigma''''$;

En "dépliant" le tout, on remarque qu'il suffit donc de calculer la matrice $M$ telle que $$M = P_2 \cdot M_{v/a} \cdot P_1 \cdot M_{e/v} \cdot P_0$$

Pour éviter de se fatiguer à tout calculer, on peut ici utiliser un logiciel de calcul formel comme [wolfram alpha](https://www.wolframalpha.com/input/?i=%7B%7B1,+l_2%7D,%7B0,+1%7D%7D+*+%7B%7B1,+0%7D,%7B0,+n_1%2Fn_2%7D%7D+*+%7B%7B1,+e%7D,%7B0,+1%7D%7D+*+%7B%7B1,+0%7D,%7B0,+n_0%2Fn_1%7D%7D+*+%7B%7B1,+l_1%7D,%7B0,+1%7D%7D). On obtient alors :

$$
M = \begin{pmatrix}
1 & l_1 + \frac{n_0}{n_1}\left( \frac{n_1}{n_2}l_2 + e \right) \\
0 & \frac{n_0}{n_2}
\end{pmatrix}
$$

On peut remarquer que, à condition que $e$ soit faible devant $\frac{n_1}{n_2}l_2$, on a

$$
M = \begin{pmatrix}
1 & l_1 + \frac{n_0}{n_2}l_2 \\
0 & \frac{n_0}{n_2}
\end{pmatrix} = \begin{pmatrix}1 & l_2\\0 & 1\end{pmatrix}\begin{pmatrix}1 & 0\\0 & \frac{n_0}{n_2}\end{pmatrix}\begin{pmatrix}1 & l_1\\0 & 1\end{pmatrix}
$$

C'est à dire que si l'on a un verre suffisamment fin, on peut ne considérer qu'une interface eau-air.

Pour finir, on peut calculer les vecteurs d'arrivée. Pour cela j'ai réalisé un petit script en Julia:

```julia
l_1 = 10 # cm
l_2 = 40 # cm
e   = 3.0e-1 # cm
n_0 = 1.3
n_1 = 1.5
n_2 = 1.0
y   = 5.0 # cm

θ_1 = 0 # rd
θ_2 = 1.7e-1 #rd


P_0  = [1  l_1; 0   1]
P_1  = [1  e;   0   1]
P_2  = [1  l_2; 0   1]
M_ev = [1  0;   0   n_0/n_1]
M_va = [1  0;   0   n_1/n_2]

M = P_2 * M_va * P_1 * M_ev * P_0
σ_1 = [y; θ_1]
σ_2 = [y; θ_2]

(M*σ_1, M*σ_2)
```

Ce qui nous donne : `([5.0, 0.0], [15.5842, 0.221])`. Comme on pouvait s'y attendre, le rayon qui part perpendiculairement aux interfaces n'est pas dévié. On peut calculer la valeur qu'aurait prise le vecteur si la propagation s'était faite sans changement de matériau :

```julia
julia> [1 l_1+l_2+e; 0 1]*σ_2
2-element Array{Float64,1}:
 13.551
  0.17
```

On voit que le rayon se serait trouvé plus bas. Inversement, pour obtenir un rayon arrivant à 15.5842 cm de haut, il aurait fallu que la source se trouve plus loin. Autrement dit, pour un observateur extérieur, la source semble plus éloignée que ce qu'elle est réellement.

<!-- ## Miroir, ô mon beau miroir

Miroir
Miroir parabolique

## Lentilles

Lentille

## Interface sphérique et prisme

## Exercice : l'œil humain -->
