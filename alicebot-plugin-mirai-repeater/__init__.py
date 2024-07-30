# For repeating group member's message

# First party modules
from random import randint
# Third party modules
from alicebot import Plugin

class Repeater(Plugin):
    priority = 2
    block = 0
    repeat_len = 2
    message_record = {}

    async def handle(self) -> None:
        try:                                                    #TODO: Support other message types
            await self.event.reply(self.event.messageChain)
        except:
            pass
    
    async def rule(self):
        if (self.event.adapter.name == "mirai" and 
            self.event.type == "GroupMessage"):

            current_message = str(self.event.messageChain)
            current_group = self.event.sender.group.id

            if not self.message_record.get(current_group):
                self.message_record[current_group] = [current_message]
                return
            
            if len(self.message_record.get(current_group)) < self.repeat_len:
                if current_message == self.message_record.get(current_group)[-1]:
                    self.message_record[current_group].append(current_message)
                    if len(self.message_record.get(current_group)) == self.repeat_len:
                        return True
                else:
                    self.message_record[current_group].clear()
                    self.message_record[current_group].append(current_message)
            else:
                if current_message == self.message_record.get(current_group)[-1]:
                    pass
                else:
                    self.message_record[current_group].clear()
                    self.repeat_len = randint(1,4)
                    print(self.repeat_len)
                    self.message_record[current_group].append(current_message)
        else:
            return False


