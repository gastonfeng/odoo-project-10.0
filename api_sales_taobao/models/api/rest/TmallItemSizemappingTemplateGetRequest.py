'''
Created by auto_sdk on 2016.02.23
'''
from base import RestApi
class TmallItemSizemappingTemplateGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.template_id = None

	def getapiname(self):
		return 'tmall.item.sizemapping.template.get'
