import paramiko

def shutdown_truenas(hostname, username, password):
    # Create an SSH client instance
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the TrueNAS server
        client.connect(hostname, username=username, password=password)

        # Execute the shutdown command
        stdin, stdout, stderr = client.exec_command('sudo shutdown -h now')

        # Print the output (optional)
        for line in stdout.readlines():
            print(line.strip())

        # Close the SSH connection
        client.close()
        print("TrueNAS system has been shut down successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")
        client.close()

if __name__ == "__main__":
    # Replace with your TrueNAS server details
    hostname = "192.168.127.116"
    username = "root"
    password = "don"

    shutdown_truenas(hostname, username, password)
