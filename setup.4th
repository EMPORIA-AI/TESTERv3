
``` >now> ~~~

'http://127.0.0.1:10000/api/engine/v1/' '__engine !
'http://127.0.0.1:10001/api/config/v1/' '__config !

datetime 'start !


'delete h-method '__config @ 'values/*?confirm=YES + h-request<300
'delete h-method '__config @ 'genres/*?confirm=YES + h-request<300
'delete h-method '__config @ 'wheres/*?confirm=YES + h-request<300
'delete h-method '__config @ 'spaces/*?confirm=YES + h-request<300
'delete h-method '__config @ 'alters/*?confirm=YES + h-request<300
'delete h-method '__config @ 'brokers/*?confirm=YES + h-request<300
'delete h-method '__config @ 'keepers/*?confirm=YES + h-request<300

'delete h-method '__config @ 'things/*?confirm=YES + h-request<300

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

