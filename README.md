# Port Scanner Project

## Description

This project is a simple Python-based port scanner that allows users to scan specified ports on a target IP address. It attempts to establish a connection to each port and retrieves any available banners.

## Features

- User-friendly input for specifying multiple ports.
- Handles exceptions and errors gracefully.
- Implements socket timeout to avoid hanging on unreachable ports.
- Retrieves and displays banners from open ports.

## Installation

1. `git clone https://github.com/W4RSH3LL/Simple_Banner_Grabber.git`
2. `cd Simple_Banner_Grabber`

## Usage

1. **Run the Script**: Execute the script using Python 3.
- `sudo python3 port_scanner.py`

Libraries Used
* `socket`
Description: The socket library provides a way to create network connections and handle network communications.
Usage in the Project:
Creating Sockets: Used to create a socket object for communication.
Connecting to Ports: Used to attempt connections to specified ports.
Receiving Data: Used to receive data (banners) from open ports.
Handling Timeouts: settimeout() is used to avoid hanging on unresponsive ports.

Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request with your improvements or bug fixes.

License
This project is licensed under the MIT License.
