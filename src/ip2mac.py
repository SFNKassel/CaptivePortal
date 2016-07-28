from isc_dhcp_leases import Lease, IscDhcpLeases


def lookup(ip):
	leases = IscDhcpLeases('/var/lib/dhcp/dhcpd.leases')
	leaseList = leases.get()
	for l in leaseList:
		if l.ip == ip:
			return l.ethernet
	return None
