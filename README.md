# Mandelbrot Image Generator
Mandelbrot Image Generator este un script folosit pentru generarea de imagini a fractalilor de tip mandelbrot.
# Instalare
Folositi packet manager-ul pip pentru a instala librariile  PIL(pillow), progressbar2, numpy
```bash
pip install pillow progressbar2 numpy
```
# Utilizare
Fisierul ***mandelbrot.py*** trebuie descarcat si inclus in fisierul principal de python (daca mandelbrot.py nu se afla in acelasi directory cu fisierul principal, va trebui specificat path-ul in  momentul in care se importa).
In continuare, prin apelarea functiei **buildFractal** vom putea genera imaginea.
```py
buildFractal(min_x, max_x, min_y, max_y, width, height, max_iterations, filename = "mandelbrot")
//min_x, min_y, max_x, max_y - coordonatele graficului care va fi reprezentat in imaginea generata
//width, height - dimensiunile imaginii
//max_iterations - iteratiile care vor fi facute pe numerele complexe reprezentate de coordonatele (x,y) (iteratii mai multe => fractal mai precis)
//filename - numele fisierului ".png" care va fi salvat in acelasi directory cu fisierul principal. Daca nu este furnizat niciun parametru filename, acesta va fi default "mandelbrot"
```
# Exemplu
```py
import mandelbrot

mandelbrot.buildFractal(-3, 2, -2.5, 2.5, 4042, 4024, 100)
```
# Imaginea generata:
![](https://github.com/Albert24GG/mandelbrot-image-generator/blob/ba09bfa7efc58dd7642435ec7db94c682441dbbf/mandelbrot.png)
