import toml

class Config:
    def __init__(self, connectionAddr = "", ledColour = [0,255,0], ledBrightness = 25, customColour = [0,255,0], colourSchemePath = "./Themes/OneLight.qss"):
        self.connectionAddr = connectionAddr
        self.ledColour = ledColour
        self.ledBrightness = ledBrightness
        self.customColour = customColour
        self.colourSchemePath = colourSchemePath

def LoadConfig(file_path):
    try:
        with open(file_path, 'r') as file:
            data = toml.load(file)
            return Config(
                connectionAddr = data['connectionAddr'],
                ledColour = data['ledColour'],
                ledBrightness = data['ledBrightness'],
                customColour = data['customColour'],
                colourSchemePath = data['colourSchemePath']
            )
            
    except Exception as e:
        print(f"Error loading TOML file: {e}")
        return None

def SaveConfig(file_path, config):
    try:
        data = {
            "connectionAddr": config.connectionAddr,
            "ledColour": config.ledColour,
            "ledBrightness": config.ledBrightness,
            "customColour": config.customColour,
            "colourScheme": config.colourSchemePath
        }
        with open(file_path, 'w') as file:
            toml.dump(data, file)
            return 0
    except Exception as e:
        print(f"Error saving to TOML file: {e}")
        return 1
