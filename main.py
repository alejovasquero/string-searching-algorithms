import dash
from dash import dcc
from dash import html

from tests.visualization.data import get_string_search_time


INITIAL_WORD_SIZE = 10000
INITIAL_ALPHABET_SIZE = 40

def main():
    app = dash.Dash()

    word_size = INITIAL_WORD_SIZE
    alphabet_size = INITIAL_ALPHABET_SIZE
    samples = 10

    data = get_string_search_time(samples=samples, length=word_size, alphabet_size=alphabet_size, pattern_size=10)

    x_axis = [0]
    x_index = 0

    booyer_moore = []
    kpm = []
    rabin_karp = []

    booyer_moore.append(data[0].values[0])
    kpm.append(data[1].values[0])
    rabin_karp.append(data[2].values[0])

    app.layout = html.Div([
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 5000,  # in milliseconds
            n_intervals=0
        ),
        html.Div(id='size_output'),
        html.Div(
            dcc.Slider(0, INITIAL_WORD_SIZE*3, 1000,
                id="size_input",
                value=word_size
            )
        ),
        html.Div(
            dcc.Slider(10, 5000, 500,
                value=alphabet_size,
                id="alphabet_size_input",
            )
        )
    ])

    @app.callback(
        dash.dependencies.Output('size_output', 'value'),
        [dash.dependencies.Input('size_input', 'value'),
         dash.dependencies.Input('alphabet_size_input', 'value')])
    def update_output(value1, value2):
        nonlocal word_size
        nonlocal alphabet_size
        word_size = value1
        alphabet_size = value2
        print(value1, value2)
        return 'You have entered {} {}'.format(word_size, alphabet_size)

    @app.callback(dash.dependencies.Output('live-update-graph', 'figure'),
                  dash.dependencies.Input('interval-component', 'n_intervals'))
    def update_data(n):
        data = get_string_search_time(samples=samples, length=word_size, alphabet_size=alphabet_size, pattern_size=10)
        print(f"Calculating data for word size {word_size} and alphabet size {alphabet_size}")
        booyer_moore.append(data[0].values[0])
        kpm.append(data[1].values[0])
        rabin_karp.append(data[2].values[0])
        nonlocal x_index
        x_index += 1
        x_axis.append(x_index + 1)

        return {
            'data': [
                {'x': x_axis, 'y': booyer_moore, 'type': 'scatter', 'name': "Booyer Moore"},
                {'x': x_axis, 'y': kpm, 'type': 'scatter', 'name': "KPM"},
                {'x': x_axis, 'y': rabin_karp, 'type': 'scatter', 'name': "Rabin Karp"}
            ],
            'layout': {'title': 'String search - Time complexity comparison'}

        }

    app.run_server(debug=False)


if __name__ == "__main__":
    main()
