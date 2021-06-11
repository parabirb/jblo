# DIABLO
### DIABLO - Database Influenced Automated Ban List of Offenders. 
DIABLO syncs up with our databases on predators, such as pedophiles and zoophiles, and prevents them from joining servers that have DIABLO. DIABLO relies on cutting-edge infrastructure to ban predators from your server in mere miliseconds. Keep your server safe from  any potential predators with DIABLO.

While Discord can take anywhere from a few days to a week to process and take action regarding reports, there is a window in which predators can still freely interact on Discord before being banned. Diablo is designed to be a short-term solution to close that window. Diablo relies on sourced data from the public to create a comprehensive database to close off any entrances that predators might walk through. The more doors we close on predators, we progress towards a safer environemnt across discord, to prevent potential predators from disrupting server operations and preventing many potential indivduals from becoming victims of predatory behavior. 

## Invite Diablo to your server:
https://top.gg/bot/751888323517349908

## How Diablo Works
### Set up Diablo with ease:
When Diablo has been invited into your server, the only thing you should do is place Diablo's role above all the server members (not including admin roles, but if you want that extra edge over your admins/server mods, I'd suggest so).

The bot has two methods of autoban. The first is the ban that occurs if a member joins the server. If a member joins the server, the bot will try to match the user ID of the member with a potential match in the database, and if there is a match in the database, the bot will ban the user from the server before they even have a chance to see any of the channels.

The second method is the loop method, which scans all the members of a server every hour for a potential database match. For example, if someone in your server gets added to Diablo, the bot will notice them on the database and they will be banned once the bot sees a database match. **Will be deactivated in next patch due to issues**
## Commands
### Bot Prefix: `d.`
The following is a list of commands that Diablo has. You can use `d.help` for a full list of commands using Diablo in a server.
### Autoban
#### Bot's main function alongside commands pertaining to it.
- `diablobans` - Creates a diablobans log channel (if there is none) `[OPTIONAL: Bot will make one automatically if offender joins.]`
- `offenders` - Gives a number of the # of offenders on Diablo
- `report` - Submit a Diablo report **Currently deactivated.**

### Basic
#### Basic, fun commands for Diablo.
- `about` - Information about Diablo, such as API latency, total guilds, and average members per guild. **Not yet updated.**
- `source` - Link to bot source page
- `whois [member]` - Information about member such as name, nicknames, account creation, etc... If member left blank, then it will show author information.
- `vote` - Sends a voting link for Diablo in order to engage users to help grow Diablo. **Not yet added.**

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
