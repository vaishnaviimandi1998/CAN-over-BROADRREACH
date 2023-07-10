mac_destination = ["00:13:3B:B0:0E:A8"]
mac_source = ["00:13:3B:B0:10:61"]
message_span = 0
# loop for to keep on sending data at an interval of 20s for total 20000s
while (message_span<1000):

    # fill the fields of ethernet message object defined
    g_ethernet_msg.mac_address_source = mac_source[0] #Logging.get_mac()
    g_ethernet_msg.mac_address_destination = mac_destination[0]
    g_ethernet_msg.payload = System.Array[Byte](bytearray("SCRIPT TEST","utf-8"))

    # send the ethernet message object and wait for 20s
    sleep(10)
    g_ethernet_msg.send()
    sleep(10)

    
    # stop sending message and decrease the message counter by one
    g_ethernet_msg.stop_capture()
    message_span-=1
