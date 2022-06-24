"""
pytest 실험용 코드
test하고자 할 경우 코드또는 파일은 test_ 로 시작해야한다. (e.g., test_xx)

pytest -q: 간략한 결과 정보 띄움
pytest -q --fixtures: 사용가능한 내장 fixture 및 custom fixture 표시

원격 서버 등에서 test가 가능케하는 testinfra는 책 305 쪽부터 확인할 것
"""
import pytest
import random

def test_string():
    # 문자열 비교가 쉽도록 로그를 찍어준다.
    assert "assert" == "asert"


def test_array():
    # list의 어느 부분이 일치하지 않았는지 알려준다.
    assert [1, 2, 3, 4] == [2, 3, 4]


class TestStringToBool:
    values = ["yes", "Yes", "0", "True", "da"]

    def string_to_bool(self, value: str):
        if value.lower() == "yes" or value.lower() == "true":
            return True
        return False

    # 함수는 하나인데 value만 다르게 해야될 경우 밑과 같이 처리 가능
    @pytest.mark.parametrize('value', values)
    def test_values(self, value: str):
        assert self.string_to_bool(value)


@pytest.fixture
def mon_keyring():
    # 키링 파일 내용 반환 함수
    def make_keyring(default=False):
        if default:
            key = "AQBvaBFZAAAABAA9VHgwCg3rWn8fMaX8KL01A=="
        else:
            key = "%032x==" % random.getrandbits(128)
        return """
        
        [mon.]
            key = %s
                caps mon = "allow *"
        """ % key
    return make_keyring


def test_default_key(mon_keyring):  # fixture를 바로 인자로 갖다 쓸 수 있음
    contents = mon_keyring(default=True)  # mon_keyring 자체가 make_keyring이므로 이런 식으로 인자 줄 수 있음
    assert "AQBvaBFZAAAABAA9VHgwCg3rWn8fMaX8KL01A==d" in contents


@pytest.fixture
def keyring_file(mon_keyring, tmpdir):  # tmpdir은 임시폴더 이름으로 test 후 삭제됨. 내장 fixture라고 함
    def generate_file(default=False):
        keyring = tmpdir.join('keyring')
        keyring.write_text(mon_keyring(default=True), encoding="utf-8")
        return keyring.strpath
    return generate_file


def test_keyring_file_contents(keyring_file):
    keyring_path = keyring_file(default=True)
    with open(keyring_path) as fp:
        contents = fp.read()
    assert "AQBvaBFZAAAABAA9VHgwCg3rWn8fMaX8KL01A==d" in contents

