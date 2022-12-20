if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    from gui.MainWindow import MainWindow

    app = QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()
