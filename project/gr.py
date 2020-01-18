import turtle as t
t.getscreen()
t.bgcolor("pink")
t.ht()
t.color("white")
t.write("NMIT ASFF",move='False',align="center",font=("Bazooka",30,'bold','underline'))

painter = t.Turtle()
painter.pencolor('white')
painter.setx(120)
painter.speed(10)

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
painter.ht()
    
t.done()
