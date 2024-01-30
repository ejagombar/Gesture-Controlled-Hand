import toml

class Config:
    def __init__(self, connectionAddr, ledColour, ledBrightness, customColour, camera_index, colourScheme):
        self.connectionAddr = connectionAddr
        self.ledColour = ledColour
        self.ledBrightness = ledBrightness
        self.customColour = customColour
        self.camera_index = camera_index
        self.colourScheme = colourScheme

def load_toml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = toml.load(file)
            return Config(
                data['connectionAddr'],
                data['ledColour'],
                data['ledBrightness'],
                data['customColour'],
                data['camera_index'],
                data['colourScheme']
            )

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading TOML file: {e}")
        return None

def save_to_toml_file(file_path, my_struct):
    try:
        data = {
            'connectionAddr': my_struct.connectionAddr,
            'ledColour': my_struct.ledColour,
            'ledBrightness': my_struct.ledBrightness,
            'customColour': my_struct.customColour,
            'camera_index': my_struct.camera_index,
            'colourScheme': my_struct.colourScheme
        }
        with open(file_path, 'w') as file:
            toml.dump(data, file)
        print(f"Data successfully saved to '{file_path}'.")
    except Exception as e:
        print(f"Error saving to TOML file: {e}")
