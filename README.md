SoundSpeed with Arduino
=======================

Introduction
------------
This is the result of a 3-days course for High School teachers on *Physics with Arduino and smartphone* at [University "La Sapienza" in Rome, Physics Department](https://www.phys.uniroma1.it/fisica/en), in collaboration with the FabLab [Fondazione Mondo Digitale](http://mondodigitale.org/en). 


Description
-----------
This work aims to measure the sound speed in air as a temperature function. In particular, is an educational tool to prove the linear approximation in the temperature range of -10°C to 60°C. 
We measure the sound speed with an ultrasonic sensor, deriving it by the time that sound waves takes to cover a certain distance. This due to a box in which me put the sensor, so we can measure both sound speed and temperature of a quite definite portion of air.


What we needs?
--------------
For this work we use:
* Arduino Uno Rev.3
* Ultrasonic sensor HC-SR04
* Temperature sensor TMP36
* Wood box 15x20x10 cm
* Felt
* Dehumidifiers salts
* Hair dryer


What we have here?
------------------
I put here the arduino sketch (inside the `soudspeed` folder), the python script to perform data visualization and a `requirements.txt` file to install all the necessary python libraries.


How it works?
-------------
We measure the sound speed with the ultrasonic sensor with:

![equation](http://www.sciweavers.org/tex2img.php?eq=v%20%20%5Capprox%20%20%5Cfrac%7B2d%7D%7Bt_s%7D%20&bc=White&fc=Black&im=jpg&fs=18&ff=mathpazo&edit=0)

where `d` is the lenght of the box (i.e. 20 cm) and `ts` the time for ultrasonic waves to travel the double of that lenght.
