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
me@my_computer# python3 junos_syslog_check_multidut.py -u user123 -p pass123 -t dut_list.txt 

Analyzing target host 10.0.0.11:
Sending command: show log messages | no-more | save /var/tmp/syslog_1681521613.865451

Sending command: show log messages | no-more

Logfile saved as /var/tmp/syslog_1681521613.865451.
################################################
########### Log Message Type Counts ############
################################################
There are 2 error messages present
There are 0 failure messages present - check BGP peerings if no route msg counts are high
There are 4 down messages present
There are 0 ddos messages present
There are 0 traceback messages present
There are 0 core messages present
There are 0 wedge messages present
There are 0 exception messages present
There are 0 restart messages present
There are 847 fpc messages present
There are 33 chassisd messages present
There are 0 heap messages present
There are 0 alarm messages present
There are 0 toggletrace messages present
There are 0 bad pdu messages present
There are 0 traceservice messages present
There are 0 jtask rpd messages present
################################################
############# System Log Analysis ##############
################################################
The first 10 error log messages are displayed below.
Apr 13 11:15:40  milnet-r1 kernel: peer_input_pending_internal: 5647: peer class: 0, type: 17, index: 0, vksid: 0, state: 1 reported a so_error 60
Apr 13 11:15:40  milnet-r1 kernel: peer_input_pending_internal: 5647: peer class: 0, type: 17, index: 0, vksid: 0, state: 1 reported a so_error 60
The first 10 log_down log messages are displayed below.
Apr 13 11:15:38  milnet-r1 rdd[6045]: RDD Peer (Ident: 0) went down.
Apr 13 11:15:38  milnet-r1 ppmd[5897]: PPMD: Connection Shutdown/Closed with  PFE: fpc0
Apr 13 11:15:49  milnet-r1 mib2d[5885]: SNMP_TRAP_LINK_DOWN: ifIndex 526, ifAdminStatus up(1), ifOperStatus down(2), ifName ge-0/0/0
Apr 13 11:15:49  milnet-r1 mib2d[5885]: SNMP_TRAP_LINK_DOWN: ifIndex 527, ifAdminStatus up(1), ifOperStatus down(2), ifName ge-0/0/1
The first 10 fpc log messages are displayed below.
Apr 10 22:20:36  milnet-r1 fpc0 SCHED: Thread 66 (PFE Statistics) ran for 1045 ms without yielding
Apr 10 22:20:38  milnet-r1 fpc0 Scheduler Oinker
Apr 10 22:20:38  milnet-r1 fpc0 Frame 0: sp = 0xda260908, pc = 0x80726c5
Apr 10 22:20:38  milnet-r1 fpc0 Frame 1: sp = 0xda260948, pc = 0x810a43b
Apr 10 22:20:38  milnet-r1 fpc0 Frame 2: sp = 0xda260988, pc = 0x8121696
Apr 10 22:20:38  milnet-r1 fpc0 Frame 3: sp = 0xda260e68, pc = 0x81665ae
Apr 10 22:20:38  milnet-r1 fpc0 Frame 4: sp = 0xda260ff8, pc = 0x80782b6
Apr 10 22:20:38  milnet-r1 fpc0 Frame 5: sp = 0xd74d0fd8, pc = 0x806f365
Apr 10 22:20:38  milnet-r1 fpc0 Frame 6: sp = 0xd74d0ff8, pc = 0x80782b6
Apr 10 22:20:38  milnet-r1 fpc0 Frame 7: sp = 0xffbbc2a8, pc = 0x8070f9a
The first 10 chassisd log messages are displayed below.
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_SNMP_TRAP7: SNMP trap generated: FRU removal (jnxFruContentsIndex 7, jnxFruL1Index 1, jnxFruL2Index 0, jnxFruL3Index 0, jnxFruName FPC: Virtual FPC @ 0/*/*, jnxFruType 3, jnxFruSlot 0)
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_FRU_OFFLINE_NOTICE: Taking FPC 0 offline: Removal
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_IPC_CONNECTION_DROPPED: Dropped IPC connection for FPC 0
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_IPC_WRITE_ERR_NULL_ARGS: FRU has no connection arguments fru_send_msg FPC 0
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_IFDEV_DETACH_FPC: ifdev_detach_fpc(0)
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_SNMP_TRAP3: ENTITY trap generated: entStateOperDisabled (entPhysicalIndex 20, entStateAdmin 3, entStateAlarm 0)
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_SNMP_TRAP0: ENTITY trap generated: entConfigChange
Apr 13 11:15:49  milnet-r1 chassisd[5872]: CHASSISD_SNMP_TRAP7: SNMP trap generated: FRU removal (jnxFruContentsIndex 7, jnxFruL1Index 1, jnxFruL2Index 0, jnxFruL3Index 0, jnxFruName FPC: Virtual FPC @ 0/*/*, jnxFruType 3, jnxFruSlot 0)
Apr 13 11:22:24  milnet-r1 chassisd[5872]: fpc_atlas_post_add() FPC slot 0 i2c_id 0xbaa is_vir [1] data_valid[1] first_install[0]is_jam[0] is_plug[0]
Apr 13 11:22:24  milnet-r1 chassisd[5872]: fpc_atlas_ok_to_powerup() FPC slot 0 i2c_id 0xbaa is_vir [1] data_valid[1]is_jam[0] is_plug[0]




Analyzing target host 10.0.0.21:
Sending command: show log messages | no-more | save /var/tmp/syslog_1681521624.719543

Sending command: show log messages | no-more

Logfile saved as /var/tmp/syslog_1681521624.719543.
################################################
########### Log Message Type Counts ############
################################################
There are 0 error messages present
There are 1632 failure messages present - check BGP peerings if no route msg counts are high
There are 11 down messages present
There are 0 ddos messages present
There are 0 traceback messages present
There are 0 core messages present
There are 0 wedge messages present
There are 0 exception messages present
There are 0 restart messages present
There are 32 fpc messages present
There are 0 chassisd messages present
There are 0 heap messages present
There are 0 alarm messages present
There are 0 toggletrace messages present
There are 0 bad pdu messages present
There are 0 traceservice messages present
There are 0 jtask rpd messages present
################################################
############# System Log Analysis ##############
################################################
The first 10 failure log messages are displayed below.
Apr 12 06:15:07  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:17:35  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:20:03  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:22:32  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:25:00  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:27:28  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:29:56  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:32:24  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:34:52  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
Apr 12 06:37:20  milnet-r4 rpd[19040]: JTASK_IO_CONNECT_FAILED: BGP_65777_65777.10.70.0.3: Connecting to 10.70.0.3+179 failed: No route to host
The first 10 log_down log messages are displayed below.
Apr 12 11:26:14  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 12 12:41:07  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 12 21:30:26  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 13 13:23:40  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 13 14:46:41  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 14 06:14:28  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 14 11:00:00  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 14 15:03:30  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 14 17:31:47  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
Apr 14 21:50:06  milnet-r4 bfdd[18854]: BFDD_TRAP_SHOP_STATE_DOWN: local discriminator: 77, new state: down, interface: ge-0/0/7.30, peer addr: 10.30.0.1
The first 10 fpc log messages are displayed below.
Apr 12 21:12:47  milnet-r4 fpc0 SCHED: Thread 71 (PFE Statistics) ran for 1006 ms without yielding
Apr 12 21:12:47  milnet-r4 fpc0 Scheduler Oinker
Apr 12 21:12:47  milnet-r4 fpc0 Frame 0: sp = 0xda6ef718, pc = 0x808cbf6
Apr 12 21:12:47  milnet-r4 fpc0 Frame 1: sp = 0xda6ef738, pc = 0x8cfb1b8
Apr 12 21:12:47  milnet-r4 fpc0 Frame 2: sp = 0xda6ef788, pc = 0x8cfe760
Apr 12 21:12:47  milnet-r4 fpc0 Frame 3: sp = 0xda6ef878, pc = 0x8c9f096
Apr 12 21:12:47  milnet-r4 fpc0 Frame 4: sp = 0xda6ef8c8, pc = 0x8cacebb
Apr 12 21:12:47  milnet-r4 fpc0 Frame 5: sp = 0xda6ef918, pc = 0x813dae9
Apr 12 21:12:47  milnet-r4 fpc0 Frame 6: sp = 0xda6efe78, pc = 0x8184e9d
Apr 12 21:12:47  milnet-r4 fpc0 Frame 7: sp = 0xda6efff8, pc = 0x8092636




Analyzing target host 10.0.0.31:
Sending command: show log messages | no-more | save /var/tmp/syslog_1681521635.277114

Sending command: show log messages | no-more

Logfile saved as /var/tmp/syslog_1681521635.277114.
################################################
########### Log Message Type Counts ############
################################################
There are 1 error messages present
There are 1 failure messages present - check BGP peerings if no route msg counts are high
There are 0 down messages present
There are 0 ddos messages present
There are 0 traceback messages present
There are 0 core messages present
There are 0 wedge messages present
There are 0 exception messages present
There are 0 restart messages present
There are 0 fpc messages present
There are 0 chassisd messages present
There are 0 heap messages present
There are 0 alarm messages present
There are 0 toggletrace messages present
There are 0 bad pdu messages present
There are 0 traceservice messages present
There are 0 jtask rpd messages present
################################################
############# System Log Analysis ##############
################################################
