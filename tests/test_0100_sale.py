#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: Elastic-2.0
# Copyright (c) 12020 - 12022 HE, Emporia.AI Pte Ltd

__banner__ = r""" (


     _         _____              _        ______
  /\| |/\     / ____|     /\     | |      |  ____|
  \ ` ' /    | (___      /  \    | |      | |__
 |_     _|    \___ \    / /\ \   | |      |  __|
  / , . \     ____) |  / ____ \  | |____  | |____
  \/|_|\/    |_____/  /_/    \_\ |______| |______|


)






"""  # __banner__

class TestCONFIG:

    memory = {}
    memory['__engine'] = 'https://z-enginetst-emporia.enscaled.sg/api/engine/v1/'
    memory['__config'] = 'https://z-enginetst-emporia.enscaled.sg/api/config/v1/'

    options = { "memory":memory }

    def test_0000(self):
        forth = r"""

``` >now> ~~~

datetime 'start !

({}) ({"mode":"debug"}) 'action s! h-data
'post h-method '__engine @ '/MANAGE + h-request
A{ h-status -> 200 }A

'delete h-method '__config @ 'values/*?confirm=YES + h-request<300
'delete h-method '__config @ 'genres/*?confirm=YES + h-request<300
'delete h-method '__config @ 'wheres/*?confirm=YES + h-request<300
'delete h-method '__config @ 'spaces/*?confirm=YES + h-request<300
'delete h-method '__config @ 'alters/*?confirm=YES + h-request<300
'delete h-method '__config @ 'brokers/*?confirm=YES + h-request<300
'delete h-method '__config @ 'keepers/*?confirm=YES + h-request<300

'delete h-method '__config @ 'things/*?confirm=YES + h-request<300

({"id":"manual", "storage":"true"})
([]) swap +  ({}) swap 'values s!
h-data 'post h-method '__config @ 'values + h-request<300

({"id":"!", "name":"Test Broker"})
([]) swap +  ({}) swap 'brokers s!
h-data 'post h-method '__config @ 'brokers + h-request<300
h-json 'obj_id s@- 0 s@- 'broker_id:Test !

({"id":"!", "name":"Milky Way Galaxy"})
'Galaxy 'scope s!
("'Milky'Way galaxy") 'program s!
([]) swap +  ({}) swap 'wheres s!
h-data 'post h-method '__config @ 'wheres + h-request<300
h-json 'obj_id s@- 0 s@- 'where_id:Milky_Way !

({"id":"!", "name":"Planet Earth"})
'Planet 'scope s!
'where_id:Milky_Way @ 'under_id s!
("'Earth planet") 'program s!
([]) swap +  ({}) swap 'wheres s!
h-data 'post h-method '__config @ 'wheres + h-request<300
h-json 'obj_id s@- 0 s@- 'where_id:Earth !

({"id":"!", "name":"Australia"})
'Country 'scope s!
'where_id:Earth @ 'under_id s!
("'AU country") 'program s!
([]) swap +  ({}) swap 'wheres s!
h-data 'post h-method '__config @ 'wheres + h-request<300
h-json 'obj_id s@- 0 s@- 'where_id:AU !

({"id":"!", "name":"New South Wales, AU"})
("'NSW state") 'program s!
'where_id:AU @ 'under_id s!
'State 'scope s!
([]) swap +  ({}) swap 'wheres s!
h-data 'post h-method '__config @ 'wheres + h-request<300
h-json 'obj_id s@- 0 s@- 'where_id:NSW !

({"id":"!", "name":"Coolamon"})
("'Coolamon city") 'program s!
'where_id:NSW @ 'under_id s!
'City 'scope s!
([]) swap +  ({}) swap 'wheres s!
h-data 'post h-method '__config @ 'wheres + h-request<300
h-json 'obj_id s@- 0 s@- 'where_id:Coolamon !

({"id":"!","name":"Doodads"})
("'System/Test major 'Doodads minor") 'program s!
([]) swap + ({}) swap 'genres s!
h-data 'post h-method '__config @ 'genres + h-request<300
h-json 'obj_id s@- 0 s@- 'genre_id:Doodads !

({"id":"!", "name":"Coolamon:Doodads"})
'where_id:Coolamon @ 'where_id s!
'genre_id:Doodads @ 'genre_id s!
([]) swap + ({}) swap 'spaces s!
h-data 'post h-method '__config @ 'spaces + h-request<300
h-json 'obj_id s@- 0 s@- 'space_id:Coolamon_Doodads !

({}) ({"mode":"verify"}) 'action s! h-data
'post h-method '__engine @ 'MANAGE + h-request<300
A{ h-json 'result s@- 'issues s@- -> ([]) }A

({}) ({"mode":"commit"}) 'action s! h-data
'post h-method '__engine @ 'MANAGE + h-request<300

datetime 'start @ - (.total_seconds) .

"""
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory


    def test_0001(self):
        forth = r"""


``` >now> ~~~

datetime 'start !

#
# restore defaults
#

'delete h-method '__config @ 'values/*?confirm=YES + h-request<300
'delete h-method '__config @ 'things/*?confirm=YES + h-request<300

({"id":"manual", "storage":"true"})
([]) swap +  ({}) swap 'values s!
h-data 'post h-method '__config @ 'values + h-request<300

({}) ({"mode":"touch;verify_and_commit"}) 'action s!
h-data 'post h-method '__engine @ 'MANAGE + h-request<300

#
#
#

(["values","genres","wheres","spaces","alters","brokers","keepers"]) do
  'get h-method '__config @ v + h-request<300
  ({}) h-json v s@- do v 'name s@ s! loop v !
loop

({"id":"!", "name":"Doodad #1"})
'genres 'Doodads *@ 'id s@- 'genre_id s!
S""

```
'thing_v0.1 abi

# the thing can be any color other than black
: color dup 'choices 'color *! 'black != if <true> else <false> then ;

""S
'program s!
([]) swap +  ({}) swap 'things s!

h-data 'post h-method '__config @ 'things + h-request<300

(["things"]) do
  'get h-method '__config @ v + h-request<300
  ({}) h-json v s@- do v 'name s@ s! loop v !
loop


#
# define some helper functions for later use
#

: step-next ({}) ({"mode":"step"}) 'action s!
h-data 'post h-method '__engine @ 'MANAGE + h-request<300 ;

#
#
#

({}) utc-iso 'clock s!
'spaces 'Coolamon:Doodads *@ 'id s@- 'space_id s!
h-data 'post h-method '__engine @ '0.SETUP + h-request<300
h-json 'handle s@- 'supply_handle !

({}) utc-iso 'clock s!
'spaces 'Coolamon:Doodads *@ 'id s@- 'space_id s!
h-data 'post h-method '__engine @ '0.SETUP + h-request<300
h-json 'handle s@- 'demand_handle !

step-next

#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
h-data 'post h-method '__engine @ '1.ENTER + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
h-data 'post h-method '__engine @ '1.ENTER + h-request<300

step-next

#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
({}) ulid 'id s! ({"value":10}) 'price s!
'wheres 'Coolamon *@ 'id s@- 'where_id s!
'things 'Doodad'#1 *@ 'id s@- 'thing_id s!

([]) swap + 'supply s!
h-data 'post h-method '__engine @ '2.OFFER + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
({}) ulid 'id s! ({"value":10}) 'price s!
'wheres 'Coolamon *@ 'id s@- 'where_id s!

S""

```

'demand_v0.1 abi
: inspect-thing
'thing @ (.color 'red )- not if stop then
<true> 'buy ! ;

""S

'program s!
([]) swap + 'demand s!
h-data 'post h-method '__engine @ '2.OFFER + h-request<300

step-next

#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
h-data 'post h-method '__engine @ '3.THINK + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
h-data 'post h-method '__engine @ '3.THINK + h-request<300

step-next


#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
h-data 'post h-method '__engine @ '4.LEAVE + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
h-data 'post h-method '__engine @ '4.LEAVE + h-request<300
h-json cr .

step-next

datetime 'start @ - (.total_seconds) cr cr .


"""
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory



    def test_0002(self):
        forth = r"""


``` >now> ~~~

datetime 'start !

#
# restore defaults
#

'delete h-method '__config @ 'values/*?confirm=YES + h-request<300
'delete h-method '__config @ 'things/*?confirm=YES + h-request<300

({"id":"manual", "storage":"true"})
([]) swap +  ({}) swap 'values s!
h-data 'post h-method '__config @ 'values + h-request<300

({}) ({"mode":"touch;verify_and_commit"}) 'action s!
h-data 'post h-method '__engine @ 'MANAGE + h-request<300

#
#
#

(["values","genres","wheres","spaces","alters","brokers","keepers"]) do
  'get h-method '__config @ v + h-request<300
  ({}) h-json v s@- do v 'name s@ s! loop v !
loop

({"id":"!", "name":"Doodad #1"})
'genres 'Doodads *@ 'id s@- 'genre_id s!
S""

```
'thing_v0.1 abi

# the thing can be any color other than black
: color dup 'choices 'color *! 'black != if <true> else <false> then ;

""S
'program s!
([]) swap +  ({}) swap 'things s!

h-data 'post h-method '__config @ 'things + h-request<300

(["things"]) do
  'get h-method '__config @ v + h-request<300
  ({}) h-json v s@- do v 'name s@ s! loop v !
loop


#
# define some helper functions for later use
#

: step-next ({}) ({"mode":"step"}) 'action s!
h-data 'post h-method '__engine @ 'MANAGE + h-request<300 ;

#
#
#

({}) utc-iso 'clock s!
'spaces 'Coolamon:Doodads *@ 'id s@- 'space_id s!
h-data 'post h-method '__engine @ '0.SETUP + h-request<300
h-json 'handle s@- 'supply_handle !

({}) utc-iso 'clock s!
'spaces 'Coolamon:Doodads *@ 'id s@- 'space_id s!
h-data 'post h-method '__engine @ '0.SETUP + h-request<300
h-json 'handle s@- 'demand_handle !

step-next

#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
h-data 'post h-method '__engine @ '1.ENTER + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
h-data 'post h-method '__engine @ '1.ENTER + h-request<300

step-next

#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
({}) ulid 'id s! ({"value":10}) 'price s!
'wheres 'Coolamon *@ 'id s@- 'where_id s!
'things 'Doodad'#1 *@ 'id s@- 'thing_id s!

([]) swap + 'supply s!
h-data 'post h-method '__engine @ '2.OFFER + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
({}) ulid 'id s! ({"value":10}) 'price s!
'wheres 'Coolamon *@ 'id s@- 'where_id s!

S""

```

'demand_v0.1 abi
: inspect-thing
'thing @ (.color 'red )- not if stop then
<true> 'buy ! ;

""S

'program s!
([]) swap + 'demand s!
h-data 'post h-method '__engine @ '2.OFFER + h-request<300

step-next

#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
h-data 'post h-method '__engine @ '3.THINK + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
h-data 'post h-method '__engine @ '3.THINK + h-request<300

step-next


#
#
#

({}) utc-iso 'clock s! 'supply_handle @ 'handle s!
h-data 'post h-method '__engine @ '4.LEAVE + h-request<300

({}) utc-iso 'clock s! 'demand_handle @ 'handle s!
h-data 'post h-method '__engine @ '4.LEAVE + h-request<300
h-json cr .

step-next

datetime 'start @ - (.total_seconds) cr cr .


"""
        e = FORTH.Engine(forth, **self.options)
        self.options["memory"] = e.root.memory


import requests
from cubed4th import FORTH

from icecream import install as install_icecream
install_icecream()


