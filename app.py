#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{{ scaffold.name | capitalize }} Service
"""
import stackhut
import re
from docx import Document

class DefaultService:
    def __init__(self):
        pass

    def replaceText(self, documentUrl, textToReplace, replacementText):
        in_file = stackhut.download_file(documentUrl)
        out_file = "out_{}".format(in_file)

        document = Document(in_file)
        searchre = re.compile(textToReplace)

        for paragraph in document.paragraphs:
            paragraph_text = paragraph.text
            if paragraph_text:
                if searchre.search(paragraph_text):
                    paragraph.text = re.sub(textToReplace, replacementText, paragraph_text)

        document.save(out_file)
        return stackhut.put_file(out_file)


# export the services
SERVICES = {"Default": DefaultService()}
