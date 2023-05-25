import tomli as tomllib

def read_config(Category,Key):
    with open("static/config.toml","rb") as file:
        data = tomllib.load(file)
    return data[Category][Key]

    