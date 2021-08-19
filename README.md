# DIABLO
### DIABLO - Database Influenced Automated Ban List of Offenders. 
DIABLO syncs up with our databases on predators, such as pedophiles and zoophiles, and prevents them from joining servers that have DIABLO. DIABLO relies on cutting-edge infrastructure to ban predators from your server in mere milliseconds. Keep your server safe from  any potential predators with DIABLO.

Diablo is designed to allow users to report potential offenders who have engaged in predatory behavior. Reported users are investigated by Diablo moderators before being placed on our database, which prevents them from joining servers that are protected by Diablo.

Although some predator accounts do get banned by Discord, there is still an window in which predators have the opportunity to roam and wage destruction on innocent servers and their populace. Diablo offers to act as a barrier to that window and prevents predators from harming innocent server members.

## Invite Diablo to your server:
https://top.gg/bot/751888323517349908

## How Diablo Works
### Set up Diablo with ease:
When Diablo has been invited into your server, please either elevate Diablo's role above all the server members (not including admin roles, but if you want that extra edge over your admins/server mods, I'd suggest so) or ggive Diablo a Bot role with ban or administrator permissions.

The bot utilizes two methods of autoban (the process in which Diablo prevents predators from joining servers). The first of which occurs when an offender (user on the Diablo database) joins the server. If an offender joins a server, the bot will instantly detect that the offender has a presence on Diablo's database by attempting to match the user ID of the member with a potential match in the database. Accordingly, Diablo will take instant measures to prevent the offender from having the ability to interact with the server or its members.

The second method is the loop method, which scans all the members of a server every 24 hours for a potential database match. For example, if someone in your server gets added to Diablo, Diablo will instantly notice and they will be banned once the bot identified a database match. **(As of August 2021, this feature is currently disabled due to issues that require reworks)**
## Commands
### Bot Prefix: `d.`
The following is a list of commands that Diablo currently has. You can use `d.help` for a full list of commands using Diablo in any server with Diablo.
### Autoban
#### Bot's main function alongside commands pertaining to it.
- `diablobans` - Creates a diablobans log channel (if there is none) `[OPTIONAL: Bot will make one automatically if offender joins.]`
- `offenders` - Gives a number of the # of offenders on Diablo
- `report` - Opens a ticket to submit a Diablo report to be investigated by Diablo moderators. **(DM ONLY)**

### Basic
#### Basic, fun commands for Diablo.
- `about` - Information about Diablo, such as API latency, total guilds, and average members per guild.
- `source` - Link to bot source page.
- `whois [member]` - Information about member such as name, nicknames, account creation, etc... If member left blank, then it will show your information.
- `vote` - Sends a voting link for Diablo in order to engage users to help grow Diablo. 
- `whatdadogdoing` - Just a fun command that shows some adorable puppers. 

### Moderation
#### Moderation commands for Diablo.
- `ban [member] [reason]` Bans a member from a server. Reason will default to "None" if no reason provided. 
- `unban [member#discriminator]` - Unbans a member from a server.
- `kick [member] [reason]` - Kicks a member from a server. Reason will default to "None" if no reason provided. 
- `mute [member]` - Mutes a member permanently until unmuted
- `ummute [member]` - Unmutes a member
- `warn [member] [reason]` - Gives a member an infraction for doing something bad. **WARNING: WARNS ARE GLOBAL. WARNINGS WILL ACCOUNT FOR ALL WARNINGS USER HAS RECIEVED WITH DIABLO**
- `warnings [member]` - Retrieves the amount of warnings a member has. **WARNING: WARNS ARE GLOBAL. WARNINGS WILL ACCOUNT FOR ALL WARNINGS USER HAS RECIEVED WITH DIABLO**
- `purge (or) clear [amount]`- Clears a specific amount of messages. Default is 1, limit is 100. 
