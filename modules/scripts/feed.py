# Importing modules...
import numpy as np
import plotly.graph_objects as go

class Feed: 
    def __init__(self, title, res=(480,480), graphical=False):
        self.title = title
        self.graphical = graphical # Toggle to activate graphical mode
        self.res = res # Change feed dimensions 

        # Create Figure 
        self.figure = go.Figure(
            layout=go.Layout(
                height=700, 
                width=900, 
                title=go.layout.Title(text=self.title)
            )
        )

        self.figure.update_yaxes(
            scaleanchor="x",
            scaleratio=1
        )
        
        self.figure.update_layout(
            xaxis_title='x',
            yaxis_title='y',
            plot_bgcolor='white',
            font=dict(
                family='Arial',
                size=15,
                color='black'
            ),
            xaxis=dict(
                gridcolor='lightgray',
                dtick = res[0]/10,
                range=[0, self.res[0]]
            ),
            yaxis=dict(
                gridcolor='lightgray',
                dtick = res[1]/10,
                range=[self.res[1], 0]
            )
        )

        self.figure.add_shape(
            type='rect',
            x0=0, y0=0, x1=res[0], y1=res[1],
            line=dict(color='black'),
        )


    def add_points(self, point, name, color=None):
        self.figure.add_trace(
            go.Scatter(
                x=point[0],
                y=point[1],
                mode='markers',
                marker=dict(
                    size=5,
                    opacity=0.80,
                    color=color
                ),
                name=name,
                legendgroup='Points',
                legendgrouptitle_text='Points',
                showlegend=self.graphical
            )
        )