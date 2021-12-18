# -*- coding:utf-8 -*-
import yaml


class Monster(yaml.YAMLObject):
	yaml_tag = u'!Monster'

	def __init__(self, name, hp, ac, attacks):
		self.name = name
		self.hp = hp
		self.ac = ac
		self.attacks = attacks

	def __repr__(self):
		return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
			self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)


# 建立全局变量registry,将需要序列化的YAMLObject全都注册进去
registry = {}


def add_constructor(target_class):
	registry[target_class.yaaml_tag] = target_class


if __name__ == '__main__':
	yaml.load("""
	--- !Monster 
	name: Cave spider 
	hp: [2,6] # 2d6 
	ac: 16 
	attacks: [BITE, HURT]
	""", Loader=yaml.Loader)

	print(yaml.dump(Monster(
		name='Cave lizard', hp=[3, 6], ac=16, attacks=['BITE', 'HURT'])))
