import json
from typing import Iterator


def iterator_json_reader(filename: str) -> Iterator[dict]:
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            # obj = json.loads(line.strip())
            yield line


def create_subdataset(input_path, output_path, percentage):
    with open(input_path, "rb") as f:
        num_lines_total = sum(1 for _ in f)
    
    num_lines = int(num_lines_total * percentage / 100)
    
    with open(output_path, 'a') as file:
        reader = iterator_json_reader(input_path)
        
        line_counter = 0
        for examples in reader:
            file.write(examples)
            if line_counter > num_lines:
                break
            line_counter += 1

def main():
    percentages = [0.1, 1, 3, 10]
    for p in percentages:
        create_subdataset("data/1m_6ex_karel/train.json", f"data/1m_6ex_karel/train_{p}percent.json", p)
    

if __name__ == "__main__":
    main()