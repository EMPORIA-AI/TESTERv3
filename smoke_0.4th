
``` >now> ~~~

'http://127.0.0.1:10000/api/engine/v1/' '__engine !
'http://127.0.0.1:10001/api/config/v1/' '__config !

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


