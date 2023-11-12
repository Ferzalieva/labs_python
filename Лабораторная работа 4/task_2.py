import csv
import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

def task() -> None:
    with open(INPUT_FILE) as f:
        lines = [line for line in csv.DictReader(f)]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(lines, f, indent=4)

if __name__ == '__main__':
    # Необходимо для проверки
    task()

    with open(OUTPUT_FILE) as output_f:
        for line in output_f:
            print(line, end="")
