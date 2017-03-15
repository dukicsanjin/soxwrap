import Tkinter
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os






def tremolo():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "tremolo " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 tremolo ' + str(var.get()) + " " + str(vara.get()))
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 tremolo ' + str(var.get()) + " " + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" tremolo ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" tremolo ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()

      wa = Label(filewin, text="tremolo")
      wa.grid(row=1,column=1)
	
	
      wa = Label(filewin, text="speed")
      wa.grid(row=2,column=1)
	
      w = Label(filewin, text="depth")
      w.grid(row=3,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=1, to=3000, variable = var ) 
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=0,column=1)
      widtscale = Scale(filewin, orient='horizontal',  from_=0, to=9, variable=vara)
      widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)








#################################################################




def speed():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "speed " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r 44100 "' + op.cget("text") + '" -t waveaudio 0 speed ' + str(var.get()) )
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r 44100 -t waveaudio 0 -t waveaudio 0 speed ' + str(var.get()) )
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r 44100 -t waveaudio 0 "' + opa.cget("text") + '" speed ' + str(var.get()) )


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" -r 44100 "' + opa.cget("text") + '" speed ' + str(var.get()) )


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()









      def playa():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r 94100 ' + str(var.get()) + ' "' + op.cget("text") + '" -t waveaudio 0 speed ' + str(var.get()) )
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def livea():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r 94100 -t waveaudio 0 -t waveaudio 0 speed ' + str(var.get()) )
      
      
      
      def reca():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r 94100 -t waveaudio 0 "' + opa.cget("text") + '" speed ' + str(var.get()) )


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox "' + op.cget("text") + '" -r 94100 "' + opa.cget("text") + '" speed ' + str(var.get()) )


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      def playb():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r 44100 "' + op.cget("text") + '" -t waveaudio 0 stretch ' + str(var.get()) )
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def liveb():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r 44100 -t waveaudio 0 -t waveaudio 0 stretch ' + str(var.get()) )
      
      
      
      def recb():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r 44100 -t waveaudio 0 "' + opa.cget("text") + '" stretch ' + str(var.get()) )


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def processb():
	os.system('sox "' + op.cget("text") + '" -r 44100 "' + opa.cget("text") + '" stretch ' + str(var.get()) )


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()









      def playc():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r 94100 ' + str(var.get()) + ' "' + op.cget("text") + '" -t waveaudio 0 stretch ' + str(var.get()) )
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def livec():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r 94100 -t waveaudio 0 -t waveaudio 0 stretch ' + str(var.get()) )
      
      
      
      def recc():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r 94100 -t waveaudio 0 "' + opa.cget("text") + '" stretch ' + str(var.get()) )


      def up_procc():
	update_the_label()
	update_the_labelout()
	process()


      def processc():
	os.system('sox "' + op.cget("text") + '" -r 94100 "' + opa.cget("text") + '" stretch ' + str(var.get()) )


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
     # vara = StringVar()
	
      wa = Label(filewin, text="speed")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="factor")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=0.1, to=5, resolution=0.1, digits=3, variable = var ) 
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
     # widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
     # widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)


      c = Label(filewin, text="-r 44100")
      c.grid(row=4,column=3)


      c = Label(filewin, text="-r 94100")
      c.grid(row=4,column=4)

      c = Label(filewin, text="speed")
      c.grid(row=3,column=3)
      
      
      c = Label(filewin, text="stretch")
      c.grid(row=3,column=5)
      c = Label(filewin, text="-r 44100")
      c.grid(row=4,column=5)


      c = Label(filewin, text="-r 94100")
      c.grid(row=4,column=6)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=3, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
      button = Button(filewin, text="play", command=playa)
      button.grid(row=5,column=4, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=6,column=4, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=7,column=4, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=8,column=4, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)




     	
      button = Button(filewin, text="play", command=playb)
      button.grid(row=5,column=5, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liveb)
      sox.grid(row=6,column=5, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recb)
      rec.grid(row=7,column=5, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processb)
      process.grid(row=8,column=5, sticky=N+S+E+W)
	
   
	
      button = Button(filewin, text="play", command=playc)
      button.grid(row=5,column=6, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livec)
      sox.grid(row=6,column=6, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recc)
      rec.grid(row=7,column=6, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processc)
      process.grid(row=8,column=6, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	


	


	




      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)





###################################################################


def reverb():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "reverb " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      
      #######################
      
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 reverb')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 reverb')
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" reverb')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" reverb')


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

################################


      #######################
      
      def playa():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 reverb -w')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def livea():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 reverb -w')
      
      
      
      def reca():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" reverb -w')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" reverb -w')


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

################################






      filewin = Toplevel(root)
      #inputfile = op(root)
      #var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="reverb")
      wa.grid(row=0,column=1)
	
      #w = Label(filewin, text="rate")
      #w.grid(row=2,column=1)
	
      #scale = Scale(filewin, orient='horizontal', from_=800, to=96000, variable = var ) 
	
      #scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      #widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      #widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)

      c = Label(filewin, text="reverb")
      c.grid(row=4,column=2)

      c = Label(filewin, text="reverb -w")
      c.grid(row=4,column=3)

	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      button = Button(filewin, text="play", command=playa)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=8,column=3, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	




      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)








#################################################################################


def riaa():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "rate " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 riaa')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 riaa')
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" riaa')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" riaa')


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      #var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="riaa")
      wa.grid(row=0,column=1)
	
      #w = Label(filewin, text="rate")
      #w.grid(row=2,column=1)
	
      #scale = Scale(filewin, orient='horizontal', from_=800, to=96000, variable = var ) 
	
      #scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      #widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      #widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)





############################################################################




def rates():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "rate " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
     
###################################################################################
     
      def play():

	os.system('sox -r ' + str(var.get()) + ' "' + op.cget("text") + '" -t waveaudio 0')

	sel()
      
      def live():
	
	os.system('sox -r ' + str(var.get()) + ' -t waveaudio 0 -t waveaudio 0 ')
      
      
      
      def rec():


     	os.system('sox -r ' + str(var.get()) + ' -t waveaudio 0 "' + opa.cget("text") + '" ')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" -r ' + str(var.get()) + ' "' + opa.cget("text") + '" ')



	sel()

###############################################################################################



###################################################################################
     
      def playa():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 rate -v')

	sel()
      
      def livea():
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 rate -v')
      
      
      
      def reca():


     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" rate -v')


      def up_proca():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" rate -v')



	sel()

###############################################################################################

###################################################################################
     
      def playb():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 rate -q')

	sel()
      
      def liveb():
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 rate -q')
      
      
      
      def recb():


     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" rate -q')


      def up_procb():
	update_the_label()
	update_the_labelout()
	process()


      def processb():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" rate -q')



	sel()

###############################################################################################



###################################################################################
     
      def playc():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 rate -l')

	sel()
      
      def livec():
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 rate -l')
      
      
      
      def recc():


     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" rate -l')


      def up_procc():
	update_the_label()
	update_the_labelout()
	process()


      def processc():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" rate -l')



	sel()

###############################################################################################


###################################################################################
     
      def playd():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 rate -m')

	sel()
      
      def lived():
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 rate -m')
      
      
      
      def recd():


     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" rate -m')


      def up_procd():
	update_the_label()
	update_the_labelout()
	process()


      def processd():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" rate -m')



	sel()

###############################################################################################


###################################################################################
     
      def playe():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 rate -h')

	sel()
      
      def livee():
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 rate -h')
      
      
      
      def rece():


     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" rate -h')


      def up_proce():
	update_the_label()
	update_the_labelout()
	process()


      def processe():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" rate -h')



	sel()

###############################################################################################









      filewin = Toplevel(root)
      #inputfile = op(root)
      #var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="rate")
      wa.grid(row=0,column=2)
	
     # w = Label(filewin, text="rate")
     # w.grid(row=2,column=1)
	
     # scale = Scale(filewin, orient='horizontal', from_=800, to=96000, variable = var ) 
	
     # scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
    #  widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
    #  widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)

      c = Label(filewin, text="very high")
      c.grid(row=4,column=2)

      c = Label(filewin, text="quick")
      c.grid(row=4,column=3)

      c = Label(filewin, text="low")
      c.grid(row=4,column=4)

      c = Label(filewin, text="medium")
      c.grid(row=4,column=5)

      c = Label(filewin, text="high")
      c.grid(row=4,column=6)












	
      button = Button(filewin, text="play", command=playa)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)


##    
      button = Button(filewin, text="play", command=playb)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liveb)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recb)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processb)
      process.grid(row=8,column=3, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
 
##    
      button = Button(filewin, text="play", command=playc)
      button.grid(row=5,column=4, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livec)
      sox.grid(row=6,column=4, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recc)
      rec.grid(row=7,column=4, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processc)
      process.grid(row=8,column=4, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	


##    
      button = Button(filewin, text="play", command=playd)
      button.grid(row=5,column=5, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=lived)
      sox.grid(row=6,column=5, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recd)
      rec.grid(row=7,column=5, sticky=N+S+E+W)
      
     # rate -v
      process = Button(filewin, text='process', command=processd)
      process.grid(row=8,column=5, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
 
##    
      button = Button(filewin, text="play", command=playe)
      button.grid(row=5,column=6, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livee)
      sox.grid(row=6,column=6, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rece)
      rec.grid(row=7,column=6, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processe)
      process.grid(row=8,column=6, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
 


	
 




      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)




###########################################



def overdrive():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "overdrive " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 overdrive '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 overdrive ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" overdrive '+ str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" overdrive ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 overdrive '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 overdrive ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" overdrive '+ str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" overdrive ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()















      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="overdrive")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="gain")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=1, to=100, variable = var )
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="color")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=1, to=20, variable=vara)
      widtscale.grid(row=3,column=2)
      
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
      cp = Label(filewin, text="   overdrive   ")
      cp.grid(row=4,column=2)

     
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

     



      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)



###############################################



def loudness():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "loudness " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)



      def playa():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 loudness ' + str(var.get()))
	sel()
      
      def livea():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 loudness ')
      
      
      
      def reca():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" loudness ' + str(var.get()))


      def up_proca():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" loudness ' + str(var.get()))

	sel()


##################


      def playb():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 loudness ' + str(var.get()))
	sel()
      
      def liveb():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 loudness ' + str(var.get()))
      
      
      
      def recb():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" loudness ' + str(var.get()))


      def up_procb():
	update_the_label()
	update_the_labelout()
	process()


      def processb():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" loudness ' + str(var.get()))

	sel()










      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="loudness")
      wa.grid(row=0,column=1)
    
    
      wa = Label(filewin, text="")
      wa.grid(row=0,column=2)
      
      
      
      
      
      #w = Label(filewin, text="rate")
      #w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=-20, to=20, variable = var ) 
	
      scale.grid(row=2,column=2)
      #f = Label(filewin, text="")
      #f.grid(row=3,column=1)
     # widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      #widtscale.grid(row=3,column=2)

 
      c = Label(filewin, text="factor")
      c.grid(row=2,column=1)


      c = Label(filewin, text="loudness")
      c.grid(row=3,column=1)
	
      button = Button(filewin, text="play", command=playa)
      button.grid(row=3,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=4,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=5,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=6,column=2, sticky=N+S+E+W)




        
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)







############################################



def flanger():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "fir" + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 fir ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 fir ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + ' ' + str(vare.get()) + ' ' + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" fir ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" fir ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
  


      filewin = Toplevel(root)
      #inputfile = op(root)
      vara = StringVar()
      varb = StringVar()
      varc = StringVar()
      vard = StringVar()
      vare = StringVar()
      varf = StringVar()



      wa = Label(filewin, text="flanger")
      wa.grid(row=0,column=1)

      wa = Label(filewin, text="delay")
      wa.grid(row=0,column=2)

      wa = Label(filewin, text="depth")
      wa.grid(row=0,column=3)
      
      wa = Label(filewin, text="regen")
      wa.grid(row=0,column=4)
      
      wa = Label(filewin, text="width")
      wa.grid(row=0,column=5)
      
      
      wa = Label(filewin, text="speed")
      wa.grid(row=0,column=6)
    
      wa = Label(filewin, text="phase")
      wa.grid(row=0,column=7)
      
      
      w = Label(filewin, text="")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal',  from_=0, to=30, variable = vara)
	
      scale.grid(row=2,column=2)
      
      
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal',  from_=0, to=100,  variable=vard)
      widtscale.grid(row=2,column=5)
      
     
      #wg = Label(filewin, text="cents")
     # wg.grid(row=2,column=3)
      
      
      scaleg = Scale(filewin, orient='horizontal',  from_=0, to=10, variable = varb )
	
      scaleg.grid(row=2,column=3)	
     
      scaleg = Scale(filewin, orient='horizontal',  from_=-95, to=95,  variable = varc )
	
      scaleg.grid(row=2,column=4)
     

      scaleg = Scale(filewin, orient='horizontal', from_=-0.9, to=0.9, resolution=0.01, digits=3, variable = varf )
	
      scaleg.grid(row=2,column=7)
     
      
      scaleg = Scale(filewin, orient='horizontal',   from_=-0.1, to=0.9, resolution=0.01, digits=3,  variable = vare )
	
      scaleg.grid(row=2,column=6)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
    


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

     
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)








###########################################



def fir():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "fir" + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 fir ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 fir ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + ' ' + str(vare.get()) + ' ' + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" fir ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" fir ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
  


      filewin = Toplevel(root)
      #inputfile = op(root)
      vara = StringVar()
      varb = StringVar()
      varc = StringVar()
      vard = StringVar()
      vare = StringVar()
      varf = StringVar()



      wa = Label(filewin, text="fir")
      wa.grid(row=0,column=1)

      wa = Label(filewin, text="1")
      wa.grid(row=0,column=2)

      wa = Label(filewin, text="2")
      wa.grid(row=0,column=3)
      
      wa = Label(filewin, text="3")
      wa.grid(row=0,column=4)
      
      wa = Label(filewin, text="4")
      wa.grid(row=0,column=5)
      
      
      wa = Label(filewin, text="5")
      wa.grid(row=0,column=6)
    
      wa = Label(filewin, text="6")
      wa.grid(row=0,column=7)
      
      
      w = Label(filewin, text="")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal',  from_=-0.9, to=0.9, resolution=0.01, digits=3,  variable = vara)
	
      scale.grid(row=2,column=2)
      
      
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal',  from_=-0.9, to=0.9, resolution=0.01, digits=3,  variable=vard)
      widtscale.grid(row=2,column=5)
      
     
      #wg = Label(filewin, text="cents")
     # wg.grid(row=2,column=3)
      
      
      scaleg = Scale(filewin, orient='horizontal',  from_=-0.9, to=0.9, resolution=0.01, digits=3,  variable = varb )
	
      scaleg.grid(row=2,column=3)	
     
      scaleg = Scale(filewin, orient='horizontal',  from_=-0.9, to=0.9, resolution=0.01, digits=3,  variable = varc )
	
      scaleg.grid(row=2,column=4)
     

      scaleg = Scale(filewin, orient='horizontal', from_=-0.9, to=0.9, resolution=0.01, digits=3, variable = varf )
	
      scaleg.grid(row=2,column=7)
     
      
      scaleg = Scale(filewin, orient='horizontal',   from_=-0.9, to=0.9, resolution=0.01, digits=3,  variable = vare )
	
      scaleg.grid(row=2,column=6)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
    


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

     
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)






#######################################



def equalizer():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "equalizer" + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 equalizer ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 equalizer ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" equalizer ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()))
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" equalizer ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()))
	    
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
		
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 echo ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
#	os.system('sox -t waveaudio 0 -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
      	os.system('sox -t waveaudio 0 -t waveaudio 0 chorus ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + " " + str(vare.get()) + ' ' + str(varf.get()) + ' -t' )
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    


     #	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
#	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))

	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    

#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()



#+ str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))











      filewin = Toplevel(root)
      #inputfile = op(root)
      vara = StringVar()
      varb = StringVar()
      varc = StringVar()
     # vard = StringVar()
     # vare = StringVar()
     # varf = StringVar()



      wa = Label(filewin, text="equlizer")
      wa.grid(row=0,column=1)

      wa = Label(filewin, text="frequency")
      wa.grid(row=0,column=2)

      wa = Label(filewin, text="width")
      wa.grid(row=0,column=3)
      
      wa = Label(filewin, text="gain")
      wa.grid(row=0,column=4)
      
     
      
      
      w = Label(filewin, text="")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal',  from_=0, to=5000,   variable = vara)
	
      scale.grid(row=2,column=2)
      
      
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
     
     
      #wg = Label(filewin, text="cents")
     # wg.grid(row=2,column=3)
      
      
      scaleg = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable = varb )
	
      scaleg.grid(row=2,column=3)	
     
      scaleg = Scale(filewin, orient='horizontal', from_=-20, to=20, variable = varc )
	
      scaleg.grid(row=2,column=4)
     

    
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
    


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

     
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)








#######################################


def choruses():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "echo" + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 echo ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 echo ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + ' ' + str(vare.get()) + ' ' + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" echo ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" echo ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
		
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 echo ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
#	os.system('sox -t waveaudio 0 -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
      	os.system('sox -t waveaudio 0 -t waveaudio 0 chorus ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + " " + str(vare.get()) + ' ' + str(varf.get()) + ' -t' )
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    


     #	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
#	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))

	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    

#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()



#+ str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))











      filewin = Toplevel(root)
      #inputfile = op(root)
      vara = StringVar()
      varb = StringVar()
      varc = StringVar()
      vard = StringVar()
      vare = StringVar()
      varf = StringVar()



      wa = Label(filewin, text="chorus")
      wa.grid(row=0,column=1)

      wa = Label(filewin, text="gain-in")
      wa.grid(row=0,column=2)

      wa = Label(filewin, text="gain-out")
      wa.grid(row=0,column=3)
      
      wa = Label(filewin, text="delay")
      wa.grid(row=0,column=4)
      
      wa = Label(filewin, text="decay")
      wa.grid(row=0,column=5)
      
      
      wa = Label(filewin, text="delay")
      wa.grid(row=0,column=6)
    
      wa = Label(filewin, text="decay")
      wa.grid(row=0,column=7)
      
      
      w = Label(filewin, text="")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable = vara)
	
      scale.grid(row=2,column=2)
      
      
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable=vard)
      widtscale.grid(row=2,column=5)
      
     
      #wg = Label(filewin, text="cents")
     # wg.grid(row=2,column=3)
      
      
      scaleg = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable = varb )
	
      scaleg.grid(row=2,column=3)	
     
      scaleg = Scale(filewin, orient='horizontal', from_=0, to=3000, variable = varc )
	
      scaleg.grid(row=2,column=4)
     

      scaleg = Scale(filewin, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable = varf )
	
      scaleg.grid(row=2,column=7)
     
      
      scaleg = Scale(filewin, orient='horizontal',  from_=0, to=3000, variable = vare )
	
      scaleg.grid(row=2,column=6)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
    


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

     
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)








##########################################


def earwax():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
    


      def playa():

	os.system('sox -r 44100 "' + op.cget("text") + '" -t waveaudio 0 earwax ' + str(var.get()))
#	sel()
      
      def livea():
  
	os.system('sox -r 44100 -t waveaudio 0 -t waveaudio 0 earwax ')
      
      
      
      def reca():
     	os.system('sox -r 44100 -t waveaudio 0 "' + opa.cget("text") + '" earwax ')


      def up_proca():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox -r 44100 "' + op.cget("text") + '" "' + opa.cget("text") + '" earwax ')

#	sel()


##################


    



      filewin = Toplevel(root)
      #inputfile = op(root)
      #var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="earwax")
      wa.grid(row=0,column=1)
    
    
      wa = Label(filewin, text="")
      wa.grid(row=0,column=2)
      
      
      
      
      
      #w = Label(filewin, text="rate")
      #w.grid(row=2,column=1)
	
     
      #f = Label(filewin, text="")
      #f.grid(row=3,column=1)
     # widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      #widtscale.grid(row=3,column=2)
     
	
      button = Button(filewin, text="play", command=playa)
      button.grid(row=4,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=5,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=6,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=7,column=2, sticky=N+S+E+W)




   	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)




###########################################


def upsample():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "rate " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)



      def playa():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 downsample ' + str(var.get()))
	sel()
      
      def livea():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 downsample ')
      
      
      
      def reca():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" downsample ' + str(var.get()))


      def up_proca():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" downsample ' + str(var.get()))

	sel()


##################


      def playb():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 upsample ' + str(var.get()))
	sel()
      
      def liveb():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 upsample ' + str(var.get()))
      
      
      
      def recb():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" upsample ' + str(var.get()))


      def up_procb():
	update_the_label()
	update_the_labelout()
	process()


      def processb():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" upsample ' + str(var.get()))

	sel()










      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="up/down sample")
      wa.grid(row=0,column=1)
    
    
      wa = Label(filewin, text="")
      wa.grid(row=0,column=2)
      
      
      
      
      
      #w = Label(filewin, text="rate")
      #w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=0, to=20, variable = var ) 
	
      scale.grid(row=2,column=2)
      #f = Label(filewin, text="")
      #f.grid(row=3,column=1)
     # widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      #widtscale.grid(row=3,column=2)
      c = Label(filewin, text="upsample")
      c.grid(row=2,column=4)
 
 
      c = Label(filewin, text="factor")
      c.grid(row=2,column=1)


      c = Label(filewin, text="downsample")
      c.grid(row=2,column=3)
	
      button = Button(filewin, text="play", command=playa)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=8,column=3, sticky=N+S+E+W)




      button = Button(filewin, text="play", command=playb)
      button.grid(row=5,column=4, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liveb)
      sox.grid(row=6,column=4, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recb)
      rec.grid(row=7,column=4, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processb)
      process.grid(row=8,column=4, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)






#####################################################


def dither():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "rate " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r ' + str(var.get()) + ' "' + op.cget("text") + '" -t waveaudio 0')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r ' + str(var.get()) + ' -t waveaudio 0 -t waveaudio 0 ')
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r ' + str(var.get()) + ' -t waveaudio 0 "' + opa.cget("text") + '" ')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" -r ' + str(var.get()) + ' "' + opa.cget("text") + '" ')


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      def playa():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f gesemann')
	sel()
      
      def livea():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f gesemann')
      
      
      
      def reca():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f gesemann')


      def up_proca():
	update_the_label()
	update_the_labelout()
	process()


      def processa():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f gesemann')

	sel()


##################


      def playb():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f shibata')
	sel()
      
      def liveb():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f shibata')
      
      
      def recb():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f shibata')


      def up_procb():
	update_the_label()
	update_the_labelout()
	process()


      def processb():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f shibata')

	sel()

      def playc():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f low-shibata')
	sel()
      
      def livec():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f low-shibata')
      
      
      
      def recc():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f low-shibata')


      def up_procc():
	update_the_label()
	update_the_labelout()
	process()


      def processc():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f low-shibata')

	sel()



      def playd():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f high-shibata')
	sel()
      
      def lived():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f high-shibata')
      
      
      
      def recd():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f high-shibata')


      def up_procd():
	update_the_label()
	update_the_labelout()
	process()


      def processd():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f high-shibata')

	sel()





      def playe():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f modified-e-weighted')
	sel()
      
      def livee():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f modified-e-weighted')
      
      
      
      def rece():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f modified-e-weighted')


      def up_proce():
	update_the_label()
	update_the_labelout()
	process()


      def processe():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f modified-e-weighted')

	sel()





      def playf():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f improved-e-weighted')
	sel()
      
      def livef():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f improved-e-weighted')
      
      
      
      def recf():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f improved-e-weighted')


      def up_procf():
	update_the_label()
	update_the_labelout()
	process()


      def processf():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f improved-e-weighted')

	sel()





      def playg():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f lipshitz')
	sel()
      
      def liveg():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f lipshitz')
      
      
      
      def recg():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f lipshitz')


      def up_procg():
	update_the_label()
	update_the_labelout()
	process()


      def processg():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f lipshitz')

	sel()





      def playh():

	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 dither -f f-weighted')
	sel()
      
      def liveh():
  
	os.system('sox -t waveaudio 0 -t waveaudio 0 dither -f f-weighted')
      
      
      
      def rech():
     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" dither -f f-weighted')


      def up_proch():
	update_the_label()
	update_the_labelout()
	process()


      def processh():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" dither -f f-weighted')

	sel()















      filewin = Toplevel(root)
      #inputfile = op(root)
      #var = StringVar()
      #vara = StringVar()
	
      wa = Label(filewin, text="diter")
      wa.grid(row=0,column=1)
	
     # w = Label(filewin, text="rate")
      #w.grid(row=2,column=1)
	
     # scale = Scale(filewin, orient='horizontal', from_=800, to=96000, variable = var ) 
	
     # scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      #widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
     # widtscale.grid(row=3,column=2)
      #c = Label(filewin, text="commands")
      #c.grid(row=1,column=1)
     
      c = Label(filewin, text="gesemann")
      c.grid(row=1,column=1)

      c = Label(filewin, text="shibata")
      c.grid(row=1,column=2)

      c = Label(filewin, text="low-shibata")
      c.grid(row=1,column=3)


      c = Label(filewin, text="high-shibata")
      c.grid(row=1,column=4)


      c = Label(filewin, text="modified-e-weighted")
      c.grid(row=1,column=5)

      c = Label(filewin, text="improved-e-weighted")
      c.grid(row=1,column=6)

      c = Label(filewin, text="lipshitz")
      c.grid(row=1,column=7)
      c = Label(filewin, text="f-weighted")
      c.grid(row=1,column=8)

 
	
      button = Button(filewin, text="play", command=playa)
      button.grid(row=2,column=1, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livea)
      sox.grid(row=3,column=1, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=reca)
      rec.grid(row=4,column=1, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processa)
      process.grid(row=5,column=1, sticky=N+S+E+W)

     
     
      button = Button(filewin, text="play", command=playb)
      button.grid(row=2,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liveb)
      sox.grid(row=3,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recb)
      rec.grid(row=4,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processb)
      process.grid(row=5,column=2, sticky=N+S+E+W)


      button = Button(filewin, text="play", command=playc)
      button.grid(row=2,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livec)
      sox.grid(row=3,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recc)
      rec.grid(row=4,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processc)
      process.grid(row=5,column=3, sticky=N+S+E+W)


      button = Button(filewin, text="play", command=playd)
      button.grid(row=2,column=4, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=lived)
      sox.grid(row=3,column=4, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recd)
      rec.grid(row=4,column=4, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processd)
      process.grid(row=5,column=4, sticky=N+S+E+W)


      button = Button(filewin, text="play", command=playe)
      button.grid(row=2,column=5, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livee)
      sox.grid(row=3,column=5, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rece)
      rec.grid(row=4,column=5, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processe)
      process.grid(row=5,column=5, sticky=N+S+E+W)


      button = Button(filewin, text="play", command=playf)
      button.grid(row=2,column=6, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=livef)
      sox.grid(row=3,column=6, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recf)
      rec.grid(row=4,column=6, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processf)
      process.grid(row=5,column=6, sticky=N+S+E+W)


      button = Button(filewin, text="play", command=playg)
      button.grid(row=2,column=7, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liveg)
      sox.grid(row=3,column=7, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recg)
      rec.grid(row=4,column=7, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processg)
      process.grid(row=5,column=7, sticky=N+S+E+W)


      button = Button(filewin, text="play", command=playh)
      button.grid(row=2,column=8, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liveh)
      sox.grid(row=3,column=8, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rech)
      rec.grid(row=4,column=8, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processh)
      process.grid(row=5,column=8, sticky=N+S+E+W)

	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=7, sticky=N+S+E+W)



#####################################################################




def delay():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "delay " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 delay ' + str(var.get()) + ' ' + str(vara.get()))
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 delay ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '"  delay ' + str(var.get()) + ' ' + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '"  "' + opa.cget("text") + '" delay ' + str(var.get()) + ' ' + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="delay")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="delay 1")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=0.1, to=3, resolution=0.1, digits=3, variable = var ) 
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="delay 2")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=0.1, to=3, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)



####################################################################




def deemph():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = " " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r 44100 "' + op.cget("text") + '" -t waveaudio 0 deemph')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r 44100 -t waveaudio 0 -t waveaudio 0 deemph')
       
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r 44100 -t waveaudio 0 "' + opa.cget("text") + '" deemph')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" -r 44100 "' + opa.cget("text") + '" deemph')


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="deemph")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, state=DISABLED, orient='horizontal', from_=800, to=96000, variable = var ) 
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)







##################################################################




def contrast():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "contrast " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r ' + str(var.get()) + ' "' + op.cget("text") + '" -t waveaudio 0')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 contrast '+ str(var.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" contrast'+ str(var.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" contrast ' + str(var.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="contrast")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="contrast")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=0, to=100, variable = var ) 
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)




####################################################################


def chorus():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "chorus " + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -s')
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 chorus ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + " " + str(vare.get()) + ' ' + str(varf.get()) + ' -s' )
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -s')
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -s')
	    
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
		
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
#	os.system('sox -t waveaudio 0 -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
      	os.system('sox -t waveaudio 0 -t waveaudio 0 chorus ' + str(vara.get()) + ' ' + str(varb.get()) + ' ' + str(varc.get()) + ' ' + str(vard.get()) + " " + str(vare.get()) + ' ' + str(varf.get()) + ' -t' )
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    


     #	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
#	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))

	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" chorus ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()) + ' -t')
	    

#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()



#+ str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))











      filewin = Toplevel(root)
      #inputfile = op(root)
      vara = StringVar()
      varb = StringVar()
      varc = StringVar()
      vard = StringVar()
      vare = StringVar()
      varf = StringVar()



      wa = Label(filewin, text="chorus")
      wa.grid(row=0,column=1)

      wa = Label(filewin, text="gain-in")
      wa.grid(row=0,column=2)

      wa = Label(filewin, text="gain-out")
      wa.grid(row=0,column=3)
      
      wa = Label(filewin, text="delay")
      wa.grid(row=0,column=4)
      
      wa = Label(filewin, text="decay")
      wa.grid(row=0,column=5)
      
      
      wa = Label(filewin, text="speed")
      wa.grid(row=0,column=6)
    
      wa = Label(filewin, text="depth")
      wa.grid(row=0,column=7)
      
      
      w = Label(filewin, text="")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable = vara)
	
      scale.grid(row=2,column=2)
      
      
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable=vard)
      widtscale.grid(row=2,column=5)
      
     
      #wg = Label(filewin, text="cents")
     # wg.grid(row=2,column=3)
      
      
      scaleg = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable = varb )
	
      scaleg.grid(row=2,column=3)	
     
      scaleg = Scale(filewin, orient='horizontal', from_=0, to=99, variable = varc )
	
      scaleg.grid(row=2,column=4)
     

      scaleg = Scale(filewin, orient='horizontal', from_=0, to=9, variable = varf )
	
      scaleg.grid(row=2,column=7)
     
      
      scaleg = Scale(filewin, orient='horizontal',  from_=0.1, to=1, resolution=0.1, digits=3,  variable = vare )
	
      scaleg.grid(row=2,column=6)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
      cp = Label(filewin, text=" sinosuidal ")
      cp.grid(row=4,column=2)

      g = Label(filewin, text=" triangluar ")
      g.grid(row=4,column=3)


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

      button = Button(filewin, text="play", command=playr)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liver)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recr)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processr)
      process.grid(row=8,column=3, sticky=N+S+E+W)
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)








######################################################################


def biquad():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "bend " + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 biquad ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 biquad ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" biquad ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" biquad ' + str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))
	    
	    
	    
	    #+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()



#+ str(vara.get()) + ' ' + str(varb.get()) + " " + str(varc.get()) + " " + str(vard.get()) + " " + str(vare.get()) + " " + str(varf.get()))











      filewin = Toplevel(root)
      #inputfile = op(root)
      vara = StringVar()
      varb = StringVar()
      varc = StringVar()
      vard = StringVar()
      vare = StringVar()
      varf = StringVar()



      wa = Label(filewin, text="biquad")
      wa.grid(row=0,column=1)

      wa = Label(filewin, text="0")
      wa.grid(row=0,column=2)

      wa = Label(filewin, text="1")
      wa.grid(row=0,column=3)
      
      wa = Label(filewin, text="2")
      wa.grid(row=0,column=4)

	
      w = Label(filewin, text="a")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=0, to=9, variable = vara )
	
      scale.grid(row=2,column=2)
      
      
      f = Label(filewin, text="b")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=0, to=9, variable=vard)
      widtscale.grid(row=3,column=2)
      
     
      #wg = Label(filewin, text="cents")
     # wg.grid(row=2,column=3)
      
      
      scaleg = Scale(filewin, orient='horizontal', from_=0, to=9, variable = varb )
	
      scaleg.grid(row=2,column=3)	
     
      scaleg = Scale(filewin, orient='horizontal', from_=0, to=9, variable = varc )
	
      scaleg.grid(row=2,column=4)
     

      scaleg = Scale(filewin, orient='horizontal', from_=0, to=9, variable = varf )
	
      scaleg.grid(row=3,column=4)
     
      
      scaleg = Scale(filewin, orient='horizontal', from_=0, to=9, variable = vare )
	
      scaleg.grid(row=3,column=3)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
      cp = Label(filewin, text="   biquad   ")
      cp.grid(row=4,column=2)

     # g = Label(filewin, text="   treble   ")
      #g.grid(row=4,column=3)


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

    #  button = Button(filewin, text="play", command=playr)
     # button.grid(row=5,column=3, sticky=N+S+E+W)
      
      #sox = Button(filewin, text='live', command=liver)
     # sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      #rec = Button(filewin, text='rec', command=recr)
      #rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
     # process = Button(filewin, text='process', command=processr)
     # process.grid(row=8,column=3, sticky=N+S+E+W)
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)



########################################################################




def bass():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "bass/treble " + str(var.get()) + " " + str(vara.get()) + " " + str(varg.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" bass ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" bass ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()














      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
      varg = StringVar()
	
      wa = Label(filewin, text="bass/treble")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="frequency")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=20, to=5000, variable = var )
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="width")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      
     
      wg = Label(filewin, text="gain")
      wg.grid(row=2,column=3)
	
      scaleg = Scale(filewin, orient='horizontal', from_=-20, to=20, variable = varg )
	
      scaleg.grid(row=3,column=3)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
      cp = Label(filewin, text="   bass   ")
      cp.grid(row=4,column=2)

      g = Label(filewin, text="   treble   ")
      g.grid(row=4,column=3)


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

      button = Button(filewin, text="play", command=playr)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liver)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recr)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processr)
      process.grid(row=8,column=3, sticky=N+S+E+W)
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)






#########################################################################




def bend():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "bend " + str(var.get()) + " " + str(varg.get()) + " " + str(vara.get())#+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bend '+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 bend '+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' '+ str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" bend '+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	    #bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" bend '+ str(var.get()) + "," + str(varg.get()) + "," + str(vara.get()))
	  #  bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bass ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 treble ' + str(varg.get()) + ' ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" treble ' + str(varg.get()) + ' ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()














      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
      varg = StringVar()
	
      wa = Label(filewin, text="bend")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="delay")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable = var )
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="duration")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=0.1, to=2, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      
     
      wg = Label(filewin, text="cents")
      wg.grid(row=2,column=3)
	
      scaleg = Scale(filewin, orient='horizontal', from_=-999, to=999, variable = varg )
	
      scaleg.grid(row=3,column=3)
     
     
     
     
     
     
     
     
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
      cp = Label(filewin, text="   bend   ")
      cp.grid(row=4,column=2)

     # g = Label(filewin, text="   treble   ")
      #g.grid(row=4,column=3)


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

    #  button = Button(filewin, text="play", command=playr)
     # button.grid(row=5,column=3, sticky=N+S+E+W)
      
      #sox = Button(filewin, text='live', command=liver)
     # sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      #rec = Button(filewin, text='rec', command=recr)
      #rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
     # process = Button(filewin, text='process', command=processr)
     # process.grid(row=8,column=3, sticky=N+S+E+W)
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)






####################################################################


def band():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "band " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bandpass -c '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 bandpass -c ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" bandpass -c '+ str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" bandpass -c ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()

      
      
      def playr():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 bandpass -c '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()







      def liver():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 bandreject ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def recr():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" bandreject '+ str(var.get()) + " " + str(vara.get()))


      def up_procr():
	update_the_label()
	update_the_labelout()
	process()


      def processr():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" bandreject ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()














      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="bandpass/bandreject")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="frequency")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=20, to=5000, variable = var )
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="width")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
      
      cp = Label(filewin, text="   bandpass   ")
      cp.grid(row=4,column=2)

      g = Label(filewin, text="   bandreject   ")
      g.grid(row=4,column=3)


      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
       

      button = Button(filewin, text="play", command=playr)
      button.grid(row=5,column=3, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=liver)
      sox.grid(row=6,column=3, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=recr)
      rec.grid(row=7,column=3, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=processr)
      process.grid(row=8,column=3, sticky=N+S+E+W)
	





      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)







##################################################################


def rate():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "rate " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	os.system('sox -r ' + str(var.get()) + ' "' + op.cget("text") + '" -t waveaudio 0')
#	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -r ' + str(var.get()) + ' -t waveaudio 0 -t waveaudio 0 ')
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -r ' + str(var.get()) + ' -t waveaudio 0 "' + opa.cget("text") + '" ')


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" -r ' + str(var.get()) + ' "' + opa.cget("text") + '" ')


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="rate")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="rate")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=800, to=96000, variable = var ) 
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, state=DISABLED, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)



#################################################################################

def donothing():
      def update_the_label():
	   updated_text = root.files
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   opa.configure(text = updated_text)
      
      def update_the_labelout(): #to je in 
	   updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
	   op.configure(text = updated_text)
      
      def update():
	update_the_label()
	update_the_labelout()

      
      
      def u_p():
	update_the_label()
	update_the_labelout()
	play()

      def u_r():
	update_the_label()
	update_the_labelout()
	rec()
  
      def sel():
		selection = "allpass " + str(var.get()) + " " + str(vara.get()) #+ " " + op.cget("text")  
		label.config(text = selection)
      def play():
	# updated_text = root.filename
	  #updated_text = op("The GM time now is %H:%M:%S.", op.cget("text"))
        # op.configure(text = updated_text)	
	
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass '+ str(var.get()) + " " + str(vara.get()))
	#os.system('sox "' + op.cget("text") + '" -t waveaudio 0')
	#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	sel()
      
      def live():
#   	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['cmd sox -t waveaudio 0 -t waveaudio 0'])
	
	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()))
      
      
      
      def rec():
#os.system('sox -t waveaudio 0 -t waveaudio 0')
#		os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
#	subprocess.call(['notepad.exe', str(var.get())])

#	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
#	sel()



     	os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" allpass '+ str(var.get()) + " " + str(vara.get()))


      def up_proc():
	update_the_label()
	update_the_labelout()
	process()


      def process():
	os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '" allpass ' + str(var.get()) + " " + str(vara.get()))


#	os.system('sox -t waveaudio 0 -t waveaudio 0')
	#	subprocess.call(['notepad.exe', str(var.get())])
	#os.system('sox -t waveaudio 0 "' + opa.cget("text") + '" '+ str(var.get()) + " " + str(vara.get()))
	sel()




      filewin = Toplevel(root)
      #inputfile = op(root)
      var = StringVar()
      vara = StringVar()
	
      wa = Label(filewin, text="allpass")
      wa.grid(row=0,column=1)
	
      w = Label(filewin, text="frequency")
      w.grid(row=2,column=1)
	
      scale = Scale(filewin, orient='horizontal', from_=20, to=5000, variable = var )
	
      scale.grid(row=2,column=2)
      f = Label(filewin, text="width")
      f.grid(row=3,column=1)
      widtscale = Scale(filewin, orient='horizontal', from_=0.1, to=1, resolution=0.1, digits=3, variable=vara)
      widtscale.grid(row=3,column=2)
      c = Label(filewin, text="commands")
      c.grid(row=4,column=1)
	
      button = Button(filewin, text="play", command=play)
      button.grid(row=5,column=2, sticky=N+S+E+W)
      
      sox = Button(filewin, text='live', command=live)
      sox.grid(row=6,column=2, sticky=N+S+E+W)
	
      rec = Button(filewin, text='rec', command=rec)
      rec.grid(row=7,column=2, sticky=N+S+E+W)
      
      
      process = Button(filewin, text='process', command=process)
      process.grid(row=8,column=2, sticky=N+S+E+W)
	
    #  stop = Button(filewin, text='stop', command=stop)
     # stop.grid(row=9, column=2, sticky=N+S+E+W)
	
     
      labelval = Label(filewin,text="effect")
      labelval.grid(row=10,column=1)
      
      label = Label(filewin)
	
      label.grid(row=10,column=2)
      #in
      opin = Label(filewin, text="in")
      opin.grid(row=11,column=1)
      
      op = Label(filewin, text="")
      op.grid(row=11,column=2)
      
      #out
      opout = Label(filewin, text="out")
      opout.grid(row=12,column=1)
      opa = Label(filewin, text="")
      opa.grid(row=12,column=2)
      
      
      updat = Button(filewin, text="update", command=update)
      updat.grid(row=13,column=2, sticky=N+S+E+W)




def open():
  root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = (("audio files","*.mp3"),("all files","*.*")))
  
  updated_text = root.filename
  
  op.configure(text = updated_text)



def saves():
  root.files = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file", defaultextension="", filetypes = (("aiff","*.aiff"),("dat","*.dat"),("mp3","*.mp3"),("ogg","*.ogg"),("raw","*.raw"),("wav","*.wav"),("8svx","*.8svx"),("aif","*.aif"),("al","*.al"),("amb","*.amb"),("amr-nb","*.amr-nb"),("amr-wb","*.amr-wb"),("au","*.au"),("avr","*.avr"),("caf","*.caf"),("cdda","*.cdda"),("cdr","*.cdr"),("cvs","*.cvs"),("cvsd","*.cvsd"),("cvu","*.cvu"),("dvms","*.dvms"),("f32","*.f32"),("f4","*.f4"),("f64","*.f64"),("f8","*.f8"),("fap","*.fap"),("flac","*.flac"),("fssd","*.fssd"),("gsm","*.gsm"),("gsrt","*.gsrt"),("hcom","*.hcom"),("htk","*.htk"),("ima","*.ima"),("ircam","*.ircam"),("la","*.la"),("lpc","*.lpc"),("lpc10","*.lpc10"),("lu","*.lu"),("mat","*.mat"),("mat4","*.mat4"),("mat5","*.mat5"),("maud","*.maud"),("mp2","*.mp2"),("nist","*.nist"),("ogg","*.ogg"),("opus","*.opus"),("oss","*.oss"),("prc","*.prc"),("pvf","*.pvf"),("s1","*.s1"),("s16","*.s16"),("s2","*.s2"),("s24","*.s24"),("s3","*.s3"),("s32","*.s32"),("s4","*.s4"),("s8","*.s8"),("sb","*.sb"),("sd2","*.sd2"),("sds","*.sds"),("sl","*.sl"),("sln","*.sln"),("smp","*.smp"),("snd","*.snd"),("sph","*.sph"),("sw","*.sw"),("txw","*.txw"),("u1","*.u1"),("u16","*.u16"),("u2","*.u2"),("u24","*.u24"),("u3","*.u3"),("u32","*.u32"),("u4","*.u4"),("u8","*.u8"),("ub","*.ub"),("ul","*.ul"),("uw","*.uw"),("vms","*.vms"),("voc","*.voc"),("vorbis","*.vorbis"),("vox","*.vox"),("w64","*.w64"),("wavpcm","*.wavpcm"),("wv","*.wv"),("wve","*.wve"),("xa","*.xa"),("xi","*.xi")))

 # root.filename = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file", defaultextension="", filetypes = (("audio files","*.mp3"),("all files","*.*")))
  
  updated_textout = root.files
  
  opa.configure(text = updated_textout)




def play():
#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0')

def playn():
#	os.system('sox -t waveaudio 0 -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])

	os.system('sox "' + opa.cget("text") + '" -t waveaudio 0')



def convert():
  os.system('sox "' + op.cget("text") + '" "' + opa.cget("text") + '"')

def sel():
	selection = "Value = " + str(var.get()) + " " + str(vara.get()) + " " + op.cget("text")  
	label.config(text = selection)


def live():
	os.system('sox "' + op.cget("text") + '" -t waveaudio 0 allpass ' + str(var.get()) + ' ' + str(vara.get()) )
	#subprocess.call(['sox.exe', op.cget("text"), str(var.get()), str(vara.get())])







root = Tk()


open = Button(root, text='in', command=open)
open.grid(row=1, column=3, sticky=N+S+E+W)


a = Label(root, text="import")
a.grid(row=1, column=1)



op = Label(root, text="")
op.grid(row=1, column=2)





save = Label(root, text="export")
save.grid(row=2, column=1)




saves = Button(root, text='out', command=saves)
saves.grid(row=2, column=3, sticky=N+S+E+W)


opa = Label(root, text="")
opa.grid(row=2, column=2)



play = Button(root, text='play', command=play)

play.grid(row=3, column=3, sticky=N+S+E+W)

convert = Button(root, text='convert', command=convert)
convert.grid(row=4, column=3, sticky=N+S+E+W)



convert = Button(root, text='playnew', command=playn)
convert.grid(row=5, column=3, sticky=N+S+E+W)






menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="New", command=donothing)

#filemenu.add_command(label="Open", command=donothing)
#filemenu.add_command(label="Save", command=donothing)
#filemenu.add_command(label="Save as...", command=donothing)
#filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="rate", command=rate)
#editmenu.add_separator()
editmenu.add_command(label="loudness", command=loudness)
editmenu.add_command(label="overdrive", command=overdrive)
editmenu.add_command(label="rates", command=rates)
editmenu.add_command(label="speed", command=speed)

menubar.add_cascade(label="Options", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)


effectsmenu = Menu(menubar, tearoff=0)
effectsmenu.add_command(label="allpass", command=donothing)
#effectsmenu.add_separator()
effectsmenu.add_command(label="bandpass", command=band)
effectsmenu.add_command(label="bend", command=bend)
effectsmenu.add_command(label="bass/treble", command=bass)
effectsmenu.add_command(label="biquad", command=biquad)
effectsmenu.add_command(label="chorus", command=chorus)
effectsmenu.add_command(label="contrast", command=contrast)
effectsmenu.add_command(label="deemph", command=deemph)
effectsmenu.add_command(label="delay", command=delay)
effectsmenu.add_command(label="dither", command=dither)
effectsmenu.add_command(label="up/downsample", command=upsample)
effectsmenu.add_command(label="earwax", command=earwax)
effectsmenu.add_command(label="choruses", command=choruses)
effectsmenu.add_command(label="equalizer", command=equalizer)
effectsmenu.add_command(label="fir", command=fir)
effectsmenu.add_command(label="flanger", command=flanger)
effectsmenu.add_command(label="riaa", command=riaa)
effectsmenu.add_command(label="reverb", command=reverb)
effectsmenu.add_command(label="tremolo", command=tremolo)




menubar.add_cascade(label="Effects", menu=effectsmenu)
helpmenu = Menu(menubar, tearoff=0)

visumenu = Menu(menubar, tearoff=0)
visumenu.add_command(label="spectogram", command=donothing)
effectsmenu.add_separator()

menubar.add_cascade(label="Visualize", menu=visumenu)
helpmenu = Menu(menubar, tearoff=0)

#helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.title("sox")
root.config(menu=menubar)
#root.resizable(True, False)
#root.geometry("250x250")
root.mainloop()





