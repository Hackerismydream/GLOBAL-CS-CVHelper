from application.detail import DETAIL
name_map = {
    "Cambridge ACS": 1,
    "ETH MSCS": 2,
    "Cambridge MLMI": 3,
    "EPFL MSCS": 4,
    "ETH Cyber Security": 5,
}

for entry in DETAIL:
    info = DETAIL[entry]['项目介绍']
    values= (
        entry,
        info['项目时长'],
        info['授课语言'],
        info['学位类型'],
        info['是否强制实习'],
        info['毕业是否需要论文'],
        info['奖学金'],
        info['其他信息']
    )
    print(values)

# 插入Pros表格数据
for entry in DETAIL:
    info = DETAIL[entry]['项目优劣势']['Pros']
    name = entry
    for item in info:
        values = (name_map.get(name), item)
        print(values)   #insert

# 插入Pros表格数据
for entry in DETAIL:
    info = DETAIL[entry]['项目优劣势']['Cons']
    name = entry
    for item in info:
        values = (name_map.get(name), item)
        print(values)   #insert


for entry in DETAIL:
    info = DETAIL[entry]['注意事项']['网申注意事项']
    name = entry
    for item in info:
        values = (name_map.get(name), item)
        print(values)  # insert

