import csv

def append_row_to_csv(file_path, row_array):
    # Check if the row_array is empty
    if not row_array:
        raise ValueError("The row array is empty.")
    
    # Append the row to the CSV file
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_array)

    print("Row appended successfully.")

# Example usage:
if __name__=="__main__":
    file_path = "D:/PROJECT/encord_T1/dataset/record.csv"
    row_array = ['value1', 'value2', 'value3', 'value4']*2  # Adjust the number of values to match the number of columns in your CSV file
    append_row_to_csv(file_path, row_array)
