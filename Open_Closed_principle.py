# 클래스는 확장에 열려있어야 하며, 수정에는 닫혀있어야 한다

from abc import ABC, abstractmethod

class Keyboard(ABC):
    """키보드 클래스"""
    @abstractmethod
    def save_input(self, content: str) -> None:
        """키보드 인풋 저장 메소드"""
        pass

    @abstractmethod
    def send_input(self) -> str:
        """키보드 인풋 전송 메소드"""
        pass

class AppleKeyboard(Keyboard):
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_input()

class SamsungKeyboard(Keyboard):
    """삼성 키보드 클래스"""
    def __init__(self):
        """키보드 인풋"""
        self.user_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input

keyboard_manager = KeyboardManager()

apple_keyboard = AppleKeyboard()
samsung_keyboard = SamsungKeyboard()

keyboard_manager.connect_to_keyboard(samsung_keyboard)
samsung_keyboard.save_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())

keyboard_manager.connect_to_keyboard(apple_keyboard)
apple_keyboard.save_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())

# message_manager
from abc import ABC, abstractmethod

class MessageNotificationManager:
    """메시지 알림 관리 클래스"""

    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.get_message() + "\n")

class Message(ABC):

    @abstractmethod
    def get_message(self):
        pass

class KakaoTalkMessage:
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(
            self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[
                                                                                :KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str

class FacebookMessage:
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def get_message(self):
        """메시지를 짧은 형태로 리턴함"""
        res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[
                                                                                                          :FacebookMessage.notification_message_max_len] + "..."

        return res_str

class TextMessage:
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_message(self):
        """메시지의 정보와 내용을 리턴함"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[
                                                                                                          :TextMessage.notification_message_max_len] + "..."
        return noti_string


# 메시지 알림 관리 인스턴스 생성
message_notification_manager = MessageNotificationManager()

# 서로 다른 종류의 메시지 3개 생성
kakao_talk_message = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같아, 미안!")
facebook_message = FacebookMessage("고대위", "서울시 성북구", "2019년 7월 1일 오후 11시 35분", "아니다, 갈게! 너네 어디서 놀고 있어?")
text_message = TextMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게, 나 지금 출발")

# 메시지 알림 관리 인스턴스에 3개의 메시지를 추가
message_notification_manager.add_new_message(kakao_talk_message)
message_notification_manager.add_new_message(facebook_message)
message_notification_manager.add_new_message(text_message)

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
message_notification_manager.display_message_notifications()