from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def perform_clustering(data):
    """
    Perform K-Means clustering on Infrastructure Score and LPI Score.
    Args:
        data (DataFrame): The dataset containing Infrastructure Score and LPI Score.
    Returns:
        DataFrame: The dataset with an additional 'Cluster' column.
    """
    features = data[['Infrastructure_Score', 'LPI_Score']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(features)
    print("Clustering completed. Added 'Cluster' column.")
    return data

def visualize_clusters(data):
    """
    Create a scatter plot to visualize clusters based on Infrastructure Score and LPI Score.
    Args:
        data (DataFrame): The dataset containing clusters.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Infrastructure_Score'], data['LPI_Score'], c=data['Cluster'], cmap='viridis', alpha=0.7, edgecolors='k')
    plt.title('Clusters of Countries Based on Infrastructure and LPI Score', fontsize=14)
    plt.xlabel('Infrastructure Score', fontsize=12)
    plt.ylabel('LPI Score', fontsize=12)
    plt.colorbar(label='Cluster')
    plt.grid(alpha=0.3)
    plt.show()

