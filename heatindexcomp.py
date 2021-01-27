
from readdata import read_data
from printing import print_comparison
from computation import compute_heatindex

# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}     

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout': float, 'heatindex': float}

# Read data from the file
data = read_data(columns, types=types)

# Running the fucntion to compute heat index
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, humout))

# Output comparison of data
print('                ORIGINAL  COMPUTED           ')
print(' DATE    TIME  HEAT INDX HEAT INDX DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_orig, hi_comp in zip_data:
    hi_diff = hi_orig - hi_comp
    print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')

