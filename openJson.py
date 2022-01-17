import json
import csv
import urllib.request, urllib.parse

class JsonData:

    def __init__(self,get_url):
        self.url = get_url
    
    def Get_Data(self):
        uh = urllib.request.urlopen(self.url)
        data = uh.read()
        info = json.loads(data)
        return info

    def upload_Data(self,x):
        with open('employee.csv', mode='w') as csv_file:
            fieldnames = ["userId", "id", "title","body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for item in x:
                for j,k in enumerate(item):
                    writer.writerow({k: item[k]})
        





url = "https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fjsonplaceholder.typicode.com%2Fposts&data=04%7C01%7Cgyan.agrahari%40infosys.com%7C78fb23f01a2f47a32e5408d9d989937a%7C63ce7d592f3e42cda8ccbe764cff5eb6%7C0%7C0%7C637780007170119648%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=%2Fob4JcJcCdbLS4szZZn44ti7Vv87X7VYnrWEMnQgrcY%3D&reserved=0"
p1 = JsonData(url)
data = p1.Get_Data()
p1.upload_Data(data)



