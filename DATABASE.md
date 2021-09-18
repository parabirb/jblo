# Database Support
jblo support for databases is complicated. Currently, jblo shares a database with Diablo. As jblo hasn't been given write access to Diablo yet, jblo does not support writing to databases (yet). For now, you should find a way to write to the database without jblo (this will be added in the future). Once writes are supported or experimental, support for more lightweight databases like raw JSON files or things like LokiJS will be added.

For a reference database driver implementation, check `drivers/mongo.js`. Drivers will be backward compatible.

## The jblo Manifesto
jblo should be easy to patch to support any database without having to write the entire bot from scratch. That's why jblo supports modular drivers, so that the user can select the drivers they need. jblo is flexible and simple--an existing codebase that can fit the same basic purpose.

## Using Drivers
Okay, now that's over: Read the [database index](DATABASE_INDEX.md) for information on every official driver. To install unofficial drivers, check the driver documentation.

## Writing Drivers
Drivers require a few basic functions (**all functions are async**):
* `config(...args)` - This is a configuration function ran every time the bot starts up.
* `Array configArray()` - This is a function ran during initial configuration of the driver. It should return a list of the arguments passed in `args`, in order. Example: `["Argument 1 Name", "Argument 2 Name", "Argument 3 Name"]`.
* `Array fetchAll()` - This should return an array of every member of the database.
* `Object findOne(String id)` - This should return an object with the entry for the ID, or `null` if no object has the ID.
* `Object write()` - Write access to the database isn't actually required--in fact, the main instance of jblo will not have write access at all to the database for a bit. To allow other instances of jblo to work while meeting jblo's needs, the write API was created. Read the below for more information.

## write()
If you have to check whether the database supports writes at runtime, you should do it in the `write()` function. This is why the function is provided in the first place.

If writes are not supported by the database, `write()` should return `null`.

Both of these must be present in the returned object for `write()` if writes are supported:
* `insert(object)` - Insert an object into the database. The object will have an `id` property, which is a Discord ID.
* `delete(id)` - Delete any object that exists with the `id` parameter `id`.