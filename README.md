# 533 lab2
Group: Nathan Smith, Mitch Harris, Ryan Koenig

Package: quickscreen

The package provides very simple tools for quickly looking at data. The package will include three subpackages: one for plotting data, another for providing a few simple summary statistics, and another which does simple manipulations and linear correlation. The package is basically a wrapper for various matplotlib and pandas functionality.

The plotting subpackage will include two modules, one module will create a generic plotting class and the second module will use that generic class to allow a user to create specific plots. The summary subpackage will include a module which provides classes which take a pandas dataframe and auto-generates various statistics such as missing data counts, max/min, etc. The second module will use the classes to provide user functions for accessing the summaries. The analysis subpackage will include a module to provide simple datafilling functionality and a second module to perform and plot simple linear analysis on selected columns on the dataframe.
