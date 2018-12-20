import boto3
import sys
import os
#from collections import OrderedDict

l = boto3.client('lambda')

def get_boto_args(args):
    for key in args.keys():
        args[key] = input("{}: ".format(key)) or args[key]

    return args

def init_local(fn_name, manifest=""):
    os.mkdir(fn_name)
    if manifest:
        with open(".lambda_config", "w") as out_file:
            out_file.write(manifest)

def repair_local(fn_name):
    folder = os.getcwd().split('/')[-1]
    if folder == fn_name:
        print("TODO: REPAIR MANIFEST")
    else:
        os.mkdir(fn_name)
        print("TODO: REPAIR MANIFEST")

def create(fn_name = ""):
    print("Creating Function")
    
    boto_args = get_boto_args({
                'FunctionName': fn_name,
                'Runtime': "",
                'Role': "",
                'Handler': "",
                'Code': ""
            })
    
    print(boto_args)

def update():
    pass

def describe():
    pass

def get(fn_name):
    response = l.get_function(
        FunctionName=fn_name
    )
    
    data = {
        'Configuration': response['Configuration'],
        'Tags': {},
        'Concurrency': {}
    }

    try:
        data['Tags'] = response['Tags']
    except:
        pass

    try:
        data['Concurrency'] = response['Concurrency']
    except:
        pass

    return data

def invoke():
    pass

actions = {
            'create' : create,
            'get': get,
            'invoke': invoke
        }

if __name__ == '__main__':
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

