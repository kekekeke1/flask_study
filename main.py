# This is a sample Python script.
import json
from io import StringIO
import paramiko
import subprocess
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paramiko
import builtins
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
RSA_PRIVATE_KEY = paramiko.RSAKey.from_private_key(StringIO("""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # ujson.loads()
    a = {"key1": "value1", "key3": "value3", "key4": None}
    b = {"key2": "value2"}
    c = {** a, ** b}
    print(type(c))
    print(c)
    command = ''
    for key in list(c.keys()):
        if c.get(key):
            command1 = "--" + key + "=" + c.get(key) + ''
            command += command1
    print(command)
    print(1111)
    command = []
#     for k, v in c.items():
#         if v is not None and v != '':
#             command.append(f"--{k}={v}")
#     command = " ".join(command)
#     print(command)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#     subprocess.run()
    import uuid
    print(uuid.uuid1())

