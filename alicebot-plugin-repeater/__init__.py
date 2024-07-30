# For repeating group member's message

# First party modules
from typing import Dict, List, Optional
# Third party modules
from alicebot import Plugin, ConfigModel
from alicebot.adapter.mirai.event import MessageEvent

class Config(ConfigModel):
    __config_name__:str = "mirai_repeater"
    repeat_len = 3
    message_record: Dict[int, List[Optional[str]]] = {}

class Repeater(Plugin[MessageEvent, int, Config], config = Config):
    priority = 2
    block = False
    
    async def handle(self) -> None:
        try:                                                        #TODO: support other message types, such as meme or image
            await self.event.reply(self.event.messageChain)
        except:
            pass
    
    async def rule(self) -> bool:
            if (self.event.adapter.name == "mirai" and 
                self.event.type == "GroupMessage"):

                current_message = str(self.event.messageChain)
                current_group: int = self.event.sender.group.id                                                  

                if not self.config.message_record.get(current_group):                                            
                    self.config.message_record[current_group] = [current_message]
                    return False
                
                if len(self.config.message_record.get(current_group)) < self.config.repeat_len:
                    if current_message == self.config.message_record.get(current_group)[-1]:
                        self.config.message_record[current_group].append(current_message)
                        if len(self.config.message_record.get(current_group)) == self.config.repeat_len:
                            return True
                    else:
                        self.config.message_record[current_group].clear()
                        self.config.message_record[current_group].append(current_message)
                    return False
                else:
                    if current_message == self.config.message_record.get(current_group)[-1]:
                        pass
                    else:
                        self.config.message_record[current_group].clear()
                        self.config.message_record[current_group].append(current_message)

                    return False
            else:
                return False


