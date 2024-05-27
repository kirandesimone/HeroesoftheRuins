import tomllib

from .entities.world import World

def read_config():
    with open("src/config.toml", "rb") as config_file:
        return tomllib.load(config_file)


def main():
    config = read_config()
    window_width = config.get("window").get("width")
    window_height = config.get("window").get("height")
    fps = config.get("game").get("fps")

    World(window_width, window_height).start(fps) 


if __name__ == "__main__":
   main() 