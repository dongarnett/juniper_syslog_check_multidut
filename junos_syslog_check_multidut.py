import paramiko, os, re, sys, getopt, time, argparse
from pprint import pprint
from lib_ssh_connectivity import Device
from lib_junos_syslog_check import get_syslog_messages
from lib_junos_syslog_check import parse_system_messages


def main(argv):
    targets_file = ''
    username = ''
    password = ''
    opts, args = getopt.getopt(argv,"ht:u:p:",["targets=", "username=", "password="])
    for opt, arg in opts:
      if opt == '-h':
         print ('''
Usage:
junos_syslog_check_multidut.py -t <device_list_file> -u <username> -p <password>

Options:
-t     <device_list_file>      List of device IPs to analyze logs
-u     <username>              Device username
-p     <password>              Device passwword
--targets     <device_list_file>      List of device IPs to analyze logs
-username     <username>              Device username
-password     <password>              Device passwword
''')
         sys.exit()
      elif opt in ("-t", "--targets"):
         targets_file = arg
      elif opt in ("-u", "--username"):
         username = arg
      elif opt in ("-p", "--password"):
         password = arg
    '''DUT Login parameters'''
    user = username
    passwd = password
    timeout = 30
    device_list = []
    with open(targets_file) as dut_file:
        for line in dut_file:
            line = line.strip()
            device_list.append(line)
    for line in device_list:
        host_ip = line
        print(f'\n')
        print(f'\n')
        print(f'Analyzing target host {host_ip}:')
        dut_host = Device(host_ip, user, passwd)
        inputs = get_syslog_messages(dut_host)
        parse_system_messages(inputs)


if __name__ == '__main__':
    main(sys.argv[1:])
