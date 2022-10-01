import os
import argparse

parser = argparse.ArgumentParser(description="arguments")
parser.add_argument("--add", type=str, nargs="+", help="add host")
parser.add_argument("--remove", type=str, nargs="+", help="remove host")

FILE_PATH = os.path.join("hosts")

with open(FILE_PATH, "r") as f:
    l = f.readlines()


def remove_host(ip: str, hostname: str):
    for i in l:
        n = i.split()
        if n[0] == ip or n[1] == hostname:
            l.remove(i)
    try:
        with open(FILE_PATH, 'w') as f:
            f.writelines(l)
        print("Success")
    except IOError as e:
        print(e)


def add_host(ip, hostname):
    for i in l:
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
