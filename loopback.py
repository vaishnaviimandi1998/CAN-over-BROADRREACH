from time import sleep

custom_mac = "00:13:3B:B0:10:61"

def on_eth_msg_received(msg):
    if msg.mac_address_source == custom_mac:
        print(("Received following message from {0}: {1}".format(custom_mac, msg)))

g_ethernet_msg.mac_address_source = custom_mac
g_ethernet_msg.mac_address_destination = Logging.get_mac()

g_ethernet_msg.payload = System.Array[Byte](bytearray.fromhex("01 02 03 04 09"))

g_ethernet_msg.on_message_received += on_eth_msg_received
g_ethernet_msg.start_capture()

sleep(5)

g_ethernet_msg.send()

sleep(1)

g_ethernet_msg.stop_capture()
g_ethernet_msg.on_message_received -= on_eth_msg_received