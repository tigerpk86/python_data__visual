#!__*__coding:utf-8__*__
import os
import pandas as pd

######################################
csv = r"data_draw_korea.csv"

m = pd.read_csv(csv, encoding="utf-8", engine="python")
print(m)

import korea_showMap
korea_showMap.drawKorea('면적', m, '광역시도', '행정구역', 'binary')

