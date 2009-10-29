
import elementary
import edje
import evas
import ecore



scroller1 = None
scroller2 = None
flipflop = False

def destroy(obj, event, data):
    print "DEBUG: window destroy callback called!"
    print "DEBUG: data:"
    print data
    elementary.exit()
    return

def _auto_hide():
    """Fill with the initial tutorial the textbox. It takes 30ms (on laptop)
       at the first time. So better to workaround a little"""
    global scroller2
    scroller2.hide()
    return

def textbox_mouse_down(entry, event):
    global flipflop
    global scroller1
    global scroller2
    if flipflop:
        print "textbox1 shown"
        scroller1.show()
        scroller2.hide()
        flipflop = False
    else:
        print "textbox1 hided"
        scroller1.hide()
        scroller2.show()
        flipflop = True
        
def __init__():
    elementary.init()

    win = elementary.Window("c_c", elementary.ELM_WIN_BASIC)
    win.title_set("gift to c_c")
    win.destroy = (destroy, ("test", "test1"))
    
    ly = elementary.Layout(win)
    ly.file_set("gui.edj", "Intone")
    win.resize_object_add(ly)
    ly.show()
    
    global scroller1
    scroller1 = elementary.Scroller(win)
    scroller1.size_hint_weight_set(1.0, 1.0)
    scroller1.size_hint_align_set(-1.0, -1.0)
    scroller1.bounce_set(0, 0)
    scroller1.show()
    
    textbox1 = elementary.Entry(win)
    textbox1.single_line_set(True)
    textbox1.entry_set("Textbox 1")
    
    textbox1.size_hint_weight_set(1.0, 1.0)
    textbox1.size_hint_align_set(-1.0, -1.0)
    textbox1.scale_set(1.8)
    textbox1.show()
    textbox1.on_mouse_down_add(textbox_mouse_down)

    
    scroller1.content_set(textbox1)
    scroller1.show()
    
    global scroller2
    scroller2 = elementary.Scroller(win)
    scroller2.size_hint_weight_set(1.0, 1.0)
    scroller2.size_hint_align_set(-1.0, -1.0)
    scroller2.bounce_set(0, 0)
    scroller2.show()
    
    textbox2 = elementary.Entry(win)
    textbox2.entry_set("Textbox2")
    
    textbox2.scale_set(3)
    textbox2.size_hint_weight_set(1.0, 1.0)
    textbox2.size_hint_align_set(-1.0, -1.0)
    
    textbox2.show()
    textbox2.on_mouse_down_add(textbox_mouse_down)
    
    scroller2.content_set(textbox2)
        
    ly.content_set('vbox1_swallow', scroller1)
    ly.content_set('vbox1b_swallow', scroller2)    
    
    win.resize(480, 640-64) # without illume keyboard
    win.show()


    ecore.idler_add(_auto_hide)
    return
    

__init__()
elementary.run()
