'''
Created by auto_sdk on 2015.11.03
'''
from base import RestApi
class WlbWaybillISearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.waybill_apply_request = None

	def getapiname(self):
		return 'taobao.wlb.waybill.i.search'
