import json
import pytest
from voice_dict import get_mapper

@pytest.fixture
def sample_speakers(tmp_path):
    # VoiceVox speakers JSON のサンプルデータ
    data = [
        {
            "name": "四国めたん",
            "styles": [
                {"id": 2}, {"id": 0}, {"id": 6}, {"id": 4}, {"id": 36}, {"id": 37}
            ]
        }
    ]
    file_path = tmp_path / "speakers.json"
    file_path.write_text(json.dumps(data), encoding='utf-8')
    return str(file_path)

def test_voicevox_mapping(sample_speakers):
    mapper = get_mapper('voicevox', sample_speakers)
    # 名前からIDリストを取得
    assert mapper.get_ids_by_name('四国めたん') == [2, 0, 6, 4, 36, 37]
    # IDから名前を取得
    assert mapper.get_name_by_id(2) == '四国めたん'
    # 存在しないIDへのアクセスは KeyError
    with pytest.raises(KeyError):
        mapper.get_name_by_id(999)