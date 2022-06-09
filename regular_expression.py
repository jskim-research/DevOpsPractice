"""Chapter 1-xx 정규 표현식 사용
"""

import re


class ReTest:
    def __init__(self, target):
        self.target = target

    def search(self, pattern):
        # 첫 번째로 일치한 항목만 반환함
        result = re.search(pattern, self.target)
        print(result)
        return result

    def findall(self, pattern):
        # 모든 일치하는 항목 반환 (list로 반환하므로 리소스 사용 증가)
        result = re.findall(pattern, self.target)
        print(result)
        return result

    def finditer(self, pattern):
        # 지연 평가
        result = re.finditer(pattern, self.target)
        print(result)
        return result

    def sub(self, pattern, replace):
        result = re.sub(pattern, replace, self.target)
        print(result)
        return result


# re 명령어 사용시엔 문자열 앞에 r을 붙인다.
# 검색
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
             Rostam Batmanglij <rostam@vpwk.com>,
             Bobbi Baio <bbaio@vpwk.com> Chraa'''

r = ReTest(cc_list)

# Rostam이 cc_list 안에 있는가?
r.search(r'Rostam')

# R 또는 B로 시작, obb, i 또는 y로 끝
r.search(r'[RB]obb[i,y]')

# a-z 사이의 값이 뒤에 두 번 나타나는가 (범위 지정)
r.search(r'Chr[a-z][a-z]')

# 해당 범위의 글자가 한 번 이상 나타나는 것들
r.search(r'[A-Za-z]+')

# 정확히 몇 번 나타나는 것들
r.search(r'[A-Za-z]{6}')

# email@address.address 찾기
r.search(r'[A-Za-z]+@[A-Za-z]+\.[a-z]+')

# 미리 정의된 기호 \w = [a-zA-Z0-9_], \d = [0-9]
r.search(r'\w+')
r.search(r'\w+@\w+\.\w+')

# 그룹 지정 (소괄호 사용), 네임드 그룹 (?P<name> 사용)
matched = r.search(r'(?P<name>\w+)@(\w+)\.(\w+)')
print(matched.group(0))
print(matched.group(1))
print(matched.group(2))
print(matched.group(3))
print(matched.group("name"))

r.findall(r'\w+@\w+\.\w+')

# 반복자 반환
matched = r.finditer(r'\w+@\w+\.\w+')
print(next(matched))
print(next(matched))
print(next(matched))

# 반복자 with group 사용 가능 + 반복문 예제
matched = r.finditer(r'(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)')
for m in matched:
    print(m.groupdict())

# 치환
print(re.sub("\d", "#", "your password is 9321"))
r.sub(r'(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)', "\g<TLD>.\g<SLD>.\g<name>")  # 그룹 순서 바꾸기

# 컴파일링 (미리 객체로 만들어두기)
regex = re.compile(r'(?P<name>\w+)@(\w+)\.(\w+)')
print(regex.search(cc_list))

