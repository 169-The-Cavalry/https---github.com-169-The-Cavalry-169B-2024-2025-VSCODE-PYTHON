
# Clear the screen and set pen color
brain.screen.clear_screen()
brain.screen.set_pen_color(Color.WHITE)

# Draw "169" using rectangles & circles
brain.screen.draw_rectangle(20, 50, 20, 50)  # "1" (Vertical line)
brain.screen.draw_circle(80, 75, 25)         # "6" (Circle)
brain.screen.draw_rectangle(105, 50, 20, 50)  # "9" (Straight part)
brain.screen.draw_circle(115, 75, 25)         # "9" (Circle)

# Draw "B" using rectangles & arcs
brain.screen.draw_rectangle(160, 50, 20, 50)  # Straight part of "B"
brain.screen.draw_circle(170, 65, 15)         # Top curve of "B"
brain.screen.draw_circle(170, 85, 15)         # Bottom curve of "B"

# Keep display on
while True:
    wait(1, SECONDS)