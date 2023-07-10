from time import sleep

custom_mac = "00:13:3B:B0:10:61"

g_ethernet_msg.mac_address_source = custom_mac
g_ethernet_msg.mac_address_destination = "00:13:3B:B0:0E:A8"
g_ethernet_msg.payload = System.Array[Byte](bytearray.fromhex("01 02 03 04 09"))

g_ethernet_msg.start_capture()
sleep(1)
g_ethernet_msg.send()
sleep(1)
g_ethernet_msg.stop_capture()