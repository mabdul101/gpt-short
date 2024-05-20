import csv

# Mapping of short symbols to full names
replacement_map = {
    "to": "TOMATO",
    "ca": "CABBAGE",
    "co": "CORN",
    "cr": "CARROT",
    "10": "HOT DOG",
    "15": "MEAT SKEWERS",
    "25": "CHICKEN THIGHS",
    "45": "BEEF",
    "pi": "PIZZA",
    "sa": "SALAD"
}

# Reverse the mapping to use full names as keys
reverse_map = {v: k for k, v in replacement_map.items()}

# Function to replace the Result values
def replace_results(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        # Reading all rows
        rows = list(reader)
        
        # Replace the values in the Result column
        for row in rows:
            if row['Result'] in reverse_map:
                row['Result'] = reverse_map[row['Result']]
        
    # Write the updated data back to a new CSV file
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Replace the results in 'data.csv' and write to 'updated_data.csv'
replace_results('data.csv', 'updated_data.csv')
