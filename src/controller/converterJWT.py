import jwt

def encodeToJWT(data):
   return jwt.encode(data, "5ebe2294ecd0e0f08eab7690d2a6ee69", algorithm="HS256")

def decodeJWT(data):
   return jwt.decode(data, "5ebe2294ecd0e0f08eab7690d2a6ee69", algorithm=["HS256"])