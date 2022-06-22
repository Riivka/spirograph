import PySimpleGUI as sg
from spirograph import Spiro



GRAPH_SIZE = (500, 500)
DATA_SIZE = (500, 500)

SIZE_X = GRAPH_SIZE[0]//2
SIZE_Y = GRAPH_SIZE[1]//2

graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE, key='-GRAPH-', background_color='white',)

layout = [[sg.Text('enter radius....')],
          [graph],
          [sg.Button('draw')]]
window = sg.Window(title="spirograph", layout=layout)


while True:
     
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event is None:
        break
    if event == 'draw':
        is_animated = False
        graph.erase()

        #draw_axis()
        spirog = Spiro(200, 170, 0.6, SIZE_X, SIZE_Y)
        plot = spirog.draw()
        prev_x, prev_y = None, None
        for x,y in plot:
            if prev_x is not None:
                graph.draw_line((prev_x, prev_y), (x, y), color='red')
            prev_x, prev_y = x, y
    if event == sg.WIN_CLOSED:
        break
    if event is None:
        break

window.close()
