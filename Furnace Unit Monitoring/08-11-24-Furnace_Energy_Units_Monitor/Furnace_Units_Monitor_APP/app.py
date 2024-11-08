from flask import Flask, render_template
from datetime import datetime
import openpyxl
import re

app = Flask(__name__)

def read_shift_timings(file_path):
    time_ranges = {}
    with open(file_path, 'r') as file:
        for line in file:
            raw_line = line.strip()  # Remove leading/trailing whitespace
            print(f"Raw line: {raw_line}")  # Debug output

            # Use regex to find start and end times
            match = re.match(r"(\w+)=start:(\d{2}:\d{2}) end:(\d{2}:\d{2})", raw_line)
            if match:
                shift_name = match.group(1)
                start_time_str = match.group(2)
                end_time_str = match.group(3)

                print(f"Matched shift: {shift_name}, start: {start_time_str}, end: {end_time_str}")  # Debug output

                try:
                    start_time = datetime.strptime(start_time_str, "%H:%M").time()
                    end_time = datetime.strptime(end_time_str, "%H:%M").time()
                    time_ranges[shift_name] = (start_time, end_time)
                except ValueError as e:
                    print(f"Error parsing time for {shift_name}: {e}")  # Log the issue
            else:
                print(f"No match for line: {raw_line}")  # Log if line format is incorrect

    return time_ranges

@app.route('/')
def index():
    # Load the shift timings from the text file
    time_ranges = read_shift_timings('shifts.txt')

    # Load the workbook and select a worksheet
    workbook = openpyxl.load_workbook('data.xlsx')
    sheet = workbook.active

    # Initialize variables for current shift
    current_shift_value = None
    current_shift_name = None

    # Get the current time
    current_time = datetime.now().time()
    print(f"Current time: {current_time}")  # Debug output

    # Check which shift is currently active
    for shift_name, (start, end) in time_ranges.items():
        print(f"Checking shift: {shift_name}, start: {start}, end: {end}")  # Debug output
        if (start <= end and start <= current_time <= end) or (start > end and (current_time >= start or current_time <= end)):
            current_shift_name = shift_name
            print(f"Current shift found: {current_shift_name}")  # Debug output
            break

    # Iterate through the rows to find the maximum value for the current shift
    if current_shift_name:
        max_value = None
        max_row = None
        column_mapping = {
            'fullnight': 'B',
            'dayshift': 'C',
            'halfnight': 'D'
        }
        current_column = column_mapping.get(current_shift_name)

        for row in range(2, sheet.max_row + 1):
            cell_value = sheet[f'{current_column}{row}'].value
            if isinstance(cell_value, (int, float)):
                if max_value is None or cell_value > max_value:
                    max_value = cell_value
                    max_row = row

        if max_value is not None:
            current_shift_value = max_value

    return render_template('index.html', current_shift_value=current_shift_value)


if __name__ == '__main__':
    app.run(debug=True)
