
#gdal should be installed

from subprocess import call
import os

mar_extent = [68, 10, 88, 30] # xmin, ymin, xmax, ymax


def cropRaster(in_raster_path, out_raster_path, extent, epsg_code = '4326'):
    SC = ("gdalwarp -t_srs EPSG:%s -te %f %f %f %f %s %s" 
          % (epsg_code, extent[0], extent[1], 
             extent[2], extent[3], in_raster_path, out_raster_path))
    call(SC, shell=True)
   


