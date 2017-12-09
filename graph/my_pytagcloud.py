#!__*__coding:utf-8__*__

"""
프로그램 설치
pip install simplejson
pip install pygame
pip install pytagcloud

한글 폰트 복사
아래와는 경로가 다를 수 있음
copy c:\windows\fonts\malgun.ttf C:\Anaconda3\Lib\site-packages\pytagcloud\fonts

한글 폰트 등록
C:\Anaconda3\Lib\site-packages\pytagcloud\fonts\fonts.json 수정
web 항목은 수정할 필요 없음
{
    "name": "Malgun",
    "ttf": "Malgun.ttf",
    "web": "http://fonts.googleapis.com/css?family=Nobile"
},


폰트 등록 다른 예
구글 노토 폰트 다운로드
https://www.google.com/get/noto/#sans-kore

{
    "name": "NotoSansCJKkr-Bold",
    "ttf": "NotoSansCJKkr-Bold.otf",
    "web": "http://fonts.googleapis.com/css?family=Nobile"
},

"""
import os
import collections
import pytagcloud
from pytagcloud import create_tag_image, create_html_data, make_tags, LAYOUT_HORIZONTAL, LAYOUTS, LAYOUT_MIX, LAYOUT_VERTICAL, LAYOUT_MOST_HORIZONTAL, LAYOUT_MOST_VERTICAL
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts


def make_pytagcloud_image(data, imagefilename, most_top_number=50):
    """
    data 은 리스트 형태로 데이터가 들어와야 함
    """
    imagefile_size = (1000, 1000)
    max_word_size = 200
    background_color = (255, 255, 255)

    c = collections.Counter(data)
    d = c.most_common(most_top_number)
    tags = make_tags(d, maxsize = max_word_size)

    (i,j) = os.path.splitext(imagefilename)
    vertical_image = i + "_vertical" + j
    horizontal_image = i + "_horizontal" + j

    create_tag_image(tags, imagefilename,  size=imagefile_size, background=background_color, fontname='NotoSansCJKkr-Bold')
    create_tag_image(tags, vertical_image,  size=imagefile_size, background=background_color, fontname='NotoSansCJKkr-Bold', layout=LAYOUT_VERTICAL)
    create_tag_image(tags, horizontal_image,  size=imagefile_size, background=background_color, fontname='NotoSansCJKkr-Bold', layout=LAYOUT_HORIZONTAL)


if __name__ == "__main__":
    a = """
도널드 트럼프 대통령의 핵심 측근인 니키 헤일리 유엔주재 미국 대사가 2018년 평창 동계 올림픽에 미국 선수단을 파견하는 데 대해 “고민해야 할 문제(open question)”라며 유보적인 입장을 보였다. 북한의 위협에 날로 고조되고 있다는 이유에서다.
헤일리 대사는 6일(현지시간) 미국 폭스뉴스 인터뷰에서 ‘미국 선수들의 평창올림픽 참가가 기정사실이냐’는 질문에 “아직 그것(올림픽 참가)에 대해 들은 게 없지만, 관건은 어떻게 우리가 미국인들을 보호하느냐는 것이다. 이와 관련된 논의가 매일 이뤄지고 있다”며 이 같이 밝혔다.
헤일리 대사는 “그때 북한의 상황이 어떤지에 따라 달라질 것이다. 북한의 상황이 하루가 다르게 변하고 있다”며 “(미국 정부가 미국 선수 보호를 위해) 최선의 방법을 찾을 것”이라고 말했다. 그는 또 ‘선수단 가족이 함께 가는 것도 안전할 것이라고 생각하느냐’는 질문에는 “상황이 어떻게 진행되느냐에 달려 있다고 본다. 우리는 북한 상황을 매일 점검하고 있다”고 답했다.
그러면서도 헤일리 대사는 “우리는 아무것도 두렵지 않다. 우리는 우리의 삶을 산다”며 “선수들에게는 올림픽에 참석해 그동안 노력해 온 것들을 펼칠 수 있는 완벽한 기회며, 우리는 선수단의 안전을 사전에 확인하기 위해 모든 조치를 다 할 것”이라고 말하기도 했다.
미 정부 고위 인사가 평창 올림픽 선수단 파견 문제에 대해 발언한 것은 이번이 처음으로 전해졌다. 비록 헤일리 대사의 발언은 원론적 성격이 강하지만, 한반도 긴장 고조 여부에 따라 상황 변화가 생길 가능성을 언급한 것인 만큼 논란이 될 것으로 보인다.
일단 미국올림픽위원회(USOC)는 지난 9월 “미국 선수들은 올림픽에 참가할 것이다. 안전과 안보 준비를 확신한다”을 입장을 밝힌 상태다.
"""
    data = a.split()
    make_pytagcloud_image(data, "test_pycloud.png", most_top_number=20)