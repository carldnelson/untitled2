import PySimpleGUI as sg

column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
           [sg.Text('Director'), sg.Spin(values=('0', '1', '2', '3'), initial_value='0',enable_events=True, key='_Director_'), ],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [[sg.Text('Stopwatch', size=(20, 2), justification='center')],
          [sg.Text('', size=(10, 2), font=('Helvetica', 20), justification='center', key='_OUTPUT_')],
          [sg.Column(column1, background_color='#F7F3EC')],
          [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

window = sg.Window('Stopwatch Timer', layout)

# who is in the meeting this list gets updated via the buttons
Team = ['Team']

# minute rate for each level
Rate = {'CEO': 100, 'Director': 50, 'Manager': 35, 'Supervisor': 25, 'Coordinator': 15, 'Team': 9}

# sum up the current cost
cost = sum([Rate[x] for x in Team])

while True:  # Event Loop
    event, values = window.Read(timeout=100)  # Please try and use as high of a timeout value as you can
    if event is None or event == 'Quit':  # if user closed the window using X or clicked Quit button
        break
    elif event == '_Director_':
        Team.append('Director')

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values,
         'Team is "{}"'.format(Team))
