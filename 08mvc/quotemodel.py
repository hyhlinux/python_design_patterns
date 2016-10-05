#coding:utf-8
#data for quotes
quotes = (
	'一寸光阴',
	'时间是一切财富中最宝贵的财富',
	'友谊是一棵可以庇荫的树',
	'不达成功誓不休',
	'爱情原如树叶一样，在人忽视里绿了，在忍耐里露出蓓蕾',
	'我需要三件东西：爱情友谊和图书。然而这三者之间何其相通！炽热的爱情可以充实图书的内容，图书又是人们最忠实的朋友',
	'爱情从爱情中来',
	'忠诚的爱情充溢在我的心里，我无法估计自己享有的财富',
	'爱情的意义在于帮助对方提高，同时也提高自己',
)


class QuotesModel(object):
	"""docstring for QuotesModel"""
	def get_quote(self, n):
		try:
			values = quotes[n]
		except IndexError as err:
			values = 'not found'
		# print'-'*20 print values print'-'*20
		return values	

def test():
	model = QuotesModel()
	print '-'*20
	print model.get_quote(2)
	print '-'*20

if __name__ == '__main__':
	test()

