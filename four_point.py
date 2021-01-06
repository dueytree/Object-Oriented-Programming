## 추상화

# Google_docstring:
"""유저에게 추천할 영상을 찾아준다
Parameters:
  number_of_suggestions (int): 추천하고 싶은 영상 수
    (기본값은 5)

Returns:
  list: 추천할 영상 주소가 담긴 리스트
"""

# reStructuredText(파이썬 공식 문서화 기준):
"""유저에게 추천할 영상을 찾아준다

:param number_of_suggestions: 추천하고 싶은 영상 수
  (기본값은 5)
:type number_of_suggestions: int
:returns: 추천할 영상 주소가 담긴 리스트
:rtype: list
"""
# NumPy / SciPy(통계, 과학분야에서 쓰이는 Python 라이브러리):
"""유저에게 추천할 영상을 찾아준다

Parameters
----------
number_of_suggestions: int
  추천하고 싶은 영상 수 (기본값은 5)

Returns
-------
list 
  추천할 영상 주소가 담긴 리스트
"""

## 캡슐화
# 캡슐화를 하기 위해 변수나 메소드를 숨기기
# _(언더바) = 변수/메소드는 클래스 외부에서 직접 접근하지 말라는 약속
class Citizen:
    """주민 클래스"""
    drinking_age = 19  # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self.__resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self.__age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다")
            self.__age = 0
        else:
            self.__age = value

