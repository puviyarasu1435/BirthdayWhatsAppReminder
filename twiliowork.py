import twilio
import datetime
from twilio.rest import Client 
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler
 
account_sid = '*******************************'# your account_sid form twilio 
auth_token = '*******************************' #  your auth_token from twilio
client = Client(account_sid, auth_token)
sched = BlockingScheduler()
def TwilioSend(massage):
    message = client.messages.create( 
                                from_='whatsapp:+1*********',  # twilio number 
                                body=massage,      
                                to='whatsapp:+91**********' #enter your twilio number
                            ) 
    
    print(message.sid)
    

class work():
    def __init__(self,B_date,massage):
        self.B_date=B_date
        self.massage=massage
    def reminder(self):
        print("set successfully")
        sched.add_job(TwilioSend, 'date', run_date=date(B_date.year, B_date.month, B_date.day), args=[massage])
        sched.start()

while True:
    print("1) add reminder\n2) exit \n")
    w=int(input())
    if w==1:
        print("------reminder-----\n Enter reminder name ")
        massage=input()
        print("Enter the date d/m/y\n")
        day, month, year=map(int,input().split('/'))
        print(date,month,year)
        B_date = datetime.date(year, month, day)
        user=work(B_date=B_date,massage=massage)
        user.reminder()
    else:
        break
print("-"*40)
