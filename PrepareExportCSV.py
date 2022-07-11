import csv
import json
import os
from datetime import datetime
import requests

url = 'https://tagproject-api.sfedu.ru/api/v1/map/markers/export_markers_json'

response = requests.get(url)
markers_jsn = json.loads(response.content.decode())

DAILY_UPLOAD_FILE_ABSPATH = '/opt/rosambros/DailyUpload.csv'

m_e = []
for marker in markers_jsn:
    # response = requests.get(f'''https://nominatim.openstreetmap.org/reverse?lat={marker['gps'].split(',')[0].strip(' ')}&lon={marker['gps'].split(',')[1].strip(' ')}&format=json''')
    # jsn = json.loads(response.content.decode())
    # street = ''
    # street += str(jsn['address']['road'])
    # if 'house_number' in jsn['address']:
    #     street += ' ' + str(jsn['address']['house_number'])
    # dt_object = datetime.fromtimestamp(marker['created_on'].timestamp())
    # createdon = dt_object.strftime("%d.%m.%Y %H:%M:%S")
    # street = str(jsn['display_name'])
    street = marker['street']
    dt_object = datetime.strptime(marker['created_on'], "%Y-%m-%dT%H:%M:%S.%f%z")
    createdon = dt_object.strftime("%d.%m.%Y %H:%M:%S")
    marker_obj = {
        'street': street,
        'gps': marker['gps'],
        'created_on': createdon,
        'description': marker['description'],
    }
    m_e.append(marker_obj)

    with open(DAILY_UPLOAD_FILE_ABSPATH, 'w', newline='', encoding='utf-8-sig') as csv_file:
        # csv_file.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(csv_file, delimiter=';', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        header = ['Координаты', 'Улица', 'Дата и время', 'Описание']
        writer.writerow(header)
        for marker in m_e:
            writer.writerow([marker['gps'], marker['street'], marker['created_on'], marker['description']])
        csv_file.close()