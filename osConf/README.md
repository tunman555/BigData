### OS and system Installation

1. Download fedora image from https://getfedora.org/en/workstation/download/ and create USB installation via software
   ex. rufus for example ==> https://linuxhint.com/install-fedora-workstation-35-usb/
2. Config each of NIC in path /etc/sysconfig/network-scripts/ to suit your operation
  ==> https://www.tecmint.com/set-add-static-ip-address-in-linux/
3. Config static route 
  ==> https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_static_routes_with_ip_commands
4. install vsftpd to jail ftp if you want 
  ==> https://phoenixnap.com/kb/how-to-setup-ftp-server-install-vsftpd-centos-7
5. config ntp server to get time syncing from time server 
6. Allowing Firewall 
7. Allowing multicast protocol : firewall-cmd --zone=zone-name --add-protocol=igmp
8. config sshd server
