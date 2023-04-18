import pandas as pd
import plotly.express as px

#import functions

import datetime
import numpy as np
from flask import Flask, jsonify
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

dataset = 'analytics-sales-rawdata-202302.csv'

data = (pd.read_csv(dataset, thousands = ',').query("사업부코드 == 10.0 and 년월 == 202301"))
data = data[data['RX 총Net매출(VAT제외)']!=0].sort_values(by='년월')


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "의원사업부 매출 현황"

fig = px.treemap(data, path=[px.Constant("의원사업부 수도6"), '품목군명', '품목명'], values='RX 총Net매출(VAT제외)',
                  color='RX 총Net매출(VAT제외)', hover_data=['품목명'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(data['품목단가'], weights=data['RX 총Net매출(VAT제외)']))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig1 = px.treemap(data, path=[px.Constant("의원사업부 수도6"), '품목군명', '거래처명'], values='RX 총Net매출(VAT제외)',
                  color='RX 총Net매출(VAT제외)', hover_data=['담당자명'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(data['품목단가'], weights=data['RX 총Net매출(VAT제외)']))
fig1.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig2 = px.treemap(data, path=[px.Constant("의원사업부 수도6"), '품목군명', '담당자명'], values='RX 총Net매출(VAT제외)',
                  color='RX 총Net매출(VAT제외)', hover_data=['품목군코드'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(data['품목단가'], weights=data['RX 총Net매출(VAT제외)']))
fig2.update_layout(margin = dict(t=50, l=25, r=25, b=25))

app.layout = html.Div(
    children=[


        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="데이터 관리", className="header-title"
                ),
                html.P(
                    children=(
                        "의원사업부"
                        " 수도6"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        dcc.Graph(
            id="graph",
            figure=fig
        ),
        dcc.Graph(
            id="graph1",
            figure=fig1
        ),
        dcc.Graph(
            id="graph2",
            figure=fig2
        ),
        # html.Div(
        #     children=[
        #         html.Div(
        #             children=dcc.Graph(
        #                 id="price-chart",
        #                 config={"displayModeBar": False},
        #                 figure={
        #                     "data": [
        #                         {
        #                             "x": data["년월"],
        #                             "y": data["RX 총Net매출(VAT제외)"],
        #                             "type": "lines",
        #                             "hovertemplate": (
        #                                 "$%{y:.2f}<extra></extra>"
        #                             ),
        #                         },
        #                     ],
        #                     "layout": {
        #                         "title": {
        #                             "text": "Average Price of Avocados",
        #                             "x": 0.05,
        #                             "xanchor": "left",
        #                         },
        #                         "xaxis": {"fixedrange": True},
        #                         "yaxis": {
        #                             "tickprefix": "$",
        #                             "fixedrange": True,
        #                         },
        #                         "colorway": ["#17b897"],
        #                     },
        #                 },
        #             ),
        #             className="card",
        #         ),
        #         html.Div(
        #             children=dcc.Graph(
        #                 id="volume-chart",
        #                 config={"displayModeBar": False},
        #                 figure={
        #                     "data": [
        #                         {
        #                             "x": data["년월"],
        #                             "y": data["RX 총Net매출(VAT제외)"],
        #                             "type": "lines",
        #                         },
        #                     ],
        #                     "layout": {
        #                         "title": {
        #                             "text": "Avocados Sold",
        #                             "x": 0.05,
        #                             "xanchor": "left",
        #                         },
        #                         "xaxis": {"fixedrange": True},
        #                         "yaxis": {"fixedrange": True},
        #                         "colorway": ["#E12D39"],
        #                     },
        #                 },
        #             ),
        #             className="card",
        #         ),
        #     ],
        #     className="wrapper",
        # ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
