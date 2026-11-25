"""
reciperank - a small library to analyse Food.com recipes and build a fair ranking.

The package is organised in modules, each one with a single responsibility:
- `loader`   : load and clean RAW_recipes.csv and RAW_interactions.csv
- `scoring`  : Bayesian average and weighted scoring formulas
- `analysis` : statistical comparisons across categories, tags, and prep time
- `plots`    : charts built with matplotlib and seaborn
"""

__version__ = "0.1.0"
