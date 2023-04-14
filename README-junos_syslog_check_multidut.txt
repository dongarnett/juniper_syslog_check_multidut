# junos_syslog_check


Purpose:
This tool sweeps log messages across multiple devices by reading a list of device IP addresses from an external file.

It perform the following workflow on each device:
1. Obtain system log messages
2. Timestamps and saves the log file to /var/tmp
3. Inform interesting message type counts
4. Displays the first 10 entries of any interesting type logging messages.

This tool can be run at the end of a larger script after device triggers have been exercised.
This tool can also be run without triggers to determine any existing messages present.


The system log are inspected for the following interesting message types:
1.  errors
2.  failures
3.  fail_no_route
4.  down
5.  ddos
6.  traceback
7.  core
8.  wedge
9.  exception
10. restart
11. fpc
12. chassisd
13. heap
14. alarm
15. toggletrace
16. badpdu
17. tracesevice
18. jtask_rpd_toggle_trace
19. jtask_tracethread
20. lacp_bad_pdu


Requirements:
The Paramiko SSH library is required for connectivity to the target device.


Usage:
junos_syslog_check_multidut.py -t <device_list_file> -u <username> -p <password>

Options:
-t     <device_list_file>      List of device IPs to analyze logs
-u     <username>              Device username
-p     <password>              Device passwword
--targets     <device_list_file>      List of device IPs to analyze logs
-username     <username>              Device username
-password     <password>              Device passwword



Example Run:
