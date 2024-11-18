import pandas as pd

file_path = "data/International_LPI_from_2007_to_2023.csv"

def load_data(file_path):
    """
    Load the dataset from the given file path.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        DataFrame: Loaded dataset.
    """
    data = pd.read_csv(file_path)
    return data

# Example usage
data = load_data(file_path)
print(data.head())  # Print the first few rows of the dataset
