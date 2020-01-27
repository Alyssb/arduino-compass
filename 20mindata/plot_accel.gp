set term png
set output 'accel_clean.png'
plot 'C:\Users\alyss\Documents\arduino-compass\20mindata\xaccelclean' w lines title 'X Accel', (1.5911366666666484), (1.674559583333327), 'C:\Users\alyss\Documents\arduino-compass\20mindata\yaccelclean' w lines title 'Y Accel'
unset output