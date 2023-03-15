# Asteroid Hunting with synthetic data

In some sitiations, the data may be rare or hard to find. For example, NASA’s [discovery statistics database](https://cneos.jpl.nasa.gov/stats/totals.html) as of 10th of March 2023 contained records of 31,519 Near Earth Objects (NEO) collected over period of 20 years. Still, none of them closely matched characteristics of [asteroid `Oumuamua](https://solarsystem.nasa.gov/asteroids-comets-and-meteors/comets/oumuamua/in-depth), discovered in 2017.

So, for this project I generated synthetic asteroid images using some open source and proprietary 3D software platforms. Object detection model was then trained with Azure Custom Vision solution and exported into TensorFlow format. It also generated a template class to perform predictions.


