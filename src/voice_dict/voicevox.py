import json
from typing import List, Any, Dict

from .core import SpeechMapper


class VoicevoxMapper(SpeechMapper):
    """
    VoiceVox の speakers JSON 出力を読み込み、音声名<->IDマッピングを提供するクラス
    """

    def __init__(self) -> None:
        self._name_to_ids: Dict[str, List[int]] = {}
        self._id_to_name: Dict[int, str] = {}

    def load(self, data: Any) -> None:
        if isinstance(data, str):
            info = json.loads(data)
        else:
            info = data
        for speaker in info:
            name = speaker.get("name")
            ids = [style.get("id") for style in speaker.get("styles", []) if "id" in style]
            self._name_to_ids[name] = ids
            for _id in ids:
                self._id_to_name[_id] = name

    def get_ids_by_name(self, name: str) -> List[int]:
        return self._name_to_ids.get(name, [])

    def get_name_by_id(self, id: int) -> str:
        if id not in self._id_to_name:
            raise KeyError(f"ID '{id}' に対応する音声名が見つかりません")
        return self._id_to_name[id]
