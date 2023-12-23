import paramiko

def shutdown_truenas(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, username=username, password=password)

        stdin, stdout, stderr = client.exec_command('poweroff')

        for line in stdout.readlines():
            print(line.strip())

        client.close()
        print("TrueNAS system has been shut down successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")
        client.close()

if __name__ == "__main__":
    hostname = "192.168.127.116"
    username = "root"
    password = "don"

    shutdown_truenas(hostname, username, password)

