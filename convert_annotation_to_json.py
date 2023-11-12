import json

def convert_to_json(input_file):
    data = []

    with open(input_file, 'r') as file:
        lines = file.readlines()

        current_id = None
        current_caption = []

        for line in lines:
            line = line.strip()
            parts = line.split(' ', 1)

            if current_id is None or parts[0] != current_id:
                if current_id is not None:
                    data.append({"caption": current_caption, "id": current_id  + '.avi'})

                current_id = parts[0]
                current_caption = [parts[1]]
            else:
                current_caption.append(parts[1])

        if current_id is not None:
            data.append({"caption": current_caption, "id": current_id + '.avi'})

    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Replace 'input.txt' and 'output.json' with your actual file names
input_file_path = 'annotations.txt'
output_file_path = 'annotations.json'

data = convert_to_json(input_file_path)
save_to_json(data, output_file_path)
