#!/usr/bin/env python3
#encoding=UTF-8
#  
#  Copyright 2014 MopperWhite <mopperwhite@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from PyQt5.Qt import QApplication,QWidget,QObject,QTimer,QCursor
from collections import OrderedDict
import time

class TestWindow(QWidget):
        def __init__(self,parent=None):
                super(QWidget,self).__init__(parent)
                self.poslabel=QLabel(self)
                self.resize(300,100)
                self.poslabel.move(0,0)
                self.poslabel.resize(300,100)
        def mouseMoveEvent(self,event):
                self.poslabel.setText(unicode(event.globalPos())+unicode(event.pos()))
                
class Sampler(QObject):
        '''
        Directions:
                789
                456
                123
        '''
        DIRECTIONS=dict([
        (7,"LeftTop"),             (8,"Top"),              (9,"RightTop"),
        (4,"Left"),                   (5,"Center"),         (6,"Right"),
        (1,"LeftBottom"),       (2,"Bottom"),         (3,"RightBottom"),
        ])
        DIRECTION_DICT={
        #(if x>0, if y>0 , if abs(x)>=abs(y))
        (1,1,1):,
        ():,
        ():,
        ():,
        ():,
        ():,
        ():,
        ():,
        }
        def __init__(self,sampling_time,parent=None):
                super(QObject,self).__init__()
                self.sampling_time=sampling_time
                self.timer=QTimer()
                self.timer.connect(SIGNAL("timeout()"),self.sample
                self.mouse_positions=OrderedDict()
                self.moving_directions=OrderedDict()
        @classmethod
        def direction_to_mark(self,direction):
                return 
                
        def sample(self):
                time_=time.time()
                self.mousepos_list.append(QCursor.pos())
        def sample_pos(self,time_):
                self.mouse_positions[time_]=QCursor.pos()
        def sample_direction(self,time_):
                if len(self.mouse_positions)>1:
                        self.mouse_positions[time_]=QCursor.pos()

def qpoint_to_complex(qpoint):
        return complex(qpoint.x(),qpoint.y())
def complex_to_qpoint(complex_)
        return QPoint(complex_.real,complex_.imag)

app=QApplication([])
window=Sampler(1)
window.show()
app.exec_()
