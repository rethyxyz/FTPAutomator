import ftplib
import logging

# Setup logging
logging.basicConfig(filename='ftp_session.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def list_directory(ftp, path):
    """
    Recursively list the contents of a directory on the FTP server.
    """
    original_dir = ftp.pwd()  # Remember the current working directory
    try:
        ftp.cwd(path)  # Change to the directory to list
        items = ftp.nlst()  # Get directory contents
        for item in items:
            try:
                ftp.cwd(item)  # Try to change directory to item
                logging.info(f"Entering directory: {ftp.pwd()}")
                print(f"Entering directory: {ftp.pwd()}")
                list_directory(ftp, item)  # Recursively list subdirectories
                ftp.cwd('..')  # Change back to the parent directory
            except ftplib.error_perm:
                # If an error occurs, it's not a directory, so just print the item
                logging.info(f"Found file: {item}")
                print(f"Found file: {item}")
    except ftplib.error_perm as e:
        logging.error(f"Access denied to {path}: {e}")
        print(f"Access denied to {path}: {e}")
    finally:
        ftp.cwd(original_dir)  # Always change back to the original directory

def try_login(ip):
    try:
        # Try anonymous login first
        ftp = ftplib.FTP(ip)
        ftp.login()  # Anonymous login
        logging.info(f"Successfully logged into {ip} with anonymous login.")
        print(f"Successfully logged into {ip} with anonymous login.")
        print("Directory listing:")
        list_directory(ftp, '.')
        ftp.quit()
        return True
    except ftplib.error_perm as e:
        # If anonymous login fails, try empty login
        try:
            ftp = ftplib.FTP(ip)
            ftp.login(user='', passwd='')  # Empty login
            logging.info(f"Successfully logged into {ip} with empty login.")
            print(f"Successfully logged into {ip} with empty login.")
            print("Directory listing:")
            list_directory(ftp, '.')
            ftp.quit()
            return True
        except:
            logging.error(f"Failed to log into {ip} with empty login.")
    except Exception as e:
        logging.error(f"Failed to access {ip}: {e}")
    return False

def main():
    filename = "ips.txt"
    try:
        with open(filename, 'r') as file:
            ips = file.readlines()
    except FileNotFoundError:
        logging.error(f"The file {filename} was not found.")
        print(f"The file {filename} was not found.")
        return

    for ip in ips:
        ip = ip.strip()
        if try_login(ip):
            logging.info(f"{ip} is accessible.")
            print(f"{ip} is accessible.")
        else:
            logging.info(f"{ip} is not accessible.")
            print(f"{ip} is not accessible.")

if __name__ == "__main__":
    main()

