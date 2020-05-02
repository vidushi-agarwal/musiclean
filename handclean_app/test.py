import django
django.setup()
from handclean_app.models import LyricModel
model = LyricModel.objects.all()

class check():
    def do_it():
        set1=set()
        hashmap = dict()
        nav_dict=dict()
        for m in model:
            str1 = m.song_title
            str1 = str1.lower()
            if (str1 in set1):
                hashmap[str1] = hashmap[str1] + 1
            else:
                set1.add(str1)
                hashmap[str1]=1
        list_sort = sorted(hashmap.items(), key=lambda t: t[1], reverse=True)
        ctr=0
        for k, v in list_sort:
            if (ctr == 5):
                break
            m = LyricModel.objects.filter(song_title=k)
            if (len(m) > 0):
                nav_dict[k]=m[0].id
                ctr+=1
        return(nav_dict)

print(check.do_it())

    