# Practical No. 4
# Real-time Undo/Redo System using Stack
# --------------------------------------
# Operations:
# 1. Make a Change
# 2. Undo Action
# 3. Redo Action
# 4. Display Document State
# --------------------------------------

class TextEditor:
    def __init__(self):
        self.undo_stack = []   # Stack for undo actions
        self.redo_stack = []   # Stack for redo actions
        self.document = ""     # Current document state

    # 1. Make a Change
    def make_change(self, new_text):
        # Save current state in undo stack
        self.undo_stack.append(self.document)

        # Clear redo stack (new changes overwrite redo history)
        self.redo_stack.clear()

        # Apply change
        self.document = new_text
        print(f"Change made: {self.document}")

    # 2. Undo Action
    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        # Move current state to redo stack
        self.redo_stack.append(self.document)
        # Restore last state from undo stack
        self.document = self.undo_stack.pop()
        print(f"Undo performed. Current document: {self.document}")

    # 3. Redo Action
    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        # Save current state in undo stack
        self.undo_stack.append(self.document)
        # Restore state from redo stack
        self.document = self.redo_stack.pop()
        print(f"Redo performed. Current document: {self.document}")

    # 4. Display Document State
    def display(self):
        print(f"Current Document: {self.document}")


# Example Usage
if __name__ == "__main__":
    editor = TextEditor()

    editor.make_change("Hello")
    editor.make_change("Hello, World")
    editor.make_change("Hello, World!!!")

    editor.undo()
    editor.undo()

    editor.redo()

    editor.display()
