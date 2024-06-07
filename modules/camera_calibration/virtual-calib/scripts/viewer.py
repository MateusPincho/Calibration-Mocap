# Importing modules...
import numpy as np
import plotly.graph_objects as go

class Viewer: 
    def __init__(self, title, graphical=False, size=5):
        self.title = title
        self.graphical = graphical # Toggle to activate graphical mode
        self.size = size # Change graph dimensions 

        # Create Figure 
        self.figure = go.Figure(
            layout=go.Layout(
                height=700, 
                width=900,
                title=go.layout.Title(text=self.title)
            )
        )

        # Set up layout enviroment
        self.figure.update_layout(
            scene_aspectmode='cube',
            scene = dict(
                xaxis_title='x'*self.graphical,
                yaxis_title='y'*self.graphical, 
                zaxis_title='z'*self.graphical, 
                xaxis=dict(
                    range=[-self.size,self.size],
                    showbackground=self.graphical,
                    showticklabels=self.graphical,
                    showaxeslabels=self.graphical,
                    showgrid=self.graphical,
                    showspikes=self.graphical
                    ),
                yaxis=dict(
                    range=[-self.size,self.size],
                    showbackground=self.graphical,
                    showticklabels=self.graphical,
                    showaxeslabels=self.graphical,
                    showgrid=self.graphical,
                    showspikes=self.graphical
                    ), 
                zaxis=dict(
                    range=[-self.size,self.size],
                    showbackground=self.graphical,
                    showticklabels=self.graphical,
                    showaxeslabels=self.graphical,
                    showgrid=self.graphical,
                    showspikes=self.graphical
                    )
            )
        )

        # Change camera settings
        self.figure.update_layout(
            scene=dict(
                camera=dict(
                    projection=dict(
                        type='orthographic'
                    )
                )
            )
        )

    def add_frame(self, frame, name, axis_size=1, color=None):

        # Set default colors
        axis_name_list = ['x', 'y', 'z']
        axis_color_list = ['red', 'green', 'blue']

        self.figure.add_trace(
            go.Scatter3d(
                x=frame.t[0],
                y=frame.t[1],
                z=frame.t[2],
                mode='markers',
                marker=dict(
                    size=4,
                    opacity=0.80,
                    color=color
                ),
                name=name,
                legendgroup='Frames',
                legendgrouptitle_text='Frames',
                showlegend=True
            )
        )

        for axis, axis_color in enumerate(axis_color_list):

            arrow = np.hstack((frame.t, frame.t + frame.R[:,axis].reshape(-1,1) * axis_size)) # Arrow of an axis

            self.figure.add_trace(
                go.Scatter3d(
                    x=arrow[0], 
                    y=arrow[1],
                    z=arrow[2], 
                    mode='lines',
                    line=dict(
                        width=2,
                        color=axis_color
                        ),
                    showlegend=False,
                    name=axis_name_list[axis]+name,
                    hoverinfo = None if self.graphical else 'skip'
                )
            )

    def add_points(self, point, name, color=None):
        self.figure.add_trace(
            go.Scatter3d(
                x=point[0],
                y=point[1],
                z=point[2],
                mode='markers',
                marker=dict(
                    size=3,
                    opacity=0.80,
                    color=color
                ),
                name=name,
                legendgroup='Points',
                legendgrouptitle_text='Points',
                showlegend=self.graphical
            )
        )

    def add_solid(self, vertices, name, color=None):
        self.figure.add_trace(
            go.Mesh3d(
                x=vertices[0],
                y=vertices[1],
                z=vertices[2],
                alphahull=0,
                color=color,
                flatshading=True,
                name=name,
                legendgroup='Objects',
                legendgrouptitle_text='Objects',
                showlegend=self.graphical
            )
        )
    def add_plane(self, vertices, name, color=None):
        self.figure.add_trace(
            go.Mesh3d(
                x=vertices[0],
                y=vertices[1],
                z=vertices[2],
                opacity=0.5,
                color=color,
                flatshading=True,
                name=name,
                legendgroup='References',
                legendgrouptitle_text='References',
                hoverinfo='skip',
                showlegend=True
            )
        )

    def connect_points_to_frame(self, points, frame, color):
        for p in range(points.shape[1]):
            edge = np.hstack((frame.t, points[:,[p]])) # Arrow of an axis
            self.figure.add_trace(
                go.Scatter3d(
                    x=edge[0], 
                    y=edge[1],
                    z=edge[2], 
                    mode='lines',
                    line=dict(
                        width=1,
                        color=color
                        ),
                    showlegend=False,
                    hoverinfo='skip'
                )
            )

    def camera_shape(self, points, frame, color):
        for p in range(points.shape[1]):
            edge = np.hstack((frame.t,points[:,[p]])) # Arrow of an axis
            self.figure.add_trace(
                go.Scatter3d(
                    x=edge[0], 
                    y=edge[1],
                    z=edge[2], 
                    mode='lines',
                    line=dict(
                        width=3,
                        color=color
                        ),
                    showlegend=False,
                    hoverinfo='skip'
                )
            )

        points = np.hstack([points, points[:,[0]]]) # Repeat first column in the last column

        self.figure.add_trace(
            go.Scatter3d(
                x=points[0],
                y=points[1],
                z=points[2],
                mode='lines',
                line=dict(
                    width=3,
                    color=color,
                    ),
                showlegend=False,
                hoverinfo='skip'
            )
        )

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

    def add_points(self, point, name, color=None):
        self.figure.add_trace(
            go.Scatter(
                x=point[0],
                y=point[1],
                mode='markers',
                marker=dict(
                    size=7,
                    opacity=0.80,
                    color=color
                ),
                name=name,
                legendgroup='Points',
                legendgrouptitle_text='Points',
                showlegend=self.graphical
            )
        )
