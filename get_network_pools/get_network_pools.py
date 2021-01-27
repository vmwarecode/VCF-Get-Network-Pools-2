#Get Network Pools
#Gets the list of all network pools available
import requests
import json
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class GetNetworkPools:
    def __init__(self):
        print('Get Network Pools')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def get_network_pools(self):
        get_network_pools_url = 'https://'+self.hostname+'/v1/network-pools'
        response = self.utils.get_request(get_network_pools_url)
        pprint.pprint(response)

if __name__== "__main__":
    GetNetworkPools().get_network_pools()
