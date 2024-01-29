# Approximated data from Reliable Internet Sources. 
# Open a new file in write mode ('w')
with open('data.txt', 'w') as f:
    # Write some data to the file
    f.write('N = 1,137,938,708\n')  # Total population (src = "https://en.wikipedia.org/wiki/Sub-Saharan_Africa")
    f.write('I0 = 7,200000\n')  # Initial number of infected individuals for the year 2021
    f.write('R0 = N*0.8\n')  # Initial number of recovered individuals
    f.write('beta = 0.65\n')  # Contact rate
    f.write('gamma = 0.8\n')  # Mean recovery rate
