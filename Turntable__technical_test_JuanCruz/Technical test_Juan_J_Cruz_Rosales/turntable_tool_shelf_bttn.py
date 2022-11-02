
# do not use reload in a production invirnment
import turntable_gui 
reload(turntable_gui)


from turntable_gui import TurntableView

TurntableView.show_turntable()