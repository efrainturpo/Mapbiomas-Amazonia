#Script para mostras mosaicos anuales col2 MapbiomasAmazonia
#by:EYTC
# Param
code_region = '702'

import ee
from ee_plugin import Map

years = []
for x in range(34):
    years.append(x+1985)
print(years)

for num in years:
    image = ee.ImageCollection("projects/mapbiomas-raisg/MOSAICOS/workspace-c3-v2")\
              .filterMetadata('year', 'equals', num)\
              .filterMetadata('region_code', 'equals', code_region)\
              .mosaic()
    descrip = 'Mosaic'+str(num)
    Map.addLayer(image, {'bands': ['swir1_median','nir_median','red_median'], 'min': 200, 'max': 5000},descrip,False)
   
