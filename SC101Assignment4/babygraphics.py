"""
File: babygraphics.py
Name: Stanley
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    x1 = GRAPH_MARGIN_SIZE + (CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS)*year_index
    return x1


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # window = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i),
                           CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)

    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 0), 0, get_x_coordinate(CANVAS_WIDTH, 0),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
    #                    text='1900', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 1), 0, get_x_coordinate(CANVAS_WIDTH, 1),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 1) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1910', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 2), 0, get_x_coordinate(CANVAS_WIDTH, 2),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 2) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1920', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 3), 0, get_x_coordinate(CANVAS_WIDTH, 3),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 3) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1930', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 4), 0, get_x_coordinate(CANVAS_WIDTH, 4),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 4) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1940', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 5), 0, get_x_coordinate(CANVAS_WIDTH, 5),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 5) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1950', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 6), 0, get_x_coordinate(CANVAS_WIDTH, 6),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 6) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1960', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 7), 0, get_x_coordinate(CANVAS_WIDTH, 7),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 7) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1970', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 8), 0, get_x_coordinate(CANVAS_WIDTH, 8),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 8) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1980', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 9), 0, get_x_coordinate(CANVAS_WIDTH, 9),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 9) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='1990', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 10), 0, get_x_coordinate(CANVAS_WIDTH, 10),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 10) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='2000', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 11), 0, get_x_coordinate(CANVAS_WIDTH, 11),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 11) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='2010', anchor=tkinter.NW)
    # canvas.create_line(get_x_coordinate(CANVAS_WIDTH, 12), 0, get_x_coordinate(CANVAS_WIDTH, 12),
    #                    CANVAS_HEIGHT, width=LINE_WIDTH)
    # canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 12) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
    #                    text='2020', anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    name_count = 0
    rate = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000
    for name in lookup_names:
        color_index = name_count % 4    # 用取餘數來區分顏色輪迴
        name_count += 1
        for i in range(len(YEARS)-1):
            if str(YEARS[i]) in name_data[name]:
                x1 = get_x_coordinate(CANVAS_WIDTH, i)
                y1 = rate * int(name_data[name][str(YEARS[i])]) + GRAPH_MARGIN_SIZE
                x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)
                y2 = rate * int(name_data[name][str(YEARS[i + 1])]) + GRAPH_MARGIN_SIZE
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_index])
            else:
                x1 = get_x_coordinate(CANVAS_WIDTH, i)
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                if str(YEARS[i+1]) not in name_data[name]:
                    x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_index])
                else:
                    x2 = get_x_coordinate(CANVAS_WIDTH, i + 1)
                    y2 = rate * int(name_data[name][str(YEARS[i + 1])]) + GRAPH_MARGIN_SIZE
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_index])
        for c in range(len(YEARS)):
            if str(YEARS[c]) in name_data[name]:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, c) + TEXT_DX,
                                   rate * int(name_data[name][str(YEARS[c])]) + GRAPH_MARGIN_SIZE,
                                   text=name + name_data[name][str(YEARS[c])], anchor=tkinter.SW,
                                   fill=COLORS[color_index])
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, c) + TEXT_DX,
                                   CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=name + '*', anchor=tkinter.SW,
                                   fill=COLORS[color_index])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
