with import <nixpkgs> {};
(python39.withPackages(ps: with ps;
[cycler
kiwisolver
matplotlib
networkx
numpy
openpyxl
pandas
plotly
prettytable
pyparsing
python-dateutil
pytz
scipy
six
tenacity
wcwidth
xlrd
])).env
