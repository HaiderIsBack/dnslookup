import socket

def reverse_dns_lookup(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        return host_name[0]  # The first element of the tuple is the primary domain name
    except socket.herror as e:
        return f"Error: {e}"
    
def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return f"Error: {e}"

def main():
    while True:
        print("\n\n")
        print("[1] DNS Lookup (*domain name required)")
        print("[2] Reverse DNS Lookup (*ip address required)")
        print("\n[Press Enter to Exit]")
        inp = input("\nEnter opt: ")
        try:
            if inp == "":
                break
            else:
                if int(inp) == 1:
                    domain_name = input("Enter a domain name: ")
                    result = dns_lookup(domain_name)
                    print(f"DNS Lookup result: {result}")
                elif int(inp) == 2:
                    ip_address = input("Enter an IP address: ")
                    result = reverse_dns_lookup(ip_address)
                    print(f"Reverse DNS lookup result: {result}")
                else:
                    print("\nInvalid option!\n")
        except:
            print("\nInvalid Input!\n")

if __name__ == "__main__":
    main()
    