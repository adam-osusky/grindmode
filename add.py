import json


def save_list_to_yaml(file_path, data_list):
    """
    Saves a list of strings into a YAML file.

    :param file_path: Path to the YAML file.
    :param data_list: List of strings to save.
    """
    if not isinstance(data_list, list) or not all(
        isinstance(item, str) for item in data_list
    ):
        raise ValueError("data_list must be a list of strings.")

    with open(file_path, "w") as yaml_file:
        json.dump(data_list, yaml_file)


# Example usage
data = ["youtube.com"]
file_name = "blocked_sites.json"

save_list_to_yaml(file_name, data)

print(f"List saved to {file_name}")
