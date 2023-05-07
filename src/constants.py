from types import SimpleNamespace
from src.utils.keyborad import create_keyborad


keys = SimpleNamespace(
    random_connect=":bust_in_silhouette: Random Connect",
    setting=":gear: Settings"
)
keybords = SimpleNamespace(
    main=create_keyborad(keys.random_connect, keys.setting)
)
