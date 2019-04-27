from objc_util import *

import ui
import math
import motion

class FaceDown(ui.View):
	def __init__(self,name='facedown', frame=(0,0,350,200), background_color= 'white'):
		self.name=name
		self.frame=frame
		self.update_interval=.5
		self.background_color=background_color
		
		ih=10
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,300,30)
		lab.text='UIDevice.orientation:'
		self.add_subview(lab)
		
		self.ori=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.ori.frame=(310,ih,400,30)
		self.ori.text=''
		self.add_subview(self.ori)	
		ih+=40	
		
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,300,30)
		lab.text='Roll,Pitch,Yaw:'
		self.add_subview(lab)
		
		self.att=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.att.frame=(310,ih,400,30)
		self.att.text=''
		self.add_subview(self.att)	
		ih+=40	
		
	def update(self):		

		UIDevice = ObjCClass('UIDevice').currentDevice()
		#print(UIDevice.orientation())
		# https://developer.apple.com/documentation/uikit/uideviceorientation?language=objc
		# 6 = UIDeviceOrientationFaceDown
		
		self.ori.text=str(UIDevice.orientation())
		
		att=motion.get_attitude()
		self.att.text='{:.3f} {:.3f} {:.3f}'.format(math.degrees(att[0]),math.degrees(att[1]),math.degrees(att[2]))

if __name__ == '__main__':			

	motion.start_updates()
	facedown=FaceDown(frame=(0,0,500,500))
	
	facedown.present('fullscreen', hide_close_button=False)	
	facedown.wait_modal()
	motion.stop_updates()

