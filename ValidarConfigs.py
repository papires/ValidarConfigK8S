#!/bin/python3
# coding: utf-8
import yaml,sys,logging

if len(sys.argv) != 4:
  msg = "* Erro na entrada dos argumentos. *\nPrecisa de 3 argumentos.\nNumber of arguments: %s"  %(len(sys.argv))
  print(msg +"\n"+str(sys.argv))
  print("1* ARG - openapi.yaml ")
  print("2* ARG - deployment.yaml ")
  print("3* ARG - virtualservices.yaml ")
  sys.exit(1)
file_openapi  = sys.argv[1]
file_deployment = sys.argv[2]
file_deployment_vs = sys.argv[3]

class OpenAPI:
    def __init__(self, arg):
        self.yaml_load = yaml.load(open(arg),Loader=yaml.FullLoader)
    def getTitle(self):
        return self.yaml_load["info"]["title"]
    def getHost(self):
        return self.yaml_load["host"]
    def getBasePath(self):
        return self.yaml_load["basePath"]
    def getSchemes(self):
        return self.yaml_load["schemes"]
    def get_xgoogleissuer(self):
        return self.yaml_load["securityDefinitions"]["oauth2_key"]["x-google-issuer"]
    def get_xgooglejwksuri(self):
        return self.yaml_load["securityDefinitions"]["oauth2_key"]["x-google-jwks_uri"]
    def get_xgoogleaudiences(self):
        return self.yaml_load["securityDefinitions"]["oauth2_key"]["x-google-audiences"]

class VirtualService:
    def __init__(self, arg):
        self.yaml_load = yaml.load(open(arg),Loader=yaml.FullLoader)
    def getName(self):
        return self.yaml_load["metadata"]["name"]
    def getGateways(self):
        return self.yaml_load["spec"]["gateways"]
    def getHosts(self):
        return self.yaml_load["spec"]["hosts"]
    def getURI(self):
        return self.yaml_load["spec"]["http"][0]["match"][0]["uri"]
    def getDestinationHost(self):
        return self.yaml_load["spec"]["http"][0]["route"][0]["destination"]["host"]
    def getDestinationHostPort(self):
        return self.yaml_load["spec"]["http"][0]["route"][0]["destination"]["port"]["number"]

class Deployment:
    
# print("-----")
# virtualsvc = VirtualService(file_deployment_vs)
# print(virtualsvc.getName())
# print("-----")
# print(virtualsvc.getGateways())
# print("-----")
# print(virtualsvc.getHosts())
# print("-----")
# print(virtualsvc.getURI())
# print("-----")
# print(virtualsvc.getDestinationHost())
# print("-----")
# print(virtualsvc.getDestinationHostPort())

#opeanapi = OpenAPI(file_openapi)
#print(opeanapi.getTitle())
#print(opeanapi.getHost())
#print(opeanapi.getBasePath())
#print(opeanapi.get_xgoogleissuer())
