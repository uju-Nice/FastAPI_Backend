from typing import Any


def userDetails(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title() 
    return full_name + " " + "You are welcome to python programming!"

print(userDetails("Nice", "Edox"))

def get_items(items: list[str]):
    for many_item in items:
      return many_item.upper()
print(get_items(["Python", "Java", "C++", "JavaScript"]))

class Server:
    def __init__(self, distro: str, ip_address: int):
        self.distro =distro
        self.ip_address = ip_address

    def get_server_info(operating_system, Server):     
        return operating_system.distro