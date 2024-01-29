# Learning Guide for Disease Simulation Project

This project simulates the spread of a disease (Typhoid fever in this case) in a population over time using the SIR (Susceptible, Infected, Recovered) model. This guide will help you understand how it works.

## Understanding the SIR Model

The SIR model is a simple mathematical model that describes the dynamics of infectious diseases in a population. It divides the population into three groups:

- **Susceptible (S)**: Individuals who can catch the disease.
- **Infected (I)**: Individuals who have caught the disease and can spread it to susceptible individuals.
- **Recovered (R)**: Individuals who have recovered from the disease and are now immune.

The model is represented by a set of differential equations that describe how individuals move between these groups over time.

## Understanding the Code

The main part of the code is the `deriv` function, which represents the SIR model in the form of differential equations. The function takes the current number of susceptible, infected, and recovered individuals, as well as the effective contact rate (`beta`) and the recovery rate (`gamma`), and calculates the rate of change of `S`, `I`, and `R`.

The `odeint` function from the `scipy.integrate` module is used to solve these differential equations and simulate the spread of the disease over time.

The results of the simulation are then plotted using the `matplotlib.pyplot` module.

## Running the Simulation

To run the simulation, you need to set the initial parameters in the `data.txt` file. This includes the total population, the initial number of infected and recovered individuals, and the contact and recovery rates.
Also, create the data file by running `python3 src/data.py`

Then, you can run the `python3 src/simulate_diff.py` script to perform the simulation and plot the results.

## Further Learning

To learn more about the SIR model and disease modeling in general, you might find the following resources helpful:

- [Compartmental models in epidemiology - Wikipedia](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)
- [The SIR epidemic model - Learning Scientific Programming with Python](https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/)