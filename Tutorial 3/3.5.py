import turtle

def draw_radial_hexagons():
    t = turtle.Turtle()
    def draw_hexagon():
        for _ in range(6):
            t.forward(50)
            t.right(60)
    for _ in range(10):
        draw_hexagon()
        t.right(36)
    turtle.done()