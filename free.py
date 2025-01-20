def unblock_sites():
    """
    Removes all site blocking entries added by the blocking script from the /etc/hosts file.
    """
    hosts_path = "/etc/hosts"
    start_marker = "# Blocked Sites"

    try:
        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        # Identify the lines to keep (everything before or not related to # Blocked Sites)
        keep_lines = []
        is_blocking_section = False

        for line in lines:
            if start_marker in line:
                is_blocking_section = True
                continue
            if is_blocking_section and line.strip() == "":
                is_blocking_section = False
                continue
            if not is_blocking_section:
                keep_lines.append(line)

        # Write the updated content back to the hosts file
        with open(hosts_path, "w") as hosts_file:
            hosts_file.writelines(keep_lines)

        print("Successfully removed all blocked site entries from the hosts file.")

    except PermissionError:
        print(
            "Permission denied. Please run this script with administrative privileges."
        )
    except Exception as e:
        print(f"An error occurred while modifying /etc/hosts: {e}")


if __name__ == "__main__":
    unblock_sites()
