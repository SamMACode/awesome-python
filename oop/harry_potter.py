# -*- coding:utf-8 -*-
import copy


class Document:
	WELCOME_STR = 'Welcome! The context for this book is {}.'

	def __init__(self, title, author, context):
		print(f"initialize function called")
		self.title = title
		self.author = author
		self.__context = context  # __开头的属性为私有属性

	def get_context_length(self):
		"""成员函数，与类的实例进行绑定"""
		return len(self.__context)

	def intercept_context(self, length):
		self.__context = self.__context[:length]

	@classmethod
	def create_empty_book(cls, title, author):
		"""define class method which decorated with @classmethod annotation"""
		return cls(title=title, author=author, context='nothing')

	@staticmethod
	def get_welcome(context):
		"""有疑惑的地方：静态函数、类函数之间的区别是什么？"""
		return Document.WELCOME_STR.format(context)


def func_param_verify(dict):
	"""验证python中的参数传递，值传递、引用传递"""
	dict['a'] = 10
	dict['b'] = 20


if __name__ == '__main__':
	harry_potter = Document('Harry Potter', 'J. K. Rowling', 'Forever Do not believe any thing is capable of '
															 'thinking independently')
	print(f"title: {harry_potter.title}, author: {harry_potter.author}, context_length: "
		  f"{harry_potter.get_context_length()}")
	l1 = [[1, 2], (30, 40)]
	# deepcopy#当存在指向自身的引用时，很容易陷入无限循环
	l2 = copy.deepcopy(l1)
	l1.append(100)
	l1[0].append(3)
	# l1 data: [[1, 2, 3], (30, 40), 100], l2 value: [[1, 2], (30, 40)]
	print(f"l1 data: {l1}, l2 value: {l2}")

	# l3与l2#id是相等的，l1与l2指向不同的内存地址
	l1 = [1, 2, 3]
	l2 = [1, 2, 3]
	l3 = l2
	# id(l1): 140235426092672, id(l2): 140235426092864, id(l3): 140235426092864
	print(f"id(l1): {id(l1)}, id(l2): {id(l2)}, id(l3): {id(l3)}")

	dict_map = {'a': 1, 'b': 2}
	func_param_verify(dict_map)
	# after adjust parameter, dict_map: {'a': 10, 'b': 20}
	print(f"after adjust parameter, dict_map: {dict_map}")
