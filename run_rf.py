# -*- coding: utf-8 -*-
"""
read jlib file and run the RF model

sklearn version 1.2.2
"""
import joblib
import pandas as pd
import numpy as np


# Input file name
inp_f = r"toc_texture.csv"

# model file
rf_f = r"model.jlib"

# Output file
out_f = r"output.csv"



# Loading the model
with open(rf_f, "rb") as f:
    model = joblib.load(f)

# data for BD
data_all = pd.read_csv(inp_f)
dat_bd = data_all[[ "Sand%", "Clay%", "OM%" ]].values.tolist()

# Bulk density estimative
bd_estimates = model.predict(dat_bd)

# Organizing data to save as csv
dat = np.array(dat_bd)
silt = 100 - np.array(dat[:,0]) - np.array(dat[:,1])
data_out = np.c_[dat[:,0], dat[:,1], silt, dat[:,2], bd_estimates]

# Saving file
df = pd.DataFrame(data_out, columns = ["Sand%", "Clay%", "Silt%", "OM%", "BD_[g/cm3]"])
df.to_csv(out_f,index=False)




