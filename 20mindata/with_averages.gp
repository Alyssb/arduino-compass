# this is a script for plotting clean accel data with averages
# the averages are not lined up, too lazy to do that rn

set term png 
set output 'accel_clean_with_avg'

# set arrows starting with yaccel
set arrow 1 from 0,-1.412496873697379 to 2400,-1.412496873697379 nohead front
set arrow 2 from 2400,-0.9508841183826662 to 4800,-0.9508841183826662 nohead front
set arrow 3 from 4800,-2.148459358065861 to 7200,-2.148459358065861 nohead front
set arrow 4 from 7200,0.06412546894539412 to 9600,0.06412546894539412 nohead front
set arrow 5 from 9600,-1.4493509795748276 to 12000,-1.4493509795748276 nohead front

set arrow 6 from 0,1.5911366666666484 to 2400,1.5911366666666484 nohead front
set arrow 7 from 2400,-1.133009166666665 to 4800,-1.133009166666665 nohead front
set arrow 8 from 4800,-0.5107612499999972 to 7200,-0.5107612499999972 nohead front
set arrow 9 from 7200,-0.004218333333333139 to 9600,-0.004218333333333139 nohead front
set arrow 10 from 9600,1.674559583333327 to 12000,1.674559583333327 nohead front

plot 'xaccelclean' w lines, 'yaccelclean' w lines
