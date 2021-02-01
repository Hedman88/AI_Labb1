import inhabitanthandler as ih
class MsgHandler:

#Takes a message and finds the inhabitant to send it to.
    def HandleMsg(self, msg):
        print("Inhabitant ID", msg.senderID, "sends:",'"', msg.content,'"', "to reciever ID:", msg.rcvrID)
        print("")
        for i in range(len(ih.handler.inhabitants)):
            if(msg.rcvrID == ih.handler.inhabitants[i].ID):
                ih.handler.inhabitants[i].RcvMessage(msg)
                break;

class Message:
    def __init__(self, senderID, rcvrID, content):
        self.senderID = senderID
        self.rcvrID = rcvrID
        self.content = content

handler = MsgHandler()
