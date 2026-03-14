"""Create the figures for the repo README"""

import semitone as st


def adjust_figure(figure):
    figure.update_layout(showlegend=False)
    figure.update_layout(font=dict(size=20))
    figure.update_traces(marker_size=7)
    figure.update_layout(width=360, height=310)


scale = st.Chromatic("C").extend(0, 2)
fig = st.SpiralPlot.draw((scale,))
adjust_figure(fig)
fig.write_image("chrom_c.png")

scale = st.HarmonicOctave("C", 19)
fig = st.SpiralPlot.draw((scale,))
adjust_figure(fig)
fig.write_image("harm_c.png")
