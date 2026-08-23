"""
Abstract Factory Practice Question

Problem:
You are building a notification settings screen that should work on Android and
iOS.

Each platform has its own style of UI components. The screen needs:
- a toggle
- a dropdown
- a button

Goal:
Design this using the Abstract Factory pattern.

Constraint:
The client code that renders the settings screen should not directly create
Android or iOS classes.

Example output:

Rendering Android notification settings
Rendering Android toggle
Rendering Android dropdown
Rendering Android button

Rendering iOS notification settings
Rendering iOS toggle
Rendering iOS dropdown
Rendering iOS button
"""

from abc import ABC, abstractmethod

class Element(ABC):
    
    @abstractmethod
    def render(self):
        pass
    
class AndroidToggle(Element):
    
    def render(self):
        print(f"Rendering Android toggle")
        
class AndroidDropdown(Element):
    
    def render(self):
        print(f"Rendering Android dropdown")
        
class AndroidButton(Element):
    
    def render(self):
        print(f"Rendering Android button")
        
class IosToggle(Element):
    
    def render(self):
        print(f"Rendering Ios toggle")
        
class IosDropdown(Element):
    
    def render(self):
        print(f"Rendering Ios dropdown")
        
class IosButton(Element):
    
    def render(self):
        print(f"Rendering Ios button")
        
class UIFactory(ABC):
    
    @abstractmethod
    def get_toggle(self):
        ...
        
    @abstractmethod
    def get_dropdown(self):
        ...
        
    @abstractmethod
    def get_button(self):
        ...

class AndroidUIFactory(UIFactory):
    
    def __init__(self):
        print("Rendering Android notification settings")
    
    def get_toggle(self):
        return AndroidToggle()
            
    def get_dropdown(self):
        return AndroidDropdown()
        
    def get_button(self):
        return AndroidButton()
        

class IosUIFactory(UIFactory):

    def __init__(self):
        print("Rendering iOS notification settings")
           
    def get_toggle(self):
        return IosToggle()
            
    def get_dropdown(self):
        return IosDropdown()
        
    def get_button(self):
        return IosButton()
        

android = AndroidUIFactory()
android.get_button().render()
android.get_dropdown().render()
android.get_toggle().render()