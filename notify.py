from plyer import notification
import datetime

def send_notification(title,message,duration=10,app_name="Noti: app"):
     notification.notify(title=title,message=message,timeout=duration,app_name=app_name)

if __name__ == "__main__":
    now = datetime.datetime.now()
    send_notification("Python Notificatioin",f"Notification sent at {now.strftime("%Y-%m-%d %H:%M:%S")}",10,"My app")