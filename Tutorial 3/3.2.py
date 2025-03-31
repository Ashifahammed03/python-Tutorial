import turtle

def draw_pentagon():
    t = turtle.Turtle()
    for _ in range(5):
        t.forward(100)
        t.right(72)
    turtle.done()