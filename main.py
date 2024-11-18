from modules.load_data import load_data
from modules.clean_data import clean_data
from modules.eda import enhanced_visualization, calculate_correlation
from modules.cluster_analysis import perform_clustering, visualize_clusters

def main():
    # Step 1: Load data
    file_path = r"C:\Users\sgbal\Documents\IIT_Projects\supply_chain_project\data\International_LPI_from_2007_to_2023.csv"
    data = load_data(file_path)
    print("Data loaded successfully.")

    # Step 2: Clean data
    data = clean_data(data)
    print("Data cleaned successfully.")

    # Step 3: Enhanced Visualization
    enhanced_visualization(data)

    # Step 4: Calculate Correlation
    calculate_correlation(data)

    # Step 5: Perform Clustering
    data = perform_clustering(data)
    visualize_clusters(data)

    # Step 6: Save results
    output_path = r"C:\Users\sgbal\Documents\IIT_Projects\supply_chain_project\results\processed_file.csv"
    data.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

if __name__ == "__main__":
    main()

