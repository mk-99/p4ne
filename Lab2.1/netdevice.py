import paramiko, time, re

host_ip = '10.31.70.209'
login = 'restapi'
password = 'j0sg1280-7@'

def net_command(session, cmd, timeout=1):
    "Send command cmd to Cisco device using session session, returns decondes string"

    BUF_SIZE = 65536

    session.send("\n")
    session.recv(BUF_SIZE)
    if cmd[:-1] != "\n":
        cmd = cmd + "\n"
    session.send(cmd)
    time.sleep(timeout)
    return session.recv(BUF_SIZE).decode()

def disable_scrolling(session):
    return net_command(session, 'terminal length 0')

# Create ssh connector to network device
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to network device
ssh_connection.connect(host_ip, username=login, password=password, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

# Send commands and receive command outputs
disable_scrolling(session)
cmd_lines = net_command(session, 'show interfaces', timeout=3).split('\n')

for current_line in cmd_lines:
    if m := re.match("^([A-Z].+?) is", current_line):
        print("Interface " + m.group(1))
    if m := re.match("^.+?([0-9]+) packets input, ([0-9]+) bytes", current_line):
        print("Packets/bytes input: ", m.group(1), "/", m.group(2))

    if m := re.match("^.+?([0-9]+) packets output, ([0-9]+) bytes", current_line):
        print("Packets/bytes output: ", m.group(1), "/", m.group(2))


ssh_connection.close()

