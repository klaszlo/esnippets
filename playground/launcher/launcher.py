import elementary
import edje
import evas

elementary.init()

win = elementary.Window("inject", elementary.ELM_WIN_BASIC)
win.title_set("inject")
win.autodel_set(True)

ly = elementary.Layout(win)
ly.file_set("launcher.edj", "main")
#ly.size_hint_weight_set(1.0, 1.0)
win.resize_object_add(ly)
ly.show()



box = elementary.Box(win)
#box.size_hint_weight_set(-1.0, -1.0)
box.show()

link1 = elementary.Layout(win)
link1.file_set("launcher.edj", 'link')
link1.size_hint_weight_set(-1.0, -1.0)
link1.size_hint_align_set(-1.0, 0.0)
link1_edje = link1.edje_get()
link1_edje.part_text_set("texter","this is the link1")
w,h = link1_edje.size_min_get()
link1.size_hint_min_set(-1,h+1)
link1.show()
box.pack_end(link1)

link2 = elementary.Layout(win)
link2.file_set("launcher.edj", 'link')
link2.size_hint_weight_set(-1.0, -1.0)
link2.size_hint_align_set(-1.0, 0.0)
link2_edje = link2.edje_get()
link2_edje.part_text_set("texter","this is the link2")
w,h = link2_edje.size_min_get()
link2.size_hint_min_set(-1,h+1)
link2.show()
box.pack_end(link2)

link3 = elementary.Layout(win)
link3.file_set("launcher.edj", 'link')
link3.size_hint_weight_set(-1.0, -1.0)
link3.size_hint_align_set(-1.0, 0.0)
link3_edje = link3.edje_get()
link3_edje.part_text_set("texter","this is the link3")
w,h = link3_edje.size_min_get()
link3.size_hint_min_set(-1,h+1)
link3.show()
box.pack_end(link3)

link4 = elementary.Layout(win)
link4.file_set("launcher.edj", 'link')
link4.size_hint_weight_set(-1.0, 1.0)
link4.size_hint_align_set(-1.0, -1.0)
link4_edje = link4.edje_get()
link4_edje.part_text_set("texter","this is the link4")
w,h = link4_edje.size_min_get()
link4.size_hint_min_set(-1,h+1)
link4.show()
box.pack_end(link4)

ly.content_set('link-box', box)
win.resize(480, 640-64)
win.show()

elementary.run()
elementary.shutdown()
