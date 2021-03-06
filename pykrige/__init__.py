__author__ = 'Benjamin S. Murphy'
__version__ = '1.4.dev0'
__doc__ = """Code by Benjamin S. Murphy
bscott.murphy@gmail.com

Dependencies:
    numpy
    scipy
    matplotlib
    Cython

Modules:
    ok: Contains class OrdinaryKriging, which is a convenience class
        for easy access to 2D ordinary kriging.
    uk: Contains class UniversalKriging, which provides more control over
        2D kriging by utilizing drift terms. Supported drift terms
        currently include point-logarithmic, regional linear, and external
        z-scalar. Generic functions of the spatial coordinates may also be
        supplied to provide drift terms, or the point-by-point values of a drift
        term may be supplied.
    ok3d: Contains class OrdinaryKriging3D, which provides support for
        3D ordinary kriging.
    uk3d: Contains class UniversalKriging3D, which provide support for
        3D universal kriging. A regional linear drift is the only drift term
        currently supported, but generic drift functions or point-by-point
        values of a drift term may also be supplied.
    kriging_tools: Contains a set of functions to work with *.asc files.
    variogram_models: Contains the definitions for the implemented variogram
        models. Note that the utilized formulas are as presented in Kitanidis,
        so the exact definition of the range (specifically, the associated
        scaling of that value) may differ slightly from other sources.
    core: Contains the backbone functions of the package that are called by
        both the various kriging classes. The functions were consolidated here
        in order to reduce redundancy in the code.
    test: Contains the test script.

References:
    P.K. Kitanidis, Introduction to Geostatistics: Applications in Hydrogeology,
    (Cambridge University Press, 1997) 272 p.
    
Copyright (c) 2015-2016 Benjamin S. Murphy
"""

from . import kriging_tools as kt
from .ok import OrdinaryKriging
from .uk import UniversalKriging
from .ok3d import OrdinaryKriging3D
from .uk3d import UniversalKriging3D

__all__ = ['ok', 'uk', 'ok3d', 'uk3d', 'kriging_tools']
