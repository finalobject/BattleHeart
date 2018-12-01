# -*- coding:utf-8 -*- 
import pygame, gameEngine, random
from pygame.locals import *
class Hero(gameEngine.SuperSprite):
	"""docstring for Hero"""
	def __init__(self,scene,canControl,role,loc,maxHP,maxSP):
		gameEngine.SuperSprite.__init__(self,scene)

		self.NOTCON=0
		self.UPDOWN=1
		self.WS=2

		self.KNIGHT=0
		self.MOOD=1

		self.ATTACK=1
		self.MOVE=2

		
		
		self.canControl=canControl
		self.role = role
		self.isToRight = 0
		

		self.x=loc[0]
		self.y=loc[1]
		self.speeds=[0,0]
		self.constantSpeed = 100

		self.actionType=0
		self.offset=0
		#第一个值无所谓，第二个是attackSpeed，第三个是moveSpeed
		self.actionSpeed=[0,1,1]
		self.imageMaster=[]
		self.actionImages=[]
		self.setImages()
		self.maxHP=maxHP
		self.HP=maxHP
		self.maxSP=maxSP
		self.SP=maxSP
	def checkEvents(self):
		if(self.canControl==self.UPDOWN):
			keys = pygame.key.get_pressed()
			if(self.actionType==0):
				if keys[pygame.K_LEFT]:
					self.HP+=50
					self.isToRight=0;
					self.actionType=self.MOVE
					self.speeds[0]=-self.constantSpeed
				if keys[pygame.K_RIGHT]:
					self.HP+=50
					self.isToRight=1;
					self.actionType=self.MOVE
					self.speeds[0]=self.constantSpeed
				if keys[pygame.K_UP]:
					self.HP+=50
					self.actionType=self.MOVE
					self.speeds[1]=-self.constantSpeed
				if keys[pygame.K_DOWN]:
					self.HP+=50
					self.actionType=self.MOVE
					self.speeds[1]=self.constantSpeed
				if keys[pygame.K_a]:
					self.HP-=100
					self.actionType=self.ATTACK
					self.scene.sound_attack_begin.play()
		elif(self.canControl==self.WS):
			pass
		elif(self.canControl==self.NOTCON):
			pass
	def update(self):
		self.oldCenter = self.rect.center
		self.checkEvents()
		self.checkBounds()
		self.updateAction()
		self.updateState()
		self.updatePos()
		self.updateImage()
		self.rect.center = (self.x, self.y)
	def updateAction(self):

		if(self.actionType!=0):
			if(self.offset*self.actionSpeed[self.actionType]+1>=len(self.actionImages[self.actionType][self.isToRight])):
				self.actionType=0
				self.offset=0
			else:
				self.offset+=1
	def updateState(self):
		if(self.HP>self.maxHP):
			self.HP=self.maxHP
		elif(self.HP<0):
			self.HP=0
		if(self.SP>self.maxSP):
			self.SP=self.maxSP
		elif(self.SP<0):
			self.SP=0
	def updateImage(self):
		def drawHp(image,maxHP,HP,maxSP,SP):
			cen=image.get_width()/2
			HP=float(HP)
			SP=float(SP)
			if(HP/maxHP<0.2):
				color1=[160,0,0]
				color2=[198,0,68]
				color3=[227,80,110]
			elif(HP/maxHP<0.4):
				color1=[255,121,0]
				color2=[255,180,14]
				color3=[237,229,213]
			else:
				color1=[0,160,0]
				color2=[0,198,68]
				color3=[80,227,110]
			pygame.draw.rect(image,[200,200,240],Rect((cen-50,0),(101,26)))
			pygame.draw.rect(image,[0,0,0],Rect((cen-50,0),(101,26)),2)
			pygame.draw.rect(image,[0,0,0],Rect((cen-47,3),(95,12)))
			pygame.draw.rect(image,color1,Rect((cen-47,3),(int(95*HP/maxHP),12)))
			pygame.draw.rect(image,color2,Rect((cen-47,6),(int(95*HP/maxHP),2)))
			pygame.draw.rect(image,color3,Rect((cen-47,8),(int(95*HP/maxHP),2)))
			pygame.draw.rect(image,[0,0,0],Rect((cen-47,3),(95,12)),2)
			tmp=maxHP-maxHP%100
			while tmp>0:
				if(tmp%500)==0:
					tmpWidth=2
				else:
					tmpWidth=1
				pygame.draw.line(image, [0,0,0], [cen-47+int(95*tmp/maxHP)-1,3], [cen-47+int(95*tmp/maxHP)-1,3+12],tmpWidth)
				tmp-=100

			pygame.draw.rect(image,[0,0,0],Rect((cen-47,17),(95,6)))
			pygame.draw.rect(image,[0,82,183],Rect((cen-47,17),(int(95*SP/maxSP),6)))
			pygame.draw.rect(image,[85,136,159],Rect((cen-47,17),(int(95*SP/maxSP),2)))
			pygame.draw.rect(image,[0,0,0],Rect((cen-47,17),(95,6)),2)
		if self.actionType!=0 and int(self.offset*self.actionSpeed[self.actionType])<len(self.actionImages[self.actionType][self.isToRight]):
			self.image=self.actionImages[self.actionType][self.isToRight][int(self.offset*self.actionSpeed[self.actionType])]
			#print("%d\n"%(int(self.offset*self.actionSpeed[self.actionType])))
		else:
			self.image=self.imageMaster[self.isToRight]
		drawHp(self.image,self.maxHP,self.HP,self.maxSP,self.SP)
	def updatePos(self):
		if(self.actionType==self.MOVE):
			self.x+=self.speeds[0]/len(self.actionImages[self.MOVE][self.isToRight])*self.actionSpeed[self.actionType];
			self.y+=self.speeds[1]/len(self.actionImages[self.MOVE][self.isToRight])*self.actionSpeed[self.actionType];
		else:
			self.speeds[0]=0
			self.speeds[1]=0
	def setImages(self):
		self.actionImages.append([])#第一个元素无所谓

		self.actionImages.append([[],[]])#第二个元素对应attack图片,左，右
		self.actionImages.append([[],[]])#第三个元素对应move图片,左，右
		if(self.role==self.KNIGHT):
			#设置主图像
			self.imageMaster.append(pygame.transform.flip(pygame.image.load("../res/knight/knight.gif").convert(),True,False))
			self.imageMaster.append(pygame.image.load("../res/knight/knight.gif").convert())
			
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_01.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_02.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_03.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_04.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_05.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_06.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_07.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_08.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/attack_09.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))


			
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_01.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_02.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_03.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_04.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_05.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_06.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_07.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
			self.actionImages[self.MOVE][1].append(pygame.image.load("../res/knight/move_08.gif").convert())
			self.actionImages[self.MOVE][0].append(pygame.transform.flip(self.actionImages[self.MOVE][1][-1], True, False))
		elif(self.role==self.MOOD):
			#设置主图像
			self.imageMaster.append(pygame.transform.flip(pygame.image.load("../res/knight/mood.gif").convert(),True,False))
			self.imageMaster.append(pygame.image.load("../res/knight/mood.gif").convert())
			#第一张就是站立姿势
			self.actionImages[self.ATTACK][1].append(pygame.image.load("../res/knight/mood.gif").convert())
			self.actionImages[self.ATTACK][0].append(pygame.transform.flip(self.actionImages[self.ATTACK][1][-1], True, False))
class Game(gameEngine.Scene):
	def __init__(self):
		gameEngine.Scene.__init__(self)
		self.screen = pygame.display.set_mode((1280,960))
		self.background = pygame.Surface(self.screen.get_size())
		self.background.fill((0, 0, 0))
		self.sound_attack_begin = pygame.mixer.Sound("../res/sound/attack_begin.wav")
		self.sprites=[Hero(self,1,0,[480,320],3200,200),Hero(self,0,1,[800,320],500,500)];
		#self.sprites=[Hero(self,1,0,[480,320],3200,200)]
		
def main():
	game = Game()
	game.start()
if  __name__ == '__main__':
	main()