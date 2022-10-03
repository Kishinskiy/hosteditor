import os
import argparse

parser = argparse.ArgumentParser(description="arguments")
parser.add_argument("--add", type=str, nargs="+", help="add host")
parser.add_argument("--remove", type=str, nargs="+", help="remove host")

FILE_PATH = os.path.join("/etc/hosts")


def _read_host():
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
    return lines


def remove_host(ip: str, hostname: str):
    lines = _read_host()
    for i in lines:
        n = i.split()
        if n[0] == ip or n[1] == hostname:
            lines.remove(i)
    try:
        with open(FILE_PATH, 'w') as file:
            file.writelines(lines)
        print("Success")
    except IOError as e:
        print(e)


def add_host(ip, hostname):
    lines = _read_host()
    for i in lines:
        n = i.split()
        if n[0] == ip or n[1] == hostname:
            print("host already exists")
            return
    try:
        with open(FILE_PATH, 'a') as f:
            f.write(ip + "      " + hostname)
            print(f"Added IP {ip}  for HOSTNAME {hostname} to " + FILE_PATH)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    arg = parser.parse_args()

    if arg.add:
        add_host(arg.add[0], arg.add[1])
    elif arg.remove:
        remove_host(arg.remove[0], arg.remove[1])
