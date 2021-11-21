from PyQt5.QtWidgets import QListWidget, QListWidgetItem
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

    def mouseDoubleClickEvent(self, e): # Let user edit the item when double clicking certain item
        item = self.itemAt(e.pos())
        self.openPersistentEditor(item)
        self.__persistent_editor_activated_flag = True
        return super().mouseDoubleClickEvent(e)

    def keyPressEvent(self, e): # make editor closed when user pressed enter
        if e.key() == Qt.Key_Return or e.key() == 16777235 or e.key() == 16777237:
            self.closeIfPersistentEditorStillOpen()
            # return --> If you insert this then it won't make you consecutively add the next item.
        elif e.key() == Qt.Key_F2: # Let user edit the item when pressing F2
            item = self.currentItem()
            if item:
                self.openPersistentEditor(item)
                self.__persistent_editor_activated_flag = True
        return super().keyPressEvent(e)

    def closeIfPersistentEditorStillOpen(self): # Check if user are editing item
        item = self.currentItem()
        if item:
            if self.isPersistentEditorOpen(item):
                self.closePersistentEditor(item)
                self.__persistent_editor_activated_flag = False



