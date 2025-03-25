import json

def convert_to_json(input_file):
    data = []

    with open(input_file, 'r') as file:
        lines = file.readlines()

        current_id = None
        current_caption = []

        for line in lines:
            line = line.strip()
            parts = line.split(' ', 2)

            if current_id is None or parts[0] != current_id:
                if current_id is not None:
                    data.append({"caption": current_caption, "id": current_id})

                current_id = parts[0]
                current_caption = [parts[2]]
            else:
                current_caption.append(parts[2])

        if current_id is not None:
            data.append({"caption": current_caption, "id": current_id})

    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Replace 'input.txt' and 'output.json' with your actual file names
input_file_path = 'input.txt'
output_file_path = 'output.json'

data = convert_to_json(input_file_path)
save_to_json(data, output_file_path)
