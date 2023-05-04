set INTERS;
set PATHS;
set FIXED;
set PROHIBITED;
set PATH_INTER within {PATHS, INTERS};
set INTERS_NEIGHT within {INTERS, INTERS};

param flows{PATHS} >= 0;
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
((sum{(p,i) in PATH_INTER}sensor[i]) > (2*x[p]) - 1);

subject to neighbors{(i1, i2) in INTERS_NEIGHT}:
 (sensor[i1] + sensor[i2] < 2);

subject to fixed{i in FIXED}:
sensor[i] = 1;

subject to prohibed{i in PROHIBITED}:
sensor[i] = 0;
