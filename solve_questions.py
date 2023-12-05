# script to run selenium, load a website, read the text, convert it into equation and write the answer in the text box

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# open the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://arithmetic.zetamac.com/")
time.sleep(2)

# find the start button by xpath and click it
start_button = driver.find_element(By.XPATH, '//*[@id="welcome"]/form/input')
start_button.click()
time.sleep(2)


while True:
    # find the span field with class problem contaning the equation
    problem_text = str(driver.find_element(By.CLASS_NAME, 'problem').text)
    
    if "–" in problem_text:
        problem_text = problem_text.replace("–", "-")
    elif "÷" in problem_text:
        problem_text = problem_text.replace("÷", "//")
    elif "×" in problem_text:
        problem_text = problem_text.replace("×", "*")

    # convert the algebraic equation string to expression
    evaluation_answer = eval(problem_text)

    # find the input field and write the answer
    answer = driver.find_element(By.CLASS_NAME, 'answer')

    answer.send_keys(evaluation_answer)
    





