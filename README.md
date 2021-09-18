# jblo
jblo is a fork of diablo written in javascript. This will be updated when the port is complete.

## installation
* use or write a compatible database driver. [more information](DATABASE.md)
* run `npm i`.
* run `node config-gen.js`.
* you're done with the installation! you can now just run jblo on demand.

## q&a
### what is jblo?
jblo is a port of diablo to javascript with additional features. diablo has its flaws, which jblo attempts to resolve.
### what will jblo do?
jblo will come with the basic features of diablo, including, but not limited to:
* offender database (jblo will not autoban, but will instead warn moderators)
* whois (displays user info)
* about (displays bot info)
* source (displays source link)
* vote (gives link to vote)
* kick
* ban
* unban
* report

some features being considered include user-contributed offender databases.

in order to limit feature creep, warnings, mutes, and irrelevant commands will not be provided.
### accessibility
jblo instances can be run by the average person. jblo will come with a web api which drivers will be written for, allowing users to run off the diablo database.