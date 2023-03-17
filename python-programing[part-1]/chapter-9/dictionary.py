# python3 chapter-9/dictionary.py

marks = {'DH1001': {'Bangla': 68, 'English': 90}, 'DH1002': {'Bangla': 98, 'English': 97}}
print(marks['DH1001']['English'])

bd_division_info = {}

bd_division_info['Barisal'] = {'districts': 6, 'upazilas': 42 , 'union': 333}
bd_division_info['Chittagong'] = {'districts': 11, 'upazilas': 103, 'union': 949}
bd_division_info['Dhaka'] = {'districts': 13, 'upazilas': 88, 'union': 1248}
bd_division_info['Khulna'] = {'districts': 10, 'upazilas': 59, 'union': 270}
bd_division_info['Mymensingh'] = {'districts': 4, 'upazilas': 35, 'union': 350}
bd_division_info['Rajshahi'] = {'districts': 8, 'upazilas': 67, 'union': 558}
bd_division_info['Rangpur'] = {'districts': 8, 'upazilas': 58, 'union': 536}
bd_division_info['Sylhet'] = {'districts': 4, 'upazilas': 40, 'union': 334}

print(bd_division_info['Dhaka'])

divisions = bd_division_info.keys()
print(divisions)

for division in divisions:
    print('Division - ', division, bd_division_info[division]['upazilas'])

for key in bd_division_info:
    print(key)
    print(bd_division_info[key])

for key, value in bd_division_info.items():
    print(key)
    print(value)

# calculate districts, upazilas, union
districts = 0
upazilas = 0
union = 0
for division in divisions:
    districts = districts +  bd_division_info[division]['districts']
    upazilas = upazilas + bd_division_info[division]['upazilas']
    union = union + bd_division_info[division]['union']

print('total-districts', districts)
print('total-upazilas', upazilas)
print('total-union', union)