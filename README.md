# editor-list-widget
Easily editable list widget

## General Info
When you are suppposed to add the item to editor-list-widget, editor-list-widget will automatically open the editor to let you edit right after that happened. If you press enter, you can conveniently add new item. Clicking something else that editor will be closed.

You can edit certain item to double click it or press F2 on the selected item.

## Requirements
PyQt5 >= 5.8

## Setup
```
pip install git+https://github.com/yjg30737/editor-list-widget.git --upgrade
```

## Usage

Before add item, you have to write `closeIfPersistentEditorStillOpen()`.

## Example

![editorListWidgetExample](./example/editorListWidgetExample.png)
