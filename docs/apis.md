# Setting up the APIs
Setting up the Discord bot API is, of course, **100% necessary**.
And, even tho it may be frustrating, it's recommended to also set up **MongoDB** - most of the data is saved there and a lot of features might break.
The other ones are optional (some features that need the API may not work), but the more APIs, the better.

Now, the set-up the APIs mentioned below. The set-up process won't be described, but I hope, you'll find some cool tutorials on how to set them up. I wish you good luck! 👍  

# List of all APIs
The default APIs NeoVision is using are:
- **Watch2Gether** (W2G): Creating video synchronization rooms
- **MongoDB** (DB): Managing database  
- **Hypixel** (HYPIXEL): Player stats for the popular video game *Minecraft*-server "Hypixel.net"
- **Discord** (DC): The Discord bot

# Setting up .env file
You may set up the `.env` in this format:

```
W2G=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DB=mongodb+srv://USER:PASSWORD@CLUSTER.SERVER.mongodb.net/DATABASE?retryWrites=true&w=majority
HYPIXEL=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
DC=XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXX-XXXXXXXXXXX`
```
Don't be confused why the MongoDB value is so complicated - you can generate such string easily using the MongoDB connect-popup. 

OK, thats it! Have fun!