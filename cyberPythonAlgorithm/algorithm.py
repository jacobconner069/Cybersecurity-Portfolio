import_file = "allow_list.txt"
remove_list = {}
with open(import_file, "r") as file:
    ip_addresses = file.read().split()
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)
ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(ip_addresses)
