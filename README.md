# Asteroid Hunting with synthetic data

In some sitiations, data may be rare or hard to find. For example, NASA’s [discovery statistics database](https://cneos.jpl.nasa.gov/stats/totals.html) as of 10th of March 2023 contained records of 31,519 Near Earth Objects (NEO) collected over the period of 20 years. Still, none of them even closely matched characteristics of [asteroid `Oumuamua](https://solarsystem.nasa.gov/asteroids-comets-and-meteors/comets/oumuamua/in-depth), that was discovered in 2017.

For this project with a great help and support from my colleagues (Pedro Urbina, Shannon Monroe, Jon Hanzelka and Luke Tiday), I was able to generate synthetic asteroid images using some of the best 3D modelling platforms. The object detection model was then trained in Azure Custom Vision, before being exported into TensorFlow format. Export process also generated a template class to perform object (asteroid) detection that was then utilised in a custom ```asteroids.py``` inference code.

- You can check [this YouTube video](https://youtu.be/MGzjm-F5YcA) for an output of ML model, tested on the video stream of an asteroid's fly-by.
[![Img alt text](https://img.youtube.com/vi/MGzjm-F5YcA/0.jpg)](https://www.youtube.com/watch?v=MGzjm-F5YcA)

- This is link to the [original YouTube video](https://youtu.be/36XNdP4i7IA) from the European Southern Observatory (ESO).
[![Img alt text](https://img.youtube.com/vi/36XNdP4i7IA/0.jpg)](https://www.youtube.com/watch?v=36XNdP4i7IA)
