import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Open the data file in read mode ('r')
with open('data.txt', 'r') as f:
    # Read the data from the file
    lines = f.readlines()

# Parse the data
N = int(lines[0].split('=')[1].replace(',', '').strip()) 
I0 = int(lines[1].split('=')[1].replace(',', '').strip())
R0 = float(lines[2].split('=')[1].strip())  # Use float() instead of int()
beta = float(lines[3].split('=')[1].strip())
gamma = float(lines[4].split('=')[1].strip())

# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0

# A grid of time points (in days)
t = np.linspace(0, 160, 160)

# Calculates the rate of change of susceptible, infected and recovered individuals
def deriv(y, t, N, beta, gamma): # (Y= tuple containing the values of S I R, 
                                 #t= time, N= total population, beta= contact rate,
                                 #gamma= mean recovery rate)
    
    dSdt = -beta * S0 * I0 / N  # dSdt = rate of change of susceptible individuals
    dIdt = beta * S0 * I0 / N - gamma * I0  # dIdt = rate of change of infected individuals
    dRdt = gamma * I0  # dRdt = rate of change of recovered individuals
    return dSdt, dIdt, dRdt   # returns a tuple containing the rates of change of S I R

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')

# Add a title to the plot
ax.set_title('SIR Model Simulation')

ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,1.2)

# Highlight the peak of the 'Infected' curve
max_I = max(I/1000)
max_t = t[list(I/1000).index(max_I)]
ax.plot(max_t, max_I, 'ro')
ax.annotate('Peak (day {:.0f})'.format(max_t), xy=(max_t, max_I), xytext=(max_t+5, max_I),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

# Save the plot to a file
fig.savefig('sir_model_simulation.png') 
