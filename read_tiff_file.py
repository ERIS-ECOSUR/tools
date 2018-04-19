#!/usr/bin/env python
# ECOSUR-ERIS Project
# Author: Javier Arellano-Verdejo
# Created: 19/04/2018
# Last updated: 19/04/2018

import gdal

def read_tiff_file(file_name):
  ds = gdal.Open(file_name)
  band = ds.GetRasterBand(1)
  arr = band.ReadAsArray()
  return arr

if __name__ == "__main__":
    data = read_tiff_file("LC80190472016212LGN00_B1.TIF")
    [cols, rows] = data.shape
    print("Cols: ", cols)
    print("Rows: ", rows)
