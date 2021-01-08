# 클래스가 사용하지 않을 메소드에 의존할 것을 강요하면 안 된다.
# 뚱뚱한 클래스 = 약속을 어기기 쉽다

# 뚱뚱한 프린터
# from abc import ABC, abstractmethod
#
#
# class IPrinter(ABC):
#     @abstractmethod
#     def print_file(self, file: str) -> bool:
#         """문서 출력 메소드"""
#         pass
#
#     @abstractmethod
#     def scan(self, content: str) -> bool:
#         """문서 스캔 메소드"""
#         pass
#
#
# class SamsungPrinter(IPrinter):
#     def __init__(self, has_ink, has_paper, is_connected):
#         self.has_ink = has_ink
#         self.has_paper = has_paper
#         self.is_connected = is_connected
#
#     def print_file(self, file):
#         """문서 출력 메소드"""
#         if self.has_ink and self.has_paper and self.is_connected:
#             print("문서 {}을/를 출력 중입니다!".format(file))
#             return True
#         return False
#
#     def scan(self, content):
#         """문서 스캔 메소드"""
#         if self.is_connected:
#             print("{}을/를 이미지 파일로 저장합니다.".format(content))
#             return True
#         return False
#
#
# class LGPrinter(IPrinter):
#     def __init__(self, has_ink, has_paper, is_connected):
#         self.has_ink = has_ink
#         self.has_paper = has_paper
#         self.is_connected = is_connected
#
#     def print_file(self, file):
#         """문서 출력 메소드"""
#         if self.has_ink and self.has_paper and self.is_connected:
#             print("문서 {}을/를 출력합니다.".format(file))
#             return True
#         return False
#
#     def scan(self, content):
#         """LG 프린터는 스캔 기능이 없기 때문에 False 리턴"""
#         print("이 프린터는 문서를 스캔하는 기능이 없습니다.")
#         return False
#
#
# samsung_printer = SamsungPrinter(True, True, True)
# lg_printer = LGPrinter(True, True, True)
#
# samsung_printer.print_file("4월 보고서.docx")
# lg_printer.print_file("4월 보고서.docx")
#
# samsung_printer.scan("스캔 테스트 문서")
# lg_printer.scan("스캔 테스트 문서")
#
# print(SamsungPrinter.mro())
# print(LGPrinter.mro())


from abc import ABC, abstractmethod
# 프린터 인터페이스
class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass

# 스캐너 인터페이스
class IScanner(ABC):
    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass

class SamsungPrinter(IPrinter, IScanner):

    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False

class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False

# 테스트
samsung_printer = SamsungPrinter(True, True, True)
lg_printer = LGPrinter(True, True, True)

samsung_printer.print_file("4월 보고서.docx")
lg_printer.print_file("4월 보고서.docx")

samsung_printer.scan("스캔 테스트 문서")
#lg_printer.scan("스캔 테스트 문서")

print(SamsungPrinter.mro())
print(LGPrinter.mro())
