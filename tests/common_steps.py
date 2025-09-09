from seleniumbase import BaseCase
import random
import os
class CommonSteps(BaseCase):
  
  def open_home_and_verify_page(self):
      self.open("https://automationexercise.com/")
      self.assert_element("//html")

  def click_signup_btn_and_verify_text(self):
      self.click("//a[@href='/login']")
      self.assert_text("New User Signup!")

  def click_login_btn_and_verify_text(self):
      self.click("//a[@href='/login']")
      self.assert_text("Login to your account", "//h2")    

  def input_name_email_click_signup_btn_and_verify_text(self):
      self.type("//input[@data-qa='signup-name']", "thutrang")
      self.type("//input[@data-qa='signup-email']", "test1124@yopmail.com")
      self.click("//button[@data-qa='signup-button']")
      self.assert_text("ENTER ACCOUNT INFORMATION", "//b")

  def input_name_existing_email_click_signup_btn_and_verify_text(self):
      self.type("//input[@data-qa='signup-name']", "thutrang")
      self.type("//input[@data-qa='signup-email']", "test5555@yopmail.com")
      self.click("//button[@data-qa='signup-button']")
      self.assert_text("Email Address already exist!")  

  def input_correct_email_password_click_login_btn_and_verify_text_tc2(self):
      self.type("//input[@data-qa='login-email']", "test852456@yopmail.com")
      self.type("//input[@data-qa='login-password']", "1")
      self.click("//button[@data-qa='login-button']")
      self.assert_element("//a[contains(text(),'Logged in as')]")

  def input_correct_email_password_click_login_btn_and_verify_text_tc3(self):
      self.type("//input[@data-qa='login-email']", "test3333@yopmail.com")
      self.type("//input[@data-qa='login-password']", "1")
      self.click("//button[@data-qa='login-button']")
      self.assert_element("//a[contains(text(),'Logged in as')]")    

  def input_incorrect_email_password_click_login_btn_and_verify_text(self):
      self.type("//input[@data-qa='login-email']", "test0807@yopmail.com")
      self.type("//input[@data-qa='login-password']", "1")
      self.click("//button[@data-qa='login-button']")
      self.assert_text("Your email or password is incorrect!")    

  def input_enter_account_information_and_verify_text(self):
      self.click("//input[@id='id_gender2']")
      self.type("//input[@id='password']", "1")
      self.select_option_by_value("//select[@id='days']", "5")
      self.select_option_by_value("//select[@id='months']", "3")
      self.select_option_by_value("//select[@id='years']", "2000")
      self.click("//input[@id='newsletter']")
      self.click("//input[@id='optin']")
      self.type("//input[@id='first_name']", "trang")
      self.type("//input[@id='last_name']", "thu")
      self.type("//input[@id='company']", "ABC cp")
      self.type("//input[@id='address1']", "ABC st1")
      self.type("//input[@id='address2']", "ABC st2")
      self.select_option_by_value("//select[@id='country']", "Australia")
      self.type("//input[@id='state']", "123 state")
      self.type("//input[@id='city']", "ABC city")
      self.type("//input[@id='zipcode']", "456")
      self.type("//input[@id='mobile_number']", "0912568989")
      self.click("//button[@type='submit']")
      self.assert_text("ACCOUNT CREATED!", "//b")

  def click_continue_btn_and_verify_text(self):
      self.click("//a[@data-qa='continue-button']")
      self.assert_element("//a[contains(text(),'Logged in as')]")

  def click_delete_btn_and_verify_text(self):
      self.click("//a[@href='/delete_account']")
      self.assert_text("ACCOUNT DELETED!", "b")    
      self.sleep(2)

  def click_logout_btn_and_verify_text(self):
      self.click("//a[@href='/logout']")
      self.assert_text("Login to your account", "//h2")    

  def click_contact_btn_verify_text_and_input_form_and_submit(self):
      self.click("//a[@href='/contact_us']")
      self.assert_text("GET IN TOUCH")

      self.type("//input[@name='name']", "1")
      self.type("//input[@name='email']", "abc@gmail.com")
      self.type("//input[@name='subject']", "abc@gmail.com")
      self.type("//textarea", "3")

      file_path = os.path.join(os.getcwd(), "tests", "resources", "1a6f030b-eb0f-49c3-849e-ea8bbc0dedc3.mp3")
      self.choose_file("//input[@name='upload_file']", file_path)

      self.sleep(2)
      self.click("//input[@name='submit']", timeout=10)
      self.sleep(2)
      self.click("//input[@name='submit']", timeout=10)
      self.sleep(2)
      self.click("//input[@name='submit']", timeout=10)
      self.click("//input[@name='submit']")
      self.accept_alert(timeout=5)
      self.sleep(200)
      self.assert_text("Success! Your details have been submitted successfully.","//div[@class='status alert alert-success']")   
      self.click("//a[@href='/']")
      self.assert_text("AutomationExercise")
  
  def click_testcase_btn_and_verify_text(self):
      self.click("//a[@href='/test_cases']")
      self.assert_text("Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:")

  def click_products_btn_and_verify_text(self):
      self.click("//a[@href='/products']")
      self.assert_text("ALL PRODUCTS")
      self.assert_element("//div[@class='features_items']")

  def click_view_product_and_verify_element(self):    
      self.click("//a[@href='/product_details/1']")
      self.assert_element("//div[@class='product-information']//h2") #name
      self.assert_element("//div[@class='product-information']//p[contains(text(),'Category:')]") #Category
      self.assert_element("//div[@class='product-information']//span/span")#price
      self.assert_element("//div[@class='product-information']//span/label")
      self.assert_element("//div[@class='product-information']//b[contains(text(),'Availability:')]")
      self.assert_element("//div[@class='product-information']//b[contains(text(),'Condition:')]")
      self.assert_element("//div[@class='product-information']//b[contains(text(),'Brand:')]")


  def search_product_and_verify_result(self):
      keyword = "Tshirt"

      # nhập từ khóa search
      self.type("//input[@id='search_product']", keyword)
      self.click("//button[@id='submit_search']")

      # verify text 'SEARCHED PRODUCTS'
      self.assert_text("SEARCHED PRODUCTS")

      # lấy danh sách kết quả
      product_names = self.find_elements("//div[@class='productinfo text-center']/p")
      assert len(product_names) > 0, "No products found for search!"

    # hàm chuẩn hóa text: bỏ khoảng trắng, dấu '-' và đưa về lowercase
  def normalize(text):
      return text.lower().replace("-", "").replace(" ", "")

    # verify từng sản phẩm trong kết quả chứa từ khóa
      for product in product_names:
          product_text = product.text
          assert normalize(keyword) in normalize(product_text), \
              f"Product '{product_text}' does not match search keyword '{keyword}'"

  def scroll_down_and_input_email_click_arrow_verify_text(self):
      self.scroll_to_bottom()
      self.type("//input[@id='susbscribe_email']", "test1225@yopmail.com")
      self.click("//button[@id='subscribe']")
      self.assert_text("You have been successfully subscribed!", timeout=5)

  def click_product_btn_add_product_and_view_cart(self):
      self.click("//a[@href='/products']")
      self.scroll_into_view("//img[@src='/get_product_picture/1']")
      self.hover("//img[@src='/get_product_picture/1']")
      self.click("//a[@data-product-id='1']")
      self.click("//button[@class='btn btn-success close-modal btn-block']")
      self.hover("//img[@src='/get_product_picture/2']")
      self.click("//a[@data-product-id='2']")
      self.click("//a[@href='/view_cart']")
      self.assert_element("//tr[@id='product-1']//p")
      self.assert_element("//tr[@id='product-1']//button")
      self.assert_element("//tr[@id='product-1']//p[@class='cart_total_price']")
      self.assert_element("//tr[@id='product-2']//p")
      self.assert_element("//tr[@id='product-2']//button")
      self.assert_element("//tr[@id='product-2']//p[@class='cart_total_price']")
  
  
      self.sleep(2)

  def view_product_verify_page_increase_quantity_add_cart_view_cart_verify_quantity(self):
      self.click("//a[@href='/product_details/1']")
      self.assert_text("WRITE YOUR REVIEW")
      self.clear("//input[@id='quantity']")
      self.type("//input[@id='quantity']", "4")
      self.click("//button[@type='button']")
      self.wait_for_element_visible("//div[@class='modal-content']", timeout=10)
      self.click("//a[@href='/view_cart']")
      self.sleep(3)
      self.assert_text("4", "//tr[@id='product-1']//button[@class='disabled']")

  def click_proceed_btn_and_register(self):
      self.click("//a[@class='btn btn-default check_out']")
      self.wait_for_element_visible("//div[@class='modal-content']", timeout=10)
      self.click("//a[@href='/login']")

  def click_cart_and_proceed_and_verify_text_input_comment_and_submit(self):
      self.click("//a[@href='/view_cart']")
      self.click("//a[@class='btn btn-default check_out']")
      self.assert_text("Address Details")
      self.assert_text("Review Your Order")
      self.type("//textarea[@name='message']", "abc")
      self.click("//a[@href='/payment']")

  def input_payment_detail_verify_text(self):
      self.type("//input[@name='name_on_card']", "1")
      self.type("//input[@name='card_number']", "1")
      self.type("//input[@name='cvc']", "1")
      self.type("//input[@name='expiry_month']", "1")
      self.type("//input[@name='expiry_year']", "1")
      self.click("//button[@id='submit']")
      # self.assert_text("Your order has been placed successfully!", "body") dang fix bug

  def add_product_and_view_cart(self):
      self.scroll_into_view("//img[@src='/get_product_picture/1']")
      self.hover("//img[@src='/get_product_picture/1']")
      self.click("//a[@data-product-id='1']")
      self.click("//button[@class='btn btn-success close-modal btn-block']")
      self.click("//a[@href='/view_cart']")
      self.sleep(5)

  def remove_product_in_cart_and_verify_element(self):
      self.click("//a[@class='cart_quantity_delete']")
      self.assert_element_absent("//img[@src='get_product_picture/1']/ancestor::tr")

  def verify_category_click_sub_menu_and_verify_text(self):
    self.assert_text("CATEGORY")
    self.click("//a[@href='#Women']")
    self.click("//a[@href='/category_products/1']")
    self.assert_text("WOMEN - DRESS PRODUCTS")
    self.click("//a[@href='#Men']")
    self.click("//a[@href='/category_products/3']")
    self.assert_text("MEN - TSHIRTS PRODUCTS")

  def click_brand_name_and_verify_element(self):
    self.click("//a[@href='/brand_products/Polo']")
    self.assert_element("//div[@class='features_items']")
    self.click("//a[@href='/brand_products/H&M']")
    self.assert_element("//div[@class='features_items']")

  def search_product_and_verify_result(self):
    keyword = "Tshirt"


    # nhập từ khóa search
    self.type("//input[@id='search_product']", keyword)
    self.click("//button[@id='submit_search']")


    # verify text 'SEARCHED PRODUCTS'
    self.assert_text("SEARCHED PRODUCTS")


    # lấy danh sách kết quả
    product_names = self.find_elements("//div[@class='productinfo text-center']/p")
    assert len(product_names) > 0, "No products found for search!"


    # hàm chuẩn hóa text: bỏ khoảng trắng, dấu '-' và đưa về lowercase
    def normalize(text):
        return text.lower().replace("-", "").replace(" ", "")


    # verify từng sản phẩm trong kết quả chứa từ khóa
    for product in product_names:
        product_text = product.text
        assert normalize(keyword) in normalize(product_text), \
            f"Product '{product_text}' does not match search keyword '{keyword}'"

  def add_tshirt_product_and_click_cart_and_verify_product(self):
      self.scroll_into_view("(//div[@class='productinfo text-center'])[1]")
      self.hover("(//div[@class='productinfo text-center'])[1]")
      self.click("//a[@data-product-id='2']")
      self.click("//button[@class='btn btn-success close-modal btn-block']")      
      self.hover("(//div[@class='productinfo text-center'])[2]")
      self.click("//a[@data-product-id='28']")
      self.click("//a[@href='/view_cart']")      
      self.assert_element("//img[@src='get_product_picture/28']")
      self.assert_element("//img[@src='get_product_picture/2']")     

  def click_view_cart_and_verify_element(self):
      self.click("//a[@href='/view_cart']")      
      self.assert_element("//img[@src='get_product_picture/28']")
      self.assert_element("//img[@src='get_product_picture/2']")
      
  def click_view_product_and_verify_text(self):
      self.click("//a[@href='/product_details/1']")
      self.assert_text("WRITE YOUR REVIEW")
      self.type("//input[@id='name']", "trang")
      self.type("//input[@id='email']", "test123@yopmai.com")
      self.type("//textarea[@id='review']", "abc")
      self.click("//button[@id='button-review']")
      self.assert_text("Thank you for your review.", timeout=5)    