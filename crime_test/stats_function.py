import pandas as pd

def calculate_mean_age(data):
    """Calculates the mean of the Vict Age column."""
    return data['Vict Age'].mean()

def calculate_median_age(data):
    """Calculates the median of the Vict Age column."""
    return data['Vict Age'].median()

if __name__ == "__main__":
    # Load the dataset
    csv_file = "Crime_Data_from_2020_to_Present.csv"
    data = pd.read_csv(csv_file)

    # Perform calculations
    mean_age = calculate_mean_age(data)
    median_age = calculate_median_age(data)

    print(f"Mean Age: {mean_age}")
    print(f"Median Age: {median_age}")
