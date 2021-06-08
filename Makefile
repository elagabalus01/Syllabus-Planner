run: build
	python -B main.py
tkinter:
	python -B tkinter_ui.py

build: ./views/qt_view.py ./views/widgets/ui_tab_temario.py ./views/widgets/ui_sutema_edit_dialog.py ./views/widgets/ui_calendarizador_dialog.py

rebuild: build run

./views/qt_view.py: ./qt_view/new_view.ui
	pyuic5 ./qt_view/new_view.ui -o ./views/qt_view/ui_MainWindow.py

./views/widgets/ui_tab_temario.py: ./qt_view/tab_temario.ui
	pyuic5 ./qt_view/tab_temario.ui -o ./views/widgets/ui_tab_temario.py

./views/widgets/ui_sutema_edit_dialog.py: ./qt_view/subtema_dialog.ui
	pyuic5 ./qt_view/subtema_dialog.ui -o ./views/widgets/ui_sutema_edit_dialog.py

./views/widgets/ui_calendarizador_dialog.py: ./qt_view/calendarizador_dialog.ui
	pyuic5 ./qt_view/calendarizador_dialog.ui -o ./views/widgets/ui_calendarizador_dialog.py
