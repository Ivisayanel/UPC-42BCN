set INTERS;
set PATHS;
set FIXED;
set PROHIBITED;

param flows {PATHS} >= 0;
param f {PATHS, INTERS} >= 0;
#f = intersecció está o no en el path (1 si està), else 0
var x {j in PATHS} binary;
var sensor {i in INTERS} binary;
#x = path sensorizado o no
#sensor = intersecció i amb sensor o no

#Función objetivo
maximize Total_Flow: sum{j in PATHS} flows[j] * x[j];

#Restricciones

subject to maxsensor{i in INTERS}:
((sum{j in INTERS}sensor[j]) < 16);

subject to sensorizado{p in PATHS}:
((sum{i in INTERS}sensor[i] * f[p,i]) > (2*x[p]) - 1);

subject to fixed{i in FIXED}:
sensor[i] = 1;

subject to prohibed{i in PROHIBITED}:
sensor[i] = 0;

