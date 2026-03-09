"""Create the figure for the repo README"""

import semitone as st

scale = st.Chromatic("C").extend(0, 2)
fig = st.SpiralPlot.draw((scale,))

fig.update_layout(showlegend=False)
fig.update_layout(font=dict(size=24))
fig.update_traces(marker_size=10)

fig.write_image("chrom_c.png")
