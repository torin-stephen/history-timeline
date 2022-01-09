from airium import Airium
a = Airium()

#define variables
date = ''
cont = ''

#write data to html with Airium
with open('data.txt') as file:
    cnt = 0
    for line in file:
        print(line)
        date = line.partition("|")[0]
        cont = line.partition("|")[2]
        if (cnt % 2) == 0:
            with a.div(klass='container left'):
                with a.div(klass='content'):
                    a.h2(_t=date)
                    with a.p():
                        a(cont)
        else:
            with a.div(klass='container right'):
                with a.div(klass='content'):
                    a.h2(_t=date)
                    with a.p():
                        a(cont)
        cnt += 1

html = str(a)

out = open("output.html", "x")
out.write(html)
