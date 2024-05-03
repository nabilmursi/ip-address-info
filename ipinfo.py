import sys
import requests

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    if len(sys.argv) < 2:
        # If no IP address is provided, default to fetching information for the requester's IP
        ip_address = ""
    else:
        ip_address = sys.argv[1]

    ip_info = get_ip_info(ip_address)
    if ip_info and ip_info.get('status') == 'success':
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Failed to retrieve information. Error:", ip_info.get('message', 'Unknown error'))

if __name__ == "__main__":
    main()
