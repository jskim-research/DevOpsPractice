"""docker 실습

docker 설치관련:
https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/

wsl 설치관련:
https://docs.microsoft.com/en-us/windows/wsl/

docker를 이용한 연구환경 마련:
https://www.omnious.com/resources/research-team-docker-environment/

docker를 이용한 재구현 가능 환경 마련:
https://gzupark.dev/blog/A-guide-to-make-the-reproducible-environment-using-the-Docker-for-deep-learning-researcher/

docker 대상은 이름이 "Dockerfile"이어야 함

docker build -t image_name .  (./Dockerfile 로부터 image를 생성)
docker images image_name  (최근 image들 표시)
(--rm: 실행 종료 후 삭제, -d: daemon, -v: 파일 변화 시 적용, volume의 경우 현재 잘 안되고 있음)
docker run --rm -d 0.0.0.0:5000:5000/tcp --name dockertest image_name[:tag_name]
docker ps (or docker ps -a)
docker logs container_id
docker stop container_id
docker rm container_id
docker rmi image_name
docker tag image_name image_name:tag_name (태그 붙이기)
docker tag image_name hub_name/image_name:tag_name
docker push hub_name/image_name:tag_name  (이미 존재하는 이미지 및 태그 이어야함)
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! (from a Docker container with modified coddsae dd)'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
