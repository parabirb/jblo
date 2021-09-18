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
*/

const fs = require("fs");
const path = require("path");
const drivers = require(path.join(__dirname, "drivers/drivers.json"));
const { question } = require("readline-sync");

let config = {};

// i feel kinda uncomfortable not putting this into a function
function main() {
    console.log("Welcome to the jblo configuration utility!");
    config.token = question("Please enter the Discord token you will use for the bot: ");
    console.log("Great! For your bot to work, you will need a database driver.");
    console.table(drivers);
    let driver = question("Please pick a driver by index: ");
    if (isNaN(+driver) || +driver < 0 || +driver >= drivers.length) {
        console.log("Configuration cancelled: You did not enter a proper index.");
        process.exit(1);
    }
    config.driver = drivers[+driver].path;
    driver = require(path.join(__dirname, "drivers", drivers[+driver].path));
    try {
        let arr = [];
        let configArr = driver.configArray();
        console.log("This portion is the driver configuration portion. Please consult the documentation for your driver to determine what to enter in each field.");
        for (let i = 0; i < configArr.length; i++) {
            arr.push(question(configArr[i] + ": "));
        }
        config.driverConfig = arr;
    }
    catch (e) {
        console.log("Your database driver is not written properly. Please make sure it contains the necessary configuration functions.");
    }
    fs.writeFileSync("config.json", JSON.stringify(config, null, 4));
    console.log("Congratulations! Your jblo configuration is complete. Please check config.json to make sure it looks correct.");
}

main();