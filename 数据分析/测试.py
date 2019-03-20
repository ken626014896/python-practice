
import  json

a=[{"model": "homepage.post", "pk": 1, "fields": {"title": "办公效率提升N倍，这些神器赶紧收藏", "sort": "科技"}}, {"model": "homepage.post", "pk": 2, "fields": {"title": "索尼三星西门子，你们能不能别再降了", "sort": "科技"}}, {"model": "homepage.post", "pk": 3, "fields": {"title": "神评 | 移动的骚操作，被电信联通抓了现行", "sort": "科技"}}, {"model": "homepage.post", "pk": 4, "fields": {"title": "华为P30 Pro红色版图赏，水滴屏、4000W后置三摄", "sort": "科技"}}, {"model": "homepage.post", "pk": 5, "fields": {"title": "Android Q简单上手，这些地方有升级", "sort": "科技"}}, {"model": "homepage.post", "pk": 6, "fields": {"title": "主打陌生人社交，腾讯内测类似漂流瓶功能", "sort": "科技"}}, {"model": "homepage.post", "pk": 7, "fields": {"title": "exo-cbx 为了你", "sort": "娱乐"}}]
print(len(a))
a=json.dumps(a)

print(type(a))
print(a)