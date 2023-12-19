
<p align="center">
  <a><img src="https://github.com/infoleon/BD_PTF_Br/blob/main/logo/LOGO_plot_obs_predic.png?raw=true" alt="Logo" width="350"/></a>
  <br />
  <br />
  

</p>



## Setup

Dedicated to host PTF to predict bulk density (g cm-3) for Brazilian soils.

The file "model.jlib" contains the trained model ("joblib" format, version 1.2.0), which can be loaded as a scikit-learn Random Forest Regressor. The model was fitted using scikit-learn version was 1.2.2..

For the other libraries used in this script:
pandas version 1.5.3
numpy version 1.23.5

To run the example, download the files:
run_rf.py
model.jlib
toc_texture.csv

Then run the Python script "run_rf.py".

The model was fitted using the <a href="https://doi.org/10.2136/vzj2017.05.0095">HYBRAS soil dataset</a> (Ottoni et al. 2018)

## References
Ottoni, M. V., Ottoni Filho, T. B., Schaap, M. G., LopesAssad, M. L. R., and Rotunno Filho, O. C.: Hydrophysical Database for Brazilian Soils (HYBRAS) and Pedotransfer Functions for Water Retention, Vadose Zone J., 17, 170095, 2018
https://doi.org/10.2136/vzj2017.05.0095





