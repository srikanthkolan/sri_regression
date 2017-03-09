from selenium import webdriver
import time
import unittest


locators = {
    'button': "//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]"

}

class regressionclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def negative_testing(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://gatwick.stage.otrl.io")
        driver.find_element_by_xpath(locators['button']).click()
        #        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]").click()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("srikanth.kolan@ontrackretail.co.uk")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("London")
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(3)
        error = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/section/div/div/div[3]/p").text

#        assert "Log in failed. Please check your details and try again" in error
        try:
            assert "Log in failed. Please cils and try again" in error
        except:
            pass
        print("test past")

    def test_gatwick_ticket_week(self):

        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the page >
        driver.get("https://gatwick.stage.otrl.io")
        #<Result 1:  page is opened >

        #<Step 2: Login page >
        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]").click()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("srikanth.kolan@ontrackretail.co.uk")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("Londonbridge")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        #<Result 2: logged in succesfully >
        time.sleep(2)
        #<Step 3:Journey Selection London victoria to Gatwick>
        driver.find_element_by_xpath("//*[@id='journey']/option[3]").click()
        time.sleep(2)
        #<Result 3:Journey selected>

        #<Step 4: outbond journey >
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[1]/div/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rw_1_calendar__month_2-14']/span").click()
        time.sleep(2)
        driver.find_element_by_xpath(("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[2]/button")).click()
        time.sleep(2)
        #<Result 4:outbond journey selected>

        #<Step 5:Return journey>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[2]/div/div[1]/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rw_3_calendar__month_2-21']/span").click()
        time.sleep(2)
        #<Result 5:Return journey selected>

        #<Step 6:Add passengers & Find trains>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/section/div[1]/div/div[1]/div/button[2]/i").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        #<Result 6:Passengers added >

        #<Step 7:click on find train button>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/footer/button").click()
        time.sleep(2)
        #<Result 7:train times are displayed>

        #<Step 8:select train for outbound journey>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[2]/div/div[1]/div[2]/div/button").click()
        time.sleep(2)
        #<Result 8:Outbound train selected>

        #<Step 9:Select ticket and click on continue button in a pop up >
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(2)
        #<Result 9: Ticket selected and continue>

        #<Step 10:Select train for return journey>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[2]/div/div[1]/div[2]/div/button").click()
        time.sleep(2)
        #<Result 10:Return journey selected>

        #<Step 11:click on continue button to ticket collection page>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(2)
        #<Result 11: Ticket collection page is opened>

        #<Step 12:Select collect ticket from station>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[2]/div/label/span").click()
        time.sleep(2)
        #<Result 12: Collect ticket from station selected>


        #<Step 13: click payment details button >
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        #<Result 13: Payment option displayed>

        time.sleep(2)
       #<Step 14:Se lect payment method as card payment/evoucher>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[2]/div/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div[1]/div[3]/div/div/label/span").click()
        #<Result 14:Payment method selected

        #<Step 15: click on the use existing card>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div/div[2]/div[1]/div/div/label/span").click()
        #<Result 15: unticks the use existing card>

        time.sleep(4)


        #<Step 16:Enter the card details>
        driver.find_element_by_xpath("//*[@id='cardHolderName']").send_keys("Srikanth Kolan")
        driver.find_element_by_xpath("//*[@id='cardNumber']").send_keys("9902000000005132")
        driver.find_element_by_xpath("//*[@id='expiryMonth']/option[13]").click()
        driver.find_element_by_xpath("//*[@id='expiryYear']/option[5]").click()
        driver.find_element_by_xpath("//*[@id='cvv']").send_keys(123)
        time.sleep(2)

        #<Result 16: Card details eneterd>

        #<Step 17:Click on save the card details for future payments>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div/div[2]/div[3]/div/div/label/span").click
        #<Result 17:optuon selected to save the card details>

        #<Step 18:Enter address>
        driver.find_element_by_xpath("//*[@id='addressline1']").send_keys("30 Great Guildford street")
        driver.find_element_by_xpath("//*[@id='towncity']").send_keys("London")
        driver.find_element_by_xpath("//*[@id='postcode']").send_keys("SE1 0HS")
        time.sleep(2)
        #<Result 18:Address entered>

        #<Step 19:Click on pay button>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        #<Result 19:Payment gateway opens>
        time.sleep(5)
        #<Step 20:Autorise payment>
        driver.switch_to.frame(driver.find_element_by_name("iframe"))
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='submitForm']/div[1]/input[1]").click()
        time.sleep(4)
        text=driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section/div/div[1]/div/div/p[1]").text
        try:
            assert "Your payment was successful" in text
        except:
            pass


    def test_gw_ba_ticket_nextday(self):

        driver =self.driver
        driver.maximize_window()

        #<Step 1: open the page >
        driver.get("https://gatwick-ba.stage.otrl.io")
        #<Result 1:  page is opened >

        #<Step 2: Login page >
        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]").click()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("srikanth.kolan@ontrackretail.co.uk")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("Londonbridge")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        #<Result 2: logged in succesfully >
        time.sleep(2)

        #<Step 3:Journey Selection Gatwick to victoria>
        driver.find_element_by_xpath("//*[@id='journey']/option[2]").click()
        time.sleep(4)
        #<Result 3:Journey selected>

         #<Step 4: outbond journey >
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section[2]/div/div[1]/div/div[1]/button[2]").click()
        #<Result 4:outbond journey selected>

        #<Step 5: click on find train button>
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/footer/button").click()
        #<Result 5:train times are displayed>
        time.sleep(4)

        #<Step 6: Select ticket and click on continue button in a pop up >
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/div/div/ul/li[2]/div/div[1]/div[2]/div/button").click()

        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div[2]/div/ul/li/label/div[2]/div/span[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(6)
        #<Result 6:Ticket selected and continue to ticket collection page>

        #<Step 7:Select ticket collection preferencess>
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section/div[1]/div/label/span/span").click()
        #<Result 7:Eticket selected>

        #<Step 8: click payment details button >
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[3]/div[2]/button").click()
        #<Result 8: Payment option displayed>
        time.sleep(2)
        #<Step 9:Select payment method as card payment>
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section/div/form/div/div[2]/div/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[3]/div[1]/div[3]/div/div/label/span").click()
        time.sleep(2)
        #<Result 9:Payment method selected

        #<Step 10:existing card is selected and enter cvv>
        driver.find_element_by_xpath("//*[@id='cvv']").send_keys(123)
        time.sleep(2)
        #<Result 10: card selected and cvv details are entered>

        #<Step 11:Click on pay button>
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(2)

        driver.switch_to.frame(driver.find_element_by_name("iframe"))
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='submitForm']/div[1]/input[1]").click()
        time.sleep(4)
        text=driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section/div/div[1]/div/div/p[1]").text
        try:
            assert "Your payment was successful" in text
        except:
            pass

    def test_gw_ryanair_ticket_nextday(self):
        driver =self.driver
        driver.maximize_window()

        #<Step 1: open the page >
        driver.get("https://gatwick-ryanair.stage.otrl.io")
        #<Result 1:  page is opened >

        time.sleep(2)
        #<Step 2:Journey Selection London victoria to Gatwick>
        driver.find_element_by_xpath("//*[@id='journey']/option[3]").click()
        time.sleep(2)
        #<Result 2:Journey selected>

        #<Step 3: outbond journey >
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section[2]/div/div[1]/div/div[1]/button[2]").click()
        #<Result 3:outbond journey selected>

        #<Step 4: Add passengers and click on find train button>
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section[3]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/section/div[1]/div/div[2]/div/button[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/footer/button").click()
        #<Result 4:train times are displayed>
        time.sleep(4)

        #<Step 5: Select ticket and click on continue button in a pop up >
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/div/div/ul/li[2]/div/div[1]/div[2]/div/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(4)
        #<Result 5:Ticket selected and continue to ticket collection page>

        #<Step 6:Select ticket collection preferencess>
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[1]/section/div[2]/div/label/span").click()
        #<Result 6:Eticket selected>


        #<Step 7: click payment details button >
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[3]/div[2]/button").click()
        #<Result 7: Payment option displayed>
        time.sleep(4)

        #<Step 8:Select payment method as paypaland click on pay>
        driver.find_element_by_xpath(" //*[@id='paypal-container']/div/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div[2]/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(10)
        #<Result 9:Payment method selected
        driver.switch_to.default_content


        driver.find_element_by_xpath("//*[@id='email']").send_keys("gamita.patel@otrl.io")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("testtest")
        driver.find_element_by_xpath("//*[@id='btnLogin']").click()
        time.sleep(2)


    def test_gw_ej_ticket_weekrtn(self):
        driver = self.driver
        driver.maximize_window()
       #<Step 1: open the page >
        driver.get("https://gatwick-easyjet.stage.otrl.io/search")
       #<Result 1:  page is opened >

       #<Step 2: Login page >
        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]").click()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("srikanth.kolan@ontrackretail.co.uk")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("Londonbridge")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        #<Result 2: logged in succesfully >
        time.sleep(2)
       #<Step 3:Journey Selection London victoria to Gatwick>
        driver.find_element_by_xpath("//*[@id='journey']/option[3]").click()
        time.sleep(2)
       #<Result 3:Journey selected>

        #<Step 4: outbond journey >
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[1]/div/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rw_1_calendar__month_2-14']/span").click()
        time.sleep(2)
        driver.find_element_by_xpath(("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[2]/button")).click()
        time.sleep(2)
        #<Result 4:outbond journey selected>

        #<Step 5:Return journey>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/div[2]/div/div[1]/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rw_3_calendar__month_2-14']/span").click()
        time.sleep(2)
       #<Result 5:Return journey selected>

        ##<Step 6:Add passengers & Find trains>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(4)
        #<Result 6:Passengers added >

        #<Step 7:click on find train button>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/footer/button").click()
        time.sleep(4)
        #<Result 7:train times are displayed>

        #<Step 8:select train for outbound journey>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div/ul/li[2]/div/div[1]/div[2]/div/button").click()
        time.sleep(4)
       #<Result 8:Outbound train selected>

        #<Step 9:Select first class ticket and click on continue button in a pop up >
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[2]/label/div[2]/div/span[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(2)
        #<Result 9: Ticket selected and continue>

        #<Step 10:Select train for return journey>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div/ul/li[2]/div/div[1]/div[2]/div/button").click()
        time.sleep(2)
        #<Result 10:Return journey selected>

        #<Step 11:click on continue button to ticket collection page>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(4)
        #<Result 11: Ticket collection page is opened>

        #<Step 12:Select collect ticket from station>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[2]/div[1]/label/span/span/span[1]").click()
        time.sleep(2)
        #<Result 12: Collect ticket from station selected>

        #<Step 13: click payment details button >
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        time.sleep(2)
        #<Result 13: Payment option displayed>

        #<Step 14:Se lect payment method as card payment/evoucher>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div/form/div/div[2]/div/span").click()
        #<Result 14:Payment method selected

        #<Step 15:Pay by using evouchers preselected>

        #<Result 19:Payment gateway opens>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(4)
        #<Result 19:payment successful>


        try:
         assert "Your payment was successful" in text
        except:
                pass



    def test_gw_reg(self):
        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the page >
        driver.get("https://gatwick.stage.otrl.io/search")
        #<Result 1:  page is opened >

        #<Step 2: click on register>
        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[2]").click()
        time.sleep(2)
        #<Result 2: register form is open >

        #<Step 3: fill the form>
        driver.find_element_by_xpath("//*[@id='title']/option[1]").click
        driver.find_element_by_xpath("//*[@id='firstName']").send_keys("test")
        driver.find_element_by_xpath("//*[@id='surname']").send_keys("soco")
        driver.find_element_by_xpath("//*[@id='email']").send_keys("testsoco6+28@gmail.com")
        driver.find_element_by_xpath("//*[@id='confirmemail']").send_keys("")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("testtest")
        driver.find_element_by_xpath("//*[@id='confirmPassword']").send_keys("testtest")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/section/div/div/div[2]/div/div[1]/div/div/div/label/span").click()
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()




    def test_se_ticket_month (self):
        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the page >
        driver.get("https://southeastern.stage.otrl.io")
        #<Result 1:  page is opened >

        #<Step 2:click on season tickets tab>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/nav/a[2]").click()
        time.sleep(2)
        #<Result 2: season ticket tab is open>


        #<Step 3:enter station details>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[1]/label/div/input").send_keys("Canterbury")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[3]/label/div/input").send_keys("London Terminals")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/label[1]/span").click()
        #<Result 3: station details entered>

        #<Step 4:Select start date as next week>
        driver.find_element_by_xpath("//*[@id='loadDateSelect']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rw_3_calendar__month_2-16']/span").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(2)
        #<Result 4: date selected>

        #<Step 5:Select monthly and unticket other boxes>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/div[2]/div/div/div[1]/div/div/label/span").click()
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/div[2]/div/div/div[3]/div/div/label/span").click()
        time.sleep(2)
        #<Result 5: Monthly selected>

        #<Step 6:Click on show tickets>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/footer/button").click()
        time.sleep(4)
        #<Result 6: Navigates to the ticket page>

        #<Step 7:Select std ticket and click on continue>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[1]/label/div").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        #<Result 7: Ticket selected >

        #<Step 8:Enter photo card details and continue>
        driver.find_element_by_xpath("//*[@id='name']").send_keys("Smith qa")
        driver.find_element_by_xpath("//*[@id='number']").send_keys("9865")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(4)
        #<Result 8:photo card details entered>

        #<Step 9:collection preferences 1st class ccst>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[2]/div/label/span").click()
        driver.find_element_by_xpath("//*[@id='contactName']").send_keys("Smith")
        driver.find_element_by_xpath("//*[@id='addressline1']").send_keys("30")
        driver.find_element_by_xpath("//*[@id='addressline2']").send_keys("Great Guildford Street")
        driver.find_element_by_xpath("//*[@id='towncity']").send_keys("London")
        driver.find_element_by_xpath("//*[@id='postcode']").send_keys("SE1 0HS")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button").click()
        time.sleep(2)
        #<Result 9:1st class selected and address eneterd>

        #<Step 10:Payment details>
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='paypal-container']/div/span").click()
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()

        handles = driver.window_handles
        driver.switch_to_window(handles.pop())
        time.sleep(15)
        driver.find_element_by_xpath("//*[@id='email']").send_keys("gamita.patel@otrl.io")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("testtest")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='btnLogin']").click()



    def test_se_ticket_week (self):
        driver = self.driver
        driver.maximize_window()
        #<Step 1: open the page >
        driver.get("https://southeastern.stage.otrl.io")
        #<Result 1:  page is opened >

        #<Step 2:Click on login>
        driver.find_element_by_xpath("//*[@id='container']/div/div/header/nav[2]/ul/li[2]/button[1]").click()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("srikanth.kolan@ontrackretail.co.uk")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("Londonbridge")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(2)
        #<Result 2:Logged in succesfully>

        #<Step 3:click on season tickets tab>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/nav/a[2]").click()
        time.sleep(2)
        #<Result 3: season ticket tab is open>

        #<Step 4:enter station details>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[1]/label/div/input").send_keys("Deal")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[3]/label/div/input").send_keys("Hastings")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[2]/div/label[2]/span").click()
        #<Result 4: station details entered>

        #<Step 5:Select start date tomorrow>
        driver.find_element_by_xpath("//*[@id='loadDateSelect']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='rw_23_calendar__month_2-10']/span").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(2)
        #<Result 5: date selected>

        #<Step 6:Select weekly and unticket other boxes>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/div[2]/div/div/div[3]/div/div/label/span").click()
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/div[2]/div/div/div[2]/div/div/label/span").click()
        time.sleep(2)
        #<Result 6: Monthly selected>

        #<Step 7:Click on show tickets>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/footer/button").click()
        time.sleep(4)
        #<Result 7: Navigates to the ticket page>

























def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

