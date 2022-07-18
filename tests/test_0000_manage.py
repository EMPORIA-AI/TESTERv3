#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = r""" (


     _        __  __              _   _               _____   ______
  /\| |/\    |  \/  |     /\     | \ | |     /\      / ____| |  ____|
  \ ` ' /    | \  / |    /  \    |  \| |    /  \    | |  __  | |__
 |_     _|   | |\/| |   / /\ \   | . ` |   / /\ \   | | |_ | |  __|
  / , . \    | |  | |  / ____ \  | |\  |  / ____ \  | |__| | | |____
  \/|_|\/    |_|  |_| /_/    \_\ |_| \_| /_/    \_\  \_____| |______|


)






"""  # __banner__

import platform, requests
from cubed4th import FORTH

class TestCONFIG:

    memory = {}

    if platform.node() in ["I8-BUILD5"]:
        memory["__engine"] = "http://127.0.0.1:10000/api/engine/v1/"
        memory["__config"] = "http://127.0.0.1:10000/api/config/v1/"
    else:
        memory["__engine"] = "https://z-enginetst-emporia.enscaled.sg/api/engine/v1/"
        memory["__config"] = "https://z-enginetst-emporia.enscaled.sg/api/config/v1/"

    options = {"memory": memory}

    def test_0000(self):
        forth = r"""
        ```
        datetime 'start !
        'delete h-method '__config @ 'values/*?confirm=YES + h-request<300
        'delete h-method '__config @ 'genres/*?confirm=YES + h-request<300
        'delete h-method '__config @ 'wheres/*?confirm=YES + h-request<300
        'delete h-method '__config @ 'spaces/*?confirm=YES + h-request<300
        'delete h-method '__config @ 'alters/*?confirm=YES + h-request<300
        'delete h-method '__config @ 'brokers/*?confirm=YES + h-request<300
        'delete h-method '__config @ 'keepers/*?confirm=YES + h-request<300

        'delete h-method '__config @ 'things/*?confirm=YES + h-request<300

        datetime 'start @ - (.total_seconds) .
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0100(self):
        forth = r"""
        ```
        ({"id":"!","name":"Energy Drinks"})
        ("'Drinks/Human major 'Energy/Sugar_Free minor") 'program s!
        ([]) swap +
        ({}) swap 'genres s! h-data
        'post h-method '__config @ 'genres + h-request
        A{ h-status -> 200 }A
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0101(self):
        forth = r"""
        ```
        'get h-method '__config @ 'genres + h-request
        A{ h-status -> 200 }A
        # one way to access index into the JSON object is the s@- operator
        A{ h-json 'genres s@- 0 s@- 'name s@- -> ("Energy Drinks") }A
        # another option is to use the json-path function to access the data
        A{ h-json '$.genres.0.name json-path0- -> ("Energy Drinks") }A
        # finally the python style index operation
        A{ h-json [ 'genres ] nip [ 0 ] nip [ 'name ] nip -> ("Energy Drinks") }A
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0102(self):
        forth = r"""
        ```
        'get h-method '__config @ 'genres + h-request
        A{ h-status -> 200 }A
        h-json 'genres s@- 0 s@- 'id s@- 'id !

        ({}) 'id @ 'id s! ("Human Energy Drinks") 'name s!

        ([]) swap +
        ({}) swap 'genres s! h-data
        'patch h-method '__config @ 'genres + h-request
        A{ h-status -> 200 }A

        'get h-method '__config @ 'genres + h-request
        A{ h-status -> 200 }A
        A{ h-json 'genres s@- 0 s@- 'name s@- -> ("Human Energy Drinks") }A
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0180(self):
        forth = r"""
        ```
        'delete h-method '__config @ 'genres/* + h-request
        A{ h-status -> 403 }A
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0181(self):
        forth = r"""
        ```
        'delete h-method '__config @ 'genres/*?confirm=YES + h-request
        A{ h-status -> 200 }A
        'get h-method '__config @ 'genres + h-request
        A{ h-json -> ({"genres":[]}) }A
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0190(self):
        forth = r"""
        ```
        ({"id":"!","name":"Energy Drinks"})
        ("'Drinks/Human major 'Energy/Sugar_Free minor") 'program s!
        ([]) swap +
        ({}) swap 'genres s! h-data
        'post h-method '__config @ 'genres + h-request
        A{ h-status -> 200 }A

        h-json 'obj_id s@- 0 s@- 'genre_id:Energy_Drinks !

        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0200(self):
        forth = r"""
        ```
        ({"id":"!", "name":"Coolamon"})
        ("'AU country 'NSW state") 'program s!
        ([]) swap +
        ({}) swap 'wheres s! h-data
        'post h-method '__config @ 'wheres + h-request
        A{ h-status -> 200 }A

        h-json 'obj_id s@- 0 s@- 'where_id:Coolamon !

        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0300(self):
        forth = r"""
        ```
        ({"id":"!", "name":"Coolamon, Energy Drinks"})
        'where_id:Coolamon @ 'where_id s!
        'genre_id:Energy_Drinks @ 'genre_id s!
        ([]) swap +
        ({}) swap 'spaces s! h-data
        'post h-method '__config @ 'spaces + h-request
        A{ h-status -> 200 }A
        h-json 'obj_id s@- 0 s@- 'space_id:Coolamon !
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory

    def test_0500(self):
        forth = r"""
        ```
        ({}) ({"mode":"verify"}) 'action s! h-data
        'post h-method '__engine @ 'MANAGE + h-request
        A{ h-status -> 200 }A
        A{ h-json 'result s@- 'issues s@- -> ([]) }A
        """
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory
