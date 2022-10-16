# -*- coding: utf-8 -*-
##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2022
## Author: taro.katayama@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import modules
import sys, os, arcpy

