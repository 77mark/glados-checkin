import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]
# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]
#'SCU89402Tf98b7f01ca3394b9ce9aa5e2ed1abbae5e6ca42796bb9'
# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]
#'__cfduid=d3459ec306384ca67a65170f8e2a5bd561593049467; _ga=GA1.2.766373509.1593049472; _gid=GA1.2.1338236108.1593049472; koa:sess=eyJ1c2VySWQiOjQxODMwLCJfZXhwaXJlIjoxNjE4OTY5NTI4MzY4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=6qG8SyMh_5KpSB6LBc9yRviaPvI'



def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
