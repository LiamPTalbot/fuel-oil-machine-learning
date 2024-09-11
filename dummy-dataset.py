#!/Users/home/Documents/Github/fuel-oil-machine-learning/.venv/bin/python

from datetime import datetime
import pandas as pd  # Import pandas library for data manipulation and analysis
import numpy as np  # Import numpy library for numerical operations and generating random numbers

# Set seed for reproducibility
# This ensures that every time we run the script, the same random numbers are generated.
np.random.seed(42)  # Set the seed for the random number generator

# Generate CuNi Content (ppm) between 1 and 100 ppm
# We are creating 500 random samples of CuNi content in parts per million (ppm) 
# using a uniform distribution to simulate different contamination levels.
cuni_content = np.random.uniform(1, 100, 500)  # Generate 500 random samples uniformly distributed between 1 and 100

# Generate Time Until Failure (hours)
# We assume an inverse relationship between CuNi content and time until failure.
# As CuNi content increases, the time until failure decreases. 3000 is the scaling factor i.e. 1ppm is 3000 hours tuf.
# Additionally, we add random noise using a normal distribution to make the relationship non-linear 
# and add variability to the data, which helps in testing machine learning models.
time_until_failure = (3000 / cuni_content) + np.random.normal(0, 50, size=cuni_content.shape)
# Compute time until failure as an inverse function of CuNi content with added Gaussian noise

# Creating the dataset
# A DataFrame is created to organize the two features: 'CuNi Content (ppm)' and 'Time Until Failure (hours)'
# The 'CuNi Content (ppm)' represents the input, while 'Time Until Failure (hours)' represents the output.
data = pd.DataFrame({
    'CuNi Content (ppm)': cuni_content,  # Column for CuNi content
    'Time Until Failure (hours)': time_until_failure  # Column for time until failure
})

# Preview dataset
# Display the first few rows of the dataset to verify that the data has been generated as expected.
data.head()  # Show the first few rows of the DataFrame to inspect the data

# Create a timestamp for the filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # Format the timestamp

# Define the path to the public directory and filename
public_directory = 'public'
filename = f'engine_fuel_injector_failure_{timestamp}.csv'
filepath = f'{public_directory}/{filename}'  # Create the full path for saving the file

# Save dataset to CSV
data.to_csv(filepath, index=False)  # Save DataFrame to a CSV file in the public directory without including the DataFrame index

print(f'Dataset saved to {filepath}')  # Print the path to verify that the file was saved