set term png
set output 'C:\Users\alyss\Documents\arduino-compass\20mindata\accel_clean.png'
plot 'C:\Users\alyss\Documents\arduino-compass\20mindata\xaccelclean' w lines title 'X Accel', (1.5933532380151207), (1.6784317988064736), 'C:\Users\alyss\Documents\arduino-compass\20mindata\yaccelclean' w lines title 'Y Accel'
