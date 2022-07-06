import jwt

def encodeToJWT(data: dict):
   return jwt.encode(payload=data, key="5ebe2294ecd0e0f08eab7690d2a6ee69", algorithm="HS256")

def decodeJWT(data: str):
   return jwt.decode(data, "5ebe2294ecd0e0f08eab7690d2a6ee69", algorithms=["HS256"])