import tomllib

from .world import World

def read_config():
    with open("src/config.toml", "rb") as config_file:
        return tomllib.load(config_file)


def main():
    config = read_config()
    window_width = config.get("window").get("width") # type: ignore
    window_height = config.get("window").get("height") # type: ignore
    fps = config.get("game").get("fps") # type: ignore
    tilesize = config.get("game").get("tilesize") # type: ignore

    World(window_width, window_height, tilesize).start(fps) 


if __name__ == "__main__":
   main() 