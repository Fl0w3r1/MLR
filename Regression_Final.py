import numpy as np
X = [[3,11,1,23702],[4,13,0,33252],[4,13,1,30042],[4,12,0,9607],[4,12,1,52064],[2,15,1,69711],[5,9,1,51260],[3,10,1,24609],[5,13,1,36711],[2,16,0,72421,],[2,13,1,34976],[3,11,1,50414],[6,9,0,39172],[4,11,0,34467],[4,10,0,28065],[4,15,1,41108],[3,22,1,100232],[3,16,1,71035],[6,13,0,34358],[4,11,1,36947],[4,12,0,43773],[4,12,1,45044],[4,14,1,44141],[4,11,1,27912],[3,18,0,67211],[3,14,0,32328],[5,11,0,36995],[6,14,1,37351],[3,10,1,38074],[4,13,1,42819],[5,13,1,55990],[7,15,0,54149],[4,9,0,32114],[3,20,0,101543],[4,8,1,28017],[4,9,0,41471],[4,9,1,35907],[4,14,0,40204],[4,12,0,29435],[4,14,1,41698],[2,12,1,72575],[3,14,1,45876],[3,11,1,35800],[4,12,1,49326],[2,18,1,75692],[3,13,0,34448],[3,13,1,59804],[5,9,1,40120],[5,13,0,21818],[3,10,1,51428]]
Y = [6741,5559,6512,5284,8011,11208,7875,7059,8202,11298,6451,9077,6288,6235,8149,8186,14436,12620,7084,5987,10557,8688,9790,7487,8653,7141,6714,7011,8610,10308,7718,8668,8926,14351,7985,6218,5825,5179,5512,9476,10002,8674,6350,7039,10657,6589,7927,6066,6132,8873]

import pandas as pd
df2 = pd.DataFrame(X,columns=["oikogeneia","ekpaideusi","filo","eisodima"])
df2["exoda"] = pd.Series(Y)
df2

import matplotlib.pyplot as mpl
import statsmodels.formula.api as smf
model = smf.ols(formula="exoda ~ oikogeneia + ekpaideusi",data=df2) #model = smf.ols(formula="exoda ~ oikogeneia + ekpaideusi + filo + eisodima",data=df2)
results_formula = model.fit()
results_formula.params

x_surf, y_surf = np.meshgrid(np.linspace(df2.oikogeneia.min(),df2.oikogeneia.max(),100),np.linspace(df2.ekpaideusi.min(),df2.ekpaideusi.max(),100)) #x_surf, y_surf = np.meshgrid(np.linspace(df2.oikogeneia.min(),df2.oikogeneia.max(),100),np.linspace(df2.ekpaideusi.min(),df2.ekpaideusi.max(),100),np.linspace(df2.filo.min(),df2.filo.max(),100),np.linspace(df2.eisodima.min(),df2.eisodima.max(),100))
onlyX = pd.DataFrame({"oikogeneia":x_surf.ravel(),"ekpaideusi":y_surf.ravel()}) #onlyX = pd.DataFrame({"oikogeneia":x_surf.ravel(),"ekpaideusi":y_surf.ravel(),"filo":z_surf.ravel(),"eisodima":w_surf.ravel()})
fittedY = results_formula.predict(exog=onlyX)

fittedY = np.array(fittedY)

fig = mpl.figure()
ax = fig.add_subplot(111,projection="3d")
ax.scatter(df2["oikogeneia"],df2["ekpaideusi"],df2["filo"],df2["eisodima"],df2["exoda"],c="red",marker="o",alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape),color="b",alpha=0.3)
ax.set_xlabel("oikogeneia")
ax.set_ylabel("ekpaideusi")
#ax.set_zlabel("filo")
#ax.set_wlabel("eisodima")
#ax.set_vlabel("exoda")
mpl.show()