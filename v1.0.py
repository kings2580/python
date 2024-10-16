import random as rd
import os
class core1:
    def __init__(self,size_x,size_y):
        self.data={'block':{},'mob_type':{},'item':{},'mob':{},'point':{},'type':{}}
        self.map=[]
        list=[]
        for x in range(size_x):
            for y in range(size_y):
                list+=[{'block':'None','item':'None'}]
            self.map+=[list]
            list=[]
    def add(self,type,name,*data):
    	self.data[type][name]=data
    def __str__(self):
    	return 'mob_type->크기,1일 소비열량,몸 구조 딕셔너리,소지 아이템 리스트\nblock->이름,기본 내구성\nmob->이름,몸 상태,특성 리스트,소지 아이템 리스트,x 좌표,y 좌표\ntype->내구성 배수,둔상 데미지 배수,자상 데미지 배수,방어력 배수,인화성,기타 특성들\nitem->이름,재질,기타 특성들'
    def set_map(self,name,x,y,type):
    	self.map[x][y][type]=name
class core2:
	def __init__(self):
		self.events={}
		self.event='stat'
	def set_event(self,name,text,teb,next):
		self.events[name]=[text,teb,next]
	def play(self):
		while True:
			k=self.events[self.event]
			print(k[0],end='\n\n')
			x=input(k[1])
			if x=='':
				break
			else:
				self.event=rd.choice(k[2][(int(x)+1)%(len(k[2]))])
			os.system('clear')