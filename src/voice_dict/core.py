from abc import ABC, abstractmethod
from typing import Any, List


class SpeechMapper(ABC):
    """
    TTSエンジンごとの音声名<->IDマッピングインターフェース
    """

    @abstractmethod
    def load(self, data: Any) -> None:
        pass

    @abstractmethod
    def get_ids_by_name(self, name: str) -> List[int]:
        pass

    @abstractmethod
    def get_name_by_id(self, id: int) -> str:
        pass
