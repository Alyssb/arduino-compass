**MEMS Accelerometer Compass**

**Alyssa Slayton**

**Missouri State University**

**Advisor, Dr. Matthew McKay**

**Abstract**

> It is necessary to use a compass when surveying or traveling long
> distances without access to GPS, such as on the Moon. Our goal is to
> create a practical device that can serve as a compass using
> Micro-Electro-Mechanical Systems. We have created a device using an
> accelerometer and a microcontroller which can accurately detect the
> acceleration of the Earth. We are creating a method of using 2 axes of
> acceleration data to calculate the direction the device is facing and
> communicate it to the user.

**Introduction**

A compass is a necessary tool when surveying or traveling large
distances. Compasses use Earth's magnetic field and a permanent magnet
to point toward the south magnetic pole, which lies near the geographic
north pole. Compasses only work on Earth and they do not work near any
other magnets or iron- or copper-based materials which overpower Earth's
comparatively weak magnetic field. They also cannot function in the
presence of a flowing electrical current. As exploration of the Moon and
eventually Mars becomes closer to fruition, the need for a compass that
does not require Earth's magnetic field nor the absence of any of the
previously described materials becomes apparent. The purpose of this
project is to develop a Micro-Electro-Mechanical Systems (MEMS)
accelerometer north finder that will be cheap, fast, and lightweight
enough to be practically used as carry-on equipment for an individual,
and an application that can communicate with the system through
bluetooth, so that it can be practically applied.

Gyro north finders, as used in nautical navigation, use large and
expensive multi-gyroscope systems to find North^1^. Previous
experimental work using a MEMS gyroscope^2^ and a MEMS accelerometer and
gyroscope^1^ to find north has been done. These experiments each had an
accuracy to one degree, with integration times of 5 minutes for the MEMS
gyroscope and 3 minutes for the gyroscope and accelerometer system. The
results of other available gyro north finders, as well as some
experimental results, can be seen in Table 1, from Zhang (2017)^1^.

  **Name**        **Gyromat 3000**   **HG2172**        **Octans 3000**   **SIGMA 20M**     **Experimental Zhang, 2017**
  --------------- ------------------ ----------------- ----------------- ----------------- ------------------------------
  **Producer**    DMT GmbH           Honeywell         iXBlue            SAFRAN            Zhang, 2017
  **Gyros**       Mechanical         RLG               FOG               HRG               MEMS
  **Time**        10 min             4 min             5 min             6 min             3 min
  **Precision**   3.24"              0.05°             0.1°              0.1°              1°
  **Size/mm**     Φ215 x H330        163 x 165 x 163   Φ213 x H375       208 x 136 x 292   110 x 140 x 50
  **Weight**      11.5 kg            4.1kg             15 kg             4.5 kg            1.5 kg
  **Power**       Not Specified      18 W              20 W              28 W              3.6 W
  **Type**        Product            Product           Product           Product           Prototype

**Table 1. Current available gyro north finders, and recent experimental
results using a MEMS single gyroscope single accelerometer system.**

**Hardware and Software**

Our setup consists of the following hardware:

LSM9DS1: a SparkFun Inertial Measurement Unit (IMU) which contains a
3-axis accelerometer, 3-axis gyroscope, and 3-axis magnetometer on a
single chip. Shown in Figure 1.

![](media/image1.jpeg){width="3.4375in" height="2.0833333333333335in"}

**Figure 1: Sparkfun Breakout LSM9DS1**

Sparkfun Small Stepper Motor: A small stepper motor used to turn the
sensor and take data.

Sparkfun EasyDriver: a Stepper Motor driver by Sparkfun used to
communicate with the stepper motor.

nRF52832: an Adafruit arduino microcontroller  with builtin Bluetooth
Low Energy (BLE) which was used to read and transmit data from the
sensor to the laptop, as well as control the EasyDriver. Shown in Figure
2.

![](media/image2.jpeg){width="2.21875in" height="3.1041666666666665in"}

**Figure 2: Adafruit Feather nRF52832**

Also used were a laptop to take the data from the microcontroller and an
adjustable power supply for the stepper motor set to 12 volt 1 amp, as
specified for the motor. A simple 12 volt power supply would be
sufficient. The stepper motor and EasyDriver were used to turn the
sensor accurately so that it could take data. The final form of the
system will only require the LSM9DS1 sensor and the nRF52832
microcontroller, the schema and size of which is shown in Figure 3. The
experimental setup is visualized in Figure 4, which was made by
Fritzing, a tool for visualizing hardware schematics. Not shown is the
sensor attached on top of the stepper motor.

![](media/image3.jpeg){width="2.6666666666666665in" height="3.58125in"}

**Figure 3: LSM9DS1 and NRF52832**

![](media/image4.png){width="4.3125in" height="2.46875in"}

**Figure 4: layout used for taking experimental data**

**Gyroscopic Data**

Our sensor is very inexpensive and small. The gyroscopic data were
inconclusive. Shown in figure 5 is a graph of x-axis gyroscopic data,
taken for 15 seconds every 4.5 degrees in a full circle. We will need to
purchase a more sensitive gyroscope in order to take usable data.

![](media/image5.png){width="5.083333333333333in" height="3.8125in"}

**Figure 5: graph of x-axis gyroscope data for 15 seconds every 4.5
degrees starting due north. Data were taken every half second. Every 30
points is 4.5 degrees. Y-axis is degrees per second and X-axis is the
data point number.**

**Accelerometer Data**

The accelerometer data taken yields a sine curve (Figure 6). We are
attempting to only use accelerometer data for calibration by taking the
x-axis against the y-axis, which should be in phase. To do this we are
building a lookup table from each direction, using linear interpolation
to find the most similar value, and then taking the ratio to calculate
the direction the accelerometer is facing. the values have been
obtained, however, lookup tables must be linear so the next step on this
front is to normalize the sine curve around zero, store the arcsine in
the lookup table, and then write the code to do the lookup using the
arcsine of the current normalized direction.

![](media/image6.png){width="6.5in" height="4.875in"}

**Figure 6: graph of x-axis accelerometer data taken for 15 seconds
every 4.5 degrees starting due north. Data were taken every half second.
Every 30 points is 4.5 degrees. Y-axis is gravity in G and X-axis is
data point**

The sine curves for x-acceleration and y-acceleration should be
perfectly in phase with each other because the axes are at 90 degrees.
This is not the case observed (Figure 7). These results may be because
the data were taken in Springfield, Missouri, which is at a latitude of
37 degrees.  

![](media/image7.png){width="5.116666666666666in" height="3.8375in"}

**Figure 7: graph of x-axis (purple) versus y-axis (green) accelerometer
data taken for 15 seconds every 4.5 degrees starting due north. Data
were taken every half second. Every 30 points is 4.5 degrees.**

**Application Design**

The application is still in its early phases. The idea is to first host
a webpage which will show the direction in real time from the
accelerometer data. The webpage would work offline as long as it had
been initially loaded off the internet. If necessary, we intend to
create a mobile application which will be able to communicate with the
device via bluetooth.

**Acknowledgements**

Funding for this research was provided by the Missouri Space Grant
Consortium, funded by NASA. Embedded systems expertise was provided by
Dr. Anthony Clark of the Computer Science Department at Missouri State
University.

**Biography**

Alyssa Slayton is a junior attending Missouri State University pursuing
computer science with minors in physics, astronomy, and math. She began
working with Dr. Reed during fall of 2016 as a senior attending Republic
High School. She now works for Dr. McKay and plans to continue this work
next year as a senior and continue with her master's degree.

**References**

1.  Zhang, Y., Zhou, B., Song, M., Hou, B., Xing, H., & Zhang, R.
    (2017). A Novel MEMS Gyro North Finder Design Based on the Rotation
    Modulation Technique. *Sensors (Basel, Switzerland)*, *17*(5), 973.
    https://doi.org/10.3390/s17050973

2.  Iozan, L. I., Kirkko-Jaakkola, M., Collin, J., Takala, J., &
    Rusu, C. (2010, October). North finding system using a MEMS
    gyroscope. In *Proceedings of European Navigation Conference on
    Global Navigation Satellite Systems*.
