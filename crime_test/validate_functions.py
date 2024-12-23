import pandas as pd

def validate_vict_sex(data):
    """
    Checks that the 'Vict Sex' column is either 'M' or 'F' and not missing (NULL).
    Returns a DataFrame of invalid rows.
    """
    invalid_rows = data[(data['Vict Sex'].isnull()) | (~data['Vict Sex'].isin(['M', 'F']))]
    return invalid_rows

def validate_vict_age(data):
    """
    Checks that the 'Vict Age' column values are between 1 and 100 and not missing (NULL).
    Returns a DataFrame of invalid rows.
    """
    invalid_rows = data[(data['Vict Age'].isnull()) | (~data['Vict Age'].between(1, 100))]
    return invalid_rows

if __name__ == "__main__":
    # Load the dataset
    csv_file = "Crime_Data_from_2020_to_Present.csv"
    data = pd.read_csv(csv_file)

    # Run validations
    invalid_sex = validate_vict_sex(data)
    invalid_age = validate_vict_age(data)

    print(f"Invalid Vict Sex rows:\n{invalid_sex}")
    print(f"Invalid Vict Age rows:\n{invalid_age}")
