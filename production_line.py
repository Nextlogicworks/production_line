import requests

production_line_1 = {'ID':'L201','Planned Units':500,'Produced Units':490,'Defective Units':12}
production_line_2 = {'ID':'L202','Planned Units':450,'Produced Units':425,'Defective Units':22}
production_line_3 = {'ID':'L203','Planned Units':300,'Produced Units':300,'Defective Units':9}
production_line_4 = {'ID':'L204','Planned Units':400,'Produced Units':350,'Defective Units':7}
production_line_5 = {'ID':'L205','Planned Units':250,'Produced Units':0,'Defective Units':0}
production_line_6 = {'ID':'L206','Planned Units':600,'Produced Units':610,'Defective Units':31}


production_lines = [production_line_1,production_line_2,production_line_3,production_line_4,production_line_5,production_line_6]


def calculation(units,defects):
    good_units = units - defects
    if defects <= 0:
        defect_rate = 0
        defect_status = 'Stopped'

    else:
        defect_rate = ( defects / units ) * 100
        if defect_rate >= 5:
             defect_status = 'Check'
        else:
            defect_status = 'OK'

    return good_units,defect_rate,defect_status

def calculation_2(units,planned_units):
    units_behind = units - planned_units
    if units_behind > 0:
        units_behind_plan_status = 'Line Exceeded Plan'
        units_behind_plan = 0
    else:
        units_behind_plan_status = 'Line Behind Plan'
        units_behind_plan = units_behind

    return units_behind_plan_status,units_behind_plan

total_planned = 0
total_produced = 0
total_good = 0
total_defect = 0
highest_defect_rate = None
count_stopped = 0
count_stopped_id = 0
count_check = 0
count_check_id = 0
count_ok = 0
lines_behind_more_20 = 0


for product in production_lines:

    good_units,defect_rate,defect_status = calculation(product['Produced Units'],product['Defective Units'])

    units_behind_plan_status,units_behind_plan = calculation_2(good_units,product['Planned Units'])

    print('ID:',product['ID'],'\tGood Units:',good_units,' \tDefect Rate:',round(defect_rate,1),'\t Units Behind Plan:',units_behind_plan_status,'\t Defect Status:',defect_status)

    total_planned += product['Planned Units']

    total_produced += product['Produced Units']

    total_good += good_units

    total_defect += product['Defective Units']

    if defect_status == 'Check' or defect_status == 'OK':
       if highest_defect_rate is None or defect_rate > highest_defect_rate:
        highest_defect_rate = defect_rate

    if defect_status == 'Check':
        count_check += 1
        count_check_id = product['ID']


    if defect_status == 'OK':
        count_ok += 1

    if defect_status == 'Stopped':
        count_stopped += 1
        count_stopped_id = product['ID']

    if units_behind_plan > -20:
        lines_behind_more_20 = product['ID']


    print(units_behind_plan)


print('Total Planned Units:',total_planned)

print('Total Produced Units:',total_produced)

print('Total Good Units:',total_good)

print('Total Defect Units:',total_defect)

total_defect_rate = ( total_defect / total_produced ) * 100


print('Total Defect Rate:',round(total_defect_rate,1))

print('Highest Defect Rate:',round(highest_defect_rate,1))

print('Number of Lines Check:',count_check)

print('Number of Lines OK:',count_ok)

print('Number of Lines Stopped:',count_stopped)

print('\nSupervisor Attention:')

for product in production_lines:

    problems = []

    good_units,defect_rate,defect_status = calculation(product['Produced Units'],product['Defective Units'])

    units_behind_plan_status,units_behind_plan = calculation_2(good_units,product['Planned Units'])

    if defect_status == 'Check':
         problems.append('Check')
         count_check_id = product['ID']
        
        
    if defect_status == 'Stopped':
         problems.append('Stopped')
         count_stopped_id = product['ID']
         
         
    if units_behind_plan <= -20:
           problems.append('Behind Plan')
           lines_behind_more_20  = product['ID']

    if len(problems) > 0:

        print(product['ID'],problems)

webhook_09 = 'https://sert333.app.n8n.cloud/webhook/b2dc3a80-1460-4c8b-b14a-69e1656eccfb'

webhook_09_dashboard = 'https://sert333.app.n8n.cloud/webhook/4c31c1b6-430e-42c7-9d31-df52c4418c1a'

payload = { 'production_lines':production_lines  }

responds = requests.post(webhook_09,json=payload)

responds_dash = requests.post(webhook_09_dashboard,json=payload)









