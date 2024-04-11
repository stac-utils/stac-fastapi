window.BENCHMARK_DATA = {
  "lastUpdate": 1712847313277,
  "repoUrl": "https://github.com/stac-utils/stac-fastapi",
  "entries": {
    "STAC FastAPI Benchmarks": [
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "Vincent Sarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "11e9c0facf89503c0cfdea3c08ef7f78e55bcf2e",
          "message": "update benchmark names (#652)",
          "timestamp": "2024-04-09T15:19:11Z",
          "tree_id": "43593e9481c5507a55812921fd12612ffbacce59",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/11e9c0facf89503c0cfdea3c08ef7f78e55bcf2e"
        },
        "date": 1712676083965,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 527.7749281174372,
            "unit": "iter/sec",
            "range": "stddev: 0.00010762592013021027",
            "extra": "mean: 1.8947470725200617 msec\nrounds: 262"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 168.39912071056335,
            "unit": "iter/sec",
            "range": "stddev: 0.002320333507908453",
            "extra": "mean: 5.93827328658535 msec\nrounds: 164"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.83903899183078,
            "unit": "iter/sec",
            "range": "stddev: 0.00035929820380766137",
            "extra": "mean: 23.343194047623143 msec\nrounds: 42"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 20.94532048692271,
            "unit": "iter/sec",
            "range": "stddev: 0.009669998523020288",
            "extra": "mean: 47.74336113044218 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.961354908380075,
            "unit": "iter/sec",
            "range": "stddev: 0.009698771778498587",
            "extra": "mean: 91.22959783333802 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.661779967008748,
            "unit": "iter/sec",
            "range": "stddev: 0.011243068117186592",
            "extra": "mean: 115.44971170000053 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2026256691798802,
            "unit": "iter/sec",
            "range": "stddev: 0.018684187654038845",
            "extra": "mean: 454.0036075999865 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 861.3076568920264,
            "unit": "iter/sec",
            "range": "stddev: 0.00009518101514619151",
            "extra": "mean: 1.1610253223667324 msec\nrounds: 608"
          },
          {
            "name": "Items Limit: (10)",
            "value": 508.5649817285752,
            "unit": "iter/sec",
            "range": "stddev: 0.00006935406193698263",
            "extra": "mean: 1.966317060606637 msec\nrounds: 429"
          },
          {
            "name": "Items Limit: (50)",
            "value": 167.8996576165884,
            "unit": "iter/sec",
            "range": "stddev: 0.002309538190994903",
            "extra": "mean: 5.955938291926574 msec\nrounds: 161"
          },
          {
            "name": "Items Limit: (100)",
            "value": 96.81513144652318,
            "unit": "iter/sec",
            "range": "stddev: 0.00014507972078097478",
            "extra": "mean: 10.32896392391266 msec\nrounds: 92"
          },
          {
            "name": "Items Limit: (200)",
            "value": 49.54673464096578,
            "unit": "iter/sec",
            "range": "stddev: 0.0009199674121948462",
            "extra": "mean: 20.182964775506903 msec\nrounds: 49"
          },
          {
            "name": "Items Limit: (250)",
            "value": 38.419258621536585,
            "unit": "iter/sec",
            "range": "stddev: 0.0012518668905287667",
            "extra": "mean: 26.028612625008662 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.113435882531432,
            "unit": "iter/sec",
            "range": "stddev: 0.009769169521345036",
            "extra": "mean: 98.8783645454522 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 647.9775036453324,
            "unit": "iter/sec",
            "range": "stddev: 0.00010962172267970713",
            "extra": "mean: 1.5432634533981375 msec\nrounds: 397"
          },
          {
            "name": "Collection",
            "value": 924.5967243947525,
            "unit": "iter/sec",
            "range": "stddev: 0.0001033740217755108",
            "extra": "mean: 1.0815526094953525 msec\nrounds: 653"
          },
          {
            "name": "Collections With Model validation",
            "value": 164.62298959215232,
            "unit": "iter/sec",
            "range": "stddev: 0.0011424404320429194",
            "extra": "mean: 6.074485723272702 msec\nrounds: 159"
          },
          {
            "name": "Collections",
            "value": 484.3006447932511,
            "unit": "iter/sec",
            "range": "stddev: 0.00014619355216128255",
            "extra": "mean: 2.064833096447563 msec\nrounds: 394"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "StijnCaerts@users.noreply.github.com",
            "name": "Stijn Caerts",
            "username": "StijnCaerts"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "313486b2f790237a544bafc2db2a3810b13d521d",
          "message": "add items link to inferred link relations (#634) (#640)\n\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-09T18:07:45+02:00",
          "tree_id": "bfb448c842d09e999f718b9d6cb92a7d45544b45",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/313486b2f790237a544bafc2db2a3810b13d521d"
        },
        "date": 1712678999936,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 546.891082110363,
            "unit": "iter/sec",
            "range": "stddev: 0.00008917248725177463",
            "extra": "mean: 1.8285176568269577 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 172.63863801316222,
            "unit": "iter/sec",
            "range": "stddev: 0.002571794760136628",
            "extra": "mean: 5.792446068323121 msec\nrounds: 161"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.79776597088597,
            "unit": "iter/sec",
            "range": "stddev: 0.0002655677392835872",
            "extra": "mean: 22.832214790698178 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.69967380211941,
            "unit": "iter/sec",
            "range": "stddev: 0.00793593460598682",
            "extra": "mean: 46.08364204545461 msec\nrounds: 22"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.973391980049664,
            "unit": "iter/sec",
            "range": "stddev: 0.010130127468444376",
            "extra": "mean: 91.129525111111 msec\nrounds: 9"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.717542446047576,
            "unit": "iter/sec",
            "range": "stddev: 0.014752458453130163",
            "extra": "mean: 114.71122810000054 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.240977516831022,
            "unit": "iter/sec",
            "range": "stddev: 0.018729648768988985",
            "extra": "mean: 446.2338388000006 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 796.362119319854,
            "unit": "iter/sec",
            "range": "stddev: 0.000291600033954957",
            "extra": "mean: 1.2557101546392817 msec\nrounds: 582"
          },
          {
            "name": "Items Limit: (10)",
            "value": 490.76207931442434,
            "unit": "iter/sec",
            "range": "stddev: 0.00008239951214407556",
            "extra": "mean: 2.037647247311694 msec\nrounds: 372"
          },
          {
            "name": "Items Limit: (50)",
            "value": 175.43610192251674,
            "unit": "iter/sec",
            "range": "stddev: 0.0000892090606999054",
            "extra": "mean: 5.70008104968988 msec\nrounds: 161"
          },
          {
            "name": "Items Limit: (100)",
            "value": 97.91152559762618,
            "unit": "iter/sec",
            "range": "stddev: 0.0001917271184251501",
            "extra": "mean: 10.213302202128537 msec\nrounds: 94"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.739890298084354,
            "unit": "iter/sec",
            "range": "stddev: 0.004139187863920684",
            "extra": "mean: 19.708359519999874 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.78557922235975,
            "unit": "iter/sec",
            "range": "stddev: 0.0003209586550825476",
            "extra": "mean: 23.93170128571278 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.037807044346872,
            "unit": "iter/sec",
            "range": "stddev: 0.010499050264610937",
            "extra": "mean: 99.6233535454523 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 670.7726264705393,
            "unit": "iter/sec",
            "range": "stddev: 0.0000600069008288277",
            "extra": "mean: 1.4908181409575165 msec\nrounds: 376"
          },
          {
            "name": "Collection",
            "value": 968.1805531230403,
            "unit": "iter/sec",
            "range": "stddev: 0.00007691986982613142",
            "extra": "mean: 1.0328651993415074 msec\nrounds: 607"
          },
          {
            "name": "Collections With Model validation",
            "value": 171.26882657733844,
            "unit": "iter/sec",
            "range": "stddev: 0.0025291206392790365",
            "extra": "mean: 5.8387741656444305 msec\nrounds: 163"
          },
          {
            "name": "Collections",
            "value": 499.25718630006986,
            "unit": "iter/sec",
            "range": "stddev: 0.00007564049477526484",
            "extra": "mean: 2.002975675544843 msec\nrounds: 413"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "chris@rdrn.me",
            "name": "Chris Arderne",
            "username": "carderne"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "397de7ec94c1659ba74b492a57c2288ee031e134",
          "message": "Properly type bbox and datetime (#490)\n\n* Set BBox and DateTimeType at API surface\r\n\r\n* replace conint usage\r\n\r\n* update CHANGES.md\r\n\r\n---------\r\n\r\nCo-authored-by: Pete Gadomski <pete.gadomski@gmail.com>\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-09T18:14:54+02:00",
          "tree_id": "d6710d367b8e14c032886cd9c19a456c2bd5eefe",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/397de7ec94c1659ba74b492a57c2288ee031e134"
        },
        "date": 1712679425722,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 551.2349648760971,
            "unit": "iter/sec",
            "range": "stddev: 0.00010560445598849305",
            "extra": "mean: 1.8141084360001969 msec\nrounds: 250"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 166.93780508120847,
            "unit": "iter/sec",
            "range": "stddev: 0.00230036645930884",
            "extra": "mean: 5.990254870749862 msec\nrounds: 147"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.51703928168271,
            "unit": "iter/sec",
            "range": "stddev: 0.00013895823821702443",
            "extra": "mean: 22.979504499997596 msec\nrounds: 42"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.890644648872122,
            "unit": "iter/sec",
            "range": "stddev: 0.006007666136695695",
            "extra": "mean: 45.68161495653 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.057215987991228,
            "unit": "iter/sec",
            "range": "stddev: 0.009284304793366564",
            "extra": "mean: 90.43867833332166 msec\nrounds: 9"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.634427177681415,
            "unit": "iter/sec",
            "range": "stddev: 0.013386501183111157",
            "extra": "mean: 115.81544200000167 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.1942193683942417,
            "unit": "iter/sec",
            "range": "stddev: 0.024871714406240402",
            "extra": "mean: 455.7429464000279 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 871.1329375192103,
            "unit": "iter/sec",
            "range": "stddev: 0.00006934203814821149",
            "extra": "mean: 1.1479304213290042 msec\nrounds: 572"
          },
          {
            "name": "Items Limit: (10)",
            "value": 468.9434280566169,
            "unit": "iter/sec",
            "range": "stddev: 0.00016549162533985206",
            "extra": "mean: 2.1324533838637505 msec\nrounds: 409"
          },
          {
            "name": "Items Limit: (50)",
            "value": 172.05951874014218,
            "unit": "iter/sec",
            "range": "stddev: 0.00016427818049363758",
            "extra": "mean: 5.81194232857456 msec\nrounds: 140"
          },
          {
            "name": "Items Limit: (100)",
            "value": 95.81251147811058,
            "unit": "iter/sec",
            "range": "stddev: 0.0003076221781841565",
            "extra": "mean: 10.43705028260804 msec\nrounds: 92"
          },
          {
            "name": "Items Limit: (200)",
            "value": 48.22448094197034,
            "unit": "iter/sec",
            "range": "stddev: 0.005282687542032095",
            "extra": "mean: 20.736355901960327 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 39.59623055397195,
            "unit": "iter/sec",
            "range": "stddev: 0.0010980744982447296",
            "extra": "mean: 25.25492921951099 msec\nrounds: 41"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 9.92477371597016,
            "unit": "iter/sec",
            "range": "stddev: 0.012823119025464198",
            "extra": "mean: 100.75796472728432 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 676.1512835912655,
            "unit": "iter/sec",
            "range": "stddev: 0.00011694506649285629",
            "extra": "mean: 1.478958961208601 msec\nrounds: 464"
          },
          {
            "name": "Collection",
            "value": 969.2774027576127,
            "unit": "iter/sec",
            "range": "stddev: 0.00010012755859285501",
            "extra": "mean: 1.03169639275091 msec\nrounds: 662"
          },
          {
            "name": "Collections With Model validation",
            "value": 167.869631024004,
            "unit": "iter/sec",
            "range": "stddev: 0.002598629882384942",
            "extra": "mean: 5.95700362179868 msec\nrounds: 156"
          },
          {
            "name": "Collections",
            "value": 490.3696507079259,
            "unit": "iter/sec",
            "range": "stddev: 0.00018044230119868067",
            "extra": "mean: 2.039277917294315 msec\nrounds: 399"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "42484306+zachcoleman@users.noreply.github.com",
            "name": "Zachary Coleman",
            "username": "zachcoleman"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "d18f2d6af6996e8c4c1cd7429dd748ec110c5e66",
          "message": "`base_url` usage on landing page (#635)\n\n* base_url usage\r\n\r\n* pre-commit formatting\r\n\r\n---------\r\n\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-09T20:14:44+02:00",
          "tree_id": "f14ca2e74945965cc4cf4131b2e64dd4dd2772ac",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/d18f2d6af6996e8c4c1cd7429dd748ec110c5e66"
        },
        "date": 1712686627941,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 580.3947754794394,
            "unit": "iter/sec",
            "range": "stddev: 0.00007540810987273214",
            "extra": "mean: 1.7229651992886093 msec\nrounds: 281"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.52183879044216,
            "unit": "iter/sec",
            "range": "stddev: 0.0019232269951859776",
            "extra": "mean: 5.864351493587405 msec\nrounds: 156"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.884164631681344,
            "unit": "iter/sec",
            "range": "stddev: 0.0012807980412075255",
            "extra": "mean: 22.787262977271507 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.737368601239496,
            "unit": "iter/sec",
            "range": "stddev: 0.000478069662183187",
            "extra": "mean: 43.98046306666667 msec\nrounds: 15"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.286623442401323,
            "unit": "iter/sec",
            "range": "stddev: 0.007848176576944395",
            "extra": "mean: 88.60045744444909 msec\nrounds: 9"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.869637824863842,
            "unit": "iter/sec",
            "range": "stddev: 0.010622475027319174",
            "extra": "mean: 112.74417509999637 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2476705186573755,
            "unit": "iter/sec",
            "range": "stddev: 0.012615582307550765",
            "extra": "mean: 444.90506580000897 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 841.4645089977914,
            "unit": "iter/sec",
            "range": "stddev: 0.000945495279960743",
            "extra": "mean: 1.1884042515245579 msec\nrounds: 656"
          },
          {
            "name": "Items Limit: (10)",
            "value": 491.8076164780195,
            "unit": "iter/sec",
            "range": "stddev: 0.00009740297019565113",
            "extra": "mean: 2.033315399141838 msec\nrounds: 466"
          },
          {
            "name": "Items Limit: (50)",
            "value": 178.2158616295371,
            "unit": "iter/sec",
            "range": "stddev: 0.0001317175227787436",
            "extra": "mean: 5.61117282634882 msec\nrounds: 167"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.14658762799503,
            "unit": "iter/sec",
            "range": "stddev: 0.0002003625702885548",
            "extra": "mean: 10.188841244183644 msec\nrounds: 86"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.96935177199928,
            "unit": "iter/sec",
            "range": "stddev: 0.003962922266944644",
            "extra": "mean: 19.619633470586216 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 42.57043384210463,
            "unit": "iter/sec",
            "range": "stddev: 0.00023021640648056765",
            "extra": "mean: 23.490481767440716 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.70928921195462,
            "unit": "iter/sec",
            "range": "stddev: 0.007438948903728678",
            "extra": "mean: 93.3768787272749 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 692.84934372152,
            "unit": "iter/sec",
            "range": "stddev: 0.00005552380911640021",
            "extra": "mean: 1.443315215727381 msec\nrounds: 496"
          },
          {
            "name": "Collection",
            "value": 896.6933329595298,
            "unit": "iter/sec",
            "range": "stddev: 0.000977977085431094",
            "extra": "mean: 1.1152084701014864 msec\nrounds: 602"
          },
          {
            "name": "Collections With Model validation",
            "value": 178.61104497769875,
            "unit": "iter/sec",
            "range": "stddev: 0.0001524298812925397",
            "extra": "mean: 5.598757905060459 msec\nrounds: 158"
          },
          {
            "name": "Collections",
            "value": 503.0610515994516,
            "unit": "iter/sec",
            "range": "stddev: 0.00009878260236299887",
            "extra": "mean: 1.9878302977751143 msec\nrounds: 450"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "34507919+rhysrevans3@users.noreply.github.com",
            "name": "rhysrevans3",
            "username": "rhysrevans3"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "6e74b21c07c5b79b13a55b6f76bd87157cf69fdd",
          "message": "Update collection update endpoint. (#631)\n\n* Update collection update endpoint.\r\n\r\n* Fixing line length.\r\n\r\n* Updating registration and tests.\r\n\r\n* Adding tests to make file.\r\n\r\n* Registry and async update_collection fix.\r\n\r\n* Fixing pre-commit error.\r\n\r\n---------\r\n\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-09T20:21:15+02:00",
          "tree_id": "16d278cd7139d94bf2e4251d408095eda26d13c9",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/6e74b21c07c5b79b13a55b6f76bd87157cf69fdd"
        },
        "date": 1712687008630,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 557.2138481549724,
            "unit": "iter/sec",
            "range": "stddev: 0.0000958340466798591",
            "extra": "mean: 1.7946431218663463 msec\nrounds: 279"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 168.44226249438222,
            "unit": "iter/sec",
            "range": "stddev: 0.0018772868357377654",
            "extra": "mean: 5.936752363637667 msec\nrounds: 154"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.919277831414085,
            "unit": "iter/sec",
            "range": "stddev: 0.003779138689658912",
            "extra": "mean: 23.299553266669033 msec\nrounds: 45"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.0551832748767,
            "unit": "iter/sec",
            "range": "stddev: 0.005314622451979813",
            "extra": "mean: 45.3408156956515 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.096695907194874,
            "unit": "iter/sec",
            "range": "stddev: 0.009138360549513357",
            "extra": "mean: 90.11691483332622 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.934650796316765,
            "unit": "iter/sec",
            "range": "stddev: 0.009909581740049843",
            "extra": "mean: 111.92379230000142 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2568304788934412,
            "unit": "iter/sec",
            "range": "stddev: 0.016333530847793053",
            "extra": "mean: 443.0992976000198 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 870.7182028315648,
            "unit": "iter/sec",
            "range": "stddev: 0.0000736581229754758",
            "extra": "mean: 1.1484771958918654 msec\nrounds: 633"
          },
          {
            "name": "Items Limit: (10)",
            "value": 478.13817884153207,
            "unit": "iter/sec",
            "range": "stddev: 0.0000932070590498217",
            "extra": "mean: 2.0914456202239964 msec\nrounds: 445"
          },
          {
            "name": "Items Limit: (50)",
            "value": 176.5204637406362,
            "unit": "iter/sec",
            "range": "stddev: 0.000046609186423876614",
            "extra": "mean: 5.665065561289896 msec\nrounds: 155"
          },
          {
            "name": "Items Limit: (100)",
            "value": 97.84957883819604,
            "unit": "iter/sec",
            "range": "stddev: 0.00018676059411502384",
            "extra": "mean: 10.219768054940726 msec\nrounds: 91"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.449713294690014,
            "unit": "iter/sec",
            "range": "stddev: 0.0036846697711104617",
            "extra": "mean: 19.821718196072545 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.40081180546406,
            "unit": "iter/sec",
            "range": "stddev: 0.0036464124982998457",
            "extra": "mean: 24.154115738088507 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.74972226797715,
            "unit": "iter/sec",
            "range": "stddev: 0.007157433427913708",
            "extra": "mean: 93.0256591818141 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 668.6300067769258,
            "unit": "iter/sec",
            "range": "stddev: 0.00008260817861189766",
            "extra": "mean: 1.4955954561782456 msec\nrounds: 502"
          },
          {
            "name": "Collection",
            "value": 943.8524272148483,
            "unit": "iter/sec",
            "range": "stddev: 0.00007726074793805046",
            "extra": "mean: 1.0594876605348509 msec\nrounds: 816"
          },
          {
            "name": "Collections With Model validation",
            "value": 175.375663386576,
            "unit": "iter/sec",
            "range": "stddev: 0.00007144726909915245",
            "extra": "mean: 5.702045430304238 msec\nrounds: 165"
          },
          {
            "name": "Collections",
            "value": 493.04149021548756,
            "unit": "iter/sec",
            "range": "stddev: 0.00008106536184598068",
            "extra": "mean: 2.0282268730831197 msec\nrounds: 457"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jpolchlo@users.noreply.github.com",
            "name": "jpolchlo",
            "username": "jpolchlo"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "53711ecb21cd914f34a3efc72a1cd934d351a99f",
          "message": "Allow intersects search to use GeometryCollection (#548)\n\n* Include GeometryCollection as a valid input type ; queries can now be made with a GeometryCollection type to the 'intersects' query without raising a 400 error; has not been tested to show that the intersection is correct\r\n\r\n* Fix format problems to satisfy black\r\n\r\n* Add tests\r\n\r\n* Whoops, formatting\r\n\r\n* Update changelog\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-10T09:44:58+02:00",
          "tree_id": "fa4864c6b8dc23801a80708f381683aa5b54a93e",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/53711ecb21cd914f34a3efc72a1cd934d351a99f"
        },
        "date": 1712735234620,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 578.9120083753055,
            "unit": "iter/sec",
            "range": "stddev: 0.00008474886953468366",
            "extra": "mean: 1.7273782293900966 msec\nrounds: 279"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 172.917767960883,
            "unit": "iter/sec",
            "range": "stddev: 0.00205420575704252",
            "extra": "mean: 5.7830956979864405 msec\nrounds: 149"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.55702657679442,
            "unit": "iter/sec",
            "range": "stddev: 0.003442065273202767",
            "extra": "mean: 22.958408288888183 msec\nrounds: 45"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.670797045327216,
            "unit": "iter/sec",
            "range": "stddev: 0.0054840954805668845",
            "extra": "mean: 44.10960929166426 msec\nrounds: 24"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.026003307212022,
            "unit": "iter/sec",
            "range": "stddev: 0.012470561671476147",
            "extra": "mean: 90.6946943636329 msec\nrounds: 11"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.001742210690024,
            "unit": "iter/sec",
            "range": "stddev: 0.010777319202918077",
            "extra": "mean: 111.08960650000057 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.237484706042475,
            "unit": "iter/sec",
            "range": "stddev: 0.01909903974848825",
            "extra": "mean: 446.9304292000004 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 886.9779813624903,
            "unit": "iter/sec",
            "range": "stddev: 0.00007035712270118322",
            "extra": "mean: 1.1274237027438903 msec\nrounds: 656"
          },
          {
            "name": "Items Limit: (10)",
            "value": 512.4659468555355,
            "unit": "iter/sec",
            "range": "stddev: 0.00007649733016786799",
            "extra": "mean: 1.9513491699027965 msec\nrounds: 412"
          },
          {
            "name": "Items Limit: (50)",
            "value": 180.11040329099401,
            "unit": "iter/sec",
            "range": "stddev: 0.00010702738033690026",
            "extra": "mean: 5.552150135294282 msec\nrounds: 170"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.89095910031182,
            "unit": "iter/sec",
            "range": "stddev: 0.00009152865505194466",
            "extra": "mean: 10.112147855555047 msec\nrounds: 90"
          },
          {
            "name": "Items Limit: (200)",
            "value": 49.85694658738799,
            "unit": "iter/sec",
            "range": "stddev: 0.004824466162499834",
            "extra": "mean: 20.057385549017233 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 40.23085304301196,
            "unit": "iter/sec",
            "range": "stddev: 0.004287216076027036",
            "extra": "mean: 24.856544774998213 msec\nrounds: 40"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.546191394076704,
            "unit": "iter/sec",
            "range": "stddev: 0.008335457059280805",
            "extra": "mean: 94.8209607272681 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 644.3969349754415,
            "unit": "iter/sec",
            "range": "stddev: 0.0011696696385023707",
            "extra": "mean: 1.551838541935509 msec\nrounds: 465"
          },
          {
            "name": "Collection",
            "value": 927.9485073147459,
            "unit": "iter/sec",
            "range": "stddev: 0.00007959734220121938",
            "extra": "mean: 1.0776460031104023 msec\nrounds: 643"
          },
          {
            "name": "Collections With Model validation",
            "value": 179.85107029907832,
            "unit": "iter/sec",
            "range": "stddev: 0.00022672228195996373",
            "extra": "mean: 5.560155957576887 msec\nrounds: 165"
          },
          {
            "name": "Collections",
            "value": 484.4662005022205,
            "unit": "iter/sec",
            "range": "stddev: 0.00006510012405585558",
            "extra": "mean: 2.0641274849790405 msec\nrounds: 466"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "Vincent Sarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8169e86092e945e069f072589c0c8721f6ba0cb4",
          "message": "add python 3.12 support and some docker cleanup (#654)\n\n* add python 3.12 support and some docker cleanup\r\n\r\n* :facepalm:",
          "timestamp": "2024-04-10T19:18:26+02:00",
          "tree_id": "7772184b30eb30578849dfc7fd64fb15a09df5bc",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/8169e86092e945e069f072589c0c8721f6ba0cb4"
        },
        "date": 1712769599414,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 541.3136047518313,
            "unit": "iter/sec",
            "range": "stddev: 0.00011777426038641354",
            "extra": "mean: 1.8473579662910122 msec\nrounds: 267"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.51056137032054,
            "unit": "iter/sec",
            "range": "stddev: 0.002137374272645706",
            "extra": "mean: 5.864739356691029 msec\nrounds: 157"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.00422600868091,
            "unit": "iter/sec",
            "range": "stddev: 0.004148684813614164",
            "extra": "mean: 23.253528613632955 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.745775927461363,
            "unit": "iter/sec",
            "range": "stddev: 0.006627974025418748",
            "extra": "mean: 45.9859424347863 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.882210237258958,
            "unit": "iter/sec",
            "range": "stddev: 0.010606716518526951",
            "extra": "mean: 91.89309691666854 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.546935715427962,
            "unit": "iter/sec",
            "range": "stddev: 0.014187539112804086",
            "extra": "mean: 117.00099700000237 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.225739013515792,
            "unit": "iter/sec",
            "range": "stddev: 0.019165228933555663",
            "extra": "mean: 449.2889749999904 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 840.1467464041915,
            "unit": "iter/sec",
            "range": "stddev: 0.00008286507862587914",
            "extra": "mean: 1.1902682528736517 msec\nrounds: 609"
          },
          {
            "name": "Items Limit: (10)",
            "value": 489.0859882537419,
            "unit": "iter/sec",
            "range": "stddev: 0.00009559989830311137",
            "extra": "mean: 2.0446302368433247 msec\nrounds: 418"
          },
          {
            "name": "Items Limit: (50)",
            "value": 175.8674128897599,
            "unit": "iter/sec",
            "range": "stddev: 0.00011832405788010052",
            "extra": "mean: 5.686101726115892 msec\nrounds: 157"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.90486062649623,
            "unit": "iter/sec",
            "range": "stddev: 0.00010897765866353444",
            "extra": "mean: 10.11072654736752 msec\nrounds: 95"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.5096935168176,
            "unit": "iter/sec",
            "range": "stddev: 0.0038270687486433013",
            "extra": "mean: 19.41382158823186 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 39.50898927996427,
            "unit": "iter/sec",
            "range": "stddev: 0.005103370324835229",
            "extra": "mean: 25.310695571428305 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.365121789583098,
            "unit": "iter/sec",
            "range": "stddev: 0.008170294394851788",
            "extra": "mean: 96.47739990908701 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 682.9690122328539,
            "unit": "iter/sec",
            "range": "stddev: 0.00006546583224048563",
            "extra": "mean: 1.4641952740003035 msec\nrounds: 500"
          },
          {
            "name": "Collection",
            "value": 973.7132417191896,
            "unit": "iter/sec",
            "range": "stddev: 0.00007575180537117014",
            "extra": "mean: 1.026996406287336 msec\nrounds: 795"
          },
          {
            "name": "Collections With Model validation",
            "value": 178.13208027545167,
            "unit": "iter/sec",
            "range": "stddev: 0.00006181912941573988",
            "extra": "mean: 5.61381194478651 msec\nrounds: 163"
          },
          {
            "name": "Collections",
            "value": 495.10214554484054,
            "unit": "iter/sec",
            "range": "stddev: 0.00008452543828261583",
            "extra": "mean: 2.019785228156382 msec\nrounds: 412"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "fabian.schindler.strauss@gmail.com",
            "name": "Fabian Schindler",
            "username": "constantinius"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a262115a1fee156525ada07c1e712735282c7cb4",
          "message": "Adding queryables link to landing page (#587)\n\n* Adding queryables link to landing page\r\n\r\n* Adding info to changelog\r\n\r\n* Fixing schemajson -> jsonschema\r\n\r\n* use `extension_is_enabled`\r\n\r\n---------\r\n\r\nCo-authored-by: Pete Gadomski <pete.gadomski@gmail.com>\r\nCo-authored-by: Vincent Sarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-10T19:27:03+02:00",
          "tree_id": "dc3aa0bca91846d133578402f858296a3b2d8e64",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/a262115a1fee156525ada07c1e712735282c7cb4"
        },
        "date": 1712770123127,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 539.6976870770958,
            "unit": "iter/sec",
            "range": "stddev: 0.00028590200402184404",
            "extra": "mean: 1.852889171002043 msec\nrounds: 269"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 168.01943789751078,
            "unit": "iter/sec",
            "range": "stddev: 0.002333095777625076",
            "extra": "mean: 5.951692331038414 msec\nrounds: 145"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.302564462918184,
            "unit": "iter/sec",
            "range": "stddev: 0.00028214788267544034",
            "extra": "mean: 22.572056767436408 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.57642212569459,
            "unit": "iter/sec",
            "range": "stddev: 0.007850222210377667",
            "extra": "mean: 46.346887086952925 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.387506928990472,
            "unit": "iter/sec",
            "range": "stddev: 0.00766167050909061",
            "extra": "mean: 87.81553383332626 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.094587893051903,
            "unit": "iter/sec",
            "range": "stddev: 0.010475825043778876",
            "extra": "mean: 109.95550449998746 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2615759515926035,
            "unit": "iter/sec",
            "range": "stddev: 0.01787376942640404",
            "extra": "mean: 442.16954079998914 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 822.229421298401,
            "unit": "iter/sec",
            "range": "stddev: 0.00007989636568097764",
            "extra": "mean: 1.2162055675663825 msec\nrounds: 629"
          },
          {
            "name": "Items Limit: (10)",
            "value": 487.3712493902825,
            "unit": "iter/sec",
            "range": "stddev: 0.00010874978021470067",
            "extra": "mean: 2.051823945813449 msec\nrounds: 406"
          },
          {
            "name": "Items Limit: (50)",
            "value": 177.6778213988139,
            "unit": "iter/sec",
            "range": "stddev: 0.00007825796162713616",
            "extra": "mean: 5.62816446153631 msec\nrounds: 169"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.15799439081415,
            "unit": "iter/sec",
            "range": "stddev: 0.00009738282548389714",
            "extra": "mean: 10.187657217388931 msec\nrounds: 92"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.846767630540164,
            "unit": "iter/sec",
            "range": "stddev: 0.00021617526361229682",
            "extra": "mean: 19.287605490201347 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 42.24477838774309,
            "unit": "iter/sec",
            "range": "stddev: 0.0004200066783711172",
            "extra": "mean: 23.671564585367555 msec\nrounds: 41"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.354432117242029,
            "unit": "iter/sec",
            "range": "stddev: 0.010188044790403186",
            "extra": "mean: 96.57700090909057 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 689.4118639895952,
            "unit": "iter/sec",
            "range": "stddev: 0.00008219619503519952",
            "extra": "mean: 1.4505117365010887 msec\nrounds: 463"
          },
          {
            "name": "Collection",
            "value": 953.4279956410422,
            "unit": "iter/sec",
            "range": "stddev: 0.00009080320017264046",
            "extra": "mean: 1.0488469025158473 msec\nrounds: 636"
          },
          {
            "name": "Collections With Model validation",
            "value": 174.14870399560203,
            "unit": "iter/sec",
            "range": "stddev: 0.002140201726317087",
            "extra": "mean: 5.7422190177496475 msec\nrounds: 169"
          },
          {
            "name": "Collections",
            "value": 486.9886822472297,
            "unit": "iter/sec",
            "range": "stddev: 0.00010801030434450274",
            "extra": "mean: 2.053435811660875 msec\nrounds: 446"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "Vincent Sarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "315cfaefef2ab2773ae087228439ba0371fb7372",
          "message": "replace inexistent enum with string while we wait for stac-pydantic update (#656)",
          "timestamp": "2024-04-11T12:19:03+08:00",
          "tree_id": "384826e240bbea43dd5dade34fbbb964cd116d40",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/315cfaefef2ab2773ae087228439ba0371fb7372"
        },
        "date": 1712809237393,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 555.1316537018184,
            "unit": "iter/sec",
            "range": "stddev: 0.00009872372353707584",
            "extra": "mean: 1.8013744907746452 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.13780084335488,
            "unit": "iter/sec",
            "range": "stddev: 0.0018786551114213144",
            "extra": "mean: 5.8775886078408615 msec\nrounds: 153"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.476677394949874,
            "unit": "iter/sec",
            "range": "stddev: 0.004001286013935741",
            "extra": "mean: 23.54233102325682 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.13372133939264,
            "unit": "iter/sec",
            "range": "stddev: 0.004952352191959015",
            "extra": "mean: 45.17993086956613 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.113841205622492,
            "unit": "iter/sec",
            "range": "stddev: 0.00916310014485493",
            "extra": "mean: 89.97789166666337 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.844093406418413,
            "unit": "iter/sec",
            "range": "stddev: 0.010373050617454629",
            "extra": "mean: 113.06981440000072 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.208701676505682,
            "unit": "iter/sec",
            "range": "stddev: 0.013885767113130216",
            "extra": "mean: 452.75467060000096 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 846.6719603640915,
            "unit": "iter/sec",
            "range": "stddev: 0.00007874317600002226",
            "extra": "mean: 1.1810949775282191 msec\nrounds: 623"
          },
          {
            "name": "Items Limit: (10)",
            "value": 498.2391389103203,
            "unit": "iter/sec",
            "range": "stddev: 0.00008377921291623649",
            "extra": "mean: 2.007068337078178 msec\nrounds: 445"
          },
          {
            "name": "Items Limit: (50)",
            "value": 174.0423798681561,
            "unit": "iter/sec",
            "range": "stddev: 0.000058502371544448714",
            "extra": "mean: 5.745726993376779 msec\nrounds: 151"
          },
          {
            "name": "Items Limit: (100)",
            "value": 97.29403707149658,
            "unit": "iter/sec",
            "range": "stddev: 0.00007249734891747893",
            "extra": "mean: 10.278122175824091 msec\nrounds: 91"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.82871997171122,
            "unit": "iter/sec",
            "range": "stddev: 0.003877803451868939",
            "extra": "mean: 19.673916647056053 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.19154401619246,
            "unit": "iter/sec",
            "range": "stddev: 0.0038899448422368946",
            "extra": "mean: 24.276827292681684 msec\nrounds: 41"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.633655469292304,
            "unit": "iter/sec",
            "range": "stddev: 0.0074754581297236155",
            "extra": "mean: 94.04103818181656 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 637.1673608054317,
            "unit": "iter/sec",
            "range": "stddev: 0.00006382561247418552",
            "extra": "mean: 1.5694463676480825 msec\nrounds: 544"
          },
          {
            "name": "Collection",
            "value": 962.8581221838402,
            "unit": "iter/sec",
            "range": "stddev: 0.00007034384741850516",
            "extra": "mean: 1.0385746113164824 msec\nrounds: 813"
          },
          {
            "name": "Collections With Model validation",
            "value": 174.30654626053752,
            "unit": "iter/sec",
            "range": "stddev: 0.00007163998167166028",
            "extra": "mean: 5.737019185184768 msec\nrounds: 162"
          },
          {
            "name": "Collections",
            "value": 508.1758691636686,
            "unit": "iter/sec",
            "range": "stddev: 0.00008989644136035158",
            "extra": "mean: 1.9678226784867843 msec\nrounds: 423"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "webmaster@mamo-net.de",
            "name": "Matthias Mohr",
            "username": "m-mohr"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "96de0e27f1c1c683947019d33e3e4a72c43bf2a5",
          "message": "Configure the landing page id, description, etc. via env vars (#639)\n\n* Allow an easy way to configure the landing page id, description, title and version via env variables\r\n\r\n* use pydantic settings (#657)\r\n\r\n* use pydantic settings\r\n\r\n* rename stac_fastapi_id to stac_fastapi_landing_id\r\n\r\n* Update docs/src/tips-and-tricks.md\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-11T16:53:31+02:00",
          "tree_id": "58157ea67613a098e224dbd6828c0ebe90c5a53d",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/96de0e27f1c1c683947019d33e3e4a72c43bf2a5"
        },
        "date": 1712847312734,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 535.7324160484384,
            "unit": "iter/sec",
            "range": "stddev: 0.00010163030522640517",
            "extra": "mean: 1.866603494662501 msec\nrounds: 281"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 168.0192062416893,
            "unit": "iter/sec",
            "range": "stddev: 0.002207567389108097",
            "extra": "mean: 5.9517005369108675 msec\nrounds: 149"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.61693661722687,
            "unit": "iter/sec",
            "range": "stddev: 0.004142480019563688",
            "extra": "mean: 23.464849409090892 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.987180599961373,
            "unit": "iter/sec",
            "range": "stddev: 0.005716269844856017",
            "extra": "mean: 45.481047260864216 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.667431355556742,
            "unit": "iter/sec",
            "range": "stddev: 0.012404340884223182",
            "extra": "mean: 93.74327958333595 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.400673446707948,
            "unit": "iter/sec",
            "range": "stddev: 0.014547288179653431",
            "extra": "mean: 119.03807549999215 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2177898981414743,
            "unit": "iter/sec",
            "range": "stddev: 0.019356120456232303",
            "extra": "mean: 450.8993394000072 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 832.7565127583913,
            "unit": "iter/sec",
            "range": "stddev: 0.00008016939431231461",
            "extra": "mean: 1.2008311969697334 msec\nrounds: 660"
          },
          {
            "name": "Items Limit: (10)",
            "value": 500.57205546176885,
            "unit": "iter/sec",
            "range": "stddev: 0.00011993465602799204",
            "extra": "mean: 1.997714393140699 msec\nrounds: 379"
          },
          {
            "name": "Items Limit: (50)",
            "value": 176.97659222261754,
            "unit": "iter/sec",
            "range": "stddev: 0.00010907921647442177",
            "extra": "mean: 5.650464773002903 msec\nrounds: 163"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.04995894702778,
            "unit": "iter/sec",
            "range": "stddev: 0.0008862004310602213",
            "extra": "mean: 10.198882393619945 msec\nrounds: 94"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.60810245498038,
            "unit": "iter/sec",
            "range": "stddev: 0.004453859016147166",
            "extra": "mean: 19.759681779999028 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.09552887484826,
            "unit": "iter/sec",
            "range": "stddev: 0.004134292058944428",
            "extra": "mean: 24.33354740476478 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.403041853977497,
            "unit": "iter/sec",
            "range": "stddev: 0.009475907134099707",
            "extra": "mean: 96.1257307272738 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 667.8918820076984,
            "unit": "iter/sec",
            "range": "stddev: 0.00008132723489598969",
            "extra": "mean: 1.4972483225787636 msec\nrounds: 434"
          },
          {
            "name": "Collection",
            "value": 918.2463522737013,
            "unit": "iter/sec",
            "range": "stddev: 0.00012603863795209003",
            "extra": "mean: 1.0890323686272922 msec\nrounds: 255"
          },
          {
            "name": "Collections With Model validation",
            "value": 172.2706996398138,
            "unit": "iter/sec",
            "range": "stddev: 0.0006685975307462192",
            "extra": "mean: 5.804817662497541 msec\nrounds: 160"
          },
          {
            "name": "Collections",
            "value": 486.7178256320397,
            "unit": "iter/sec",
            "range": "stddev: 0.0001097143678321063",
            "extra": "mean: 2.054578540864873 msec\nrounds: 416"
          }
        ]
      }
    ]
  }
}