# this is a script for plotting clean accel data with averages
# the averages are not lined up, too lazy to do that rn

set term png 
set output 'accel_clean_with_avg'

# set arrows starting with yaccel
set arrow 1 from 0,-1.4151343408900134 to 2400,-1.4151343408900134 nohead front
set arrow 2 from 2400,-0.9159902309058656 to 4800,-0.9159902309058656 nohead front
set arrow 3 from 4800,-2.1594066551426048 to 7200,-2.1594066551426048 nohead front
set arrow 4 from 7200,0.06500507614213216 to 9600,0.06500507614213216 nohead front
set arrow 5 from 9600,-1.47097515257193 to 12000,-1.47097515257193 nohead front

# xaccel arrows
set arrow 6 from 0,1.5933532380151207 to 2400,1.5933532380151207 nohead front
set arrow 7 from 2400,-1.1428511647972366 to 4800,-1.1428511647972366 nohead front
set arrow 8 from 4800,-0.5190034527406103 to 7200,-0.5190034527406103 nohead front
set arrow 9 from 7200,-0.01072627118644049 to 9600,-0.01072627118644049 nohead front
set arrow 10 from 9600,1.6784317988064736 to 12000,1.6784317988064736 nohead front

plot 'xaccelclean' w lines, 'yaccelclean' w lines
