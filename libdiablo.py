"""
    libdiablo v0.0.1
    A simple library for user blacklists that are maintained throughout multiple servers.
    This is a high level abstraction that is recommended for new users or experienced
    users who don't want to write it themselves. Please note that it is not legal to
    use this library for any bot without releasing its source code under the GPLv3 or
    any later version.
    (C) 2020 ararouge. All rights reserved.
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
"""
import pymongo
import flask
import json
import threading

# diabloserv: a diablo server
class diabloserv:
    def __init__(self, dblink):
        self.dbclient = pymongo.MongoClient(dblink)
        self.database = self.dbclient["diablo"]
        self.authorized = self.database["authorized"]
        self.banned = self.database["banned"]
        self.version = "libdiablo 0.0.1"
    def checkauth(self, userid):
        return (self.authorized.count_documents({ "userid": userid }, limit = 1) != 0)
    def checkban(self, userid):
        return (self.banned.count_documents({ "userid": userid }, limit = 1) != 0)
    def retrieveban(self, userid):
        if self.checkban(userid):
            return self.banned.find_one({ "userid": userid })
        else:
            return {}
    def addban(self, userid, reason):
        if not(self.checkban(userid)):
            self.banned.insert_one({ "userid": userid, "reason": reason })
    def addauth(self, userid):
        if not(self.checkauth(userid)):
            self.authorized.insert_one({ "userid": userid })
    def delban(self, userid):
        if not(self.checkban(userid)):
            self.banned.delete_one({ "userid": userid })
    def delauth(self, userid):
        if not(self.checkauth(userid)):
            self.authorized.delete_one({ "userid": userid, "reason": reason })
    def startwebserversync(self):
        self.app = flask.Flask(__name__)
        @self.app.route("/auth/check/<id>")
        def webcheckauth(id):
            return json.dumps({ "server": self.version, "response": json.dumps(self.checkauth(id)) })
        @self.app.route("/ban/check/<id>")
        def webcheckban(id):
            return json.dumps({ "server": self.version, "response": json.dumps(self.checkauth(id)) })
        @self.app.route("/ban/retrieve/<id>")
        def webretrieveban(id):
            return json.dumps(self.retrieveban(id))
        self.app.run()
    def startwebserver(self):
        thread = threading.Thread(target=self.startwebserversync)

# class diabloclient:
    # soon
