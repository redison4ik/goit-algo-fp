import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

   
    current_pos = t.pos()
    current_heading = t.heading()

    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.penup()
    t.setpos(current_pos)
    t.setheading(current_heading)
    t.pendown()

    t.right(45)
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.penup()
    t.setpos(current_pos)
    t.setheading(current_heading)
    t.pendown()

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, 100, level)

    turtle.done()

if __name__ == "__main__":
    main()
