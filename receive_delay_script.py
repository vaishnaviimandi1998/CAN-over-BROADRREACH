def read(msg):\
print ("Received following message from {0} || {1} || {2}".format(msg.mac_address_source, msg.payload, msg))

# loop for a total of 24000s and wait 10s for receiving each message
i = 0
while (i<1200):

    # on receiving a ethernet frame attach the frame to a ethernet message type object
    g_ethernet_msg.on_message_received += read
    g_ethernet_msg.start_capture()                  #start listening to frames

    sleep(10)                                       #wait for a frame

    g_ethernet_msg.stop_capture()                   #stop frame capture
    g_ethernet_msg.on_message_received -= read      
    # once message receving is complete remove function from message object
    i += 1
