import os

from wsdl_to_tuple import client
from wsdl_to_tuple import  gen

fp="/home/peek/project/peek-plugin-pof-soap/peek_plugin_pof_soap/_private/agent/thing.wsdl"

templateDir = os.path.abspath(os.path.join(os.path.dirname(gen.__file__)))

tuplePyTpl = os.path.join(templateDir, 'tuples_py.tpl')
tupleJsTpl = os.path.join(templateDir, 'tuples_js.tpl')

code = gen.gen(client.Client(fp), template=tuplePyTpl)

with open("call_code.py", "w") as f:
    f.write(code)


gen.Attr = gen.AttrJs

code = gen.gen(client.Client(fp), template=tupleJsTpl)

with open("call_code.ts", "w") as f:
    f.write(code)

