"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Hunter Hicks.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

stephano = rg.SimpleTurtle('turtle')
stephano.speed = 15
stephano.pen = rg.Pen('black', 5)
stephano.pen_down()
size = 150

for k in range(15):

    stephano.draw_circle(size)
    stephano.pen_up()
    stephano.right(45)
    stephano.forward(20)
    stephano.left(45)

    stephano.pen_down()
    size = size - 12

andrea = rg.SimpleTurtle('turtle')
andrea.speed = 50
andrea.pen = rg.Pen('green', 3)
andrea.pen_down()
size2 = 100
rotate = 45
rotate2 = 45
for k in range(30):

    andrea.draw_regular_polygon(12, size2)
    andrea.right(rotate)
    andrea.forward(10)
    andrea.left(45)

    andrea.pen_down()
    rotate = rotate - 2
    rotate2 = rotate2 +4

window.close_on_mouse_click()