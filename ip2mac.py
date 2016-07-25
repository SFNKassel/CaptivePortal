from isc_dhcp_leases import Lease, IscDhcpLeases


def lookup(ip):
	leases = IscDhcpLeases('/path/to/dhcpd.leases')
	return leases.get_current()[ip].ethernet 
