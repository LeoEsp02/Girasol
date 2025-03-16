# Librerías para crear arte y jugar con las matemáticas
import turtle
import math
 
# Configuración del lienzo donde nacerá nuestro girasol
screen = turtle.Screen()

# La tortuguita artista
t = turtle.Turtle()
t.speed(10)  # La velocidad de la luz... o casi

# El pincel mágico
t.pensize(8)
t.color("orange", "yellow")  # Colores soleados

# Función para dibujar un pétalo (porque los girasoles no se dibujan solos, ¿verdad?)
def petal():
    t.begin_fill()
    t.circle(100, 60)  # Curva aquí, curva allá
    t.left(120)  # Vueltita para el otro lado
    t.circle(100, 60)  # Otro pétalo listo
    t.left(120)
    t.end_fill()

# Dibuja 12 pétalos, uno para cada mes que brillas en mi vida
for _ in range(12):
    petal()
    t.left(30)

# El centro del girasol, como el corazón de quien lo recibe
t.penup()
t.goto(0, -40)
t.pendown()
t.color("brown")
t.begin_fill()
t.circle(40)
t.end_fill()

# Un mensajito del corazón
t.penup()
t.goto(-100, -150)
t.color("black")
t.write("Un sol, para mi sol", font=("Arial", 16, "bold"))
t.hideturtle()

# Mantener el regalo abierto
screen.mainloop()

#Si encuentras este codigo, compartelo con alguien que sea tu sol tambien
