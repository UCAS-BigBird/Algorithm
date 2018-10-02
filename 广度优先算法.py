import  collections
graph={}
graph['you']=['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire']=['thom','jonny']
graph['peggy']=['tom']
graph['anuj']=['sham']
graph['thom']=[]
graph['jonny']=[]
graph['shame']=[]
graph['tom']=[]
def person_is_seller(name):
    return name[-1]=='m'

def search(name):
    search_queue=collections.deque()
    search_queue+=graph[name]
    stated=[]
    while search_queue:
        person=search_queue.popleft()
        if person not in stated:
            if person_is_seller(person):
                print("{} is a chief".format(person))
            else:
                stated.append(person)
                search_queue+=graph[person]

search('you')
