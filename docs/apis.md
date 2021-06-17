# Setting up the APIs
Setting up the Discord bot API is, of course, **100% necessary**.
And, even tho it may be frustrating, it's recommended to also set up **MongoDB** - most of the data is saved there and a lot of features might break.
The other ones are optional (some features that need the API may not work), but the more APIs, the better.

Now, the set-up the APIs mentioned below. The set-up process won't be described, but I hope, you'll find some useful tutorials on how to set them up. I wish you good luck! 👍 (why does this sound so ironic, lol)

# List of all APIs
The default APIs NeoVision is using are:
| API Name     	| Abbreviation 	| How important?   	| Description                                            	| Note                                                          	| Data/needed value(s)            	|
|--------------	|--------------	|------------------	|--------------------------------------------------------	|---------------------------------------------------------------	|---------------------------------	|
| Discord      	| DC           	| 🔴 Required       	| Discord bot                                            	| -                                                             	| Bot token                       	|
| MongoDB      	| DB           	| 🟡 Recommended    	| Database                                               	| In developement                                               	| Database string                 	|
| Lyrics       	| LYRICS        | 🟢 Nice to have   	| Lyrics searching                                       	| -                                                             	| API user id, developer token ID 	|
| Watch2Gether 	| W2G          	| 🔵 Fully optional 	| YouTube video syncing website                          	| Since recently unnecessary, since party games were introduced 	| API token                       	|
| Hypixel      	| HYPIXEL      	| 🔵 Fully optional 	| Data for the popular "Minecraft" game server "Hypixel" 	| In developement                                               	| Hypixel API token               	|

# Setting up .env file
You may set up the `.env` in this format:

```
DC=XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXX-XXXXXXXXXXX`
DB=mongodb+srv://USER:PASSWORD@CLUSTER.SERVER.mongodb.net/DATABASE?retryWrites=true&w=majority
LYRICS=API_USER_ID_HERE DEVELOPER_TOKEN_ID
W2G=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
HYPIXEL=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```
Don't be confused why the MongoDB value is so complicated - you can generate such string easily using the MongoDB connect-popup. 

OK, thats it! Have fun!