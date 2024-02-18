import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def calculate_column_widths(data):
    # Transpose the data to get columns
    transposed_data = list(map(list, zip(*data)))

    # Calculate the maximum width for each column
    column_widths = [max(len(str(max(col, key=len))), len(col[0])) for col in transposed_data]

    return column_widths

def format_and_write(data, output_file_path):
    # Extract column headings from the first row
    column_headings = data[0]

    # Calculate the maximum width for each column
    column_widths = calculate_column_widths(data)

    # Write the formatted data to a new CSV file
    with open(output_file_path, 'w', newline='') as output_file:
        # Use a tab '\t' as the delimiter
        writer = csv.writer(output_file, delimiter='\t')

        # Write the column headings
        formatted_headings = [f"{heading:<{width+1}}" for heading, width in zip(column_headings, column_widths)]
        writer.writerow(formatted_headings)

        # Write the formatted data
        for row in data[1:]:
            formatted_row = [f"{str(cell):<{width+1}}" for cell, width in zip(row, column_widths)]
            writer.writerow(formatted_row)

if __name__ == "__main__":
    # Replace 'data/raw_data.csv' with the actual path to your CSV file
    input_csv_file_path = 'data/raw_data.csv'
    output_csv_file_path = 'data/clean_data.csv'

    try:
        csv_data = read_csv(input_csv_file_path)
        format_and_write(csv_data, output_csv_file_path)
        print(f"Formatted data written to {output_csv_file_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {input_csv_file_path}")
    except csv.Error:
        print(f"Error: Unable to parse CSV file at {input_csv_file_path}. Make sure it is a valid CSV file.")
