import json
from typing import Any, Dict

from .core import SpeechMapper
# 各エンジン実装を事前にインポートし、マップを用意
from .voicevox import VoicevoxMapper

# エンジン名 -> Mapperクラス のマッピング
_MAP: Dict[str, Any] = {
    "voicevox": VoicevoxMapper,
    # 他エンジンを追加する場合はここに登録
}


def get_mapper(engine: str, filepath: str) -> SpeechMapper:
    """
    エンジン名とJSONファイルパスから、対応する SpeechMapper インスタンスを取得するファクトリ関数

    :param engine: 対応エンジン名 (例: 'voicevox')
    :param filepath: マッピング用JSONファイルのパス
    :return: マッピング読み込み済みの SpeechMapper インスタンス
    """
    if engine not in _MAP:
        raise ValueError(f"エンジン '{engine}' のマッパーが見つかりません。対応可能なエンジン: {list(_MAP.keys())}")

    # JSON ファイルを読み込み
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        data = json.loads(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"ファイルが見つかりません: {filepath}")
    except json.JSONDecodeError:
        raise ValueError(f"JSON のパースに失敗しました: {filepath}")

    # Mapper クラス生成とロード
    MapperClass = _MAP[engine]
    mapper = MapperClass()
    mapper.load(data)
    return mapper
