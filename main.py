from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
class main(App):
    def build(self):
        global prmr;
        prmr=str()
        fl1=FloatLayout()
        btn1=Button(text='1',size_hint=(.25,.2),pos_hint={"center_x":.125,"center_y":.7})
        btn2=Button(text='2',size_hint=(.25,.2),pos_hint={"center_x":.375,"center_y":.7})
        btn3=Button(text='3',size_hint=(.25,.2),pos_hint={"center_x":.625,"center_y":.7})
        btn4=Button(text='4',size_hint=(.25,.2),pos_hint={"center_x":.125,"center_y":.5})
        btn5=Button(text='5',size_hint=(.25,.2),pos_hint={"center_x":.375,"center_y":.5})
        btn6=Button(text='6',size_hint=(.25,.2),pos_hint={"center_x":.625,"center_y":.5})
        btn7=Button(text='7',size_hint=(.25,.2),pos_hint={"center_x":.125,"center_y":.3})
        btn8=Button(text='8',size_hint=(.25,.2),pos_hint={"center_x":.375,"center_y":.3})
        btn9=Button(text='9',size_hint=(.25,.2),pos_hint={"center_x":.625,"center_y":.3})
        btn10=Button(text='0',size_hint=(.25,.2),pos_hint={"center_x":.375,"center_y":.1})
        bthcl=Button(text='<-',size_hint=(.25,.2),pos_hint={"center_x":.875,"center_y":.7})
        bthpls=Button(text='+',size_hint=(.25,.2),pos_hint={"center_x":.875,"center_y":.5})
        bthmuns=Button(text='-',size_hint=(.25,.2),pos_hint={"center_x":.875,"center_y":.3})
        bthumn=Button(text='*',size_hint=(.25,.2),pos_hint={"center_x":.875,"center_y":.1})
        bthpodl=Button(text='/',size_hint=(.25,.2),pos_hint={"center_x":.625,"center_y":.1})
        bthravno=Button(text='=',size_hint=(.25,.2),pos_hint={"center_x":.125,"center_y":.1})
        global lab1;
        lab1=Label(text=str(prmr),size_hint=(1,.2),pos_hint={"center_x":.5,"center_y":.9},font_size=39)
        fl1.add_widget(btn1)
        fl1.add_widget(btn2)
        fl1.add_widget(btn3)
        fl1.add_widget(btn4)
        fl1.add_widget(btn5)
        fl1.add_widget(btn6)
        fl1.add_widget(btn7)
        fl1.add_widget(btn8)
        fl1.add_widget(btn9)
        fl1.add_widget(btn10)
        fl1.add_widget(bthcl)
        fl1.add_widget(bthpls)
        fl1.add_widget(bthmuns)
        fl1.add_widget(bthumn)
        fl1.add_widget(bthpodl)
        fl1.add_widget(lab1)
        fl1.add_widget(bthravno)
        btn1.bind(on_press=self.b1)
        btn2.bind(on_press=self.b2)
        btn3.bind(on_press=self.b3)
        btn4.bind(on_press=self.b4)
        btn5.bind(on_press=self.b5)
        btn6.bind(on_press=self.b6)
        btn7.bind(on_press=self.b7)
        btn8.bind(on_press=self.b8)
        btn9.bind(on_press=self.b9)
        btn10.bind(on_press=self.b0)
        bthcl.bind(on_press=self.srez)
        bthpls.bind(on_press=self.plsz)
        bthmuns.bind(on_press=self.mins)
        bthpodl.bind(on_press=self.delt)
        bthumn.bind(on_press=self.umj)
        bthravno.bind(on_press=self.rovneet)
        return fl1
    def rovneet(self,instance):
        global prmr
        prmr=eval(str(prmr))
        lab1.text=str(prmr)
    def umj(self,instance):
        global prmr
        prmr=str(prmr)+'*'
        lab1.text=str(prmr)
    def delt(self,instance):
        global prmr
        prmr=str(prmr)+'/'
        lab1.text=str(prmr)
    def mins(self,instance):
        global prmr
        prmr=str(prmr)+'-'
        lab1.text=str(prmr)
    def plsz(self,instance):
        global prmr;
        prmr=str(prmr)+'+'
        lab1.text=str(prmr)
    def srez(self,instance):
        global prmr;
        prmr=str(prmr)[:-1]
        lab1.text=str(prmr)
    def b1(self,instance):
        global prmr;
        prmr=prmr+str('1')
        lab1.text=str(prmr)
    def b2(self,instance):
        global prmr;
        prmr=prmr+str('2')
        lab1.text=str(prmr)
    def b3(self,instance):
        global prmr;
        prmr=prmr+str('3')
        lab1.text=str(prmr)
    def b4(self,instance):
        global prmr;
        prmr=prmr+str('4')
        lab1.text=str(prmr)
    def b5(self,instance):
        global prmr;
        prmr=prmr+str('5')
        lab1.text=str(prmr)
    def b6(self,instance):
        global prmr;
        prmr=prmr+str('6')
        lab1.text=str(prmr)
    def b7(self,instance):
        global prmr;
        prmr=prmr+str('7')
        lab1.text=str(prmr)
    def b8(self,instance):
        global prmr;
        prmr=prmr+str('8')
        lab1.text=str(prmr)
    def b9(self,instance):
        global prmr;
        prmr=prmr+str('9')
        lab1.text=str(prmr)
    def b0(self,instance):
        global prmr;
        prmr=prmr+str('0')
        lab1.text=str(prmr)
if __name__=='__main__':
    main().run()