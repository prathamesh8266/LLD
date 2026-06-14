"""
Design google docs
- Google docs is a texte edditing and colloboration platform, the main functionality is text editing so lets focus on document editor part of it

what should a document editor have?
- elements (what elements are to be supported?) text and img for now
- should be able to save to file
- display the elements

Questions to discuss:
can we assume that text and img both will be string? 
- yes , we can pass the path to image as a string
"""

# Vague design
class DocmentEditor:

    elements: list[str] 
    def renderElement(self):
        ...
    def addText(self):
        ...
    def addImage(self):
        ...
        

"""
The above design breaks SRP, OCP and there is not (LSP, ISP, DIP), lets try to clean it up
"""

from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def render(self):
        ...

class TextElement(Element):

    def __init__(self, body):
        self.body = body

    def render(self):
        print(f'{self.body}\n')


class ImageElement(Element):

    def __init__(self, path):
        self.path = path

    def render(self):
         print(f'{self.path}\n')

class Document:

    def __init__(self, elements: list[Element]):
        self.elements = elements

    def addElement(self, element: Element):
        self.elements.append(element)

    def getElements(self):
        return self.elements


class Persistance(ABC):

    @abstractmethod
    def save(self, document: Document):
        ...

class SaveToFile(Persistance):

    def __init__(self, document: Document):
        self.document = document

    def save(self):
        body = self.document.getElements()
        print("Saving to file...")


class DocumentEditor:

    def __init__(self,document: Document, persistance: Persistance):
        self.document = document
        self.persistance = persistance

    def render(self):
        for elements in self.document.getElements():
            elements.render()

    def save(self):
        self.persistance.save()


# element1: Element = TextElement("Hello world ......")
# element2: Element = ImageElement("c:/user/prathamesh/main/img.png")
# element3: Element = TextElement("This workd")
# element4: Element = TextElement("Thank you")


# documents: Document = Document([element1,element2,element3,element4])
# documents.addElement(TextElement("Testing..."))
# persistance: Persistance = SaveToFile(documents)

# editor: DocumentEditor = DocumentEditor(documents, persistance)


# editor.render()
# editor.save()

r"""
                                         _________________________
                                        |     DocumentEditor      |
                                        |-------------------------|
                                        | document: Document      |
                                        | persistance: Persistance|
                                        |-------------------------|
                                        | render()                |
                                        | save()                  |
                                        |_________________________|
                                            o              o
                                            | 1            | 1
                    -------------------------              -------------------------
                    |                                                              |
            _____________________                                          _________________________
            |      Document       |<---------------------------------------|      <<abstract>>       |
            |---------------------|                                        |       Persistance       |
            | elements: list      |                                        |-------------------------|
            |---------------------|                                        |                         |
            | getElements()       |                                        |-------------------------|
            | addElement()        |                                        |                         |
            |_____________________|                                        | save(document: Document)|
                o          1                                               |_________________________|
                |          ^                                                        /_\
                |        * |                                                         |
                |          ---------------------------------------------------------o|
            _____________________                                         _________________________
            |    <<abstract>>     |                                       |       SaveToFile        |
            |       Element       |                                       |-------------------------|
            |---------------------|                                       | document: Document      |
            |                     |                                       |-------------------------|
            |---------------------|                                       | save()                  |
            | render()            |                                       |_________________________|
            |_____________________|
                          /_\
                           |
                       -------------------
                       |                 |
            _________________   _________________
            |   TextElement   | |  ImageElement   |
            |-----------------| |-----------------|
            | body            | | path            |
            |-----------------| |-----------------|
            | render()        | | render()        |
            |_________________| |_________________|`
"""

## more clean implementation, as we see there are lots of reasons for DocumentEditor to change (in case if render() changes to renderDoc() it will need to change in the DocumentEditor class

class Element(ABC):

    @abstractmethod
    def render(self):
        ...

class TextElement(Element):

    def __init__(self, body):
        self.body = body

    def render(self):
        print(f'{self.body}\n')


class ImageElement(Element):

    def __init__(self, path):
        self.path = path

    def render(self):
         print(f'{self.path}\n')

class Document:

    def __init__(self, elements: list[Element]):
        self.elements = elements

    def addElement(self, element: Element):
        self.elements.append(element)

    def getElements(self):
        return self.elements


class Persistance(ABC):

    @abstractmethod
    def save(self, document: Document):
        ...

class SaveToFile(Persistance):

    def __init__(self, document: Document):
        self.document = document

    def save(self):
        body = self.document.getElements()
        print("Saving to file...")


class DocumentEditor:

    def __init__(self,document: Document):
        self.document = document

    def addElement(self, element: Element):
        self.document.addElement(element)


class DocumentRenderer:

    def __init__(self, document: Document):
        self.document = document
    
    def render(self):
        for elements in self.document.getElements():
            elements.render()


element1: Element = TextElement("Hello world ......")
element2: Element = ImageElement("c:/user/prathamesh/main/img.png")
element3: Element = TextElement("This workd")
element4: Element = TextElement("Thank you")

documents: Document = Document([])
persistance: Persistance = SaveToFile(documents)

editor: DocumentEditor = DocumentEditor(documents)
editor.addElement(element1)
editor.addElement(element2)
editor.addElement(element3)
editor.addElement(element4)

documentRenderer: DocumentRenderer = DocumentRenderer(documents)


documentRenderer.render()
persistance.save()