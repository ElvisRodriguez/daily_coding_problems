'''
This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D,
 where A, B, C, and D are numbers between 0 and 255.
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return
 ['254.25.40.123', '254.254.0.123'].
'''


def is_valid_ip_address(ip_address):
    bytes = ip_address.split(".")
    for byte in bytes:
        if len(byte) > 3 or int(byte) < 0 or int(byte) > 255:
            return False
        if len(byte) > 1 and int(byte) == 0:
            return False
        if len(byte) > 1 and int(byte) != 0 and byte[0] == '0':
            return False
    return True


def generate_valid_ip_addresses(string):
    string_length = len(string)
    if string_length > 12:
        return []
    string_copy = string
    ip_addresses = []
    for i in range(1, string_length - 2):
        for j in range(i + 1, string_length - 1):
            for k in range(j + 1, string_length):
                string_copy = string_copy[:k] + "." + string_copy[k:]
                string_copy = string_copy[:j] + "." + string_copy[j:]
                string_copy = string_copy[:i] + "." + string_copy[i:]
                if is_valid_ip_address(string_copy):
                    ip_addresses.append(string_copy)
                string_copy = string
    return ip_addresses


if __name__ == '__main__':
    string = '2542540123'
    print(generate_valid_ip_addresses(string))
