# -*- coding: iso-8859-1 -*-

"""
    Created on May 11 2020
    
    Description: This routine selects the BT-Settl stellar model closest to the input parameters: Teff, log(g), [Fe/H]
    
    @author: Eder Martioli <martioli@iap.fr>
    
    Institut d'Astrophysique de Paris, France.
    
    Simple usage example:
    
    python select_stellar_model.py --db=stellar_models_db.json --teff=3700 --logg=4.0 --feh=0.0
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

from optparse import OptionParser
import os,sys

import stellar_models_lib

parser = OptionParser()
parser.add_option("-d", "--db", dest="db", help="Input database json file",type='string',default='')
parser.add_option("-T", "--teff", dest="teff", help="Effective temperature [K]",type='string',default='')
parser.add_option("-g", "--logg", dest="logg", help="Surface gravity",type='string',default='')
parser.add_option("-m", "--feh", dest="feh", help="Metallicity [Fe/H]",type='string',default='')
parser.add_option("-v", action="store_true", dest="verbose", help="verbose", default=False)

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print("Error: check usage with create_stellar_model_db.py -h ")
    sys.exit(1)

if options.verbose:
    print('Input database json file: ', options.db)
    print('Effective temperature [K]: ', options.teff)
    print('Surface gravity: ', options.logg)
    print('Metallicity [Fe/H]: ', options.feh)

best_model_filepath = stellar_models_lib.get_BTSettl_best_model_file (options.db, teff=float(options.teff), logg=float(options.logg), feh=float(options.feh))

print("Selected model: ", best_model_filepath)
