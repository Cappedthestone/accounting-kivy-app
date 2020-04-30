import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from database import DataBase



Builder.load_file('my.kv')

class DataErrorPopup(Popup):
    def dismiss_popup(self):
        self.dismiss()

class SignInPage(Screen):
    Config.set('graphics', 'width', '1000')
    Config.set('graphics', 'height', '1000')
    
    def validate_user(self):
        username = ObjectProperty(None)
        password = ObjectProperty(None)
        information = self.ids.info

    
        if (self.username.text == "cat" or self.password.text == 1):
            InventoryPage.current = self.username.text
            self.reset()
            scrn_manager.current = "InventoryPage"
        else:
            information.text = '[color=#000000]Please enter both the username and/or password.[/color]'

    def reset(self):
        self.username.text = ""
        self.password.text = ""

    
class InventoryPage(Screen):

    def DeleteRow1(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs1)
    
    def DeleteRow2(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs2)
        
    def DeleteRow3(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs3)

    def DeleteRow4(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs4)

    def DeleteRow5(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs5)

    def DeleteRow6(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs6)

    def DeleteRow7(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs7)

    def DeleteRow8(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs8)

    def DeleteRow9(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs9)

    def DeleteRow10(self):
        self.ids.product_details.remove_widget(self.ids.product_inputs10)    

    def validate_data(self):
        try:
            quantity1 = self.ids.qty_inp1.text
            quantity2 = self.ids.qty_inp2.text
            quantity3 = self.ids.qty_inp3.text
            quantity4 = self.ids.qty_inp4.text
            quantity5 = self.ids.qty_inp5.text
            quantity6 = self.ids.qty_inp6.text
            quantity7 = self.ids.qty_inp7.text
            quantity8 = self.ids.qty_inp8.text
            quantity9 = self.ids.qty_inp9.text
            quantity10 = self.ids.qty_inp10.text

            name1 = self.ids.name_inp1.text
            name2 = self.ids.name_inp2.text
            name3 = self.ids.name_inp3.text
            name4 = self.ids.name_inp4.text
            name5 = self.ids.name_inp5.text
            name6 = self.ids.name_inp6.text
            name7 = self.ids.name_inp7.text
            name8 = self.ids.name_inp8.text
            name9 = self.ids.name_inp9.text
            name10 = self.ids.name_inp10.text

            stock1 = self.ids.stock_inp1.text
            stock2 = self.ids.stock_inp2.text
            stock3 = self.ids.stock_inp3.text
            stock4 = self.ids.stock_inp4.text
            stock5 = self.ids.stock_inp5.text
            stock6 = self.ids.stock_inp6.text
            stock7 = self.ids.stock_inp7.text
            stock8 = self.ids.stock_inp8.text
            stock9 = self.ids.stock_inp9.text
            stock10 = self.ids.stock_inp10.text

            price1 = self.ids.price_inp1.text
            price2 = self.ids.price_inp2.text
            price3 = self.ids.price_inp3.text
            price4 = self.ids.price_inp4.text
            price5 = self.ids.price_inp5.text
            price6 = self.ids.price_inp6.text
            price7 = self.ids.price_inp7.text
            price8 = self.ids.price_inp8.text
            price9 = self.ids.price_inp9.text
            price10 = self.ids.price_inp10.text

            qty1 = int(quantity1)
            qty2 = int(quantity2)
            qty3 = int(quantity3)
            qty4 = int(quantity4)
            qty5 = int(quantity5)
            qty6 = int(quantity6)
            qty7 = int(quantity7)
            qty8 = int(quantity8)
            qty9 = int(quantity9)
            qty10 = int(quantity10)

            nme1 = str(name1)
            nme2 = str(name2)
            nme3 = str(name3)
            nme4 = str(name4)
            nme5 = str(name5)
            nme6 = str(name6)
            nme7 = str(name7)
            nme8 = str(name8)
            nme9 = str(name9)
            nme10 = str(name10)

            inventory1 = int(stock1)
            inventory2 = int(stock2)
            inventory3 = int(stock3)
            inventory4 = int(stock4)
            inventory5 = int(stock5)
            inventory6 = int(stock6)
            inventory7 = int(stock7)
            inventory8 = int(stock8)
            inventory9 = int(stock9)
            inventory10 = int(stock10)

            cost1 = float(price1)
            cost2 = float(price2)
            cost3 = float(price3)
            cost4 = float(price4)
            cost5 = float(price5)
            cost6 = float(price6)
            cost7 = float(price7)
            cost8 = float(price8)
            cost9 = float(price9)
            cost10 = float(price10)   
                
            if  type(qty1) == int or type(qty2) == int or type(qty3) == int or type(qty4) == int or type(qty5) == int or \
                type(qty6) == int or type(qty7) == int or type(qty8) == int or type(qty9) == int or type(qty10) == int or \
                type(nme1) == str or type(nme2) == str or type(nme3) == str or type(nme4) == str or type(nme5) == str or \
                type(nme6) == str or type(nme7) == str or type(nme8) == str or type(nme9) == str or type(nme10) == str or \
                type(inventory1) == int or type(inventory2) == int or type(inventory3) == int or type(inventory4) == int or\
                type(inventory5) == int or type(inventory6) == int or type(inventory7) == int or type(inventory8) == int or\
                type(inventory9) == int or type(inventory10) == int or type(cost1) == float or type(cost2) == float or\
                type(cost3) == float or type(cost4) == float or type(cost5) == float or type(cost6) == float or type(cost7) == float or\
                type(cost7) == float or type(cost8) == float or type(cost9) == float or  type(cost10) == float: 

                var1 = "stotal_inp1"   
                totalcost1 = inventory1 * cost1
                floatTotalscost1 = float(totalcost1)
                ffTotalcost1 = "${:.2f}".format(floatTotalscost1)
                self.ids[var1].text = ffTotalcost1

                var2 = "stotal_inp2" 
                totalcost2 = inventory2 * cost2   
                floatTotalscost2 = float(totalcost2)
                ffTotalcost2 = "${:.2f}".format(floatTotalscost2)
                self.ids[var2].text = ffTotalcost2

                var3 = "stotal_inp3" 
                totalcost3 = inventory3 * cost3   
                floatTotalscost3 = float(totalcost3)
                ffTotalcost3 = "${:.2f}".format(floatTotalscost3)
                self.ids[var3].text = ffTotalcost3

                var4 = "stotal_inp4" 
                totalcost4 = inventory4 * cost4   
                floatTotalscost4 = float(totalcost4)
                ffTotalcost4 = "${:.2f}".format(floatTotalscost4)
                self.ids[var4].text = ffTotalcost4
                
                var5 = "stotal_inp5" 
                totalcost5 = inventory5 * cost5   
                floatTotalscost5 = float(totalcost5)
                ffTotalcost5 = "${:.2f}".format(floatTotalscost5)
                self.ids[var5].text = ffTotalcost5

                var6 = "stotal_inp6" 
                totalcost6 = inventory6 * cost6   
                floatTotalscost6 = float(totalcost6)
                ffTotalcost6 = "${:.2f}".format(floatTotalscost6)
                self.ids[var6].text = ffTotalcost6

                var7 = "stotal_inp7" 
                totalcost7 = inventory7 * cost7   
                floatTotalscost7 = float(totalcost7)
                ffTotalcost7 = "${:.2f}".format(floatTotalscost7)
                self.ids[var7].text = ffTotalcost7

                var8 = "stotal_inp8" 
                totalcost8 = inventory8 * cost8  
                floatTotalscost8 = float(totalcost8)
                ffTotalcost8 = "${:.2f}".format(floatTotalscost8)
                self.ids[var8].text = ffTotalcost8

                var9 = "stotal_inp9" 
                totalcost9 = inventory9 * cost9   
                floatTotalscost9 = float(totalcost9)
                ffTotalcost9 = "${:.2f}".format(floatTotalscost9)
                self.ids[var9].text = ffTotalcost9

                var10 = "stotal_inp10" 
                totalcost10 = inventory10 * cost10   
                floatTotalscost10 = float(totalcost10)
                ffTotalcost10 = "${:.2f}".format(floatTotalscost10)
                self.ids[var10].text = ffTotalcost10

            

                allMerchantCost = floatTotalscost1 + floatTotalscost2 + floatTotalscost3 + floatTotalscost4 + floatTotalscost5 + floatTotalscost6 + floatTotalscost7 + floatTotalscost8 + floatTotalscost9 + floatTotalscost10

                formatedAllMerchantCost = "{:.2f}".format(allMerchantCost)

                stringAllMerchantCost = str(formatedAllMerchantCost)

                tcost = self.ids.cost

                tcost.text = '[color=#000000]All total costs combined $' + stringAllMerchantCost + '[/color]'   

        except:
            DataError_Popup()         

def DataError_Popup():
     DataError_Popup = DataErrorPopup(title="Data inputted incorrectly", size_hint=(None,None),size=(400,400)) 
     DataError_Popup.open()            


class WindowManager(ScreenManager):  
    pass

scrn_manager = WindowManager()
db = DataBase("logins.txt")


scrn_manager = WindowManager()

screens = [SignInPage(name="SignInPage"), InventoryPage(name="InventoryPage")]
for screen in screens:
    scrn_manager.add_widget(screen)

scrn_manager.current = "SignInPage"


class SigninApp(App):
    def build(self):
        return scrn_manager

if __name__=="__main__":
    SigninApp().run()
