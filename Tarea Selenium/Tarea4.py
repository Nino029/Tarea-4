from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import webbrowser
from jinja2 import Environment, FileSystemLoader


    
driver = webdriver.Chrome()

driver.maximize_window()

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def iniciar_sesion():
    driver.get("https://www.netflix.com/login")
   
    driver.implicitly_wait(10)

    driver.save_screenshot("screenshots/Captura_iniciar_sesion.png")

    username_field = driver.find_element(By.NAME, "userLoginId")
    username_field.send_keys("motapichardo30@gmail.com")
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Alfonsa3071")
    driver.save_screenshot("screenshots/Captura_iniciar_sesion_Datos.png")
    password_field.submit()

  
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "profile-icon")))

   
    driver.save_screenshot("screenshots/Captura_perfiles.png")

    
    try:
        primer_perfil = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "profile-name")))
        primer_perfil.click()
    except Exception as e:
        print("No se pudo encontrar ningún perfil disponible:", e)

def Escoger_categoria():
   
    time.sleep(5)
    driver.save_screenshot("screenshots/Captura_pantalla_principal.png")
    
    try:
        link_series = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/browse/genre/83']")))
        link_series.click()
        
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "slider-item")))
        
        driver.save_screenshot("screenshots/Captura_navegar_categoria.png")
    except Exception as e:
        print("No se pudo navegar a la categoría 'Series':", e)

def reproducir_contenido():
    try:
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "slider-item")))
        
        preview_elements = driver.find_elements(By.CLASS_NAME, "slider-item")
       
        preview_elements[0].click()
       
        time.sleep(5)
        
        try:
            play_button = driver.find_element(By.CLASS_NAME, "primary-button")
            play_button.click()
            driver.save_screenshot("screenshots/Captura_Miniatura_Serie.png")
        except:
            pass
        
        time.sleep(10)
       
        driver.save_screenshot("screenshots/Captura_reproduciendo_serie.png")
        
        
        driver.get("https://www.netflix.com/browse")
       
        time.sleep(5)
    except Exception as e:
        print("No se pudo reproducir el contenido:", e)
        
        

def perfil_niños():
    try:

        boton_niños = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='nav-element show-kids']/a")))

        boton_niños.click()


        driver.save_screenshot("screenshots/Captura_perfil_niños.png")
    except Exception as e:
        print("No se pudo navegar al perfil de niños:", e)

        
try:
    iniciar_sesion()
    print("Prueba 1: y Prueba2:  completadas correctamente.")

    Escoger_categoria()
    print("Prueba 3: completada correctamente.")

    reproducir_contenido()
    print("Prueba 4: completada correctamente.")

    perfil_niños()
    print("Prueba 5: Completada Correctamente .")

except Exception as e:
    print("Error durante los pasos:", e)

  

resultadosReportes = {
    1: True,  #Inicio De Sesion
    2: True,  #Seleccionar Perfil
    3: True,  #Escoger Categoria
    4: True,  #Reproduccion De Serie
    5: True   #Cambiar Al Perfil de Niños
}



env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("Reportes/Informe-plantilla.html")
html_content = template.render(resultadosReportes=resultadosReportes)


with open("Reportes/Informe.html", "w") as file:
    file.write(html_content)

driver.quit()