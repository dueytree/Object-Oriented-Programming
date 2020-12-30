# class User:
#     count = 0
#
#     def __init__(self, name, email, pw):
#         self.name = name
#         self.email = email
#         self.pw = pw
#         User.count += 1
#
#     def say_hello(self):
#         print("안녕하세요 저는 {}입니다!".format(self.name))
#
#     def __str__(self):
#         return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
#
#     @classmethod
#     def number_of_users(cls):
#         print("총 유저 수는: {}입니다".format(cls.count))
#
# user1 = User("강영훈", "younghoon@codeit.kr", "123456")
# user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4r")
# user3 = User("서혜린", "lisa@codeit.kr", "abc123")
#
# User.number_of_users()
# user1.number_of_users()


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        params_list = string_params.split(",")
        name = params_list[0]
        email = params_list[1]
        password = params_list[2]
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)