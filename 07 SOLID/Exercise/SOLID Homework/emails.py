from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        ...

    @abstractmethod
    def set_receiver(self, receiver):
        ...

    @abstractmethod
    def set_content(self, content):
        ...


class AbstractContent(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format_content(self):
        ...


class MyContent(AbstractContent):
    def format_content(self):
        return ' '.join(['<myML>', self.content, '</myML>'])


class HTML(AbstractContent):
    def format_content(self):
        return ' '.join(['<html>', self.content, '</html>'])


class Email(IEmail, MyContent):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format_content()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent: {content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)

print()
content2 = HTML("Hi!!!")
email.set_content(content2)
print(email)
