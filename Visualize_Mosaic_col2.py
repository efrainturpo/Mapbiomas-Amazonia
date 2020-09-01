#Script para mostras mosaicos col2 MapbiomasAmazonia
#by:EYTC
# Param
years = [2000,2018]
pais = 'PERU'
code_region = '702'

import ee
from ee_plugin import Map
for num in years:
    image = ee.ImageCollection("projects/mapbiomas-raisg/MOSAICOS/workspace-c2-v2")\
              .filterMetadata('year', 'equals', num)\
              .filterMetadata('region_code', 'equals', code_region)\
              .median()
    descrip = 'Mosaic'+str(num)
    Map.addLayer(image, {'bands': ['swir1_median','nir_median','red_median'], 'min': 200, 'max': 5000},descrip,False)
   