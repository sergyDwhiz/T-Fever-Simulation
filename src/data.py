# Approximated data from Reliable Internet Sources. 
# Open a new file in write mode ('w')
with open('data.txt', 'w') as f:
    # Write some data to the file
    N = 1137938708  # Total population
    f.write(f'N = {N}\n')
    f.write('I0 = 7200000\n')  # Initial number of infected individuals for the year 2021
    R0 = N*0.8  # Initial number of recovered individuals
    f.write(f'R0 = {R0}\n')
    f.write('beta = 0.65\n')  # Contact rate
    f.write('gamma = 0.8\n')  # Mean recovery rate