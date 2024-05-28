import ipaddress

def get_subnet_network_ids(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)
    
    print(f'Network address: {network.network_address}')
    print(f'Broadcast address: {network.broadcast_address}')
    print(f'Total subnets: {network.num_addresses}')
    
    subnet_network_ids = []
    for subnet in network.subnets():
        subnet_network_ids.append(subnet.network_address)
    
    return subnet_network_ids

# Example Usage
ip_address = input("ENTER IP ADDRESS\n")  ## Example Usage ip_address = '192.168.1.0' subnet_mask = '255.255.255.240'  # This is a /28 subnet mask
subnet_mask = input("ENTER SUBNET MASK\n")  # This is a /28 subnet mask

subnet_ids = get_subnet_network_ids(ip_address, subnet_mask)
print("Subnet Network IDs:")
for idx, subnet_id in enumerate(subnet_ids):
    print(f'Subnet {idx+1}: {subnet_id}')