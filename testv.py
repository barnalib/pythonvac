import json
import requests
import json
import time
import http.client
from datetime import datetime, timedelta, date

def publish_text_message():
    # TODO implement
    TELEGRAM_API_HOST = "api.telegram.org"
    today=datetime.today().strftime('%d-%m-%Y')
    date1=(datetime.today()+timedelta(days=7)).strftime('%d-%m-%Y')
    date2=(datetime.today()+timedelta(days=14)).strftime('%d-%m-%Y')
    date3=(datetime.today()+timedelta(days=21)).strftime('%d-%m-%Y')
    date4=(datetime.today()+timedelta(days=28)).strftime('%d-%m-%Y')
    print(today)
    datelist=[today,date1,date2,date3,date4]
    #conn = http.client.HTTPSConnection(TELEGRAM_API_HOST)
    #telegram_token='1840280628:AAHGXd1OuwGtWNgSnDcLC0bnwsbKC8HtXKM'
    #chat_id = "-489649346"
    #url_req = "https://api.telegram.org/bot" + telegram_token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + 'ads' 
    #print(url_req)
    #results = requests.get(url_req)
    #print(results.json())
    
    centers=[]
    for date_ in datelist:
        link_='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date='+date_
        resp = requests.get(link_)
       # print(link_)
        ## print(resp.json()['centers'])
        print(resp)
        centers+=resp.json()['centers']
        #time.sleep(1)
    link_='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=700056&date='+date1
    resp = requests.get(link_)
    centers+=resp.json()['centers']
    link_='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=700056&date='+today
    resp = requests.get(link_)
    centers+=resp.json()['centers']    
    test_list=[]
    test_str=''
    for todo_item in centers:
       for session in todo_item['sessions']:
##          print(session['min_age_limit'],session['available_capacity'],session['vaccine'])
            if ((session['min_age_limit']==18) & (session['vaccine']=='COVAXIN') & (session['available_capacity']>=0) | (todo_item['pincode']=='700056')):      
                  ##print('{},{},{},{}\n'.format(session['date'],todo_item['name'],todo_item['pincode'],session['available_capacity']))
                  test_list +=['{},{},{},{}'.format(session['date'],todo_item['name'],todo_item['pincode'],session['available_capacity'])]
                  test_str+=(session['date']+' , '+todo_item['name']+' , '+str(todo_item['pincode'])+' , '+str(session['available_capacity'])+'\n')
                  #test_list += [session['date']+todo_item['name']+str(todo_item['pincode'])+str(session['available_capacity'])]
    if len(test_list):
        body="Report from today till "+date_ + "\n"+ test_str
        SENDER = "Barnali <spectrum.ju@gmail.com>"
        RECIPIENT = ["spectrum.ju@gmail.com"]
        print(RECIPIENT)
        conn = http.client.HTTPSConnection(TELEGRAM_API_HOST)
        telegram_token='1840280628:AAHGXd1OuwGtWNgSnDcLC0bnwsbKC8HtXKM'
        chat_id = "-489649346"
        print("hi")
        url_req = "https://api.telegram.org/bot" + telegram_token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" +  body
        results = requests.get(url_req)
        print(results.json())
    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        #AWS_REGION = "ap-south-1"
    # The subject line for the email.
        #SUBJECT = "IMP-Vac availability"
        #CHARSET = "UTF-8"
    # Create a new SES resource and specify a region.
        #client = boto3.client('ses',region_name=AWS_REGION)
        #phone_number="+918884555214"
        #publish_text_message(phone_number, body)
        #return
    # Try to send the email.
        #Provide the contents of the email.
        print(body)
        #response = client.send_email(
        #    Destination={
        #       'ToAddresses': RECIPIENT,
        #    },
        #    Message={
        #        'Body': {
        #            'Text': {
        #                'Charset': CHARSET,
        #                'Data': body,
        #            },
        #        },
        #        'Subject': {
        #            'Charset': CHARSET,
        #            'Data': SUBJECT,
        #        },
        #    },
        #    Source=SENDER,

        #)
    return {
        'statusCode': 200,
        'body': json.dumps(test_list)
    }
publish_text_message()    
