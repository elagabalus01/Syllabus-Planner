run:
	python -B main.py

build: ./views/qt_view.py

rebuild: build run

./views/qt_view.py: ./qt_view/new_view.ui
	pyuic5 ./qt_view/new_view.ui -o ./views/qt_view.py
