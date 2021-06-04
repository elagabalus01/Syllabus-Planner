run: build
	python -B main.py

build: ./views/qt_view.py ./views/widgets/ui_tab_temario.py

rebuild: build run

./views/qt_view.py: ./qt_view/new_view.ui
	pyuic5 ./qt_view/new_view.ui -o ./views/qt_view.py

./views/widgets/ui_tab_temario.py: ./qt_view/tab_temario.ui
	pyuic5 ./qt_view/tab_temario.ui -o ./views/widgets/ui_tab_temario.py
