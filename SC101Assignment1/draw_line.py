"""
File: draw_line
Name: 黃方易
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 15
window = GWindow()
count = 0
x = 0
y = 0
x2 = 0
y2 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # global count, x, y
    onmouseclicked(create)
    # if count % 2 == 0:
    #     hole = GOval(SIZE, SIZE, x, y)
    #     window.add(hole)
    # else:
    #     hole = window.get_object_at(x, y)
    #     window.remove(hole)
    #     line = GLine(x, y, x2, y2)
    #     window.add(line)


def create(mouse):  # 只會收到xy
    global count, x, y, x2, y2
    if count % 2 == 0:
        # x = mouse.x    # 為何不會刪除
        # y = mouse.y
        x = mouse.x + SIZE // 2
        y = mouse.y + SIZE // 2
        hole = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
        window.add(hole)
        count += 1
    else:
        x2 = mouse.x
        y2 = mouse.y
        hole = window.get_object_at(x, y)
        window.remove(hole)
        line = GLine(x, y, x2, y2)
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
