/*
    jblo
    (C) 2021 parabirb. All rights reserved.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    This is the jblo database driver for MongoDB.
    It is also the reference implementation of a database
    driver. Check drivers.json for the reference implementation
    of a database driver file.
*/
const mongoose = require("mongoose");
let config = {};

/*
    config() should be a function for configuring
    your database driver. this function will always  be
    called on startup.
*/
function config(mongoUrl, database, collection) {
    config.mongoUrl = mongoUrl;
    config.database = database;
    config.collection = collection;
}

/*
    Array configArray() should return an array of all of
    the different configuration parameters in order.
    This is called during initial configuration.
*/
function configArray() {
    return ["MongoDB URL", "Database Name", "Collection Name"];
}

/*
    Array fetchAll()
    Returns all members of the offender database.
*/
async function fetchAll() {

}

/*
    Object find(String id)
    Returns a member of the offender database with that ID.
    It should return null if there is no such member.
*/
async function find(id) {

}

/*
    write support is gonna be wonky, but that is intentional
    due to the nature of the bot.

    writing is optional, which will be helpful for bots running
    off external databases with stuff such as the web driver.

    some simple pseudocode:

    async function write() {
        // writing is enabled and available?
        if (writeEnabled) {
            return {
                insert: (object) => { // insert object from the database },
                delete: (id) => { // delete object with id from the database }
            }
        }
        // if not, return null.
        return null;
    }
*/

async function write() {

}

module.exports = {
    config,
    configArray,
    fetchAll,
    find,
    write
};