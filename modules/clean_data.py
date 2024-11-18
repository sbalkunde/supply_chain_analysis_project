def clean_data(data):
    """
    Clean the dataset: handle missing values, rename columns, and filter relevant data.
    Args:
        data (DataFrame): The raw dataset.
    Returns:
        DataFrame: Cleaned dataset.
    """
    # Fill missing values in numeric columns only
    numeric_cols = data.select_dtypes(include=['number']).columns  # Select only numeric columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    # Rename columns for easier access
    data.rename(columns={
        'LPI Score': 'LPI_Score',
        'Customs Score': 'Customs_Score',
        'Infrastructure Score': 'Infrastructure_Score',
        'Timeliness Score': 'Timeliness_Score'
    }, inplace=True)

    return data


