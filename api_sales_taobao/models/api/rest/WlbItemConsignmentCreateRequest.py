'''
Created by auto_sdk on 2016.03.05
'''
from base import RestApi
class WlbItemConsignmentCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.number = None
		self.owner_item_id = None
		self.rule_id = None

	def getapiname(self):
		return 'taobao.wlb.item.consignment.create'
