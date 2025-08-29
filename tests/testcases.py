import pytest
from common_steps import CommonSteps
class Testcases(CommonSteps):

  @pytest.mark.tc1
  def test_tc1_register_user(self):
      self.open_home_and_verify_page()
      self.click_signup_btn_and_verify_text()
      self.input_name_email_click_signup_btn_and_verify_text()
      self.input_enter_account_information_and_verify_text()
      self.click_continue_btn_and_verify_text()
      self.click_delete_btn_and_verify_text()

# can set account da đăng kí thành công
  @pytest.mark.tc2
  def test_tc2_login_successful(self):
      self.open_home_and_verify_page()
      self.click_signup_btn_and_verify_text()
      self.click_login_btn_and_verify_text()
      self.input_correct_email_password_click_login_btn_and_verify_text_tc2()
      self.click_delete_btn_and_verify_text() 

  @pytest.mark.tc3
  def test_tc3_login_fail(self):
      self.open_home_and_verify_page()
      self.click_signup_btn_and_verify_text()
      self.click_login_btn_and_verify_text()
      self.input_incorrect_email_password_click_login_btn_and_verify_text()
  
  @pytest.mark.tc4
  def test_tc4_logout(self):
      self.open_home_and_verify_page()
      self.click_signup_btn_and_verify_text()
      self.click_login_btn_and_verify_text()
      self.input_correct_email_password_click_login_btn_and_verify_text_tc3()
      self.click_logout_btn_and_verify_text()

  @pytest.mark.tc5
  def test_tc5_reigister_existing_email(self):
      self.open_home_and_verify_page()
      self.click_signup_btn_and_verify_text()
      self.click_login_btn_and_verify_text()
      self.input_name_existing_email_click_signup_btn_and_verify_text()                

  @pytest.mark.tc6
  def test_tc6_contact_us_form(self):
      self.open_home_and_verify_page()
      self.click_contact_btn_verify_text_and_input_form_and_submit()

  @pytest.mark.tc7
  def test_tc7_verify_testcase_page(self):
      self.open_home_and_verify_page()
      self.click_testcase_btn_and_verify_text()

  @pytest.mark.tc8
  def test_tc8_verify_all_products_and_product_detail_page(self):
      self.open_home_and_verify_page()
      self.click_products_btn_and_verify_text()
      self.click_view_product_and_verify_element()
      self.sleep(2)

  @pytest.mark.tc9
  def test_tc9_search_product(self):
      self.open_home_and_verify_page()
      self.click_products_btn_and_verify_text()
      self.search_product_and_verify_result()
      self.sleep(2) 

  @pytest.mark.tc10
  def test_tc10_verify_subcription_homepage(self):
      self.open_home_and_verify_page()
      self.scroll_down_and_input_email_click_arrow_verify_text()
      self.sleep(2)

  @pytest.mark.tc12
  def test_tc12_add_product_in_cart(self):
      self.open_home_and_verify_page()
      self.click_product_btn_add_product_and_view_cart()

  @pytest.mark.tc13
  def test_tc13_verify_product_quantity_in_cart(self):
      self.open_home_and_verify_page()
      self.view_product_verify_page_increase_quantity_add_cart_view_cart_verify_quantity()

  @pytest.mark.tc14
  def test_tc14_place_order_register_while_check_out(self):
      self.open_home_and_verify_page()
      self.click_product_btn_add_product_and_view_cart()
      self.click_proceed_btn_and_register()
      self.input_name_email_click_signup_btn_and_verify_text()
      self.input_enter_account_information_and_verify_text()
      self.click_continue_btn_and_verify_text()
      self.click_cart_and_proceed_and_verify_text_input_comment_and_submit()
