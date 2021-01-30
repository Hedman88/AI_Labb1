
class MsgHandler:
    instance = False
    def __init__(self):
        if(instance == false):
            self.instance = True
            return self
        else:
            return self
    def HandleMsg(self, msg, inhabitants):
        for i in range(len(inhabitants)):
            if(msg.rcvrID == inhabitants[i].ID):
                inhabitants[i].RcvMessage(msg)
                break;

class Message:
    def __init__(self, senderID, rcvrID, content):
        self.senderID = senderID
        self.rcvrID = rcvrID
        self.content = content
