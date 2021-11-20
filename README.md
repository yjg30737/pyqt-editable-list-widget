# editor-list-widget
Easily editable list widget

## General Info
When you are suppposed to add the item to editor-list-widget, editor-list-widget will automatically open the editor to let you edit right after that happened. If you press enter, you can conveniently add new item. Clicking something else that editor will be closed.

## Requirements
PyQt5 >= 5.8

## Setup
```
pip install git+https://github.com/yjg30737/editor-list-widget.git --upgrade
```

## Code

editor-list-widget module code
```python
class EditorListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.__persistent_editor_activated_flag = False

    def addItem(self, item):
        super().addItem(item)
        self.setCurrentItem(item)
        self.openPersistentEditor(item) # open the editor
        self.setFocus()
        self.__persistent_editor_activated_flag = True

    def mousePressEvent(self, e): # make editor closed when user clicked somewhere else
        if self.__persistent_editor_activated_flag:
            self.closeIfPersistentEditorStillOpen()
        return super().mousePressEvent(e)

    def keyPressEvent(self, e): # make editor closed when user pressed enter 
        if e.key() == Qt.Key_Return:
            self.closeIfPersistentEditorStillOpen()
            # return --> If you insert this then it won't make you consecutively add the next item. 
        return super().keyPressEvent(e)

    def closeIfPersistentEditorStillOpen(self): # Check if user are editing item 
        item = self.currentItem()
        if item:
            if self.isPersistentEditorOpen(item):
                self.closePersistentEditor(item)
                self.__persistent_editor_activated_flag = False
```

## Usage in your module

```python
# ADD ITEM TO LIST
def __add(self):
    self.__textListWidget.closeIfPersistentEditorStillOpen() # You have to call this.
    item = QListWidgetItem('abc')
    self.__textListWidget.addItem(item)
    self.__btn_toggled()

# DELETE ITEM FROM LIST
def __delete(self):
    item = self.__textListWidget.currentItem()
    if item:
        self.__textListWidget.takeItem(self.__textListWidget.currentRow())
        self.__btn_toggled()
```
