import matplotlib.pyplot as plt

def enhanced_visualization(data):
    """
    Create an enhanced scatter plot showing the relationship between Infrastructure Score and LPI Score.
    Args:
        data (DataFrame): The dataset containing Infrastructure Score and LPI Score.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Infrastructure_Score'], data['LPI_Score'], c='blue', alpha=0.7, edgecolors='k')
    plt.title('Infrastructure vs. LPI Score', fontsize=14)
    plt.xlabel('Infrastructure Score', fontsize=12)
    plt.ylabel('LPI Score', fontsize=12)
    plt.grid(alpha=0.3)
    plt.show()

def calculate_correlation(data):
    """
    Calculate and print the correlation between Infrastructure Score and LPI Score.
    Args:
        data (DataFrame): The dataset containing Infrastructure Score and LPI Score.
    """
    correlation = data['Infrastructure_Score'].corr(data['LPI_Score'])
    print(f"Correlation between Infrastructure Score and LPI Score: {correlation:.2f}")


