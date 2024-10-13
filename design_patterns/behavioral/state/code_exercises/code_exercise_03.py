from abc import ABC, abstractmethod
from collections import deque

class TextEditorState(ABC):
    @abstractmethod
    def apply_formatting(self, text):
        pass

    @abstractmethod
    def apply_default(self, text_editor):
        pass

    @abstractmethod
    def apply_bold(self, text_editor):
        pass

    @abstractmethod
    def apply_italic(self, text_editor):
        pass    

    @abstractmethod
    def apply_underline(self, text_editor):
        pass

class DefaultState(TextEditorState):
    def apply_formatting(self, text):
        return text

    def apply_default(self, text_editor):
        print("Default formatting already applied.")

    def apply_bold(self, text_editor):
        print("Applying bold formatting...")
        text_editor.change_state(BoldState())

    def apply_italic(self, text_editor):
        print("Applying italic formatting...")
        text_editor.change_state(ItalicState())

    def apply_underline(self, text_editor):
        print("Applying underline formatting...")
        text_editor.change_state(UnderlineState())

class BoldState(TextEditorState):
    def apply_formatting(self, text):
        return f"**{text}**"

    def apply_default(self, text_editor):
        print("Removing bold formatting...")
        text_editor.change_state(DefaultState())

    def apply_bold(self, text_editor):
        print("Bold formatting already applied.")

    def apply_italic(self, text_editor):
        print("Changing from bold to italic...")
        text_editor.change_state(ItalicState())

    def apply_underline(self, text_editor):
        print("Changing from bold to underline...")
        text_editor.change_state(UnderlineState())

class ItalicState(TextEditorState):
    def apply_formatting(self, text):
        return f"*{text}*"

    def apply_default(self, text_editor):
        print("Removing italic formatting...")
        text_editor.change_state(DefaultState())

    def apply_bold(self, text_editor):
        print("Changing from italic to bold...")
        text_editor.change_state(BoldState())

    def apply_italic(self, text_editor):
        print("Italic formatting already applied.")

    def apply_underline(self, text_editor):
        print("Changing from italic to underline...")
        text_editor.change_state(UnderlineState())

class UnderlineState(TextEditorState):
    def apply_formatting(self, text):
        return f"__{text}__"

    def apply_default(self, text_editor):
        print("Removing underline formatting...")
        text_editor.change_state(DefaultState())

    def apply_bold(self, text_editor):
        print("Changing from underline to bold...")
        text_editor.change_state(BoldState())

    def apply_italic(self, text_editor):
        print("Changing from underline to italic...")
        text_editor.change_state(ItalicState())

    def apply_underline(self, text_editor):
        print("Underline formatting already applied.")

class TextEditor:
    def __init__(self):
        self.state = DefaultState()
        self.text = ""
        self.unformatted_text = ""
        self.formatting_history = deque()
        self.redo_stack = deque()

    def change_state(self, new_state):
        self.formatting_history.append(self.state)
        self.state = new_state
        self.redo_stack.clear()
        self.apply_current_formatting()

    def apply_current_formatting(self):
        self.text = self.state.apply_formatting(self.unformatted_text)

    def enter_text(self, input_text):
        print(f"Entering text: {input_text}")
        self.unformatted_text += input_text
        self.apply_current_formatting()

    def apply_default(self):
        self.state.apply_default(self)

    def apply_bold(self):
        self.state.apply_bold(self)

    def apply_italic(self):
        self.state.apply_italic(self)

    def apply_underline(self):
        self.state.apply_underline(self)

    def undo(self):
        if self.formatting_history:
            self.redo_stack.append(self.state)
            self.state = self.formatting_history.pop()
            self.apply_current_formatting()
            print("Undo successful.")
        else:
            print("No formatting changes to undo.")

    def redo(self):
        if self.redo_stack:
            self.formatting_history.append(self.state)
            self.state = self.redo_stack.pop()
            self.apply_current_formatting()
            print("Redo successful.")
        else:
            print("No formatting changes to redo.")

    def get_text(self):
        return self.text

def main():
    text_editor = TextEditor()
    text_editor.enter_text("Hello, world!")
    text_editor.apply_bold()
    text_editor.enter_text(" This is a test.")
    print(text_editor.get_text())
    text_editor.undo()
    print(text_editor.get_text())
    text_editor.redo()
    print(text_editor.get_text())

if __name__ == "__main__":
    main()
