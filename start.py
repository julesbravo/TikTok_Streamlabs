from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import SubscribeEvent, FollowEvent

# UPDATE THESE TO BE WHERE YOU WANT FILES WRITTEN
subscribersLog = "C:/Path/To/Your/SubscribersFile.txt"
followersLog = "C:/Path/To/Your/FollowersFile.txt"
streamerId = "@badaimbenny"

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id=streamerId, **({"enable_extended_gift_info": True}))

subscribersFile = open(subscribersLog, "a+")
followersFile = open(followersLog, "a+")

@client.on("subscribe")
async def on_connect(event: SubscribeEvent):
    print(f"{event.user.nickname} subscribed")
    subscribersFile.write(f"{event.user.nickname}\n")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.nickname} followed")
    followersFile.write(f"{event.user.nickname}\n")


if __name__ == '__main__':
    client.run()