# '''
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.
# '''
from graphics import Canvas


# Create a canvas object with a width and height of 400 pixels
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT:int = 400

CELL_SIZE: int = 40
ERASER_SIZE: int = 40


def erase_objects(canvas, eraser):
    """Erase the objects on the canvas that are in contact with the eraser."""
    
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')



def main():
    print("Welcome to our App :)")
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    num_rows: int = CANVAS_HEIGHT // CELL_SIZE
    num_cols: int = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()

    eraser = canvas.create_rectangle(
        last_click_x,
        last_click_y,
        last_click_x + ERASER_SIZE,
        last_click_y + ERASER_SIZE,
        'red'
    )

    # New function to update eraser and erase objects
    def update():
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        canvas.root.after(50, update)  # 50 ms baad dubara call

    update()  # Start the loop
    canvas.root.mainloop()  # Important! GUI event loop

if __name__ == '__main__':
    main()