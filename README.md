# Bulk Density for Brazilian soils, from Soil Texture and Organic Matter Content
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<p align="center">
  <a><img src="https://github.com/infoleon/BD_PTF_Br/blob/main/logo/LOGO_plot_obs_predic.png?raw=true" alt="Logo" width="300"/></a>
</p>

## Setup

A random forest model to predict bulk density (g cm-3) for Brazilian soils from texture and organic matter.

The file "model.jlib" contains the trained model in "joblib" format (version 1.2.0), which can be loaded as a scikit-learn Random Forest Regressor. The model was fitted using scikit-learn version 1.2.2.

For the other libraries:
- pandas version 1.5.3
- numpy version 1.23.5

To install the required libraries, run the following command:

```bash
pip install pandas==1.5.3 numpy==1.23.5 scikit-learn==1.2.2
```

An example is also provided.
To run the example, download the following files:
- `run_rf.py`
- `model.jlib`
- `toc_texture.csv`

Then, execute the Python script "run_rf.py" with all the files in the same folder.


The model was fitted using the <a href="https://doi.org/10.2136/vzj2017.05.0095">HYBRAS soil dataset</a> (Ottoni et al. 2018)

## References
Ottoni, M. V., Ottoni Filho, T. B., Schaap, M. G., LopesAssad, M. L. R., and Rotunno Filho, O. C.: Hydrophysical Database for Brazilian Soils (HYBRAS) and Pedotransfer Functions for Water Retention, Vadose Zone J., 17, 170095, <a href="https://doi.org/10.2136/vzj2017.05.0095">https://doi.org/10.2136/vzj2017.05.0095</a>, 2018.




