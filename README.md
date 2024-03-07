# FTPAutomator

FTPAutomator is a Python script designed to automate the process of logging into FTP servers, listing directory contents, and identifying writable directories. It supports both anonymous and empty logins, recursively explores directories, and logs session activities as well as writable directories for further analysis.

## Features

- **Automated FTP Logins:** Supports anonymous and empty logins to FTP servers.
- **Directory Exploration:** Recursively lists all directories and files on the server.
- **Writable Directory Identification:** Checks and logs all writable directories.
- **Logging:** Logs all FTP session activities to a file and separately logs servers with writable directories.

## Getting Started

### Prerequisites

- Python 3.x
- Access to the internet and permissions to connect to FTP servers

### Installation

1. Clone this repository to your local machine: `git clone https://github.com/rethyxyz/FTPAutomator.git`

2. Navigate to the cloned repository: `cd FTPAutomator`

### Usage

1. Prepare a text file named `ips.txt` containing one IP address per line. These IP addresses should be the FTP servers you want to connect to.

2. Run the script: `python ftp_automator.py`

3. Check the `ftp_session.log` and `writable_ips.log` files for the session activity and writable directories log, respectively.

## Contributing

Contributions to FTPAutomator are welcome. Please ensure to follow the contribution guidelines.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Brody Rethy - [@rethyxyz](https://x.com/rethyxyz)

Project Link: [https://github.com/rethyxyz/FTPAutomator](https://github.com/rethyxyz/FTPAutomator)
