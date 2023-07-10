from time import sleep

custom_mac = "00:13:3B:B0:10:61"

def on_eth_msg_received(msg):
    if msg.mac_address_source == custom_mac:
        print(("Received following message from {0}: {1}".format(custom_mac, msg)))

g_ethernet_msg.on_message_received += on_eth_msg_received
g_ethernet_msg.start_capture()

sleep(5)

g_ethernet_msg.stop_capture()
g_ethernet_msg.on_message_received -= on_eth_msg_received