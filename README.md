# EarthSciPy

[![Documentation Status](https://readthedocs.org/projects/earthscipy/badge/?version=latest)](http://earthscipy.readthedocs.io/en/latest/?badge=latest)

Python library for [Earth science](https://en.wikipedia.org/wiki/Earth_science) (main in geology and petro science).

## Requirements

Python 3.3 or above.

## Testing

    python3 -m unittest tests/wells_tests.py

## Usage example

    from earthscipy.wells import *
  
    WF = WellField( "North" ) # create wells field
    w = Well( 'N_well#1', 0, 0 ) # create well
    w.add_geometry_step( 10, 0 ) # add inclinometry data
    w.add_geometry_step( 10, 45 )
    w.add_geometry_step( 10, 90 )
    w.add_geometry_step( 100, 0 )
    WF.add_well( w ) # add well to field

See `examples\wells_example.py` for more.
