# Asteroid Hunting with synthetic data

In some sitiations, data may be rare or hard to find. For example, NASA’s [discovery statistics database](https://cneos.jpl.nasa.gov/stats/totals.html) as of 10th of March 2023 contained records of 31,519 Near Earth Objects (NEO) collected over the period of 20 years. Still, none of them even closely matched characteristics of [asteroid `Oumuamua](https://solarsystem.nasa.gov/asteroids-comets-and-meteors/comets/oumuamua/in-depth), that was discovered in 2017.

For this project with a great help and support from my colleagues (Pedro Urbina, Shannon Monroe, Jon Hanzelka and Luke Tiday), I was able to generate synthetic asteroid images using some of the best 3D modelling platforms. The object detection model was then trained in Azure Custom Vision, before being exported into TensorFlow format. Export process also generated a template class to perform object (asteroid) detection that was then utilised in a custom ```asteroids.py``` inference code[^1].

- You can check [this YouTube video](https://youtu.be/MGzjm-F5YcA) for an output of ML model, tested on the video stream of an asteroid's fly-by.
[![Img alt text](https://img.youtube.com/vi/MGzjm-F5YcA/0.jpg)](https://www.youtube.com/watch?v=MGzjm-F5YcA)

- This is link to the [original YouTube video](https://youtu.be/36XNdP4i7IA) from the European Southern Observatory (ESO)[^2].
[![Img alt text](https://img.youtube.com/vi/36XNdP4i7IA/0.jpg)](https://www.youtube.com/watch?v=36XNdP4i7IA)

[^1]:This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
[^2]:This short video shows an artist's impression of 2004 EW95, the first carbon-rich asteroid confirmed to exist in the Kuiper Belt and a relic of the primordial Solar System. The video shows a fly-by of the enigmatic asteroid as it tumbles through the icy outer reaches of the Solar System due to past interactions with migrating planets.
More information and download options: http://www.eso.org/public/videos/eso1.
Credit: ESO/M. Kornmesser
