
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

# Read data from file
data = read_data(columns, types=types)

# Running the fucntion to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

# Output comparison of data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)

