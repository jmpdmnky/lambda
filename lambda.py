import boto3
import sys
import os
#from collections import OrderedDict


l = boto3.client('lambda')

def get_boto_args(args):
    for key in args.keys():
        args[key] = input("{}: ".format(key)) or args[key]

    return args

def create(function = ""):
    print("Creating Function")
    
    boto_args = get_boto_args({
                'FunctionName': function,
                'Runtime': "",
                'Role': "",
                'Handler': "",
                'Code': ""
            })
    
    print(boto_args)

def get():
    pass

def invoke():
    pass

actions = {
            'create' : create,
            'get': get,
            'invoke': invoke
        }

action = sys.argv[1]
folder = os.getcwd().split('/')[-1]
opts = list(zip(*([iter(sys.argv[1:])]*2)))

print(action)
print(folder)
print(opts)

try:
    actions[action]()
except:
    print('ERROR')
