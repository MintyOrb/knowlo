# build json/js object from cypher query export 
# 
# # [
#     {
#         title:
#         thumbnail:
#         url:
#         author:?
#         uid:
#         displayType:
#         tags: [
#             {
#                 name:
#                 iconUrl:
#                 uid:
#             }
#         ]
#     }
# ]

import json

with open('resources with tags.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# print(data[0]["res"]["properties"]["author"])
# print(data[2])
for x in range(len(data[0]['tags'])):
    print(data[0]['tags'][x]['properties']['english'])

included=[x.lower() for x in['Cosmology','Biology','Chemistry','Physics','Math','Ecology','Astronomy','Geography','Molecular','Biology','Sociology','Psychology','Philosophy']] 
newRes = []

for res in range(len(data)):
    bres = {
        'title': data[res].get('title',None),
        'thumbnail':data[res]["res"]["properties"].get("thumb",None),
        'url':data[res]["res"]["properties"].get("url",None),
        'author':data[6]["res"]["properties"].get("author",None),
        # 'subTitle':data[res]["res"]["properties"].get("subTitle",None),
        'uid':data[res]["res"]["properties"].get("uid",None),
        'displayType':data[res]["res"]["properties"].get("displayType",None),
        'tags': []
    }
    for tag in range(len(data[res]['tags'])):
        # print(data[res]['tags'][tag]['properties'])
        # print('english' in data[res]['tags'][tag]['properties'])
        if 'english' in data[res]['tags'][tag]['properties'] and data[res]['tags'][tag]['properties']['english'] in included:
            # print(data[res]['tags'][tag]['properties'])
            print('match')
            bres['tags'].append(data[res]['tags'][tag]['properties']['english'])
            print( bres['tags'])
    newRes.append(bres)
print(newRes[20])
print(newRes[21])
print(newRes[22])

print(newRes[23])

print(len(newRes))