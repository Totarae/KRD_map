from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import pandas

df=pandas.DataFrame(columns=["X","Y"])
df['X']=[1,2,3,4,5]
df["Y"]=[5,6,4,5,3]
source=ColumnDataSource(df)mail

p=figure(plot_width=600,
         plot_height=600,
         title="Temperature Observations",
         tools='pan,wheel_zoom,reset',
         logo=None)
p.circle(x='X',y='Y',source=source, size=10)
p.xaxis.axis_label='Days'
p.yaxis.axis_label='Temperature'

output_file("Scatter_charts1.html")
show(p)