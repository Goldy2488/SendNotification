from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="its time to take rest.so leave your task for a will",
            # app_icon="C:/Documents/python_projects/SendNotification",
            timeout=5)
        time.sleep(20)  

#pythonw file.p : for run without compaile
