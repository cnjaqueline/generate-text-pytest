import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestExercise():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://127.0.0.1:5500/sample-exercise.html")
    self.driver.set_window_size(970, 555)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_generate_text(self):
    for i in range(3):
      self._generate_text()

  def _generate_text(self):
    self.driver.refresh()
    self.driver.find_element(By.NAME, "generate").click()
    wait = WebDriverWait(self.driver, 5)
    my_value_element = wait.until(
        expected_conditions.visibility_of_element_located((By.ID, "my-value"))
    )
    if my_value_element.text:
      generated_text = self.driver.find_element(By.ID, "my-value").text
      self.driver.find_element(By.ID, "input").clear()
      self.driver.find_element(By.ID, "input").send_keys(generated_text)
      self.driver.find_element(By.NAME, "button").click()
      alert = self.driver.switch_to.alert
      alert.accept()
      result = self.driver.find_element(By.ID, "result").text
      assert result == f"It workls! {generated_text}!"
      time.sleep(1)
