import pandas as pd
import os

# Function to save each row as a .txt file
def save_rows_as_txt(df, delimiter, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Convert the row to a string with the specified delimiter
        row_string = delimiter.join(map(str, row.values))
        
        # Define the file path for each row
        file_name = f"customer_{index + 1}.txt"
        print(file_name)
        print(row_string)
        file_path = os.path.join(output_dir, file_name)
        
        # Write the row to a .txt file
        with open(file_path, 'w') as file:
            file.write(row_string)

# Path to your CSV file
csv_file_path = 'D:\\7th-Sem-PROJECT\\CODE\\Python\\finance_receipting_robotic_process_automation_service\input_collection.csv'

# Output path
output_dir = 'D:\\7th-Sem-PROJECT\\CODE\\Python\\finance_receipting_robotic_process_automation_service\\source_files'

# Delimiter
delimiter = '$^#'

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Execute the operation
save_rows_as_txt(data, delimiter, output_dir)