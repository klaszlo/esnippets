import elementary
import edje
import evas

elementary.init()

win = elementary.Window("List with scroller", elementary.ELM_WIN_BASIC)
win.title_set("Scroller list")
win.autodel_set(True)

ly = elementary.Layout(win)
ly.file_set("inout.edj", "main")
#ly.size_hint_weight_set(1.0, 1.0)
ly.show()

scroller = elementary.Scroller(win)
scroller.size_hint_weight_set(1.0, 1.0)
scroller.size_hint_align_set(-1.0, -1.0)
scroller.bounce_set(0, 0)
scroller.show()

ly.content_set("list", scroller)

win.resize_object_add(ly)

box = elementary.Box(win)
box.size_hint_weight_set(1.0, 0.0)
box.size_hint_align_set(-1.0, -1.0)

for i in range(1,10):
    ly2 = elementary.Layout(win)
    ly2.file_set("inout.edj", "item")
    ly2_edj = ly2.edje_get()
    
    ly2_edj.part_text_set("label","hmmz")
    ly2_edj.part_text_set("subtext","hmmz__")
        
    ly2.size_hint_min_set(70,96)#
    ly2.size_hint_weight_set(1.0, 0.0)
    ly2.size_hint_align_set(-1.0, -1.0)    
    box.pack_end(ly2)
    ly2.show()

scroller.content_set(box)
box.show()
scroller.show()

win.resize(480, 640-64)
win.show()

elementary.run()
elementary.shutdown()
