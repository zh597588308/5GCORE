# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
import json
from flask_restful import Resource,reqparse
from simconf import conf_json
#from sqlalchemy import Column, String, create_engine,LargeBinary
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

from .. import tables

parser = reqparse.RequestParser()
parser.add_argument('servingNetworkName')
parser.add_argument('resynchronizationInfo')
parser.add_argument('ausfInstanceId')

CurrentPath = "~/5GCORE/UDM/Nudm_UEAuthentication/v1/api/UE_Auth.py"

def getSUPIfromSUCI(suci):
    supi_type = suci[0]
    mcc = suci[1:4]
    mnc = suci[4:6]
    home_network_identifier = mcc+mnc
    routing_indicator = suci[6:9]
    prot_scheme_id = suci[9]
    hn_pub_key = suci[10]
    scheme_output = suci[11:]

    supi = home_network_identifier+scheme_output
    return supi

class UEAUTH(Resource):
    global info
    def __init__(self):
    	pass
    def post(self,supiOrSuci):
        args = parser.parse_args()
        print(CurrentPath+":29   [UDM][INFO]   "+"receive AUSF get mysql infos with imsi("+supiOrSuci+")")
        print(CurrentPath+":30   [UDM][INFO]   "+"create engine to connect mysql")
        #get supi from suci and covert into VarUeId
        supi = getSUPIfromSUCI(supiOrSuci)
        ueId = "imsi-"+supi
        url = "http://"+conf_json['udr_sub_ip_address']+":"+conf_json['udr_sub_port_number']+"/subscription-data/"+ueId+"/authentication-data/authentication-subscription"
        req = requests.get(url)
        if req.status_code == 200:
            authinfo_dict = req.json()
            #authinfo_dict = json.load(authinfo)
        else:
           return(json.dumps({}))
        print(CurrentPath+":36   [UDM][INFO]   "+"infos about imsi("+supi+") in UDR as following")
        print("\n\n|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|      UDR user infos where imsi = "+"208930000000001"+"         |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|        imsi        |            OPc                       |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|   "+supi+" |     "+authinfo_dict['encOpcKey']+"   |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n\n")
        #data = {'imsi':args['imsi'],'msisdn':281992,'key':'8baf473f2f8fd09487cccbd7097c6862','opc':authinfo_dict['encOpcKey']}
        data = {"supportedFeatures": "supportedFeatures", "authenticationVector": "6565663636666", "authType": authinfo_dict['authenticationMethod'], "supi":supi }
        return (data)
