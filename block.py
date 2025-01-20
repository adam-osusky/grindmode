import json


def load_sites(file_path):
    """
    Load a list of sites to block from a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        list: A list of websites to block.
    """
    try:
        with open(file_path, "r") as yaml_file:
            data = json.load(yaml_file)
            return data
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        return []


def block_sites_in_hosts(forbidden_sites):
    """
    Block the given sites by appending them to the /etc/hosts file.

    Args:
        forbidden_sites (list): A list of websites to block.
    """
    hosts_path = "/etc/hosts"
    try:
        with open(hosts_path, "a") as hosts:
            hosts.write("\n\n# Blocked Sites\n")
            for site in forbidden_sites:
                hosts.write(
                    f"0.0.0.0 {site}\n0.0.0.0 www.{site}\n::0 {site}\n::0 www.{site}\n"
                )
            print(f"Successfully blocked {len(forbidden_sites)} site(s).")
    except PermissionError:
        print(
            "Permission denied. Please run this script with administrative privileges."
        )
    except Exception as e:
        print(f"An error occurred while updating /etc/hosts: {e}")


if __name__ == "__main__":
    # Path to the YAML file
    sites_file_path = "blocked_sites.json"

    # Load sites from YAML
    sites_to_block = load_sites(sites_file_path)

    if not sites_to_block:
        print("No sites to block. Make sure the json file is correctly formatted.")
    else:
        block_sites_in_hosts(sites_to_block)
