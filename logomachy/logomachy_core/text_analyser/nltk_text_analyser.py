from io import TextIOBase

from logomachy.logomachy_core.text_analyser.base_text_analyser import BaseTextAnalyser
from logomachy.logomachy_core.text_analyser.text_info import TextInfo


class NltkTextAnalyser(BaseTextAnalyser):
    def __init__(self):
        pass

    def get_text_info(self, text: str) -> TextInfo:
        pass

    def get_text_info_stream(self, text_stream: TextIOBase) -> TextInfo:
        pass
