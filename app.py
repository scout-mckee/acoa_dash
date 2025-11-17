import dash
from dash import html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.Img(src="/assets/image1.png", style={"width": "100%", "margin-bottom": "20px"}),
        html.Img(src="/assets/image2.png", style={"width": "100%", "margin-bottom": "20px"}),
        html.Img(src="/assets/image3.png", style={"width": "100%", "margin-bottom": "20px"}),
    ],
    style={"display": "flex", "flexDirection": "column", "alignItems": "center"}
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)

