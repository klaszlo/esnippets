
import elementary
elementary.init()
import edje
import evas
win = elementary.Window("inject", elementary.ELM_WIN_BASIC)
win.autodel_set(True)
ly = elementary.Layout(win)
ly.file_set("people.edj", "CreateContact")
win.resize_object_add(ly)
ly.show()
textbox = elementary.Entry(win)
textbox.single_line_set(True)
textbox.color_set(255, 255, 255, 255)
textbox.entry_set("lolza")
textbox.size_hint_weight_set(1.0, 1.0)
ly.content_set('entry2', textbox)
win.resize(480, 640)
win.show()
elementary.run()

