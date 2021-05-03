# DIABLO
### DIABLO - Database Influenced Automated Ban List of Offenders. 
DIABLO syncs up with our databases on predators, such as pedophiles and zoophiles, and prevents them from joining servers that have DIABLO. DIABLO is built upon cutting-edge infrastructure bans predators from your server in mere miliseconds. Keep your server safe from  any potential predators with DIABLO. #DeplatformTheZoos #DeplatformThePedos

Our bot is designed to source data from the public to create a comprehensive database which can potentially later be used to create a network of bots that can be used to close off any entrances that predators might walk through. The more doors we close on predators, we progress towards deplatformation of certain groups such as pedophiles and zoophiles from ever spreading their abusive ideology across the internet and affecting vulnerable individuals.

## Invite Diablo to your server:
https://top.gg/bot/751888323517349908

## How Diablo Works
### Set up Diablo with ease:
When Diablo has been invited into your server, the only thing you should do is place Diablo's role above all the server members (admin roles aren't necessary, unless you want to have an extra eye over your administration team.)

The bot has two ways of working: The first is the ban that occurs if a user on the database joins your server. If a member joins the server, the bot will try to match the user ID of the member with a potential match in the database, and if there is a match in the database, the bot will ban the user from the server before they even have a chance to see any of the channels.

The latter is the task loop, which periodically scans all the servers, also scanning every single member in the server to attempt to match user IDs to the database. This allows for existing members in your server to be covered under Diablo's ban sequence if they are added to the database at any time.
## Commands
### Bot Prefix: `d.`
The following is a list of commands that Diablo has. You can use `d.help` for a full list of commands using Diablo in a server.
### Autoban
#### Bot's main function alongside commands pertaining to it.
- `diablobans` - Creates a diablobans log channel (if there is none) `[OPTIONAL: Bot will make one automatically if offender joins.]`
- `offenders` - Gives a number of the # of offenders on Diablo
- `report` - Submit a Diablo report

### Basic
#### Basic, fun commands for Diablo.
- `about` - About Diablo
- `ping` - Shows latency of the bot
- `source` - Links to bot source page
- `whois [member]` - Information about member such as name, nicknames, account creation, etc... If member left blank, then it will show author information.

### Moderation
#### Moderation commands for Diablo.
- `ban [member] [reason]` Bans a member from the server for a reason. If reason left blank, then reason=None
- `unban [member#discriminator]` - Unbans a member from the server.
- `kick [member] [reason]` - Kicks a member from the server for a reason. If reason left blank, then reason=None.
- `mute [member]` - Mutes a member permanently until unmuted
- `ummute [member]` - Unmutes a member
- `warn [member] [reason]` - Gives a member an infraction for doing something bad. **WARNING: WARNS ARE GLOBAL. WARNINGS WILL ACCOUNT FOR ALL WARNINGS USER HAS RECIEVED WITH DIABLO**
- `warnings [member]` - Retrieves the amount of warnings a member has. **WARNING: WARNS ARE GLOBAL. WARNINGS WILL ACCOUNT FOR ALL WARNINGS USER HAS RECIEVED WITH DIABLO**
- `purge [amount]`- Clears a specific amount of messages. Default is 1.
