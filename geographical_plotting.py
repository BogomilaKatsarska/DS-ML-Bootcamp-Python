{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "initial_id",
   "metadata": {
    "collapsed": true,
    "ExecuteTime": {
     "end_time": "2024-07-12T08:13:25.777906Z",
     "start_time": "2024-07-12T08:13:25.698118Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": "        <script type=\"text/javascript\">\n        window.PlotlyConfig = {MathJaxConfig: 'local'};\n        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n        if (typeof require !== 'undefined') {\n        require.undef(\"plotly\");\n        requirejs.config({\n            paths: {\n                'plotly': ['https://cdn.plot.ly/plotly-2.32.0.min']\n            }\n        });\n        require(['plotly'], function(Plotly) {\n            window._Plotly = Plotly;\n        });\n        }\n        </script>\n        "
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "data": [
        {
         "colorbar": {
          "title": {
           "text": "Colorbar Title Goes Here"
          }
         },
         "colorscale": [
          [
           0.0,
           "rgb(247,252,245)"
          ],
          [
           0.125,
           "rgb(229,245,224)"
          ],
          [
           0.25,
           "rgb(199,233,192)"
          ],
          [
           0.375,
           "rgb(161,217,155)"
          ],
          [
           0.5,
           "rgb(116,196,118)"
          ],
          [
           0.625,
           "rgb(65,171,93)"
          ],
          [
           0.75,
           "rgb(35,139,69)"
          ],
          [
           0.875,
           "rgb(0,109,44)"
          ],
          [
           1.0,
           "rgb(0,68,27)"
          ]
         ],
         "locationmode": "USA-states",
         "locations": [
          "AZ",
          "CA",
          "NY",
          "FL"
         ],
         "text": [
          "Arizona",
          "Cali",
          "New York",
          "Pinellas Park"
         ],
         "z": [
          1.0,
          2.0,
          3.0,
          4.0
         ],
         "type": "choropleth"
        }
       ],
       "layout": {
        "geo": {
         "scope": "usa"
        },
        "template": {
         "data": {
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "bar": [
           {
            "error_x": {
             "color": "#f2f5fa"
            },
            "error_y": {
             "color": "#f2f5fa"
            },
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "baxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scatter"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#506784"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "header": {
             "fill": {
              "color": "#2a3f5f"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#f2f5fa",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#f2f5fa"
          },
          "geo": {
           "bgcolor": "rgb(17,17,17)",
           "lakecolor": "rgb(17,17,17)",
           "landcolor": "rgb(17,17,17)",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#506784"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "dark"
          },
          "paper_bgcolor": "rgb(17,17,17)",
          "plot_bgcolor": "rgb(17,17,17)",
          "polar": {
           "angularaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "radialaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "yaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "zaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#f2f5fa"
           }
          },
          "sliderdefaults": {
           "bgcolor": "#C8D4E3",
           "bordercolor": "rgb(17,17,17)",
           "borderwidth": 1,
           "tickwidth": 0
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "caxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "updatemenudefaults": {
           "bgcolor": "#506784",
           "borderwidth": 0
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          }
         }
        }
       },
       "config": {
        "showLink": false,
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly"
       }
      },
      "text/html": "<div>                            <div id=\"3677719d-ecc1-464a-9953-318f12dca22f\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"3677719d-ecc1-464a-9953-318f12dca22f\")) {                    Plotly.newPlot(                        \"3677719d-ecc1-464a-9953-318f12dca22f\",                        [{\"colorbar\":{\"title\":{\"text\":\"Colorbar Title Goes Here\"}},\"colorscale\":[[0.0,\"rgb(247,252,245)\"],[0.125,\"rgb(229,245,224)\"],[0.25,\"rgb(199,233,192)\"],[0.375,\"rgb(161,217,155)\"],[0.5,\"rgb(116,196,118)\"],[0.625,\"rgb(65,171,93)\"],[0.75,\"rgb(35,139,69)\"],[0.875,\"rgb(0,109,44)\"],[1.0,\"rgb(0,68,27)\"]],\"locationmode\":\"USA-states\",\"locations\":[\"AZ\",\"CA\",\"NY\",\"FL\"],\"text\":[\"Arizona\",\"Cali\",\"New York\",\"Pinellas Park\"],\"z\":[1.0,2.0,3.0,4.0],\"type\":\"choropleth\"}],                        {\"geo\":{\"scope\":\"usa\"},\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#f2f5fa\"},\"error_y\":{\"color\":\"#f2f5fa\"},\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"baxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#506784\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"header\":{\"fill\":{\"color\":\"#2a3f5f\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#f2f5fa\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#f2f5fa\"},\"geo\":{\"bgcolor\":\"rgb(17,17,17)\",\"lakecolor\":\"rgb(17,17,17)\",\"landcolor\":\"rgb(17,17,17)\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"#506784\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"dark\"},\"paper_bgcolor\":\"rgb(17,17,17)\",\"plot_bgcolor\":\"rgb(17,17,17)\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"radialaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"yaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"zaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"}},\"shapedefaults\":{\"line\":{\"color\":\"#f2f5fa\"}},\"sliderdefaults\":{\"bgcolor\":\"#C8D4E3\",\"bordercolor\":\"rgb(17,17,17)\",\"borderwidth\":1,\"tickwidth\":0},\"ternary\":{\"aaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"caxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"updatemenudefaults\":{\"bgcolor\":\"#506784\",\"borderwidth\":0},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2}}}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('3677719d-ecc1-464a-9953-318f12dca22f');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.graph_objects as go\n",
    "from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot\n",
    "import pandas as pd\n",
    "\n",
    "init_notebook_mode(connected=True)\n",
    "data = dict(\n",
    "    type = 'choropleth', \n",
    "    locations = ['AZ', 'CA', 'NY', 'FL'],\n",
    "    locationmode = 'USA-states',\n",
    "    colorscale = 'Greens',\n",
    "    text = ['Arizona', 'Cali', 'New York', 'Pinellas Park'],\n",
    "    z = [1.0, 2.0, 3.0, 4.0],\n",
    "    colorbar = {\n",
    "        'title': 'Colorbar Title Goes Here',\n",
    "    }\n",
    ")\n",
    "layout = dict(\n",
    "    geo = {\n",
    "        'scope': 'usa',\n",
    "    }\n",
    ")\n",
    "choromap = go.Figure(data = [data], layout = layout)\n",
    "iplot(choromap)"
   ]
  },
  {
   "cell_type": "code",
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "data": [
        {
         "colorbar": {
          "title": {
           "text": "Millions USD"
          }
         },
         "colorscale": [
          [
           0.0,
           "rgb(247,252,245)"
          ],
          [
           0.125,
           "rgb(229,245,224)"
          ],
          [
           0.25,
           "rgb(199,233,192)"
          ],
          [
           0.375,
           "rgb(161,217,155)"
          ],
          [
           0.5,
           "rgb(116,196,118)"
          ],
          [
           0.625,
           "rgb(65,171,93)"
          ],
          [
           0.75,
           "rgb(35,139,69)"
          ],
          [
           0.875,
           "rgb(0,109,44)"
          ],
          [
           1.0,
           "rgb(0,68,27)"
          ]
         ],
         "locationmode": "USA-states",
         "locations": [
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"
         ],
         "marker": {
          "line": {
           "color": "rgb(255, 255, 255)",
           "width": 2
          }
         },
         "text": [
          "Alabama<br>Beef 34.4 Dairy 4.06<br>Fruits 25.11 Veggies 14.33<br>Wheat 70.0 Corn 34.9",
          "Alaska<br>Beef 0.2 Dairy 0.19<br>Fruits 0.0 Veggies 1.56<br>Wheat 0.0 Corn 0.0",
          "Arizona<br>Beef 71.3 Dairy 105.48<br>Fruits 60.27 Veggies 386.91<br>Wheat 48.7 Corn 7.3",
          "Arkansas<br>Beef 53.2 Dairy 3.53<br>Fruits 6.88 Veggies 11.45<br>Wheat 114.5 Corn 69.5",
          " California<br>Beef 228.7 Dairy 929.95<br>Fruits 8736.4 Veggies 2106.79<br>Wheat 249.3 Corn 34.6",
          "Colorado<br>Beef 261.4 Dairy 71.94<br>Fruits 17.99 Veggies 118.27<br>Wheat 400.5 Corn 183.2",
          "Connecticut<br>Beef 1.1 Dairy 9.49<br>Fruits 13.1 Veggies 11.16<br>Wheat 0.0 Corn 0.0",
          "Delaware<br>Beef 0.4 Dairy 2.3<br>Fruits 1.53 Veggies 20.03<br>Wheat 22.9 Corn 26.9",
          "Florida<br>Beef 42.6 Dairy 66.31<br>Fruits 1371.36 Veggies 450.86<br>Wheat 1.8 Corn 3.5",
          "Georgia<br>Beef 31.0 Dairy 38.38<br>Fruits 233.51 Veggies 154.77<br>Wheat 65.4 Corn 57.8",
          "Hawaii<br>Beef 4.0 Dairy 1.16<br>Fruits 55.51 Veggies 24.83<br>Wheat 0.0 Corn 0.0",
          "Idaho<br>Beef 119.8 Dairy 294.6<br>Fruits 21.64 Veggies 319.19<br>Wheat 568.2 Corn 24.0",
          "Illinois<br>Beef 53.7 Dairy 45.82<br>Fruits 12.53 Veggies 39.95<br>Wheat 223.8 Corn 2228.5",
          "Indiana<br>Beef 21.9 Dairy 89.7<br>Fruits 12.98 Veggies 37.89<br>Wheat 114.0 Corn 1123.2",
          "Iowa<br>Beef 289.8 Dairy 107.0<br>Fruits 3.24 Veggies 7.1<br>Wheat 3.1 Corn 2529.8",
          "Kansas<br>Beef 659.3 Dairy 65.45<br>Fruits 3.11 Veggies 9.32<br>Wheat 1426.5 Corn 457.3",
          "Kentucky<br>Beef 54.8 Dairy 28.27<br>Fruits 6.6 Veggies 0.0<br>Wheat 149.3 Corn 179.1",
          "Louisiana<br>Beef 19.8 Dairy 6.02<br>Fruits 17.83 Veggies 17.25<br>Wheat 78.7 Corn 91.4",
          "Maine<br>Beef 1.4 Dairy 16.18<br>Fruits 52.01 Veggies 62.9<br>Wheat 0.0 Corn 0.0",
          "Maryland<br>Beef 5.6 Dairy 24.81<br>Fruits 12.9 Veggies 20.43<br>Wheat 55.8 Corn 54.1",
          "Massachusetts<br>Beef 0.6 Dairy 5.81<br>Fruits 80.83 Veggies 21.13<br>Wheat 0.0 Corn 0.0",
          "Michigan<br>Beef 37.7 Dairy 214.82<br>Fruits 257.69 Veggies 189.96<br>Wheat 247.0 Corn 381.5",
          "Minnesota<br>Beef 112.3 Dairy 218.05<br>Fruits 7.91 Veggies 120.37<br>Wheat 538.1 Corn 1264.3",
          "Mississippi<br>Beef 12.8 Dairy 5.45<br>Fruits 17.04 Veggies 27.87<br>Wheat 102.2 Corn 110.0",
          "Missouri<br>Beef 137.2 Dairy 34.26<br>Fruits 13.18 Veggies 17.9<br>Wheat 161.7 Corn 428.8",
          "Montana<br>Beef 105.0 Dairy 6.82<br>Fruits 3.3 Veggies 45.27<br>Wheat 1198.1 Corn 5.4",
          "Nebraska<br>Beef 762.2 Dairy 30.07<br>Fruits 2.16 Veggies 53.5<br>Wheat 292.3 Corn 1735.9",
          "Nevada<br>Beef 21.8 Dairy 16.57<br>Fruits 1.19 Veggies 27.93<br>Wheat 5.4 Corn 0.0",
          "New Hampshire<br>Beef 0.6 Dairy 7.46<br>Fruits 7.98 Veggies 4.5<br>Wheat 0.0 Corn 0.0",
          "New Jersey<br>Beef 0.8 Dairy 3.37<br>Fruits 109.45 Veggies 56.54<br>Wheat 6.7 Corn 10.1",
          "New Mexico<br>Beef 117.2 Dairy 191.01<br>Fruits 101.9 Veggies 43.88<br>Wheat 13.9 Corn 11.2",
          "New York<br>Beef 22.2 Dairy 331.8<br>Fruits 202.56 Veggies 143.37<br>Wheat 29.9 Corn 106.1",
          "North Carolina<br>Beef 24.8 Dairy 24.9<br>Fruits 74.47 Veggies 150.45<br>Wheat 200.3 Corn 92.2",
          "North Dakota<br>Beef 78.5 Dairy 8.14<br>Fruits 0.25 Veggies 130.79<br>Wheat 1664.5 Corn 236.1",
          "Ohio<br>Beef 36.2 Dairy 134.57<br>Fruits 27.21 Veggies 53.53<br>Wheat 207.4 Corn 535.1",
          "Oklahoma<br>Beef 337.6 Dairy 24.35<br>Fruits 9.24 Veggies 8.9<br>Wheat 324.8 Corn 27.5",
          "Oregon<br>Beef 58.8 Dairy 63.66<br>Fruits 315.04 Veggies 126.5<br>Wheat 320.3 Corn 11.7",
          "Pennsylvania<br>Beef 50.9 Dairy 280.87<br>Fruits 89.48 Veggies 38.26<br>Wheat 41.0 Corn 112.1",
          "Rhode Island<br>Beef 0.1 Dairy 0.52<br>Fruits 2.83 Veggies 3.02<br>Wheat 0.0 Corn 0.0",
          "South Carolina<br>Beef 15.2 Dairy 7.62<br>Fruits 53.45 Veggies 42.66<br>Wheat 55.3 Corn 32.1",
          "South Dakota<br>Beef 193.5 Dairy 46.77<br>Fruits 0.8 Veggies 4.06<br>Wheat 704.5 Corn 643.6",
          "Tennessee<br>Beef 51.1 Dairy 21.18<br>Fruits 6.23 Veggies 24.67<br>Wheat 100.0 Corn 88.8",
          "Texas<br>Beef 961.0 Dairy 240.55<br>Fruits 99.9 Veggies 115.23<br>Wheat 309.7 Corn 167.2",
          "Utah<br>Beef 27.9 Dairy 48.6<br>Fruits 12.34 Veggies 6.6<br>Wheat 42.8 Corn 5.3",
          "Vermont<br>Beef 6.2 Dairy 65.98<br>Fruits 8.01 Veggies 4.05<br>Wheat 0.0 Corn 0.0",
          "Virginia<br>Beef 39.5 Dairy 47.85<br>Fruits 36.48 Veggies 27.25<br>Wheat 77.5 Corn 39.5",
          "Washington<br>Beef 59.2 Dairy 154.18<br>Fruits 1738.57 Veggies 363.79<br>Wheat 786.3 Corn 29.5",
          "West Virginia<br>Beef 12.0 Dairy 3.9<br>Fruits 11.54 Veggies 0.0<br>Wheat 1.6 Corn 3.5",
          "Wisconsin<br>Beef 107.3 Dairy 633.6<br>Fruits 133.8 Veggies 148.99<br>Wheat 96.7 Corn 460.5",
          "Wyoming<br>Beef 75.1 Dairy 2.89<br>Fruits 0.17 Veggies 10.23<br>Wheat 20.7 Corn 9.0"
         ],
         "z": [
          1390.63,
          13.31,
          1463.17,
          3586.02,
          16472.88,
          1851.33,
          259.62,
          282.19,
          3764.09,
          2860.84,
          401.84,
          2078.89,
          8709.48,
          5050.23,
          11273.76,
          4589.01,
          1889.15,
          1914.23,
          278.37,
          692.75,
          248.65,
          3164.16,
          7192.33,
          2170.8,
          3933.42,
          1718.0,
          7114.13,
          139.89,
          73.06,
          500.4,
          751.58,
          1488.9,
          3806.05,
          3761.96,
          3979.79,
          1646.41,
          1794.57,
          1969.87,
          31.59,
          929.93,
          3770.19,
          1535.13,
          6648.22,
          453.39,
          180.14,
          1146.48,
          3894.81,
          138.89,
          3090.23,
          349.69
         ],
         "type": "choropleth"
        }
       ],
       "layout": {
        "geo": {
         "lakecolor": "rgb(85, 173, 240)",
         "scope": "usa",
         "showlakes": true
        },
        "template": {
         "data": {
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "bar": [
           {
            "error_x": {
             "color": "#f2f5fa"
            },
            "error_y": {
             "color": "#f2f5fa"
            },
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "baxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scatter"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#506784"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "header": {
             "fill": {
              "color": "#2a3f5f"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#f2f5fa",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#f2f5fa"
          },
          "geo": {
           "bgcolor": "rgb(17,17,17)",
           "lakecolor": "rgb(17,17,17)",
           "landcolor": "rgb(17,17,17)",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#506784"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "dark"
          },
          "paper_bgcolor": "rgb(17,17,17)",
          "plot_bgcolor": "rgb(17,17,17)",
          "polar": {
           "angularaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "radialaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "yaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "zaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#f2f5fa"
           }
          },
          "sliderdefaults": {
           "bgcolor": "#C8D4E3",
           "bordercolor": "rgb(17,17,17)",
           "borderwidth": 1,
           "tickwidth": 0
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "caxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "updatemenudefaults": {
           "bgcolor": "#506784",
           "borderwidth": 0
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "2011 US Agriuclture Exports by State"
        }
       },
       "config": {
        "showLink": false,
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly"
       }
      },
      "text/html": "<div>                            <div id=\"e43e23a7-1286-4899-8b69-08b5100e84fc\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"e43e23a7-1286-4899-8b69-08b5100e84fc\")) {                    Plotly.newPlot(                        \"e43e23a7-1286-4899-8b69-08b5100e84fc\",                        [{\"colorbar\":{\"title\":{\"text\":\"Millions USD\"}},\"colorscale\":[[0.0,\"rgb(247,252,245)\"],[0.125,\"rgb(229,245,224)\"],[0.25,\"rgb(199,233,192)\"],[0.375,\"rgb(161,217,155)\"],[0.5,\"rgb(116,196,118)\"],[0.625,\"rgb(65,171,93)\"],[0.75,\"rgb(35,139,69)\"],[0.875,\"rgb(0,109,44)\"],[1.0,\"rgb(0,68,27)\"]],\"locationmode\":\"USA-states\",\"locations\":[\"AL\",\"AK\",\"AZ\",\"AR\",\"CA\",\"CO\",\"CT\",\"DE\",\"FL\",\"GA\",\"HI\",\"ID\",\"IL\",\"IN\",\"IA\",\"KS\",\"KY\",\"LA\",\"ME\",\"MD\",\"MA\",\"MI\",\"MN\",\"MS\",\"MO\",\"MT\",\"NE\",\"NV\",\"NH\",\"NJ\",\"NM\",\"NY\",\"NC\",\"ND\",\"OH\",\"OK\",\"OR\",\"PA\",\"RI\",\"SC\",\"SD\",\"TN\",\"TX\",\"UT\",\"VT\",\"VA\",\"WA\",\"WV\",\"WI\",\"WY\"],\"marker\":{\"line\":{\"color\":\"rgb(255, 255, 255)\",\"width\":2}},\"text\":[\"Alabama\\u003cbr\\u003eBeef 34.4 Dairy 4.06\\u003cbr\\u003eFruits 25.11 Veggies 14.33\\u003cbr\\u003eWheat 70.0 Corn 34.9\",\"Alaska\\u003cbr\\u003eBeef 0.2 Dairy 0.19\\u003cbr\\u003eFruits 0.0 Veggies 1.56\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"Arizona\\u003cbr\\u003eBeef 71.3 Dairy 105.48\\u003cbr\\u003eFruits 60.27 Veggies 386.91\\u003cbr\\u003eWheat 48.7 Corn 7.3\",\"Arkansas\\u003cbr\\u003eBeef 53.2 Dairy 3.53\\u003cbr\\u003eFruits 6.88 Veggies 11.45\\u003cbr\\u003eWheat 114.5 Corn 69.5\",\" California\\u003cbr\\u003eBeef 228.7 Dairy 929.95\\u003cbr\\u003eFruits 8736.4 Veggies 2106.79\\u003cbr\\u003eWheat 249.3 Corn 34.6\",\"Colorado\\u003cbr\\u003eBeef 261.4 Dairy 71.94\\u003cbr\\u003eFruits 17.99 Veggies 118.27\\u003cbr\\u003eWheat 400.5 Corn 183.2\",\"Connecticut\\u003cbr\\u003eBeef 1.1 Dairy 9.49\\u003cbr\\u003eFruits 13.1 Veggies 11.16\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"Delaware\\u003cbr\\u003eBeef 0.4 Dairy 2.3\\u003cbr\\u003eFruits 1.53 Veggies 20.03\\u003cbr\\u003eWheat 22.9 Corn 26.9\",\"Florida\\u003cbr\\u003eBeef 42.6 Dairy 66.31\\u003cbr\\u003eFruits 1371.36 Veggies 450.86\\u003cbr\\u003eWheat 1.8 Corn 3.5\",\"Georgia\\u003cbr\\u003eBeef 31.0 Dairy 38.38\\u003cbr\\u003eFruits 233.51 Veggies 154.77\\u003cbr\\u003eWheat 65.4 Corn 57.8\",\"Hawaii\\u003cbr\\u003eBeef 4.0 Dairy 1.16\\u003cbr\\u003eFruits 55.51 Veggies 24.83\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"Idaho\\u003cbr\\u003eBeef 119.8 Dairy 294.6\\u003cbr\\u003eFruits 21.64 Veggies 319.19\\u003cbr\\u003eWheat 568.2 Corn 24.0\",\"Illinois\\u003cbr\\u003eBeef 53.7 Dairy 45.82\\u003cbr\\u003eFruits 12.53 Veggies 39.95\\u003cbr\\u003eWheat 223.8 Corn 2228.5\",\"Indiana\\u003cbr\\u003eBeef 21.9 Dairy 89.7\\u003cbr\\u003eFruits 12.98 Veggies 37.89\\u003cbr\\u003eWheat 114.0 Corn 1123.2\",\"Iowa\\u003cbr\\u003eBeef 289.8 Dairy 107.0\\u003cbr\\u003eFruits 3.24 Veggies 7.1\\u003cbr\\u003eWheat 3.1 Corn 2529.8\",\"Kansas\\u003cbr\\u003eBeef 659.3 Dairy 65.45\\u003cbr\\u003eFruits 3.11 Veggies 9.32\\u003cbr\\u003eWheat 1426.5 Corn 457.3\",\"Kentucky\\u003cbr\\u003eBeef 54.8 Dairy 28.27\\u003cbr\\u003eFruits 6.6 Veggies 0.0\\u003cbr\\u003eWheat 149.3 Corn 179.1\",\"Louisiana\\u003cbr\\u003eBeef 19.8 Dairy 6.02\\u003cbr\\u003eFruits 17.83 Veggies 17.25\\u003cbr\\u003eWheat 78.7 Corn 91.4\",\"Maine\\u003cbr\\u003eBeef 1.4 Dairy 16.18\\u003cbr\\u003eFruits 52.01 Veggies 62.9\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"Maryland\\u003cbr\\u003eBeef 5.6 Dairy 24.81\\u003cbr\\u003eFruits 12.9 Veggies 20.43\\u003cbr\\u003eWheat 55.8 Corn 54.1\",\"Massachusetts\\u003cbr\\u003eBeef 0.6 Dairy 5.81\\u003cbr\\u003eFruits 80.83 Veggies 21.13\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"Michigan\\u003cbr\\u003eBeef 37.7 Dairy 214.82\\u003cbr\\u003eFruits 257.69 Veggies 189.96\\u003cbr\\u003eWheat 247.0 Corn 381.5\",\"Minnesota\\u003cbr\\u003eBeef 112.3 Dairy 218.05\\u003cbr\\u003eFruits 7.91 Veggies 120.37\\u003cbr\\u003eWheat 538.1 Corn 1264.3\",\"Mississippi\\u003cbr\\u003eBeef 12.8 Dairy 5.45\\u003cbr\\u003eFruits 17.04 Veggies 27.87\\u003cbr\\u003eWheat 102.2 Corn 110.0\",\"Missouri\\u003cbr\\u003eBeef 137.2 Dairy 34.26\\u003cbr\\u003eFruits 13.18 Veggies 17.9\\u003cbr\\u003eWheat 161.7 Corn 428.8\",\"Montana\\u003cbr\\u003eBeef 105.0 Dairy 6.82\\u003cbr\\u003eFruits 3.3 Veggies 45.27\\u003cbr\\u003eWheat 1198.1 Corn 5.4\",\"Nebraska\\u003cbr\\u003eBeef 762.2 Dairy 30.07\\u003cbr\\u003eFruits 2.16 Veggies 53.5\\u003cbr\\u003eWheat 292.3 Corn 1735.9\",\"Nevada\\u003cbr\\u003eBeef 21.8 Dairy 16.57\\u003cbr\\u003eFruits 1.19 Veggies 27.93\\u003cbr\\u003eWheat 5.4 Corn 0.0\",\"New Hampshire\\u003cbr\\u003eBeef 0.6 Dairy 7.46\\u003cbr\\u003eFruits 7.98 Veggies 4.5\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"New Jersey\\u003cbr\\u003eBeef 0.8 Dairy 3.37\\u003cbr\\u003eFruits 109.45 Veggies 56.54\\u003cbr\\u003eWheat 6.7 Corn 10.1\",\"New Mexico\\u003cbr\\u003eBeef 117.2 Dairy 191.01\\u003cbr\\u003eFruits 101.9 Veggies 43.88\\u003cbr\\u003eWheat 13.9 Corn 11.2\",\"New York\\u003cbr\\u003eBeef 22.2 Dairy 331.8\\u003cbr\\u003eFruits 202.56 Veggies 143.37\\u003cbr\\u003eWheat 29.9 Corn 106.1\",\"North Carolina\\u003cbr\\u003eBeef 24.8 Dairy 24.9\\u003cbr\\u003eFruits 74.47 Veggies 150.45\\u003cbr\\u003eWheat 200.3 Corn 92.2\",\"North Dakota\\u003cbr\\u003eBeef 78.5 Dairy 8.14\\u003cbr\\u003eFruits 0.25 Veggies 130.79\\u003cbr\\u003eWheat 1664.5 Corn 236.1\",\"Ohio\\u003cbr\\u003eBeef 36.2 Dairy 134.57\\u003cbr\\u003eFruits 27.21 Veggies 53.53\\u003cbr\\u003eWheat 207.4 Corn 535.1\",\"Oklahoma\\u003cbr\\u003eBeef 337.6 Dairy 24.35\\u003cbr\\u003eFruits 9.24 Veggies 8.9\\u003cbr\\u003eWheat 324.8 Corn 27.5\",\"Oregon\\u003cbr\\u003eBeef 58.8 Dairy 63.66\\u003cbr\\u003eFruits 315.04 Veggies 126.5\\u003cbr\\u003eWheat 320.3 Corn 11.7\",\"Pennsylvania\\u003cbr\\u003eBeef 50.9 Dairy 280.87\\u003cbr\\u003eFruits 89.48 Veggies 38.26\\u003cbr\\u003eWheat 41.0 Corn 112.1\",\"Rhode Island\\u003cbr\\u003eBeef 0.1 Dairy 0.52\\u003cbr\\u003eFruits 2.83 Veggies 3.02\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"South Carolina\\u003cbr\\u003eBeef 15.2 Dairy 7.62\\u003cbr\\u003eFruits 53.45 Veggies 42.66\\u003cbr\\u003eWheat 55.3 Corn 32.1\",\"South Dakota\\u003cbr\\u003eBeef 193.5 Dairy 46.77\\u003cbr\\u003eFruits 0.8 Veggies 4.06\\u003cbr\\u003eWheat 704.5 Corn 643.6\",\"Tennessee\\u003cbr\\u003eBeef 51.1 Dairy 21.18\\u003cbr\\u003eFruits 6.23 Veggies 24.67\\u003cbr\\u003eWheat 100.0 Corn 88.8\",\"Texas\\u003cbr\\u003eBeef 961.0 Dairy 240.55\\u003cbr\\u003eFruits 99.9 Veggies 115.23\\u003cbr\\u003eWheat 309.7 Corn 167.2\",\"Utah\\u003cbr\\u003eBeef 27.9 Dairy 48.6\\u003cbr\\u003eFruits 12.34 Veggies 6.6\\u003cbr\\u003eWheat 42.8 Corn 5.3\",\"Vermont\\u003cbr\\u003eBeef 6.2 Dairy 65.98\\u003cbr\\u003eFruits 8.01 Veggies 4.05\\u003cbr\\u003eWheat 0.0 Corn 0.0\",\"Virginia\\u003cbr\\u003eBeef 39.5 Dairy 47.85\\u003cbr\\u003eFruits 36.48 Veggies 27.25\\u003cbr\\u003eWheat 77.5 Corn 39.5\",\"Washington\\u003cbr\\u003eBeef 59.2 Dairy 154.18\\u003cbr\\u003eFruits 1738.57 Veggies 363.79\\u003cbr\\u003eWheat 786.3 Corn 29.5\",\"West Virginia\\u003cbr\\u003eBeef 12.0 Dairy 3.9\\u003cbr\\u003eFruits 11.54 Veggies 0.0\\u003cbr\\u003eWheat 1.6 Corn 3.5\",\"Wisconsin\\u003cbr\\u003eBeef 107.3 Dairy 633.6\\u003cbr\\u003eFruits 133.8 Veggies 148.99\\u003cbr\\u003eWheat 96.7 Corn 460.5\",\"Wyoming\\u003cbr\\u003eBeef 75.1 Dairy 2.89\\u003cbr\\u003eFruits 0.17 Veggies 10.23\\u003cbr\\u003eWheat 20.7 Corn 9.0\"],\"z\":[1390.63,13.31,1463.17,3586.02,16472.88,1851.33,259.62,282.19,3764.09,2860.84,401.84,2078.89,8709.48,5050.23,11273.76,4589.01,1889.15,1914.23,278.37,692.75,248.65,3164.16,7192.33,2170.8,3933.42,1718.0,7114.13,139.89,73.06,500.4,751.58,1488.9,3806.05,3761.96,3979.79,1646.41,1794.57,1969.87,31.59,929.93,3770.19,1535.13,6648.22,453.39,180.14,1146.48,3894.81,138.89,3090.23,349.69],\"type\":\"choropleth\"}],                        {\"geo\":{\"lakecolor\":\"rgb(85, 173, 240)\",\"scope\":\"usa\",\"showlakes\":true},\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#f2f5fa\"},\"error_y\":{\"color\":\"#f2f5fa\"},\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"baxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#506784\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"header\":{\"fill\":{\"color\":\"#2a3f5f\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#f2f5fa\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#f2f5fa\"},\"geo\":{\"bgcolor\":\"rgb(17,17,17)\",\"lakecolor\":\"rgb(17,17,17)\",\"landcolor\":\"rgb(17,17,17)\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"#506784\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"dark\"},\"paper_bgcolor\":\"rgb(17,17,17)\",\"plot_bgcolor\":\"rgb(17,17,17)\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"radialaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"yaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"zaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"}},\"shapedefaults\":{\"line\":{\"color\":\"#f2f5fa\"}},\"sliderdefaults\":{\"bgcolor\":\"#C8D4E3\",\"bordercolor\":\"rgb(17,17,17)\",\"borderwidth\":1,\"tickwidth\":0},\"ternary\":{\"aaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"caxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"updatemenudefaults\":{\"bgcolor\":\"#506784\",\"borderwidth\":0},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"2011 US Agriuclture Exports by State\"}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('e43e23a7-1286-4899-8b69-08b5100e84fc');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.read_csv('2011_US_AGRI_Exports')\n",
    "# df.head()\n",
    "data = dict(\n",
    "    type = 'choropleth',\n",
    "    colorscale = 'Greens',\n",
    "    locations = df['code'],\n",
    "    locationmode = 'USA-states',\n",
    "    z = df['total exports'],\n",
    "    text = df['text'],\n",
    "    marker = dict(line = dict(color = 'rgb(255, 255, 255)', width = 2)), # the space between the states\n",
    "    colorbar = {\n",
    "        'title': 'Millions USD',\n",
    "    },\n",
    ")\n",
    "layout = dict(\n",
    "    title = '2011 US Agriuclture Exports by State',\n",
    "    geo = dict(\n",
    "        scope = 'usa',\n",
    "        showlakes = True,\n",
    "        lakecolor = 'rgb(85, 173, 240)',\n",
    "    )\n",
    ")\n",
    "choromap2 = go.Figure(\n",
    "    data = [data],\n",
    "    layout = layout,\n",
    ")\n",
    "iplot(choromap2)"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2024-07-12T06:36:40.852258Z",
     "start_time": "2024-07-12T06:36:40.772472Z"
    }
   },
   "id": "d19c61633e295b8e",
   "execution_count": 13
  },
  {
   "cell_type": "code",
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "data": [
        {
         "colorbar": {
          "title": {
           "text": "GDP in Billions USD"
          }
         },
         "locations": [
          "AFG",
          "ALB",
          "DZA",
          "ASM",
          "AND",
          "AGO",
          "AIA",
          "ATG",
          "ARG",
          "ARM",
          "ABW",
          "AUS",
          "AUT",
          "AZE",
          "BHM",
          "BHR",
          "BGD",
          "BRB",
          "BLR",
          "BEL",
          "BLZ",
          "BEN",
          "BMU",
          "BTN",
          "BOL",
          "BIH",
          "BWA",
          "BRA",
          "VGB",
          "BRN",
          "BGR",
          "BFA",
          "MMR",
          "BDI",
          "CPV",
          "KHM",
          "CMR",
          "CAN",
          "CYM",
          "CAF",
          "TCD",
          "CHL",
          "CHN",
          "COL",
          "COM",
          "COD",
          "COG",
          "COK",
          "CRI",
          "CIV",
          "HRV",
          "CUB",
          "CUW",
          "CYP",
          "CZE",
          "DNK",
          "DJI",
          "DMA",
          "DOM",
          "ECU",
          "EGY",
          "SLV",
          "GNQ",
          "ERI",
          "EST",
          "ETH",
          "FLK",
          "FRO",
          "FJI",
          "FIN",
          "FRA",
          "PYF",
          "GAB",
          "GMB",
          "GEO",
          "DEU",
          "GHA",
          "GIB",
          "GRC",
          "GRL",
          "GRD",
          "GUM",
          "GTM",
          "GGY",
          "GNB",
          "GIN",
          "GUY",
          "HTI",
          "HND",
          "HKG",
          "HUN",
          "ISL",
          "IND",
          "IDN",
          "IRN",
          "IRQ",
          "IRL",
          "IMN",
          "ISR",
          "ITA",
          "JAM",
          "JPN",
          "JEY",
          "JOR",
          "KAZ",
          "KEN",
          "KIR",
          "KOR",
          "PRK",
          "KSV",
          "KWT",
          "KGZ",
          "LAO",
          "LVA",
          "LBN",
          "LSO",
          "LBR",
          "LBY",
          "LIE",
          "LTU",
          "LUX",
          "MAC",
          "MKD",
          "MDG",
          "MWI",
          "MYS",
          "MDV",
          "MLI",
          "MLT",
          "MHL",
          "MRT",
          "MUS",
          "MEX",
          "FSM",
          "MDA",
          "MCO",
          "MNG",
          "MNE",
          "MAR",
          "MOZ",
          "NAM",
          "NPL",
          "NLD",
          "NCL",
          "NZL",
          "NIC",
          "NGA",
          "NER",
          "NIU",
          "MNP",
          "NOR",
          "OMN",
          "PAK",
          "PLW",
          "PAN",
          "PNG",
          "PRY",
          "PER",
          "PHL",
          "POL",
          "PRT",
          "PRI",
          "QAT",
          "ROU",
          "RUS",
          "RWA",
          "KNA",
          "LCA",
          "MAF",
          "SPM",
          "VCT",
          "WSM",
          "SMR",
          "STP",
          "SAU",
          "SEN",
          "SRB",
          "SYC",
          "SLE",
          "SGP",
          "SXM",
          "SVK",
          "SVN",
          "SLB",
          "SOM",
          "ZAF",
          "SSD",
          "ESP",
          "LKA",
          "SDN",
          "SUR",
          "SWZ",
          "SWE",
          "CHE",
          "SYR",
          "TWN",
          "TJK",
          "TZA",
          "THA",
          "TLS",
          "TGO",
          "TON",
          "TTO",
          "TUN",
          "TUR",
          "TKM",
          "TUV",
          "UGA",
          "UKR",
          "ARE",
          "GBR",
          "USA",
          "URY",
          "UZB",
          "VUT",
          "VEN",
          "VNM",
          "VGB",
          "WBG",
          "YEM",
          "ZMB",
          "ZWE"
         ],
         "text": [
          "Afghanistan",
          "Albania",
          "Algeria",
          "American Samoa",
          "Andorra",
          "Angola",
          "Anguilla",
          "Antigua and Barbuda",
          "Argentina",
          "Armenia",
          "Aruba",
          "Australia",
          "Austria",
          "Azerbaijan",
          "Bahamas, The",
          "Bahrain",
          "Bangladesh",
          "Barbados",
          "Belarus",
          "Belgium",
          "Belize",
          "Benin",
          "Bermuda",
          "Bhutan",
          "Bolivia",
          "Bosnia and Herzegovina",
          "Botswana",
          "Brazil",
          "British Virgin Islands",
          "Brunei",
          "Bulgaria",
          "Burkina Faso",
          "Burma",
          "Burundi",
          "Cabo Verde",
          "Cambodia",
          "Cameroon",
          "Canada",
          "Cayman Islands",
          "Central African Republic",
          "Chad",
          "Chile",
          "China",
          "Colombia",
          "Comoros",
          "Congo, Democratic Republic of the",
          "Congo, Republic of the",
          "Cook Islands",
          "Costa Rica",
          "Cote d'Ivoire",
          "Croatia",
          "Cuba",
          "Curacao",
          "Cyprus",
          "Czech Republic",
          "Denmark",
          "Djibouti",
          "Dominica",
          "Dominican Republic",
          "Ecuador",
          "Egypt",
          "El Salvador",
          "Equatorial Guinea",
          "Eritrea",
          "Estonia",
          "Ethiopia",
          "Falkland Islands (Islas Malvinas)",
          "Faroe Islands",
          "Fiji",
          "Finland",
          "France",
          "French Polynesia",
          "Gabon",
          "Gambia, The",
          "Georgia",
          "Germany",
          "Ghana",
          "Gibraltar",
          "Greece",
          "Greenland",
          "Grenada",
          "Guam",
          "Guatemala",
          "Guernsey",
          "Guinea-Bissau",
          "Guinea",
          "Guyana",
          "Haiti",
          "Honduras",
          "Hong Kong",
          "Hungary",
          "Iceland",
          "India",
          "Indonesia",
          "Iran",
          "Iraq",
          "Ireland",
          "Isle of Man",
          "Israel",
          "Italy",
          "Jamaica",
          "Japan",
          "Jersey",
          "Jordan",
          "Kazakhstan",
          "Kenya",
          "Kiribati",
          "Korea, North",
          "Korea, South",
          "Kosovo",
          "Kuwait",
          "Kyrgyzstan",
          "Laos",
          "Latvia",
          "Lebanon",
          "Lesotho",
          "Liberia",
          "Libya",
          "Liechtenstein",
          "Lithuania",
          "Luxembourg",
          "Macau",
          "Macedonia",
          "Madagascar",
          "Malawi",
          "Malaysia",
          "Maldives",
          "Mali",
          "Malta",
          "Marshall Islands",
          "Mauritania",
          "Mauritius",
          "Mexico",
          "Micronesia, Federated States of",
          "Moldova",
          "Monaco",
          "Mongolia",
          "Montenegro",
          "Morocco",
          "Mozambique",
          "Namibia",
          "Nepal",
          "Netherlands",
          "New Caledonia",
          "New Zealand",
          "Nicaragua",
          "Nigeria",
          "Niger",
          "Niue",
          "Northern Mariana Islands",
          "Norway",
          "Oman",
          "Pakistan",
          "Palau",
          "Panama",
          "Papua New Guinea",
          "Paraguay",
          "Peru",
          "Philippines",
          "Poland",
          "Portugal",
          "Puerto Rico",
          "Qatar",
          "Romania",
          "Russia",
          "Rwanda",
          "Saint Kitts and Nevis",
          "Saint Lucia",
          "Saint Martin",
          "Saint Pierre and Miquelon",
          "Saint Vincent and the Grenadines",
          "Samoa",
          "San Marino",
          "Sao Tome and Principe",
          "Saudi Arabia",
          "Senegal",
          "Serbia",
          "Seychelles",
          "Sierra Leone",
          "Singapore",
          "Sint Maarten",
          "Slovakia",
          "Slovenia",
          "Solomon Islands",
          "Somalia",
          "South Africa",
          "South Sudan",
          "Spain",
          "Sri Lanka",
          "Sudan",
          "Suriname",
          "Swaziland",
          "Sweden",
          "Switzerland",
          "Syria",
          "Taiwan",
          "Tajikistan",
          "Tanzania",
          "Thailand",
          "Timor-Leste",
          "Togo",
          "Tonga",
          "Trinidad and Tobago",
          "Tunisia",
          "Turkey",
          "Turkmenistan",
          "Tuvalu",
          "Uganda",
          "Ukraine",
          "United Arab Emirates",
          "United Kingdom",
          "United States",
          "Uruguay",
          "Uzbekistan",
          "Vanuatu",
          "Venezuela",
          "Vietnam",
          "Virgin Islands",
          "West Bank",
          "Yemen",
          "Zambia",
          "Zimbabwe"
         ],
         "z": [
          21.71,
          13.4,
          227.8,
          0.75,
          4.8,
          131.4,
          0.18,
          1.24,
          536.2,
          10.88,
          2.52,
          1483.0,
          436.1,
          77.91,
          8.65,
          34.05,
          186.6,
          4.28,
          75.25,
          527.8,
          1.67,
          9.24,
          5.2,
          2.09,
          34.08,
          19.55,
          16.3,
          2244.0,
          1.1,
          17.43,
          55.08,
          13.38,
          65.29,
          3.04,
          1.98,
          16.9,
          32.16,
          1794.0,
          2.25,
          1.73,
          15.84,
          264.1,
          10360.0,
          400.1,
          0.72,
          32.67,
          14.11,
          0.18,
          50.46,
          33.96,
          57.18,
          77.15,
          5.6,
          21.34,
          205.6,
          347.2,
          1.58,
          0.51,
          64.05,
          100.5,
          284.9,
          25.14,
          15.4,
          3.87,
          26.36,
          49.86,
          0.16,
          2.32,
          4.17,
          276.3,
          2902.0,
          7.15,
          20.68,
          0.92,
          16.13,
          3820.0,
          35.48,
          1.85,
          246.4,
          2.16,
          0.84,
          4.6,
          58.3,
          2.74,
          1.04,
          6.77,
          3.14,
          8.92,
          19.37,
          292.7,
          129.7,
          16.2,
          2048.0,
          856.1,
          402.7,
          232.2,
          245.8,
          4.08,
          305.0,
          2129.0,
          13.92,
          4770.0,
          5.77,
          36.55,
          225.6,
          62.72,
          0.16,
          28.0,
          1410.0,
          5.99,
          179.3,
          7.65,
          11.71,
          32.82,
          47.5,
          2.46,
          2.07,
          49.34,
          5.11,
          48.72,
          63.93,
          51.68,
          10.92,
          11.19,
          4.41,
          336.9,
          2.41,
          12.04,
          10.57,
          0.18,
          4.29,
          12.72,
          1296.0,
          0.34,
          7.74,
          6.06,
          11.73,
          4.66,
          112.6,
          16.59,
          13.11,
          19.64,
          880.4,
          11.1,
          201.0,
          11.85,
          594.3,
          8.29,
          0.01,
          1.23,
          511.6,
          80.54,
          237.5,
          0.65,
          44.69,
          16.1,
          31.3,
          208.2,
          284.6,
          552.2,
          228.2,
          93.52,
          212.0,
          199.0,
          2057.0,
          8.0,
          0.81,
          1.35,
          0.56,
          0.22,
          0.75,
          0.83,
          1.86,
          0.36,
          777.9,
          15.88,
          42.65,
          1.47,
          5.41,
          307.9,
          304.1,
          99.75,
          49.93,
          1.16,
          2.37,
          341.2,
          11.89,
          1400.0,
          71.57,
          70.03,
          5.27,
          3.84,
          559.1,
          679.0,
          64.7,
          529.5,
          9.16,
          36.62,
          373.8,
          4.51,
          4.84,
          0.49,
          29.63,
          49.12,
          813.3,
          43.5,
          0.04,
          26.09,
          134.9,
          416.4,
          2848.0,
          17420.0,
          55.6,
          63.08,
          0.82,
          209.2,
          187.8,
          5.08,
          6.64,
          45.45,
          25.61,
          13.74
         ],
         "type": "choropleth"
        }
       ],
       "layout": {
        "geo": {
         "projection": {
          "type": "mercator"
         },
         "showframe": false
        },
        "template": {
         "data": {
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "bar": [
           {
            "error_x": {
             "color": "#f2f5fa"
            },
            "error_y": {
             "color": "#f2f5fa"
            },
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "baxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scatter"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#506784"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "header": {
             "fill": {
              "color": "#2a3f5f"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#f2f5fa",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#f2f5fa"
          },
          "geo": {
           "bgcolor": "rgb(17,17,17)",
           "lakecolor": "rgb(17,17,17)",
           "landcolor": "rgb(17,17,17)",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#506784"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "dark"
          },
          "paper_bgcolor": "rgb(17,17,17)",
          "plot_bgcolor": "rgb(17,17,17)",
          "polar": {
           "angularaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "radialaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "yaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "zaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#f2f5fa"
           }
          },
          "sliderdefaults": {
           "bgcolor": "#C8D4E3",
           "bordercolor": "rgb(17,17,17)",
           "borderwidth": 1,
           "tickwidth": 0
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "caxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "updatemenudefaults": {
           "bgcolor": "#506784",
           "borderwidth": 0
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "2014 Global GDP"
        }
       },
       "config": {
        "showLink": false,
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly"
       }
      },
      "text/html": "<div>                            <div id=\"b82d0185-5285-477a-aebd-5b8aea8d1282\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"b82d0185-5285-477a-aebd-5b8aea8d1282\")) {                    Plotly.newPlot(                        \"b82d0185-5285-477a-aebd-5b8aea8d1282\",                        [{\"colorbar\":{\"title\":{\"text\":\"GDP in Billions USD\"}},\"locations\":[\"AFG\",\"ALB\",\"DZA\",\"ASM\",\"AND\",\"AGO\",\"AIA\",\"ATG\",\"ARG\",\"ARM\",\"ABW\",\"AUS\",\"AUT\",\"AZE\",\"BHM\",\"BHR\",\"BGD\",\"BRB\",\"BLR\",\"BEL\",\"BLZ\",\"BEN\",\"BMU\",\"BTN\",\"BOL\",\"BIH\",\"BWA\",\"BRA\",\"VGB\",\"BRN\",\"BGR\",\"BFA\",\"MMR\",\"BDI\",\"CPV\",\"KHM\",\"CMR\",\"CAN\",\"CYM\",\"CAF\",\"TCD\",\"CHL\",\"CHN\",\"COL\",\"COM\",\"COD\",\"COG\",\"COK\",\"CRI\",\"CIV\",\"HRV\",\"CUB\",\"CUW\",\"CYP\",\"CZE\",\"DNK\",\"DJI\",\"DMA\",\"DOM\",\"ECU\",\"EGY\",\"SLV\",\"GNQ\",\"ERI\",\"EST\",\"ETH\",\"FLK\",\"FRO\",\"FJI\",\"FIN\",\"FRA\",\"PYF\",\"GAB\",\"GMB\",\"GEO\",\"DEU\",\"GHA\",\"GIB\",\"GRC\",\"GRL\",\"GRD\",\"GUM\",\"GTM\",\"GGY\",\"GNB\",\"GIN\",\"GUY\",\"HTI\",\"HND\",\"HKG\",\"HUN\",\"ISL\",\"IND\",\"IDN\",\"IRN\",\"IRQ\",\"IRL\",\"IMN\",\"ISR\",\"ITA\",\"JAM\",\"JPN\",\"JEY\",\"JOR\",\"KAZ\",\"KEN\",\"KIR\",\"KOR\",\"PRK\",\"KSV\",\"KWT\",\"KGZ\",\"LAO\",\"LVA\",\"LBN\",\"LSO\",\"LBR\",\"LBY\",\"LIE\",\"LTU\",\"LUX\",\"MAC\",\"MKD\",\"MDG\",\"MWI\",\"MYS\",\"MDV\",\"MLI\",\"MLT\",\"MHL\",\"MRT\",\"MUS\",\"MEX\",\"FSM\",\"MDA\",\"MCO\",\"MNG\",\"MNE\",\"MAR\",\"MOZ\",\"NAM\",\"NPL\",\"NLD\",\"NCL\",\"NZL\",\"NIC\",\"NGA\",\"NER\",\"NIU\",\"MNP\",\"NOR\",\"OMN\",\"PAK\",\"PLW\",\"PAN\",\"PNG\",\"PRY\",\"PER\",\"PHL\",\"POL\",\"PRT\",\"PRI\",\"QAT\",\"ROU\",\"RUS\",\"RWA\",\"KNA\",\"LCA\",\"MAF\",\"SPM\",\"VCT\",\"WSM\",\"SMR\",\"STP\",\"SAU\",\"SEN\",\"SRB\",\"SYC\",\"SLE\",\"SGP\",\"SXM\",\"SVK\",\"SVN\",\"SLB\",\"SOM\",\"ZAF\",\"SSD\",\"ESP\",\"LKA\",\"SDN\",\"SUR\",\"SWZ\",\"SWE\",\"CHE\",\"SYR\",\"TWN\",\"TJK\",\"TZA\",\"THA\",\"TLS\",\"TGO\",\"TON\",\"TTO\",\"TUN\",\"TUR\",\"TKM\",\"TUV\",\"UGA\",\"UKR\",\"ARE\",\"GBR\",\"USA\",\"URY\",\"UZB\",\"VUT\",\"VEN\",\"VNM\",\"VGB\",\"WBG\",\"YEM\",\"ZMB\",\"ZWE\"],\"text\":[\"Afghanistan\",\"Albania\",\"Algeria\",\"American Samoa\",\"Andorra\",\"Angola\",\"Anguilla\",\"Antigua and Barbuda\",\"Argentina\",\"Armenia\",\"Aruba\",\"Australia\",\"Austria\",\"Azerbaijan\",\"Bahamas, The\",\"Bahrain\",\"Bangladesh\",\"Barbados\",\"Belarus\",\"Belgium\",\"Belize\",\"Benin\",\"Bermuda\",\"Bhutan\",\"Bolivia\",\"Bosnia and Herzegovina\",\"Botswana\",\"Brazil\",\"British Virgin Islands\",\"Brunei\",\"Bulgaria\",\"Burkina Faso\",\"Burma\",\"Burundi\",\"Cabo Verde\",\"Cambodia\",\"Cameroon\",\"Canada\",\"Cayman Islands\",\"Central African Republic\",\"Chad\",\"Chile\",\"China\",\"Colombia\",\"Comoros\",\"Congo, Democratic Republic of the\",\"Congo, Republic of the\",\"Cook Islands\",\"Costa Rica\",\"Cote d'Ivoire\",\"Croatia\",\"Cuba\",\"Curacao\",\"Cyprus\",\"Czech Republic\",\"Denmark\",\"Djibouti\",\"Dominica\",\"Dominican Republic\",\"Ecuador\",\"Egypt\",\"El Salvador\",\"Equatorial Guinea\",\"Eritrea\",\"Estonia\",\"Ethiopia\",\"Falkland Islands (Islas Malvinas)\",\"Faroe Islands\",\"Fiji\",\"Finland\",\"France\",\"French Polynesia\",\"Gabon\",\"Gambia, The\",\"Georgia\",\"Germany\",\"Ghana\",\"Gibraltar\",\"Greece\",\"Greenland\",\"Grenada\",\"Guam\",\"Guatemala\",\"Guernsey\",\"Guinea-Bissau\",\"Guinea\",\"Guyana\",\"Haiti\",\"Honduras\",\"Hong Kong\",\"Hungary\",\"Iceland\",\"India\",\"Indonesia\",\"Iran\",\"Iraq\",\"Ireland\",\"Isle of Man\",\"Israel\",\"Italy\",\"Jamaica\",\"Japan\",\"Jersey\",\"Jordan\",\"Kazakhstan\",\"Kenya\",\"Kiribati\",\"Korea, North\",\"Korea, South\",\"Kosovo\",\"Kuwait\",\"Kyrgyzstan\",\"Laos\",\"Latvia\",\"Lebanon\",\"Lesotho\",\"Liberia\",\"Libya\",\"Liechtenstein\",\"Lithuania\",\"Luxembourg\",\"Macau\",\"Macedonia\",\"Madagascar\",\"Malawi\",\"Malaysia\",\"Maldives\",\"Mali\",\"Malta\",\"Marshall Islands\",\"Mauritania\",\"Mauritius\",\"Mexico\",\"Micronesia, Federated States of\",\"Moldova\",\"Monaco\",\"Mongolia\",\"Montenegro\",\"Morocco\",\"Mozambique\",\"Namibia\",\"Nepal\",\"Netherlands\",\"New Caledonia\",\"New Zealand\",\"Nicaragua\",\"Nigeria\",\"Niger\",\"Niue\",\"Northern Mariana Islands\",\"Norway\",\"Oman\",\"Pakistan\",\"Palau\",\"Panama\",\"Papua New Guinea\",\"Paraguay\",\"Peru\",\"Philippines\",\"Poland\",\"Portugal\",\"Puerto Rico\",\"Qatar\",\"Romania\",\"Russia\",\"Rwanda\",\"Saint Kitts and Nevis\",\"Saint Lucia\",\"Saint Martin\",\"Saint Pierre and Miquelon\",\"Saint Vincent and the Grenadines\",\"Samoa\",\"San Marino\",\"Sao Tome and Principe\",\"Saudi Arabia\",\"Senegal\",\"Serbia\",\"Seychelles\",\"Sierra Leone\",\"Singapore\",\"Sint Maarten\",\"Slovakia\",\"Slovenia\",\"Solomon Islands\",\"Somalia\",\"South Africa\",\"South Sudan\",\"Spain\",\"Sri Lanka\",\"Sudan\",\"Suriname\",\"Swaziland\",\"Sweden\",\"Switzerland\",\"Syria\",\"Taiwan\",\"Tajikistan\",\"Tanzania\",\"Thailand\",\"Timor-Leste\",\"Togo\",\"Tonga\",\"Trinidad and Tobago\",\"Tunisia\",\"Turkey\",\"Turkmenistan\",\"Tuvalu\",\"Uganda\",\"Ukraine\",\"United Arab Emirates\",\"United Kingdom\",\"United States\",\"Uruguay\",\"Uzbekistan\",\"Vanuatu\",\"Venezuela\",\"Vietnam\",\"Virgin Islands\",\"West Bank\",\"Yemen\",\"Zambia\",\"Zimbabwe\"],\"z\":[21.71,13.4,227.8,0.75,4.8,131.4,0.18,1.24,536.2,10.88,2.52,1483.0,436.1,77.91,8.65,34.05,186.6,4.28,75.25,527.8,1.67,9.24,5.2,2.09,34.08,19.55,16.3,2244.0,1.1,17.43,55.08,13.38,65.29,3.04,1.98,16.9,32.16,1794.0,2.25,1.73,15.84,264.1,10360.0,400.1,0.72,32.67,14.11,0.18,50.46,33.96,57.18,77.15,5.6,21.34,205.6,347.2,1.58,0.51,64.05,100.5,284.9,25.14,15.4,3.87,26.36,49.86,0.16,2.32,4.17,276.3,2902.0,7.15,20.68,0.92,16.13,3820.0,35.48,1.85,246.4,2.16,0.84,4.6,58.3,2.74,1.04,6.77,3.14,8.92,19.37,292.7,129.7,16.2,2048.0,856.1,402.7,232.2,245.8,4.08,305.0,2129.0,13.92,4770.0,5.77,36.55,225.6,62.72,0.16,28.0,1410.0,5.99,179.3,7.65,11.71,32.82,47.5,2.46,2.07,49.34,5.11,48.72,63.93,51.68,10.92,11.19,4.41,336.9,2.41,12.04,10.57,0.18,4.29,12.72,1296.0,0.34,7.74,6.06,11.73,4.66,112.6,16.59,13.11,19.64,880.4,11.1,201.0,11.85,594.3,8.29,0.01,1.23,511.6,80.54,237.5,0.65,44.69,16.1,31.3,208.2,284.6,552.2,228.2,93.52,212.0,199.0,2057.0,8.0,0.81,1.35,0.56,0.22,0.75,0.83,1.86,0.36,777.9,15.88,42.65,1.47,5.41,307.9,304.1,99.75,49.93,1.16,2.37,341.2,11.89,1400.0,71.57,70.03,5.27,3.84,559.1,679.0,64.7,529.5,9.16,36.62,373.8,4.51,4.84,0.49,29.63,49.12,813.3,43.5,0.04,26.09,134.9,416.4,2848.0,17420.0,55.6,63.08,0.82,209.2,187.8,5.08,6.64,45.45,25.61,13.74],\"type\":\"choropleth\"}],                        {\"geo\":{\"projection\":{\"type\":\"mercator\"},\"showframe\":false},\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#f2f5fa\"},\"error_y\":{\"color\":\"#f2f5fa\"},\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"baxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#506784\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"header\":{\"fill\":{\"color\":\"#2a3f5f\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#f2f5fa\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#f2f5fa\"},\"geo\":{\"bgcolor\":\"rgb(17,17,17)\",\"lakecolor\":\"rgb(17,17,17)\",\"landcolor\":\"rgb(17,17,17)\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"#506784\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"dark\"},\"paper_bgcolor\":\"rgb(17,17,17)\",\"plot_bgcolor\":\"rgb(17,17,17)\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"radialaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"yaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"zaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"}},\"shapedefaults\":{\"line\":{\"color\":\"#f2f5fa\"}},\"sliderdefaults\":{\"bgcolor\":\"#C8D4E3\",\"bordercolor\":\"rgb(17,17,17)\",\"borderwidth\":1,\"tickwidth\":0},\"ternary\":{\"aaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"caxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"updatemenudefaults\":{\"bgcolor\":\"#506784\",\"borderwidth\":0},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"2014 Global GDP\"}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('b82d0185-5285-477a-aebd-5b8aea8d1282');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.read_csv('2014_World_GDP')\n",
    "# df.head()\n",
    "data = dict(\n",
    "    type = 'choropleth',\n",
    "    locations = df['CODE'],\n",
    "    z = df['GDP (BILLIONS)'],\n",
    "    text = df['COUNTRY'],\n",
    "    colorbar = {\n",
    "        'title': 'GDP in Billions USD',\n",
    "    }\n",
    ")\n",
    "layout = dict(\n",
    "    title = '2014 Global GDP',\n",
    "    geo = dict(\n",
    "        showframe = False,\n",
    "        projection = {\n",
    "            'type': 'mercator',\n",
    "        }\n",
    "    )\n",
    ")\n",
    "choromap3 = go.Figure(\n",
    "    data = [data],\n",
    "    layout = layout,\n",
    ")\n",
    "iplot(choromap3)"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2024-07-12T07:01:47.862329Z",
     "start_time": "2024-07-12T07:01:47.787531Z"
    }
   },
   "id": "1de47338e5e59e63",
   "execution_count": 19
  },
  {
   "cell_type": "code",
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "data": [
        {
         "colorbar": {
          "title": {
           "text": "Power Consumption KWH"
          }
         },
         "colorscale": [
          [
           0.0,
           "#440154"
          ],
          [
           0.1111111111111111,
           "#482878"
          ],
          [
           0.2222222222222222,
           "#3e4989"
          ],
          [
           0.3333333333333333,
           "#31688e"
          ],
          [
           0.4444444444444444,
           "#26828e"
          ],
          [
           0.5555555555555556,
           "#1f9e89"
          ],
          [
           0.6666666666666666,
           "#35b779"
          ],
          [
           0.7777777777777778,
           "#6ece58"
          ],
          [
           0.8888888888888888,
           "#b5de2b"
          ],
          [
           1.0,
           "#fde725"
          ]
         ],
         "locationmode": "country names",
         "locations": [
          "China",
          "United States",
          "European",
          "Russia",
          "Japan",
          "India",
          "Germany",
          "Canada",
          "Brazil",
          "Korea,",
          "France",
          "United Kingdom",
          "Italy",
          "Taiwan",
          "Spain",
          "Mexico",
          "Saudi",
          "Australia",
          "South",
          "Turkey",
          "Iran",
          "Indonesia",
          "Ukraine",
          "Thailand",
          "Poland",
          "Egypt",
          "Sweden",
          "Norway",
          "Malaysia",
          "Argentina",
          "Netherlands",
          "Vietnam",
          "Venezuela",
          "United Arab Emirates",
          "Finland",
          "Belgium",
          "Kazakhstan",
          "Pakistan",
          "Philippines",
          "Austria",
          "Chile",
          "Czechia",
          "Israel",
          "Switzerland",
          "Greece",
          "Iraq",
          "Romania",
          "Kuwait",
          "Colombia",
          "Singapore",
          "Portugal",
          "Uzbekistan",
          "Hong",
          "Algeria",
          "Bangladesh",
          "New",
          "Bulgaria",
          "Belarus",
          "Peru",
          "Denmark",
          "Qatar",
          "Slovakia",
          "Libya",
          "Serbia",
          "Morocco",
          "Syria",
          "Nigeria",
          "Ireland",
          "Hungary",
          "Oman",
          "Ecuador",
          "Puerto",
          "Azerbaijan",
          "Croatia",
          "Iceland",
          "Cuba",
          "Korea,",
          "Dominican",
          "Jordan",
          "Tajikistan",
          "Tunisia",
          "Slovenia",
          "Lebanon",
          "Bosnia",
          "Turkmenistan",
          "Bahrain",
          "Mozambique",
          "Ghana",
          "Sri",
          "Kyrgyzstan",
          "Lithuania",
          "Uruguay",
          "Costa",
          "Guatemala",
          "Georgia",
          "Trinidad",
          "Zambia",
          "Paraguay",
          "Albania",
          "Burma",
          "Estonia",
          "Congo,",
          "Panama",
          "Latvia",
          "Macedonia",
          "Zimbabwe",
          "Kenya",
          "Bolivia",
          "Luxembourg",
          "Sudan",
          "El",
          "Cameroon",
          "West",
          "Ethiopia",
          "Armenia",
          "Honduras",
          "Angola",
          "Cote",
          "Tanzania",
          "Nicaragua",
          "Moldova",
          "Cyprus",
          "Macau",
          "Namibia",
          "Mongolia",
          "Afghanistan",
          "Yemen",
          "Brunei",
          "Cambodia",
          "Montenegro",
          "Nepal",
          "Botswana",
          "Papua",
          "Jamaica",
          "Kosovo",
          "Laos",
          "Uganda",
          "New",
          "Mauritius",
          "Senegal",
          "Bhutan",
          "Malawi",
          "Madagascar",
          "Bahamas,",
          "Gabon",
          "Suriname",
          "Guam",
          "Liechtenstein",
          "Swaziland",
          "Burkina",
          "Togo",
          "Curacao",
          "Mauritania",
          "Barbados",
          "Niger",
          "Aruba",
          "Benin",
          "Guinea",
          "Mali",
          "Fiji",
          "Congo,",
          "Virgin",
          "Lesotho",
          "South",
          "Bermuda",
          "French",
          "Jersey",
          "Belize",
          "Andorra",
          "Guyana",
          "Cayman",
          "Haiti",
          "Rwanda",
          "Saint",
          "Djibouti",
          "Seychelles",
          "Somalia",
          "Antigua",
          "Greenland",
          "Cabo",
          "Eritrea",
          "Burundi",
          "Liberia",
          "Maldives",
          "Faroe",
          "Gambia,",
          "Chad",
          "Micronesia,",
          "Grenada",
          "Central",
          "Turks",
          "Gibraltar",
          "American",
          "Sierra",
          "Saint",
          "Saint",
          "Timor-Leste",
          "Equatorial",
          "Samoa",
          "Dominica",
          "Western",
          "Solomon",
          "Sao",
          "British",
          "Vanuatu",
          "Guinea-Bissau",
          "Tonga",
          "Saint",
          "Comoros",
          "Cook",
          "Kiribati",
          "Montserrat",
          "Nauru",
          "Falkland",
          "Saint",
          "Niue",
          "Gaza",
          "Malta",
          "Northern"
         ],
         "reversescale": true,
         "text": [
          "China",
          "United States",
          "European",
          "Russia",
          "Japan",
          "India",
          "Germany",
          "Canada",
          "Brazil",
          "Korea,",
          "France",
          "United Kingdom",
          "Italy",
          "Taiwan",
          "Spain",
          "Mexico",
          "Saudi",
          "Australia",
          "South",
          "Turkey",
          "Iran",
          "Indonesia",
          "Ukraine",
          "Thailand",
          "Poland",
          "Egypt",
          "Sweden",
          "Norway",
          "Malaysia",
          "Argentina",
          "Netherlands",
          "Vietnam",
          "Venezuela",
          "United Arab Emirates",
          "Finland",
          "Belgium",
          "Kazakhstan",
          "Pakistan",
          "Philippines",
          "Austria",
          "Chile",
          "Czechia",
          "Israel",
          "Switzerland",
          "Greece",
          "Iraq",
          "Romania",
          "Kuwait",
          "Colombia",
          "Singapore",
          "Portugal",
          "Uzbekistan",
          "Hong",
          "Algeria",
          "Bangladesh",
          "New",
          "Bulgaria",
          "Belarus",
          "Peru",
          "Denmark",
          "Qatar",
          "Slovakia",
          "Libya",
          "Serbia",
          "Morocco",
          "Syria",
          "Nigeria",
          "Ireland",
          "Hungary",
          "Oman",
          "Ecuador",
          "Puerto",
          "Azerbaijan",
          "Croatia",
          "Iceland",
          "Cuba",
          "Korea,",
          "Dominican",
          "Jordan",
          "Tajikistan",
          "Tunisia",
          "Slovenia",
          "Lebanon",
          "Bosnia",
          "Turkmenistan",
          "Bahrain",
          "Mozambique",
          "Ghana",
          "Sri",
          "Kyrgyzstan",
          "Lithuania",
          "Uruguay",
          "Costa",
          "Guatemala",
          "Georgia",
          "Trinidad",
          "Zambia",
          "Paraguay",
          "Albania",
          "Burma",
          "Estonia",
          "Congo,",
          "Panama",
          "Latvia",
          "Macedonia",
          "Zimbabwe",
          "Kenya",
          "Bolivia",
          "Luxembourg",
          "Sudan",
          "El",
          "Cameroon",
          "West",
          "Ethiopia",
          "Armenia",
          "Honduras",
          "Angola",
          "Cote",
          "Tanzania",
          "Nicaragua",
          "Moldova",
          "Cyprus",
          "Macau",
          "Namibia",
          "Mongolia",
          "Afghanistan",
          "Yemen",
          "Brunei",
          "Cambodia",
          "Montenegro",
          "Nepal",
          "Botswana",
          "Papua",
          "Jamaica",
          "Kosovo",
          "Laos",
          "Uganda",
          "New",
          "Mauritius",
          "Senegal",
          "Bhutan",
          "Malawi",
          "Madagascar",
          "Bahamas,",
          "Gabon",
          "Suriname",
          "Guam",
          "Liechtenstein",
          "Swaziland",
          "Burkina",
          "Togo",
          "Curacao",
          "Mauritania",
          "Barbados",
          "Niger",
          "Aruba",
          "Benin",
          "Guinea",
          "Mali",
          "Fiji",
          "Congo,",
          "Virgin",
          "Lesotho",
          "South",
          "Bermuda",
          "French",
          "Jersey",
          "Belize",
          "Andorra",
          "Guyana",
          "Cayman",
          "Haiti",
          "Rwanda",
          "Saint",
          "Djibouti",
          "Seychelles",
          "Somalia",
          "Antigua",
          "Greenland",
          "Cabo",
          "Eritrea",
          "Burundi",
          "Liberia",
          "Maldives",
          "Faroe",
          "Gambia,",
          "Chad",
          "Micronesia,",
          "Grenada",
          "Central",
          "Turks",
          "Gibraltar",
          "American",
          "Sierra",
          "Saint",
          "Saint",
          "Timor-Leste",
          "Equatorial",
          "Samoa",
          "Dominica",
          "Western",
          "Solomon",
          "Sao",
          "British",
          "Vanuatu",
          "Guinea-Bissau",
          "Tonga",
          "Saint",
          "Comoros",
          "Cook",
          "Kiribati",
          "Montserrat",
          "Nauru",
          "Falkland",
          "Saint",
          "Niue",
          "Gaza",
          "Malta",
          "Northern"
         ],
         "z": [
          5.523E12,
          3.832E12,
          2.771E12,
          1.065E12,
          9.21E11,
          8.647E11,
          5.401E11,
          5.11E11,
          4.835E11,
          4.824E11,
          4.511E11,
          3.191E11,
          3.031E11,
          2.495E11,
          2.431E11,
          2.34E11,
          2.316E11,
          2.226E11,
          2.116E11,
          1.97E11,
          1.953E11,
          1.675E11,
          1.598E11,
          1.559E11,
          1.39E11,
          1.356E11,
          1.305E11,
          1.264E11,
          1.185E11,
          1.171E11,
          1.168E11,
          1.083E11,
          9.769E10,
          9.328E10,
          8.204E10,
          8.189E10,
          8.029E10,
          7.889E10,
          7.527E10,
          6.975E10,
          6.339E10,
          6.055E10,
          5.983E10,
          5.801E10,
          5.773E10,
          5.341E10,
          5.073E10,
          5.0E10,
          4.938E10,
          4.718E10,
          4.625E10,
          4.521E10,
          4.421E10,
          4.287E10,
          4.152E10,
          4.03E10,
          3.799E10,
          3.788E10,
          3.569E10,
          3.196E10,
          3.053E10,
          2.836E10,
          2.754E10,
          2.691E10,
          2.67E10,
          2.57E10,
          2.478E10,
          2.424E10,
          2.155E10,
          2.036E10,
          1.902E10,
          1.862E10,
          1.779E10,
          1.697E10,
          1.694E10,
          1.62E10,
          1.6E10,
          1.514E10,
          1.456E10,
          1.442E10,
          1.331E10,
          1.302E10,
          1.294E10,
          1.256E10,
          1.175E10,
          1.169E10,
          1.128E10,
          1.058E10,
          1.017E10,
          9.943E9,
          9.664E9,
          9.559E9,
          8.987E9,
          8.915E9,
          8.468E9,
          8.365E9,
          8.327E9,
          8.125E9,
          7.793E9,
          7.765E9,
          7.417E9,
          7.292E9,
          7.144E9,
          7.141E9,
          6.96E9,
          6.831E9,
          6.627E9,
          6.456E9,
          6.108E9,
          5.665E9,
          5.665E9,
          5.535E9,
          5.312E9,
          5.227E9,
          5.043E9,
          5.036E9,
          4.842E9,
          4.731E9,
          4.545E9,
          4.412E9,
          4.305E9,
          4.296E9,
          4.291E9,
          4.238E9,
          4.204E9,
          3.893E9,
          3.838E9,
          3.766E9,
          3.553E9,
          3.465E9,
          3.239E9,
          3.213E9,
          3.116E9,
          3.008E9,
          2.887E9,
          2.874E9,
          2.821E9,
          2.716E9,
          2.658E9,
          2.586E9,
          2.085E9,
          2.027E9,
          1.883E9,
          1.716E9,
          1.68E9,
          1.572E9,
          1.566E9,
          1.36E9,
          1.295E9,
          9.855E8,
          9.76E8,
          9.68E8,
          9.626E8,
          9.38E8,
          9.302E8,
          9.207E8,
          9.11E8,
          9.03E8,
          8.826E8,
          7.776E8,
          7.4E8,
          7.235E8,
          7.07E8,
          6.941E8,
          6.642E8,
          6.529E8,
          6.301E8,
          6.05E8,
          5.624E8,
          5.58E8,
          5.459E8,
          4.52E8,
          3.655E8,
          3.364E8,
          3.116E8,
          2.939E8,
          2.93E8,
          2.93E8,
          2.92E8,
          2.855E8,
          2.84E8,
          2.829E8,
          2.769E8,
          2.671E8,
          2.613E8,
          2.186E8,
          1.907E8,
          1.786E8,
          1.78E8,
          1.683E8,
          1.674E8,
          1.6E8,
          1.46E8,
          1.349E8,
          1.302E8,
          1.274E8,
          1.253E8,
          9.3E7,
          9.04E7,
          8.975E7,
          8.37E7,
          7.905E7,
          6.045E7,
          5.115E7,
          4.929E7,
          4.65E7,
          4.464E7,
          3.999E7,
          3.999E7,
          2.895E7,
          2.418E7,
          2.325E7,
          2.325E7,
          1.116E7,
          7440000.0,
          2790000.0,
          202000.0,
          174700.0,
          48300.0
         ],
         "type": "choropleth"
        }
       ],
       "layout": {
        "geo": {
         "projection": {
          "type": "mercator"
         },
         "showframe": false
        },
        "title": {
         "text": "2014 Power Consumption"
        },
        "template": {
         "data": {
          "histogram2dcontour": [
           {
            "type": "histogram2dcontour",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ]
           }
          ],
          "choropleth": [
           {
            "type": "choropleth",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            }
           }
          ],
          "histogram2d": [
           {
            "type": "histogram2d",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ]
           }
          ],
          "heatmap": [
           {
            "type": "heatmap",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ]
           }
          ],
          "heatmapgl": [
           {
            "type": "heatmapgl",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ]
           }
          ],
          "contourcarpet": [
           {
            "type": "contourcarpet",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            }
           }
          ],
          "contour": [
           {
            "type": "contour",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ]
           }
          ],
          "surface": [
           {
            "type": "surface",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ]
           }
          ],
          "mesh3d": [
           {
            "type": "mesh3d",
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            }
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scatter"
           }
          ],
          "parcoords": [
           {
            "type": "parcoords",
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "scatterpolargl": [
           {
            "type": "scatterpolargl",
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "bar": [
           {
            "error_x": {
             "color": "#f2f5fa"
            },
            "error_y": {
             "color": "#f2f5fa"
            },
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "scattergeo": [
           {
            "type": "scattergeo",
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "scatterpolar": [
           {
            "type": "scatterpolar",
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scattergl"
           }
          ],
          "scatter3d": [
           {
            "type": "scatter3d",
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "scattermapbox": [
           {
            "type": "scattermapbox",
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "scatterternary": [
           {
            "type": "scatterternary",
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "scattercarpet": [
           {
            "type": "scattercarpet",
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            }
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "baxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "type": "carpet"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#506784"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "header": {
             "fill": {
              "color": "#2a3f5f"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "type": "table"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ]
         },
         "layout": {
          "autotypenumbers": "strict",
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#f2f5fa"
          },
          "hovermode": "closest",
          "hoverlabel": {
           "align": "left"
          },
          "paper_bgcolor": "rgb(17,17,17)",
          "plot_bgcolor": "rgb(17,17,17)",
          "polar": {
           "bgcolor": "rgb(17,17,17)",
           "angularaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "radialaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "ternary": {
           "bgcolor": "rgb(17,17,17)",
           "aaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "caxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "sequential": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ],
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ]
          },
          "xaxis": {
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "automargin": true,
           "zerolinewidth": 2
          },
          "yaxis": {
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "automargin": true,
           "zerolinewidth": 2
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3",
            "gridwidth": 2
           },
           "yaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3",
            "gridwidth": 2
           },
           "zaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3",
            "gridwidth": 2
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#f2f5fa"
           }
          },
          "annotationdefaults": {
           "arrowcolor": "#f2f5fa",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "geo": {
           "bgcolor": "rgb(17,17,17)",
           "landcolor": "rgb(17,17,17)",
           "subunitcolor": "#506784",
           "showland": true,
           "showlakes": true,
           "lakecolor": "rgb(17,17,17)"
          },
          "title": {
           "x": 0.05
          },
          "updatemenudefaults": {
           "bgcolor": "#506784",
           "borderwidth": 0
          },
          "sliderdefaults": {
           "bgcolor": "#C8D4E3",
           "borderwidth": 1,
           "bordercolor": "rgb(17,17,17)",
           "tickwidth": 0
          },
          "mapbox": {
           "style": "dark"
          }
         }
        }
       },
       "config": {
        "showLink": false,
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly"
       }
      },
      "text/html": "<div>                            <div id=\"848cd290-145c-438e-a641-c9d6b2808299\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"848cd290-145c-438e-a641-c9d6b2808299\")) {                    Plotly.newPlot(                        \"848cd290-145c-438e-a641-c9d6b2808299\",                        [{\"colorbar\":{\"title\":{\"text\":\"Power Consumption KWH\"}},\"colorscale\":[[0.0,\"#440154\"],[0.1111111111111111,\"#482878\"],[0.2222222222222222,\"#3e4989\"],[0.3333333333333333,\"#31688e\"],[0.4444444444444444,\"#26828e\"],[0.5555555555555556,\"#1f9e89\"],[0.6666666666666666,\"#35b779\"],[0.7777777777777778,\"#6ece58\"],[0.8888888888888888,\"#b5de2b\"],[1.0,\"#fde725\"]],\"locationmode\":\"country names\",\"locations\":[\"China\",\"United States\",\"European\",\"Russia\",\"Japan\",\"India\",\"Germany\",\"Canada\",\"Brazil\",\"Korea,\",\"France\",\"United Kingdom\",\"Italy\",\"Taiwan\",\"Spain\",\"Mexico\",\"Saudi\",\"Australia\",\"South\",\"Turkey\",\"Iran\",\"Indonesia\",\"Ukraine\",\"Thailand\",\"Poland\",\"Egypt\",\"Sweden\",\"Norway\",\"Malaysia\",\"Argentina\",\"Netherlands\",\"Vietnam\",\"Venezuela\",\"United Arab Emirates\",\"Finland\",\"Belgium\",\"Kazakhstan\",\"Pakistan\",\"Philippines\",\"Austria\",\"Chile\",\"Czechia\",\"Israel\",\"Switzerland\",\"Greece\",\"Iraq\",\"Romania\",\"Kuwait\",\"Colombia\",\"Singapore\",\"Portugal\",\"Uzbekistan\",\"Hong\",\"Algeria\",\"Bangladesh\",\"New\",\"Bulgaria\",\"Belarus\",\"Peru\",\"Denmark\",\"Qatar\",\"Slovakia\",\"Libya\",\"Serbia\",\"Morocco\",\"Syria\",\"Nigeria\",\"Ireland\",\"Hungary\",\"Oman\",\"Ecuador\",\"Puerto\",\"Azerbaijan\",\"Croatia\",\"Iceland\",\"Cuba\",\"Korea,\",\"Dominican\",\"Jordan\",\"Tajikistan\",\"Tunisia\",\"Slovenia\",\"Lebanon\",\"Bosnia\",\"Turkmenistan\",\"Bahrain\",\"Mozambique\",\"Ghana\",\"Sri\",\"Kyrgyzstan\",\"Lithuania\",\"Uruguay\",\"Costa\",\"Guatemala\",\"Georgia\",\"Trinidad\",\"Zambia\",\"Paraguay\",\"Albania\",\"Burma\",\"Estonia\",\"Congo,\",\"Panama\",\"Latvia\",\"Macedonia\",\"Zimbabwe\",\"Kenya\",\"Bolivia\",\"Luxembourg\",\"Sudan\",\"El\",\"Cameroon\",\"West\",\"Ethiopia\",\"Armenia\",\"Honduras\",\"Angola\",\"Cote\",\"Tanzania\",\"Nicaragua\",\"Moldova\",\"Cyprus\",\"Macau\",\"Namibia\",\"Mongolia\",\"Afghanistan\",\"Yemen\",\"Brunei\",\"Cambodia\",\"Montenegro\",\"Nepal\",\"Botswana\",\"Papua\",\"Jamaica\",\"Kosovo\",\"Laos\",\"Uganda\",\"New\",\"Mauritius\",\"Senegal\",\"Bhutan\",\"Malawi\",\"Madagascar\",\"Bahamas,\",\"Gabon\",\"Suriname\",\"Guam\",\"Liechtenstein\",\"Swaziland\",\"Burkina\",\"Togo\",\"Curacao\",\"Mauritania\",\"Barbados\",\"Niger\",\"Aruba\",\"Benin\",\"Guinea\",\"Mali\",\"Fiji\",\"Congo,\",\"Virgin\",\"Lesotho\",\"South\",\"Bermuda\",\"French\",\"Jersey\",\"Belize\",\"Andorra\",\"Guyana\",\"Cayman\",\"Haiti\",\"Rwanda\",\"Saint\",\"Djibouti\",\"Seychelles\",\"Somalia\",\"Antigua\",\"Greenland\",\"Cabo\",\"Eritrea\",\"Burundi\",\"Liberia\",\"Maldives\",\"Faroe\",\"Gambia,\",\"Chad\",\"Micronesia,\",\"Grenada\",\"Central\",\"Turks\",\"Gibraltar\",\"American\",\"Sierra\",\"Saint\",\"Saint\",\"Timor-Leste\",\"Equatorial\",\"Samoa\",\"Dominica\",\"Western\",\"Solomon\",\"Sao\",\"British\",\"Vanuatu\",\"Guinea-Bissau\",\"Tonga\",\"Saint\",\"Comoros\",\"Cook\",\"Kiribati\",\"Montserrat\",\"Nauru\",\"Falkland\",\"Saint\",\"Niue\",\"Gaza\",\"Malta\",\"Northern\"],\"reversescale\":true,\"text\":[\"China\",\"United States\",\"European\",\"Russia\",\"Japan\",\"India\",\"Germany\",\"Canada\",\"Brazil\",\"Korea,\",\"France\",\"United Kingdom\",\"Italy\",\"Taiwan\",\"Spain\",\"Mexico\",\"Saudi\",\"Australia\",\"South\",\"Turkey\",\"Iran\",\"Indonesia\",\"Ukraine\",\"Thailand\",\"Poland\",\"Egypt\",\"Sweden\",\"Norway\",\"Malaysia\",\"Argentina\",\"Netherlands\",\"Vietnam\",\"Venezuela\",\"United Arab Emirates\",\"Finland\",\"Belgium\",\"Kazakhstan\",\"Pakistan\",\"Philippines\",\"Austria\",\"Chile\",\"Czechia\",\"Israel\",\"Switzerland\",\"Greece\",\"Iraq\",\"Romania\",\"Kuwait\",\"Colombia\",\"Singapore\",\"Portugal\",\"Uzbekistan\",\"Hong\",\"Algeria\",\"Bangladesh\",\"New\",\"Bulgaria\",\"Belarus\",\"Peru\",\"Denmark\",\"Qatar\",\"Slovakia\",\"Libya\",\"Serbia\",\"Morocco\",\"Syria\",\"Nigeria\",\"Ireland\",\"Hungary\",\"Oman\",\"Ecuador\",\"Puerto\",\"Azerbaijan\",\"Croatia\",\"Iceland\",\"Cuba\",\"Korea,\",\"Dominican\",\"Jordan\",\"Tajikistan\",\"Tunisia\",\"Slovenia\",\"Lebanon\",\"Bosnia\",\"Turkmenistan\",\"Bahrain\",\"Mozambique\",\"Ghana\",\"Sri\",\"Kyrgyzstan\",\"Lithuania\",\"Uruguay\",\"Costa\",\"Guatemala\",\"Georgia\",\"Trinidad\",\"Zambia\",\"Paraguay\",\"Albania\",\"Burma\",\"Estonia\",\"Congo,\",\"Panama\",\"Latvia\",\"Macedonia\",\"Zimbabwe\",\"Kenya\",\"Bolivia\",\"Luxembourg\",\"Sudan\",\"El\",\"Cameroon\",\"West\",\"Ethiopia\",\"Armenia\",\"Honduras\",\"Angola\",\"Cote\",\"Tanzania\",\"Nicaragua\",\"Moldova\",\"Cyprus\",\"Macau\",\"Namibia\",\"Mongolia\",\"Afghanistan\",\"Yemen\",\"Brunei\",\"Cambodia\",\"Montenegro\",\"Nepal\",\"Botswana\",\"Papua\",\"Jamaica\",\"Kosovo\",\"Laos\",\"Uganda\",\"New\",\"Mauritius\",\"Senegal\",\"Bhutan\",\"Malawi\",\"Madagascar\",\"Bahamas,\",\"Gabon\",\"Suriname\",\"Guam\",\"Liechtenstein\",\"Swaziland\",\"Burkina\",\"Togo\",\"Curacao\",\"Mauritania\",\"Barbados\",\"Niger\",\"Aruba\",\"Benin\",\"Guinea\",\"Mali\",\"Fiji\",\"Congo,\",\"Virgin\",\"Lesotho\",\"South\",\"Bermuda\",\"French\",\"Jersey\",\"Belize\",\"Andorra\",\"Guyana\",\"Cayman\",\"Haiti\",\"Rwanda\",\"Saint\",\"Djibouti\",\"Seychelles\",\"Somalia\",\"Antigua\",\"Greenland\",\"Cabo\",\"Eritrea\",\"Burundi\",\"Liberia\",\"Maldives\",\"Faroe\",\"Gambia,\",\"Chad\",\"Micronesia,\",\"Grenada\",\"Central\",\"Turks\",\"Gibraltar\",\"American\",\"Sierra\",\"Saint\",\"Saint\",\"Timor-Leste\",\"Equatorial\",\"Samoa\",\"Dominica\",\"Western\",\"Solomon\",\"Sao\",\"British\",\"Vanuatu\",\"Guinea-Bissau\",\"Tonga\",\"Saint\",\"Comoros\",\"Cook\",\"Kiribati\",\"Montserrat\",\"Nauru\",\"Falkland\",\"Saint\",\"Niue\",\"Gaza\",\"Malta\",\"Northern\"],\"z\":[5523000000000.0,3832000000000.0,2771000000000.0,1065000000000.0,921000000000.0,864700000000.0,540100000000.0,511000000000.0,483500000000.0,482400000000.0,451100000000.0,319100000000.0,303100000000.0,249500000000.0,243100000000.0,234000000000.0,231600000000.0,222600000000.0,211600000000.0,197000000000.0,195300000000.0,167500000000.0,159800000000.0,155900000000.0,139000000000.0,135600000000.0,130500000000.0,126400000000.0,118500000000.0,117100000000.0,116800000000.0,108300000000.0,97690000000.0,93280000000.0,82040000000.0,81890000000.0,80290000000.0,78890000000.0,75270000000.0,69750000000.0,63390000000.0,60550000000.0,59830000000.0,58010000000.0,57730000000.0,53410000000.0,50730000000.0,50000000000.0,49380000000.0,47180000000.0,46250000000.0,45210000000.0,44210000000.0,42870000000.0,41520000000.0,40300000000.0,37990000000.0,37880000000.0,35690000000.0,31960000000.0,30530000000.0,28360000000.0,27540000000.0,26910000000.0,26700000000.0,25700000000.0,24780000000.0,24240000000.0,21550000000.0,20360000000.0,19020000000.0,18620000000.0,17790000000.0,16970000000.0,16940000000.0,16200000000.0,16000000000.0,15140000000.0,14560000000.0,14420000000.0,13310000000.0,13020000000.0,12940000000.0,12560000000.0,11750000000.0,11690000000.0,11280000000.0,10580000000.0,10170000000.0,9943000000.0,9664000000.0,9559000000.0,8987000000.0,8915000000.0,8468000000.0,8365000000.0,8327000000.0,8125000000.0,7793000000.0,7765000000.0,7417000000.0,7292000000.0,7144000000.0,7141000000.0,6960000000.0,6831000000.0,6627000000.0,6456000000.0,6108000000.0,5665000000.0,5665000000.0,5535000000.0,5312000000.0,5227000000.0,5043000000.0,5036000000.0,4842000000.0,4731000000.0,4545000000.0,4412000000.0,4305000000.0,4296000000.0,4291000000.0,4238000000.0,4204000000.0,3893000000.0,3838000000.0,3766000000.0,3553000000.0,3465000000.0,3239000000.0,3213000000.0,3116000000.0,3008000000.0,2887000000.0,2874000000.0,2821000000.0,2716000000.0,2658000000.0,2586000000.0,2085000000.0,2027000000.0,1883000000.0,1716000000.0,1680000000.0,1572000000.0,1566000000.0,1360000000.0,1295000000.0,985500000.0,976000000.0,968000000.0,962600000.0,938000000.0,930200000.0,920700000.0,911000000.0,903000000.0,882600000.0,777600000.0,740000000.0,723500000.0,707000000.0,694100000.0,664200000.0,652900000.0,630100000.0,605000000.0,562400000.0,558000000.0,545900000.0,452000000.0,365500000.0,336400000.0,311600000.0,293900000.0,293000000.0,293000000.0,292000000.0,285500000.0,284000000.0,282900000.0,276900000.0,267100000.0,261300000.0,218600000.0,190700000.0,178600000.0,178000000.0,168300000.0,167400000.0,160000000.0,146000000.0,134900000.0,130200000.0,127400000.0,125300000.0,93000000.0,90400000.0,89750000.0,83700000.0,79050000.0,60450000.0,51150000.0,49290000.0,46500000.0,44640000.0,39990000.0,39990000.0,28950000.0,24180000.0,23250000.0,23250000.0,11160000.0,7440000.0,2790000.0,202000.0,174700.0,48300.0],\"type\":\"choropleth\"}],                        {\"geo\":{\"projection\":{\"type\":\"mercator\"},\"showframe\":false},\"title\":{\"text\":\"2014 Power Consumption\"},\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#f2f5fa\"},\"error_y\":{\"color\":\"#f2f5fa\"},\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scattergl\"}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"baxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#506784\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"header\":{\"fill\":{\"color\":\"#2a3f5f\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#f2f5fa\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"rgb(17,17,17)\",\"plot_bgcolor\":\"rgb(17,17,17)\",\"polar\":{\"bgcolor\":\"rgb(17,17,17)\",\"angularaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"rgb(17,17,17)\",\"aaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#f2f5fa\"}},\"annotationdefaults\":{\"arrowcolor\":\"#f2f5fa\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"rgb(17,17,17)\",\"landcolor\":\"rgb(17,17,17)\",\"subunitcolor\":\"#506784\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"rgb(17,17,17)\"},\"title\":{\"x\":0.05},\"updatemenudefaults\":{\"bgcolor\":\"#506784\",\"borderwidth\":0},\"sliderdefaults\":{\"bgcolor\":\"#C8D4E3\",\"borderwidth\":1,\"bordercolor\":\"rgb(17,17,17)\",\"tickwidth\":0},\"mapbox\":{\"style\":\"dark\"}}}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('848cd290-145c-438e-a641-c9d6b2808299');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.read_csv('2014_World_Power_Consumption')\n",
    "# df.head()\n",
    "data = dict(\n",
    "    type = 'choropleth',\n",
    "    colorscale = 'viridis',\n",
    "    reversescale = True,\n",
    "    locations = df['Country'],\n",
    "    locationmode = 'country names',\n",
    "    z = df['Power Consumption KWH'],\n",
    "    text = df['Country'],\n",
    "    colorbar = {\n",
    "        'title': 'Power Consumption KWH',\n",
    "    }\n",
    ")\n",
    "layout = dict(\n",
    "    title = '2014 Power Consumption',\n",
    "    geo = dict(\n",
    "        showframe = False,\n",
    "        projection = {\n",
    "            'type': 'mercator',\n",
    "        },\n",
    "    )\n",
    ")\n",
    "choromap4 = go.Figure(\n",
    "    data = [data],\n",
    "    layout = layout,\n",
    ")\n",
    "iplot(\n",
    "    choromap4,\n",
    "    validate=False,\n",
    ")"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2024-07-12T07:57:47.352798Z",
     "start_time": "2024-07-12T07:57:47.311909Z"
    }
   },
   "id": "59ab9728694603be",
   "execution_count": 37
  },
  {
   "cell_type": "code",
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "data": [
        {
         "colorbar": {
          "title": {
           "text": "Voting Age Population"
          }
         },
         "colorscale": [
          [
           0.0,
           "#440154"
          ],
          [
           0.1111111111111111,
           "#482878"
          ],
          [
           0.2222222222222222,
           "#3e4989"
          ],
          [
           0.3333333333333333,
           "#31688e"
          ],
          [
           0.4444444444444444,
           "#26828e"
          ],
          [
           0.5555555555555556,
           "#1f9e89"
          ],
          [
           0.6666666666666666,
           "#35b779"
          ],
          [
           0.7777777777777778,
           "#6ece58"
          ],
          [
           0.8888888888888888,
           "#b5de2b"
          ],
          [
           1.0,
           "#fde725"
          ]
         ],
         "locationmode": "USA-states",
         "locations": [
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "District of Columbia",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"
         ],
         "reversescale": true,
         "text": [
          "Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",
          "Colorado",
          "Connecticut",
          "Delaware",
          "District of Columbia",
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconsin",
          "Wyoming"
         ],
         "z": [
          3707440.0,
          543763.0,
          4959270.0,
          2242740.0,
          2.8913129E7,
          3981208.0,
          2801375.0,
          715708.0,
          528848.0,
          1.5380947E7,
          7452696.0,
          1088335.0,
          1173727.0,
          9827043.0,
          4960376.0,
          2356209.0,
          2162442.0,
          3368684.0,
          3495847.0,
          1064779.0,
          4553853.0,
          5263550.0,
          7625576.0,
          4114820.0,
          2246931.0,
          4628500.0,
          785454.0,
          1396507.0,
          2105976.0,
          1047978.0,
          6847503.0,
          1573400.0,
          1.5344671E7,
          7496980.0,
          549955.0,
          8896930.0,
          2885093.0,
          3050747.0,
          1.0037099E7,
          834983.0,
          3662322.0,
          631472.0,
          4976284.0,
          1.9185395E7,
          1978956.0,
          502242.0,
          6348827.0,
          5329782.0,
          1472642.0,
          4417273.0,
          441726.0
         ],
         "type": "choropleth"
        }
       ],
       "layout": {
        "geo": {
         "lakecolor": "rgb(85, 173, 240)",
         "scope": "usa",
         "showlakes": true
        },
        "template": {
         "data": {
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "bar": [
           {
            "error_x": {
             "color": "#f2f5fa"
            },
            "error_y": {
             "color": "#f2f5fa"
            },
            "marker": {
             "line": {
              "color": "rgb(17,17,17)",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "baxis": {
             "endlinecolor": "#A2B1C6",
             "gridcolor": "#506784",
             "linecolor": "#506784",
             "minorgridcolor": "#506784",
             "startlinecolor": "#A2B1C6"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "color": "#283442"
             }
            },
            "type": "scatter"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0.0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1.0,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#506784"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "header": {
             "fill": {
              "color": "#2a3f5f"
             },
             "line": {
              "color": "rgb(17,17,17)"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#f2f5fa",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0.0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1.0,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#f2f5fa"
          },
          "geo": {
           "bgcolor": "rgb(17,17,17)",
           "lakecolor": "rgb(17,17,17)",
           "landcolor": "rgb(17,17,17)",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "#506784"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "dark"
          },
          "paper_bgcolor": "rgb(17,17,17)",
          "plot_bgcolor": "rgb(17,17,17)",
          "polar": {
           "angularaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "radialaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "yaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           },
           "zaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "#C8D4E3"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#f2f5fa"
           }
          },
          "sliderdefaults": {
           "bgcolor": "#C8D4E3",
           "bordercolor": "rgb(17,17,17)",
           "borderwidth": 1,
           "tickwidth": 0
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           },
           "bgcolor": "rgb(17,17,17)",
           "caxis": {
            "gridcolor": "#506784",
            "linecolor": "#506784",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "updatemenudefaults": {
           "bgcolor": "#506784",
           "borderwidth": 0
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "#283442",
           "linecolor": "#506784",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "#283442",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "2012 Election Data"
        }
       },
       "config": {
        "showLink": false,
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly"
       }
      },
      "text/html": "<div>                            <div id=\"8b4a34ff-dbc7-40a0-b014-d5f6cb77aa3e\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"8b4a34ff-dbc7-40a0-b014-d5f6cb77aa3e\")) {                    Plotly.newPlot(                        \"8b4a34ff-dbc7-40a0-b014-d5f6cb77aa3e\",                        [{\"colorbar\":{\"title\":{\"text\":\"Voting Age Population\"}},\"colorscale\":[[0.0,\"#440154\"],[0.1111111111111111,\"#482878\"],[0.2222222222222222,\"#3e4989\"],[0.3333333333333333,\"#31688e\"],[0.4444444444444444,\"#26828e\"],[0.5555555555555556,\"#1f9e89\"],[0.6666666666666666,\"#35b779\"],[0.7777777777777778,\"#6ece58\"],[0.8888888888888888,\"#b5de2b\"],[1.0,\"#fde725\"]],\"locationmode\":\"USA-states\",\"locations\":[\"AL\",\"AK\",\"AZ\",\"AR\",\"CA\",\"CO\",\"CT\",\"DE\",\"District of Columbia\",\"FL\",\"GA\",\"HI\",\"ID\",\"IL\",\"IN\",\"IA\",\"KS\",\"KY\",\"LA\",\"ME\",\"MD\",\"MA\",\"MI\",\"MN\",\"MS\",\"MO\",\"MT\",\"NE\",\"NV\",\"NH\",\"NJ\",\"NM\",\"NY\",\"NC\",\"ND\",\"OH\",\"OK\",\"OR\",\"PA\",\"RI\",\"SC\",\"SD\",\"TN\",\"TX\",\"UT\",\"VT\",\"VA\",\"WA\",\"WV\",\"WI\",\"WY\"],\"reversescale\":true,\"text\":[\"Alabama\",\"Alaska\",\"Arizona\",\"Arkansas\",\"California\",\"Colorado\",\"Connecticut\",\"Delaware\",\"District of Columbia\",\"Florida\",\"Georgia\",\"Hawaii\",\"Idaho\",\"Illinois\",\"Indiana\",\"Iowa\",\"Kansas\",\"Kentucky\",\"Louisiana\",\"Maine\",\"Maryland\",\"Massachusetts\",\"Michigan\",\"Minnesota\",\"Mississippi\",\"Missouri\",\"Montana\",\"Nebraska\",\"Nevada\",\"New Hampshire\",\"New Jersey\",\"New Mexico\",\"New York\",\"North Carolina\",\"North Dakota\",\"Ohio\",\"Oklahoma\",\"Oregon\",\"Pennsylvania\",\"Rhode Island\",\"South Carolina\",\"South Dakota\",\"Tennessee\",\"Texas\",\"Utah\",\"Vermont\",\"Virginia\",\"Washington\",\"West Virginia\",\"Wisconsin\",\"Wyoming\"],\"z\":[3707440.0,543763.0,4959270.0,2242740.0,28913129.0,3981208.0,2801375.0,715708.0,528848.0,15380947.0,7452696.0,1088335.0,1173727.0,9827043.0,4960376.0,2356209.0,2162442.0,3368684.0,3495847.0,1064779.0,4553853.0,5263550.0,7625576.0,4114820.0,2246931.0,4628500.0,785454.0,1396507.0,2105976.0,1047978.0,6847503.0,1573400.0,15344671.0,7496980.0,549955.0,8896930.0,2885093.0,3050747.0,10037099.0,834983.0,3662322.0,631472.0,4976284.0,19185395.0,1978956.0,502242.0,6348827.0,5329782.0,1472642.0,4417273.0,441726.0],\"type\":\"choropleth\"}],                        {\"geo\":{\"lakecolor\":\"rgb(85, 173, 240)\",\"scope\":\"usa\",\"showlakes\":true},\"template\":{\"data\":{\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"bar\":[{\"error_x\":{\"color\":\"#f2f5fa\"},\"error_y\":{\"color\":\"#f2f5fa\"},\"marker\":{\"line\":{\"color\":\"rgb(17,17,17)\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"baxis\":{\"endlinecolor\":\"#A2B1C6\",\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"minorgridcolor\":\"#506784\",\"startlinecolor\":\"#A2B1C6\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatter\":[{\"marker\":{\"line\":{\"color\":\"#283442\"}},\"type\":\"scatter\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#506784\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"header\":{\"fill\":{\"color\":\"#2a3f5f\"},\"line\":{\"color\":\"rgb(17,17,17)\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#f2f5fa\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#f2f5fa\"},\"geo\":{\"bgcolor\":\"rgb(17,17,17)\",\"lakecolor\":\"rgb(17,17,17)\",\"landcolor\":\"rgb(17,17,17)\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"#506784\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"dark\"},\"paper_bgcolor\":\"rgb(17,17,17)\",\"plot_bgcolor\":\"rgb(17,17,17)\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"radialaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"yaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"},\"zaxis\":{\"backgroundcolor\":\"rgb(17,17,17)\",\"gridcolor\":\"#506784\",\"gridwidth\":2,\"linecolor\":\"#506784\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"#C8D4E3\"}},\"shapedefaults\":{\"line\":{\"color\":\"#f2f5fa\"}},\"sliderdefaults\":{\"bgcolor\":\"#C8D4E3\",\"bordercolor\":\"rgb(17,17,17)\",\"borderwidth\":1,\"tickwidth\":0},\"ternary\":{\"aaxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"},\"bgcolor\":\"rgb(17,17,17)\",\"caxis\":{\"gridcolor\":\"#506784\",\"linecolor\":\"#506784\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"updatemenudefaults\":{\"bgcolor\":\"#506784\",\"borderwidth\":0},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"#283442\",\"linecolor\":\"#506784\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"#283442\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"2012 Election Data\"}},                        {\"responsive\": true}                    ).then(function(){\n                            \nvar gd = document.getElementById('8b4a34ff-dbc7-40a0-b014-d5f6cb77aa3e');\nvar x = new MutationObserver(function (mutations, observer) {{\n        var display = window.getComputedStyle(gd).display;\n        if (!display || display === 'none') {{\n            console.log([gd, 'removed!']);\n            Plotly.purge(gd);\n            observer.disconnect();\n        }}\n}});\n\n// Listen for the removal of the full notebook cells\nvar notebookContainer = gd.closest('#notebook-container');\nif (notebookContainer) {{\n    x.observe(notebookContainer, {childList: true});\n}}\n\n// Listen for the clearing of the current output cell\nvar outputEl = gd.closest('.output');\nif (outputEl) {{\n    x.observe(outputEl, {childList: true});\n}}\n\n                        })                };                });            </script>        </div>"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "usdf = pd.read_csv('2012_Election_Data')\n",
    "usdf.head()\n",
    "data = dict(\n",
    "    type = 'choropleth',\n",
    "    colorscale = 'viridis',\n",
    "    reversescale = True, #colours look better, makes darker colours with higher quantity\n",
    "    locations = usdf['State Abv'],\n",
    "    z = usdf['Voting-Age Population (VAP)'],\n",
    "    locationmode = 'USA-states',\n",
    "    text = usdf['State'],\n",
    "    colorbar = {\n",
    "        'title': 'Voting Age Population',\n",
    "    }\n",
    ")\n",
    "layout = dict(\n",
    "    title='2012 Election Data',\n",
    "    geo = dict(\n",
    "        scope = 'usa',\n",
    "        showlakes = True,\n",
    "        lakecolor = 'rgb(85, 173, 240)',\n",
    "    )\n",
    ")\n",
    "choromap5 = go.Figure(\n",
    "    data = [data],\n",
    "    layout = layout,\n",
    ")\n",
    "iplot(choromap5, validate=True)"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2024-07-12T08:07:02.320021Z",
     "start_time": "2024-07-12T08:07:02.256187Z"
    }
   },
   "id": "afdda2d5d5138724",
   "execution_count": 41
  },
  {
   "cell_type": "code",
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false
   },
   "id": "8d64314e3324f219"
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
