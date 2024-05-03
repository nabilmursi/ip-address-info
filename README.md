IP address input to retrieve information, or by default, it fetches details of the requester's IP address if none is specified.

Comprehensive Output: Provides detailed information such as location, ISP, IP type, and more.
Easy to Use: Simple command-line interface suitable for beginners and advanced users alike.
Prerequisites
To run this script, you will need:

Python: The script is written in Python, so you need Python 3.x installed on your machine. You can download it from python.org.
Requests Library: This script uses the requests library to make HTTP requests. You can install it using pip:

$ pip install requests

Installation
To get started with this script, follow these steps:

Clone the Repository:
First, clone this repository to your local machine using Git:

$ git clone https://github.com/nabilmursi/ip-address-info.git
$ cd ipinfo-fetcher

Navigate to the Project Directory:
Change into the project directory:

$ cd ipinfo-fetcher

Usage
The script can be executed from the command line. Here’s how you can use it:

Running the Script
To run the script, open your terminal and execute:

$ python3 ipinfo.py [IP address]

If an IP address is provided, the script will fetch information for that IP.
If no IP address is provided, the script will automatically fetch information for the IP address of the machine making the request.

Examples
Fetch Information for a Specific IP:

python3 ipinfo.py 8.8.8.8

This will fetch and display information about the IP address 8.8.8.8.
Fetch Information for Your Own IP:

$ python3 ipinfo.py

This will fetch and display information about your own IP address.
Understanding the Output
The output of the script includes several pieces of information about the IP address:

Query: The IP address queried.
Status: Success or fail.
Country, RegionName, City: Location details.
Zip: Postal code.
Lat, Lon: Latitude and Longitude.
Timezone: Local timezone of the IP.
Isp: Internet service provider.
Org: Organization name.
Troubleshooting
If you encounter any issues while using the script, consider the following common solutions:

Dependencies Not Installed: Ensure you have Python and the requests library installed. You can install requests using pip install requests.
Network Issues: Check your internet connection. A stable internet connection is required to fetch data from ip-api.com.
API Limit Reached: The ip-api.com service may temporarily block requests if too many are made in a short period. If this happens, try again after some time or from a different IP address.
License
This project is licensed under the MIT License. See the LICENSE file in the repository for more details.

Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Contact
If you have any suggestions or questions, please open an issue in the GitHub repository.

