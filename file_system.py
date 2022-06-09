"""Chapter2 파일시스템 관련 예제

대용량 파일 => generator (yield) 활용

os module => remove, rmdir, mkdir 등 상당수의 로우 레벨 OS 시스템 콜 처리 (특정 OS에 종속된 명령은 피해야함)
pathlib => path를 문자열이 아닌 객체로 관리하여 객체 생성 후 함수를 통해 cwd 또는 parent 등을 얻을 수 있음
"""
import os


# 경로 관련 명령
cur_dir = os.getcwd()
print(cur_dir)

# 최하위 경로와 상위 경로 나누기
print(os.path.split(cur_dir))

# 상위 경로 반환
print(os.path.dirname(cur_dir))

# 최하위 경로 반환
print(os.path.basename(cur_dir))

print("File tree")
while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)

print(os.path.join("root\\sub1", "filename"))
print(os.path.abspath(__file__))
print(os.path.exists(__file__))


def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)

    for child in childs:
        child_path = os.path.join(parent_path, child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            size = os.path.getsize(child_path)
            print(f"File: {child_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)


# walk_path("./")


def lib_walk_path(parent_path):
    # os.walk => parent path로부터 모든 하위 파일 walk (generator)
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")

        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            print(f"File: {file_path}")


lib_walk_path("./")
