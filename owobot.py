import requests
import time

payload={
    "content":"owoh"

}
header = {
    "authorization":"MTAyMjE5MDA2ODMxNzgzMTIzOA.GplVNn.SpJwIJ7dW8YNQvgf19BlcDfW8YLWEEiB66QYG4"
}


while True:
    for i in range(15):
        payload["content"] = "owoh"
        time.sleep(20)
        r = requests.post("https://discord.com/api/v9/channels/1022903491921973321/messages",data=payload,headers=header)
    time.sleep(1800)