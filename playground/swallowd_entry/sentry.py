
import elementary
import edje
import evas

def destroy(obj, event, data):
    print "DEBUG: window destroy callback called!"
    print "DEBUG: data:"
    print data
    elementary.exit()

elementary.init()

win = elementary.Window("inject", elementary.ELM_WIN_BASIC)
win.destroy = (destroy, ("test", "test1"))

ly = elementary.Layout(win)
ly.file_set("people.edj", "CreateContact")
win.resize_object_add(ly)
ly.show()

scroller = elementary.Scroller(win)
scroller.size_hint_weight_set(1.0, 1.0)
scroller.size_hint_align_set(-1.0, -1.0)
scroller.bounce_set(0, 0)
scroller.show()



textbox = elementary.Entry(win)
textbox.single_line_set(True)
textbox.color_set(255, 255, 255, 255)
textbox.entry_set("lolza")

textbox.size_hint_weight_set(1.0, 1.0)
textbox.size_hint_align_set(-1.0, -1.0)

#textbox.size_hint_min_set(400,400)

scroller.content_set(textbox)
scroller.show()


ly.content_set('entry2', scroller)
win.resize(480, 640)
win.show()
elementary.run()

elementary.shutdown()

