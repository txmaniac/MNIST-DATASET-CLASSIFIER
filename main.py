import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

class Launch(FloatLayout):
	
	def __init__(self, **kwargs):
		#super(Launch, self).__init__(**kwargs)
		#mybutton = Button(
	#			            text = 'Click me',
	#			            size = (80,80),
	#			            size_hint = (None,None)
	#			          )
	#	mybutton.bind(on_press = self.init) # Note: here say_hello doesn't have brackets.
	#	Launch.add_widget(mybutton)

		super(Launch, self).__init__(**kwargs)
		self.btn1 = Button(text="Initialize",size = (80,80),size_hint = (None,None), pos=(100,100))
		self.btn2 = Button(text="Test",size = (80,80),size_hint = (None,None), pos=(100,300))
		self.btn3 = Button(text="Train",size = (80,80),size_hint = (None,None), pos=(300,100))
		self.btn4 = Button(text="Graph",size = (80,80),size_hint = (None,None), pos=(300,300))
		self.ep_btn1 = Button(text="10",size = (80,80),size_hint = (None,None), pos=(480,300))
		self.ep_btn2 = Button(text="50",size = (80,80),size_hint = (None,None), pos=(560,300))
		self.ep_btn3 = Button(text="100",size = (80,80),size_hint = (None,None), pos=(640,300))
		self.l_btn1 = Button(text="0.5",size = (80,80),size_hint = (None,None), pos=(480,200))
		self.l_btn2 = Button(text="1.0",size = (80,80),size_hint = (None,None), pos=(560,200))
		self.l_btn3 = Button(text="1.5",size = (80,80),size_hint = (None,None), pos=(640,200))
		self.lbl1 = Label(text="",size = (100,20), pos = (200,200))
		self.lbl2 = Label(text="",size = (100,20), pos = (200,100))
		self.lbl3 = Label(text="",size = (100,20), pos = (200,200))
		#self.lbl_e = Label(text="",size = (100,20), pos = (100,300))
		
		self.btn1.bind(on_press = self.init)
		self.btn2.bind(on_press = self.run)
		self.btn3.bind(on_press = self.train)
		self.btn4.bind(on_press = self.graph)
		self.ep_btn1.bind(on_press = self.ep1)
		self.ep_btn2.bind(on_press = self.ep2)
		self.ep_btn3.bind(on_press = self.ep3)
		self.l_btn1.bind(on_press = self.l1)
		self.l_btn2.bind(on_press = self.l2)
		self.l_btn3.bind(on_press = self.l3)
		
		self.add_widget(self.btn1)
		self.add_widget(self.btn2)
		self.add_widget(self.btn3)
		self.add_widget(self.btn4)
		self.add_widget(self.lbl1)
		self.add_widget(self.lbl2)
		self.add_widget(self.lbl3)
		self.add_widget(self.ep_btn1)
		self.add_widget(self.ep_btn2)
		self.add_widget(self.ep_btn3)
		self.add_widget(self.l_btn1)
		self.add_widget(self.l_btn2)
		self.add_widget(self.l_btn3)
		#self.add_widget(self.lbl_e)
		
	def ep1(self,instance):
		#self.lbl_e = "Epoch 10"
		self.val = 10

	def ep2(self,instance):
		#self.lbl_e = "Epoch 50"
		self.val = 50
		
	def ep3(self,instance):
		#self.lbl_e = "Epoch 100"
		self.val = 100
	
	def l1(self,instance):
		#self.lbl_e = "Epoch 10"
		self.val2 = 0.5

	def l2(self,instance):
		#self.lbl_e = "Epoch 50"
		self.val2 = 1.0
		
	def l3(self,instance):
		#self.lbl_e = "Epoch 100"
		self.val2 = 1.5
		
	def init(self,instance):
		self.train_x, self.train_y, self.test_x, self.test_y = load_data()
		self.lbl1.text = "Data initialized"
	
	def train(self,instance):	
		self.n_epochs = self.val 
		self.alpha = self.val2
		
		self.cost, self.acc, self.y_pred = runModel(self.train_x, self.train_y, self.test_x, self.test_y, self.n_epochs, self.alpha)
		self.lbl1.text = str(self.n_epochs) + " epochs executed."
		self.lbl2.text = "Model Trained"
		self.x_a = [i for i in range(self.acc.shape[0])]
		self.x_c = [i for i in range(len(self.cost))]
		self.accuracy = self.acc[self.n_epochs-1]
		
	def run(self,instance):
		self.lbl1.text = ""
		self.lbl2.text = ""
		self.lbl3.text = "Final prediction accuracy is: " + str(self.accuracy)
			
	def graph(self,instance):
		plt.subplot(221)
		plt.plot(self.x_c, self.cost)
		plt.subplot(222)
		plt.plot(self.x_a, self.acc)
		plt.show()

class App(App):
	def build(self):
		return Launch()
		
filename = "/home/txm/Documents/Simple-Neural-Network-master/nn2.py"
exec(compile(open(filename, "rb").read(), filename, 'exec'))

App().run()
