import hvac

str_url   = "http://aea32a80c9c164190aec9f2196a4731a-881278748.ap-northeast-2.elb.amazonaws.com:8200"
str_token = "s.UJ0yJi3j3VIVfPYPWRdF0pHP"
client = hvac.Client(url=str_url, token=str_token)

str_mount_point = 'spin-hal-path'
str_secret_path = 'test'
read_secret_result = client.secrets.kv.v1.read_secret(mount_point=str_mount_point, path=str_secret_path)
print(read_secret_result)