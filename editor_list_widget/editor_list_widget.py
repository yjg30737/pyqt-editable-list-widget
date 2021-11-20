from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt


class EditorListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.__persistent_editor_activated_flag = False

    def addItem(self, item):
        super().addItem(item)
        self.setCurrentItem(item)
        self.openPersistentEditor(item)
        self.setFocus()
        self.__persistent_editor_activated_flag = True

    def mousePressEvent(self, e):
        if self.__persistent_editor_activated_flag:
            self.closeIfPersistentEditorStillOpen()
        return super().mousePressEvent(e)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.closeIfPersistentEditorStillOpen()
        return super().keyPressEvent(e)

    def closeIfPersistentEditorStillOpen(self):
        item = self.currentItem()
        if item:
            if self.isPersistentEditorOpen(item):
                self.closePersistentEditor(item)
                self.__persistent_editor_activated_flag = False


