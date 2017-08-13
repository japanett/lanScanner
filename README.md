LAN Scanner
by Japanet
=================

.. figure:: https://scontent.fcpq1-1.fna.fbcdn.net/v/t1.0-9/20769963_1537134596352409_8197520883418071590_n.jpg?oh=1622271396d06fd57f17f4bbd633790c&oe=59EFB299
	:align: center


Simple python script to scan LAN network

1. Find hosts that are on the LAN passively
2. Uses an arp-ping to actively identify hosts
3. Scan each host to determine open ports and services
4. Store record of hosts in JSON file, html webpage, or prints to screen

**Note:** Since IP addresses change, the hosts are finger printed via their MAC address.

Alternatives
--------------

`Fing <http://www.overlooksoft.com/fing>`__ is a great and fast network scanner, I have
their app on my iPad. However, the ``fing`` commandline tool for
RPi I have noticed errors in the MAC address and therefor don't trust it for this
application.

Install
--------

Pre-requisites::


