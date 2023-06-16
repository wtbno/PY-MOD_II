import dash
import plotly.express as px
from dash import dcc
from dash import html

# Resto do código...


# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Definir os dados
dados = {
    'Categorias': ['A', 'B', 'C', 'D'],
    'Valores': [20, 14, 23, 25]
}

# Layout do dashboard
app.layout = html.Div(
    children=[
        html.H1("Dashboard em Python"),
        dcc.Graph(
            figure=px.bar(dados, x='Categorias', y='Valores',
                          title='Gráfico de Barras')
        ),
        dcc.Graph(
            figure=px.pie(dados, values='Valores',
                          names='Categorias', title='Gráfico de Pizza')
        )
    ]
)

# Executar o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
