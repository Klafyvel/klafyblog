Title: Matrices et optique géométrique #2
Date: 2019-08-11 10:00
Category: Optics
Tags: french, optics
Status: published

Dans [le dernier article]({filename}/2019/07/matrix_optics.md) nous avons introduit moult concepts un petit peu théoriques. Dans ce deuxième article je vous propose de mettre un peu en pratique tout cela afin de donner une application pratique à nos matrices : se débarrasser des formules de conjugaisons pour les lentilles minces.

# La racine du mal

Si vous avez suivi une première S, un des principaux système optique utilisé est la lentille mince.

![Lentille mince converente]({attach}matrix_optics/lense.svg)

Ici j'ai représenté une lentille mince convergente. On la caractérise par une dimension : sa distance focale, notée $f'$ et qui est égale à la distance $\overline{OF'}$ (la barre indique qu'il s'agit d'une distance orientée, ici positive si on se déplace dans le sens des $x$ croissants).

Toujours si vous avez suivi une première S, il y a de grandes chances que l'on vous ait donné cette fameuse formule de conjugaison :

$$
\frac{1}{\overline{OA'}} - \frac{1}{\overline{OA}} = V = \frac{1}{f'}
$$

Ou encore, si vous êtes passés par la case prépa,

$$
\overline{F'A'}\cdot\overline{FA} = f \cdot f'
$$

Et il est très probable que vous vous soyez lamentablement trompés en tentant de les appliquer en mélangeant les $'$.

Avant de continuer, petit rappel pour celles et ceux qui se sont accidentellement endormis contre le radiateur quand ces formules sont passées au tableau.

Tout d'abord qu'est-ce que ces histoires de $'$ ? Il s'agit d'une convention : le prime indique que l'on parle d'un point image. Son absence indique que l'on parle d'un point objet. Un objet est un point d'intersection des rayons incidents. Une image est un point d'intersection des rayons qui sortent du système optique.

Le point $O$ indique le centre de la lentille, $F$ son foyer objet et $F'$ son foyer image. La lentille mince possède trois propriétés intéressantes :

  1. Un rayon qui passe par $O$ n'est pas dévié;
  2. Un rayon qui passe par $F$ sort de la lentille parallèle à l'axe optique;
  3. Un rayon qui est parallèle à l'axe optique sort sur une trajectoire passant par $F'$.

Les dernières variables qui n'ont pas été explicitées sont $A$ et $A'$. Il s'agit respectivement d'un point quelconque et de son image. En effet, on suppose que les lentilles (et la plupart des systèmes optiques que l'on étudie) sont stigmatiques (l'image d'un point est un point, c'est à dire que tous les rayons émergents se croisent au même endroit) et aplanétiques (deux objets sur le même plan donnent des images sur un même plan).

![Image d'un point à travers une lentille mince]({attach}matrix_optics/lense_ray.svg)

Le schéma précédent résume les propriétés que nous avons énuméré. Les formules de conjugaisons permettent de lier la position des points $A$ et $A'$ grâce aux caractéristiques de la lentille. On pourra ensuite lier les positions des points $B$ et $B'$ avec la relation de grandissement, (oh, tiens, une autre formule à apprendre)

$$
\gamma = \frac{\overline{A'B'}}{\overline{AB}} = \frac{\overline{OA'}}{\overline{OA}}
$$

Je pense qu'arrivés à ce stade, si vous me ressemblez un peu, vous aimeriez ne pas avoir à retenir ces formules. Pourquoi ne pas tenter d'utiliser nos matrices optiques ? (oui je sais, vous ne vous y attendiez pas)

# Les matrices à la rescousse

Nous avons donc quatre paramètres à déterminer pour obtenir notre matrice. La première chose à remarquer est qu'un rayon $$V = \begin{pmatrix}
y \\
\theta
\end{pmatrix}$$ ne change pas de hauteur lorsqu'il traverse une lentille. C'est une bonne chose pour nous : cela signifie que nous avons déjà fait la moitié du travail, la première ligne de la matrice est simplement $(1, 0)$. On cherche donc la matrice $M$ telle que

\begin{equation}
M = \begin{pmatrix}
  1 & 0 \\
  c & d
\end{pmatrix}
\end{equation}

Enfin, on appelle $$V' = \begin{pmatrix}
y' \\
\theta'
\end{pmatrix}$$

le vecteur en sortie de la lentille.

Nous allons maintenant appliquer nos trois propriétés pour en déduire $c$ et $d$.

## Un rayon qui passe par $O$

Dans ce cas, le vecteur $V$ s'écrit $$\begin{pmatrix}
0 \\
\theta
\end{pmatrix}$$

Puisqu'il n'est pas dévié, $$V' = \begin{pmatrix}
0 \\
\theta
\end{pmatrix}$$

or $$V' = M\cdot V = \begin{pmatrix}
0 \\
c \times 0 + d \times \theta
\end{pmatrix}$$

On a donc facilement $$d = 1$$

## Un rayon qui passe par $F$

On suppose que $y\neq 0$. Dans ce cas, le rayon en sortie est parallèle à l'axe optique, donc $$V' = \begin{pmatrix}
y \\
0
\end{pmatrix}$$
avec $$V = \begin{pmatrix}
y \\
θ
\end{pmatrix}$$

On a donc :
$$V' = M\cdot V = \begin{pmatrix}
y \\
c \times y + 1 \times \theta
\end{pmatrix} = \begin{pmatrix}
y \\
0
\end{pmatrix}$$

Plus précisément :
\begin{equation}
0 = c\times y + θ \\
c = - \frac{θ}{y}
\end{equation}

Il nous reste à évaluer le rapport $\frac{θ}{y}$. Si on appelle $E$ le point sur la lentille où le rayon arrive, on a $\theta = \widehat{OFE}$, donc $$\tan \theta = \frac{\overline{OE}}{\overline{FO}} = \frac{y}{f'}$$

On a donc, dans l'approximation des petits angles, $$c = -\frac{1}{f'}$$

On a donc \begin{equation}
M = \begin{pmatrix}
  1 & 0 \\
  -\frac{1}{f'} & 1
\end{pmatrix}
\end{equation}

## Un rayon parallèle à l'axe optique

Nous pouvons vérifier qu'un rayon parallèle à l'axe optique passe par le point $F'$. Il suffit d'évaluer le vecteur rayon après son passage dans la lentille et un parcours de distance $f'$.

\begin{eqnarray}
V' &=&  \begin{pmatrix}1 & f'\\ 0 & 1\end{pmatrix} \cdot \begin{pmatrix}
  1 & 0 \\
  -\frac{1}{f'} & 1
\end{pmatrix} \cdot \begin{pmatrix}
y \\
0
\end{pmatrix} \\
&=& \begin{pmatrix}1 & f'\\ 0 & 1\end{pmatrix} \cdot \begin{pmatrix}
y \\
0 - \frac{y}{f'}
\end{pmatrix} \\
&=& \begin{pmatrix}
y - f' \times \frac{y}{f'}\\
-\frac{y}{f'}
\end{pmatrix}\\
&=& \begin{pmatrix}
0\\
-\frac{y}{f'}
\end{pmatrix}
\end{eqnarray}

Bonne nouvelle, notre matrice respecte les trois propriétés des lentilles minces.

# Un petit exercice

À venir...
