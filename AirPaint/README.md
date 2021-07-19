# AirPaint
So we're basically using OpenCV to build this thing. It displays what we write in front of the webcam.
We have used the webcam module, the contours functions and the findcolor module, the latter two of which are defined locally. We detect the colour using the HSV image and the colorpicker  function and then tweaking the values so that we get the accurate colour, and then we feed it to the program to draw the colour that we desire, in the form of points which are noted continuously and then portrayed using another function.
