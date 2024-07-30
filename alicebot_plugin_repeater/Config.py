"""插件配置。"""

from alicebot import ConfigModel
from typing import Dict, List, Optional


class Config(ConfigModel):
    __config_name__:str = "mirai_repeater"
    repeat_len = 3
    message_record: Dict[int, List[Optional[str]]] = {}
