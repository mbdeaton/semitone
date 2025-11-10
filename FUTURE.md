# Backlog for semitone
Somewhat in order of operation, first at top, delete as they're completed.

- Introduce pre-commit hooks for validating format and lint rules, not actually
  applying them. Let the developer do that manually. (Probably through
  pre-commit package, so it's configured in pyproject.toml and run by poetry.)
- Expand Scale to provide an interface that returns the frequencies in a given
  range. Common use would be to plot many octaves on a spiral plot.
- Convert all this inheritance to composition, probably using @abc.abstractmethod.
  Note, the has-a relationships might be: a scale has a collection of primaries,
  a picth-shifter, a translator, a plotter. And some types of scales (e.g.
  EqualTempered) have key. I don't know.
- Create interfaces where appropriate, to decouple the different components,
  especially 3rd-party stuff. E.g. wrap plotly in something like FigMaker.
