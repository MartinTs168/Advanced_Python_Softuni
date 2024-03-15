from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class MyMl(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):
    def format(self):
        return '\n'.join(['<HTML>', self.text, '</HTML>'])


class IProtocol(ABC):
    def __init__(self, protocol):
        self.protocol = protocol

    @abstractmethod
    def format(self, data):
        ...


class IMProtocol(IProtocol):
    def format(self, data):
        return ''.join(["I'm ", data])


class Email(IEmail):

    def __init__(self, protocol: IProtocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = self.protocol.format(sender)

    def set_receiver(self, receiver):
        self.__receiver = self.protocol.format(receiver)

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


protocol = IMProtocol('IM')
email = Email(protocol)
email.set_sender('qmal')
email.set_receiver('james')
content = HTML('Hello, there!')
email.set_content(content)
print(email)
