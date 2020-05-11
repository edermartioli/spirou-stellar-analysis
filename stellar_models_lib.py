# -*- coding: iso-8859-1 -*-
"""
    Created on May 11 2020
    
    Description: python library to use a library of BT-Settl stellar models
    
    @author: Eder Martioli <martioli@iap.fr>
    
    Institut d'Astrophysique de Paris, France.
    
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys

import astropy.io.fits as fits
import numpy as np
import json


def get_BTSettl_spectrum_info_from_fits(filename) :
    
    """
        Get information in stellar model FITS header
        
        :param filename: string, input stellar model FITS file name

        :return loc: dict, dictionary containing information on input stellar model
        """

    loc = {}
    hdr = fits.getheader(filename,1)
    # store filename and filepath
    loc['filename'] = os.path.basename(filename)
    loc['filepath'] = os.path.abspath(filename)
    # [K] effective temperature
    loc['teff'] = hdr['TEFF']
    # [cm/s^2] log (surface gravity)
    loc['logg'] = hdr['LOGG']
    # [Fe/H] metallicity (re. sol. - Caffau &a 2011)
    loc['feh'] = hdr['METAL']
    # [a/Fe] alpha element enhancement
    loc['alpha'] = hdr['ALPHA']
    
    return loc


def get_BTSettl_best_model_file (modeldb, teff=5777., logg=4.4374, feh=0.0) :
    
    """
        Get file path of best model in input database
        
        :param modeldb: string, json database file name
        :param teff: float, input effective temperature [K]
        :param logg: float, input log of surface gravity
        :param feh: float, input [Fe/H] metallicity
        
        :return filepath: string, file path for best model matching input params
        """

    # load json database file containig all models in the library
    try :
        with open(modeldb, 'r') as f:
            datastore = json.load(f)
    except :
        print("ERROR: could not open models database file ",modeldb)
        exit()

    mindteff, mindlogg, mindfeh = 1.e6, 1.e6, 1.e6
    minkey = None

    # loop over all entried in the database to get best matched model file
    for key in datastore.keys() :
        dteff = np.abs(datastore[key]['teff'] - teff)
        dlogg = np.abs(datastore[key]['logg'] - logg)
        dfeh = np.abs(datastore[key]['feh'] - feh)
        
        if dteff <= mindteff and dlogg <= mindlogg and dfeh <= mindfeh :
            mindteff = dteff
            mindlogg = dlogg
            mindfeh = dfeh
            minkey = key

    # return best model file path
    return datastore[minkey]['filepath']
