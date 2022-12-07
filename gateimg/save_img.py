import requests
from datetime import datetime
import threading

def save_img_by_name(name):
    if name % 100 == 0:
        print(name)
    img_url = f"https://jksb.v.zzu.edu.cn/imagesss/title316_{name}.png"
    r = requests.get(img_url)
    if r.status_code !=200:
        return
    print(img_url)
    m_time_str= r.headers['Last-Modified'][5:-4]
    m_time = datetime.strptime(m_time_str, '%d %b %Y %H:%M:%S')
    img_name = str(name) + '_' + m_time.strftime('%Y%m%d_%H%M%S') + '.png'
    with open(img_name, 'wb') as handler:
        handler.write(r.content)


class myThread(threading.Thread):
   def __init__(self, tid):
      threading.Thread.__init__(self)
      self.tid= tid

   def run(self):
    for i in range(self.tid*10000, (self.tid+1)*10000):
        save_img_by_name(i)
        


threads = []
for i in range(1, 10):
    t = myThread(i)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print("all threads done!!!")

