#import 'pythonista'

# see https://medium.com/swiftly-swift/how-to-build-a-compass-app-in-swift-2b6647ae25e8

import motion
import math
import ui

class Mag(ui.View):
	def __init__(self,wv,name='my_mag', frame=(0,0,350,200), background_color= 'white'):
		self.name=name
		self.frame=frame
		self.wv=wv
		self.update_interval=.5
		self.background_color=background_color
		
		motion.start_updates()
		
		ih=10
		
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,200,30)
		lab.text='Magnetic Field:'
		self.add_subview(lab)
		
		self.mf=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.mf.frame=(210,ih,400,30)
		self.mf.text=''
		self.add_subview(self.mf)
		ih+=40

		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,200,30)
		lab.text='Acceleration:'
		self.add_subview(lab)
		
		self.acc=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.acc.frame=(210,ih,400,30)
		self.acc.text=''
		self.add_subview(self.acc)	
		ih+=40
								
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,200,30)
		lab.text='Gravity:'
		self.add_subview(lab)
				
		self.grav=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.grav.frame=(210,ih,400,30)
		self.grav.text=''
		self.add_subview(self.grav)
		ih+=40
		
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,200,30)
		lab.text='Orientation:'
		self.add_subview(lab)
		
		self.ori=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.ori.frame=(210,ih,400,30)
		self.ori.text=''
		self.add_subview(self.ori)	
		ih+=40	
						
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,200,30)
		lab.text='Attitude:'
		self.add_subview(lab)
		
		self.att=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.att.frame=(210,ih,400,30)
		self.att.text=''
		self.add_subview(self.att)	
		ih+=40
		
		lab=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		lab.frame=(10,ih,200,30)
		lab.text='Angle:'
		self.add_subview(lab)
		
		self.ang=ui.Label(alignment=ui.ALIGN_LEFT, font=('<system>',25))
		self.ang.frame=(210,ih,400,30)
		self.ang.text=''
		self.add_subview(self.ang)	
		ih+=40		
																				
	def update(self):
		m = motion.get_magnetic_field()
		self.mf.text='{:.1f} {:.1f} {:.1f} {:.3f}'.format(m[0],m[1],m[2],m[3])
		
		acc=motion.get_user_acceleration()
		self.acc.text='{:.3f} {:.3f} {:.3f}'.format(acc[0],acc[1],acc[2])
				
		grav = motion.get_gravity()
		self.grav.text='{:.3f} {:.3f} {:.3f}'.format(grav[0],grav[1],grav[2])
		
		#determine screen orientation. Portrait modes flip 180 deg if the device is face down. Use local z gravity to detect.
		
		orient=int(self.wv.eval_js('window.orientation'))
		
		if (orient==0):
			#portrait, home button on bottom
			if grav[2] <= 0.:
				init_angle=-90
			else:
				init_angle=90
				
		elif (orient==90):
			#landscape, home button on right
			init_angle=0
			
		elif (orient==-90):
			#landscape, home button on right
			init_angle=180
			
		else:
			#portrait, home button on top
			if grav[2] <= 0.:
				init_angle=90
			else:
				init_angle=-90
				
		self.ori.text=str(orient)

		att=motion.get_attitude()
		self.att.text='{:.3f} {:.3f} {:.3f}'.format(att[0],att[1],att[2])	

		
		ang=(init_angle-int(math.degrees(att[2]))) % 360
		self.ang.text=str(ang)

if __name__ == '__main__':			

	#use webview to find device orientation	
	wv=ui.WebView()
	wv.hidden=True
	wv.present('fullscreen',hide_close_button=False)

	my_mag=Mag(wv,frame=(0,0,400,400))
	
	my_mag.present('fullscreen', hide_close_button=False)
	my_mag.wait_modal()
	motion.stop_updates()
	
