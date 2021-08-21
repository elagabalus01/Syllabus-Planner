src=./src
views_path=./src/views
ui_src_path=./ui_src

run: build
	python -B $(src)/main.py

prueba:
	python -B $(src)/debug.py

tkinter:
	python -B $(src)/tkinter_ui.py

$widgets=$(views_path)/qt_view.py \
$(views_path)/widgets/ui_tab_temario.py\
$(views_path)/widgets/ui_sutema_edit_dialog.py\
$(views_path)/widgets/ui_calendarizador_dialog.py

build: $(widgets)

rebuild: build run

$(views_path)/qt_view.py: $(ui_src_path)/new_view.ui
	pyuic5 $< -o $@

$(views_path)/widgets/ui_tab_temario.py: $(ui_src_path)/tab_temario.ui
	pyuic5 $< -o $@

$(views_path)/widgets/ui_sutema_edit_dialog.py: $(ui_src_path)/subtema_dialog.ui
	pyuic5 pyuic5 $< -o $@

$(views_path)/widgets/ui_calendarizador_dialog.py: $(ui_src_path)/calendarizador_dialog.ui
	pyuic5 $< -o $@
