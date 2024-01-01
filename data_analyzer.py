import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def clean_data(self):
        if self.data is not None:
            # Drop duplicates and handle missing values
            self.data = self.data.drop_duplicates()
            self.data = self.data.dropna()
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data['Year'] = self.data['Date'].dt.year
            self.data['Month'] = self.data['Date'].dt.month_name()

            print("Data cleaned successfully.")
        else:
            print("No data to clean. Please load data first.")

    def analyze_data(self):
        if self.data is not None:
            # Generate summary statistics
            summary_stats = self.data.describe()
            print("Summary Statistics:")
            print(summary_stats)

            # Total sales per month
            monthly_sales = self.data.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
            plt.figure(figsize=(10, 6))
            for year in monthly_sales['Year'].unique():
                year_data = monthly_sales[monthly_sales['Year'] == year]
                plt.plot(year_data['Month'], year_data['Sales'], label=str(year))

            plt.title('Monthly Sales Over the Years')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.legend()
            plt.show()

        else:
            print("No data to analyze. Please load data first.")

    def run_analysis(self):
        self.load_data()
        self.clean_data()
        self.analyze_data()

if __name__ == "__main__":
    file_path = input("Enter the path to your CSV file: ")
    analyzer = DataAnalyzer(file_path)
    analyzer.run_analysis()
  # It's good just customize it as you want :)
