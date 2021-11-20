from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt


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



