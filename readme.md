# Beamng.tech Reinforcement Learning, West Coast USA, test
The goal of this Git is to test the implementation of the Reinforcement Learning algorithm DDPG. This first repo is a test, in order to see how the RL is doable on my setup
## Getting started

The repo depend on the following library
* Numpy : Math library
* Matplotlib : Plotting library
* gymnasium : RL library
* open-cv : Image library
* beamngpy : Access point to the beamng.tech program [code](https://github.com/BeamNG/BeamNGpy), [documentation](https://beamngpy.readthedocs.io/en/latest/index.html)
* beamnggym : Beamng gym environnement [code](https://github.com/BeamNG/BeamNG.gym)

### Prerequisites
You will need the access to beamng.tech : [beamng.tech](https://beamng.tech/), [documentation](https://documentation.beamng.com/beamng_tech/)

You also need to install conda (anaconda or miniconda) [website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Install
To install all the library, you can use the .yml file and install the library from it using the following command : 
```
conda env create -f environment.yml
```
You also need to set the environment variable "BEAMNG_TECH_HOME" to the folder where beamng.tech is located, for example : C:\Users\someone\Desktop\BeamNG.tech.v0.30.6.0

## Structure of the Git
### Object
#### Vehicule
This class will be used to create the same vehicule with specified sensors (Camera, electrics, damage sensors) with a bunch of method. Such as Get sensors, set ai mod or reset.
#### OU
This class will be used to create noise for the DDPG implementation, it is based on the wikipedia [article](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process) about Ornstein Ulhenbeck process. The outputed noise is based on the previous sample

## To be done 
* Explain the math behind the wcarace class of beamng.gym
* The DDPG algorithm
* Link between beamng.gym and ddpg algo
* Test of the training

## Blibliography
### Papers
* [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)
### Article
* [Ornstein Ulhenbeck process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)
### Video
* [Yosh](https://www.youtube.com/@yoshtm)'s videos
### Documentation
* [BeamNG.Tech](https://documentation.beamng.com/beamng_tech/)
* [BeamNGpy](https://beamngpy.readthedocs.io/en/latest/index.html)
### Github
* [BeamNG.Gym](https://github.com/BeamNG/BeamNG.gym)
* [BeamNGpy](https://github.com/BeamNG/BeamNGpy)



