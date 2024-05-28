import ipaddress

def ip_class(ip):
    first_octet = int(ip.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'
    else:
        return None

def network_address(ip, ip_class):
    octets = ip.split('.')
    if ip_class == 'A':
        return f"{octets[0]}.0.0.0"
    elif ip_class == 'B':
        return f"{octets[0]}.{octets[1]}.0.0"
    elif ip_class == 'C':
        return f"{octets[0]}.{octets[1]}.{octets[2]}.0"
    else:
        return None

def convert_binary_to_dotted_decimal(binary_ip):
    binary_octets = [binary_ip[i:i+8] for i in range(0, 32, 8)]
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    return '.'.join(decimal_octets)

def main():
    ip_input = input("Enter IP address (in dotted decimal or binary format): ").strip()
    
    # Determine if input is binary or dotted decimal
    if '.' in ip_input:  # Dotted decimal format
        try:
            ip_obj = ipaddress.ip_address(ip_input)
            ip = str(ip_obj)
        except ValueError:
            print("Invalid IP address format.")
            return
    else:  # Binary format
        if len(ip_input) == 32 and all(c in '01' for c in ip_input):
            ip = convert_binary_to_dotted_decimal(ip_input)
        else:
            print("Invalid binary IP address format.")
            return
    
    ip_cls = ip_class(ip)
    if ip_cls in ['A', 'B', 'C']:
        net_address = network_address(ip, ip_cls)
        print(f"IP Address: {ip}")
        print(f"Class: {ip_cls}")
        print(f"Network Address: {net_address}")
    elif ip_cls in ['D', 'E']:
        print(f"IP Address: {ip}")
        print(f"Class: {ip_cls} (No network address for Class {ip_cls} IPs)")
    else:
        print("Invalid IP address.")

if __name__ == "__main__":
    main()
