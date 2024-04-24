window.BENCHMARK_DATA = {
  "lastUpdate": 1713974667183,
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
          "id": "f7d2eb3c30bef338e3bf6cce5c425b531a653a5e",
          "message": "add deprecation warning for the ContextExtension (#658)",
          "timestamp": "2024-04-11T23:17:31+02:00",
          "tree_id": "8d5ec44552f7494cceaa99f6809269671dc0ed73",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/f7d2eb3c30bef338e3bf6cce5c425b531a653a5e"
        },
        "date": 1712870352859,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 531.2471080358297,
            "unit": "iter/sec",
            "range": "stddev: 0.00009680566137661063",
            "extra": "mean: 1.8823631881918037 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 167.95942046653593,
            "unit": "iter/sec",
            "range": "stddev: 0.0021431084783254803",
            "extra": "mean: 5.953819066666993 msec\nrounds: 165"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.458120390971644,
            "unit": "iter/sec",
            "range": "stddev: 0.00014508183601736965",
            "extra": "mean: 22.493078681821096 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.752268231260942,
            "unit": "iter/sec",
            "range": "stddev: 0.00039401909563757984",
            "extra": "mean: 43.95166186666302 msec\nrounds: 15"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.448404670991012,
            "unit": "iter/sec",
            "range": "stddev: 0.008344493653043657",
            "extra": "mean: 87.3484148000017 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.964732148470079,
            "unit": "iter/sec",
            "range": "stddev: 0.010626564892231903",
            "extra": "mean: 111.54822959999535 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2518758106361956,
            "unit": "iter/sec",
            "range": "stddev: 0.015876335683056093",
            "extra": "mean: 444.0742225999941 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 840.6594559436331,
            "unit": "iter/sec",
            "range": "stddev: 0.00008398442077984012",
            "extra": "mean: 1.1895423205315743 msec\nrounds: 677"
          },
          {
            "name": "Items Limit: (10)",
            "value": 492.4243604115183,
            "unit": "iter/sec",
            "range": "stddev: 0.0000957420115883147",
            "extra": "mean: 2.030768744187029 msec\nrounds: 430"
          },
          {
            "name": "Items Limit: (50)",
            "value": 178.28467602280168,
            "unit": "iter/sec",
            "range": "stddev: 0.00014609214487272838",
            "extra": "mean: 5.609007023531878 msec\nrounds: 170"
          },
          {
            "name": "Items Limit: (100)",
            "value": 99.52268703833107,
            "unit": "iter/sec",
            "range": "stddev: 0.00007888574780546631",
            "extra": "mean: 10.047960216496676 msec\nrounds: 97"
          },
          {
            "name": "Items Limit: (200)",
            "value": 53.28719880689206,
            "unit": "iter/sec",
            "range": "stddev: 0.0003009420331865985",
            "extra": "mean: 18.766233211543145 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 43.310002429749005,
            "unit": "iter/sec",
            "range": "stddev: 0.00012452327723454825",
            "extra": "mean: 23.089354511629278 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.72694522084969,
            "unit": "iter/sec",
            "range": "stddev: 0.00840486577269952",
            "extra": "mean: 93.22318511110932 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 659.0459071010695,
            "unit": "iter/sec",
            "range": "stddev: 0.0000700289668870272",
            "extra": "mean: 1.5173449819280083 msec\nrounds: 498"
          },
          {
            "name": "Collection",
            "value": 922.04405333011,
            "unit": "iter/sec",
            "range": "stddev: 0.00007216195571304678",
            "extra": "mean: 1.0845468786316006 msec\nrounds: 585"
          },
          {
            "name": "Collections With Model validation",
            "value": 171.19313776595675,
            "unit": "iter/sec",
            "range": "stddev: 0.002087872198533514",
            "extra": "mean: 5.841355635219035 msec\nrounds: 159"
          },
          {
            "name": "Collections",
            "value": 498.9498607884981,
            "unit": "iter/sec",
            "range": "stddev: 0.00008701962042067408",
            "extra": "mean: 2.0042093977532827 msec\nrounds: 445"
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
          "id": "bc5263542595cb82076da2bc6428e97fea2f44bc",
          "message": "prepare release 2.5.0 (#659)\n\n* prepare release 2.5.0\r\n\r\n* Update CHANGES.md\r\n\r\n---------\r\n\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-04-17T08:26:49+02:00",
          "tree_id": "e068cf0ac618aae9fcbf414529e84e6aa273dc09",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/bc5263542595cb82076da2bc6428e97fea2f44bc"
        },
        "date": 1713335309611,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 540.117534448527,
            "unit": "iter/sec",
            "range": "stddev: 0.00013403382918972384",
            "extra": "mean: 1.8514488721811708 msec\nrounds: 266"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 171.0472563575814,
            "unit": "iter/sec",
            "range": "stddev: 0.0019931025494473987",
            "extra": "mean: 5.846337563634803 msec\nrounds: 165"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.864933028283296,
            "unit": "iter/sec",
            "range": "stddev: 0.00015624727217423127",
            "extra": "mean: 22.797253545450957 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.635119899582502,
            "unit": "iter/sec",
            "range": "stddev: 0.0002858831038883451",
            "extra": "mean: 44.179134214281085 msec\nrounds: 14"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.95073648028512,
            "unit": "iter/sec",
            "range": "stddev: 0.010821260786587452",
            "extra": "mean: 91.31805899998824 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.854196611836102,
            "unit": "iter/sec",
            "range": "stddev: 0.01138225676743396",
            "extra": "mean: 112.94079450000254 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2445105511657464,
            "unit": "iter/sec",
            "range": "stddev: 0.016614158901408688",
            "extra": "mean: 445.53143200000704 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 868.6681507832369,
            "unit": "iter/sec",
            "range": "stddev: 0.00006748442087577278",
            "extra": "mean: 1.1511875957445286 msec\nrounds: 658"
          },
          {
            "name": "Items Limit: (10)",
            "value": 493.0831493135366,
            "unit": "iter/sec",
            "range": "stddev: 0.00009197810236880067",
            "extra": "mean: 2.028055514353281 msec\nrounds: 418"
          },
          {
            "name": "Items Limit: (50)",
            "value": 179.97028946384805,
            "unit": "iter/sec",
            "range": "stddev: 0.000142879470016005",
            "extra": "mean: 5.556472698794416 msec\nrounds: 166"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.83477035706767,
            "unit": "iter/sec",
            "range": "stddev: 0.0001881154885068303",
            "extra": "mean: 10.117896731962103 msec\nrounds: 97"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.8685959992435,
            "unit": "iter/sec",
            "range": "stddev: 0.00462552764279347",
            "extra": "mean: 19.658494211534197 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.125192472751735,
            "unit": "iter/sec",
            "range": "stddev: 0.0040895941581884365",
            "extra": "mean: 24.315995619049534 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.569765912384067,
            "unit": "iter/sec",
            "range": "stddev: 0.009082847439912785",
            "extra": "mean: 94.6094746363635 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 679.6836017050734,
            "unit": "iter/sec",
            "range": "stddev: 0.00007572293951853805",
            "extra": "mean: 1.4712728061871314 msec\nrounds: 485"
          },
          {
            "name": "Collection",
            "value": 1004.5373959977218,
            "unit": "iter/sec",
            "range": "stddev: 0.00006336656221823231",
            "extra": "mean: 995.4830989709296 usec\nrounds: 778"
          },
          {
            "name": "Collections With Model validation",
            "value": 177.82655777239475,
            "unit": "iter/sec",
            "range": "stddev: 0.0001214895931647949",
            "extra": "mean: 5.623456993864371 msec\nrounds: 163"
          },
          {
            "name": "Collections",
            "value": 502.97557797319035,
            "unit": "iter/sec",
            "range": "stddev: 0.00007278972168888008",
            "extra": "mean: 1.9881681015798784 msec\nrounds: 443"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jon9595@gmail.com",
            "name": "Jon Lantsberger",
            "username": "jon9595"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "1078c2d3ea708e9989f0bd72e519ea457938bcdc",
          "message": "Update context.py (#660)\n\n* Update context.py\r\n\r\ntypo in warning, \"warm\" insteand of \"warn\"\r\n\r\n* Update routes.py\r\n\r\nfixing warn call\r\n\r\n* Update CHANGES.md\r\n\r\n* Update CHANGES.md\r\n\r\n* Update CHANGES.md\r\n\r\n---------\r\n\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-04-18T13:31:43+08:00",
          "tree_id": "7f9eec42f4e61e7aa4d5059b72dc5f8d57c626f0",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/1078c2d3ea708e9989f0bd72e519ea457938bcdc"
        },
        "date": 1713418394112,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 525.5619000199163,
            "unit": "iter/sec",
            "range": "stddev: 0.00007397020457027134",
            "extra": "mean: 1.9027254448279163 msec\nrounds: 290"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 171.35677381461045,
            "unit": "iter/sec",
            "range": "stddev: 0.0017533311580040258",
            "extra": "mean: 5.835777470238161 msec\nrounds: 168"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.20114337874137,
            "unit": "iter/sec",
            "range": "stddev: 0.0034655107855706834",
            "extra": "mean: 23.14753549999987 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.46256601410115,
            "unit": "iter/sec",
            "range": "stddev: 0.004940937961864721",
            "extra": "mean: 44.518511347823654 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.20062746960448,
            "unit": "iter/sec",
            "range": "stddev: 0.009464260784501199",
            "extra": "mean: 89.28071241666895 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.904477565966504,
            "unit": "iter/sec",
            "range": "stddev: 0.013005950675309649",
            "extra": "mean: 112.30305120000139 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.287687662347513,
            "unit": "iter/sec",
            "range": "stddev: 0.012437700595622336",
            "extra": "mean: 437.1226092000029 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 848.6210647210494,
            "unit": "iter/sec",
            "range": "stddev: 0.00007324799026897134",
            "extra": "mean: 1.178382250420228 msec\nrounds: 595"
          },
          {
            "name": "Items Limit: (10)",
            "value": 497.73449442490204,
            "unit": "iter/sec",
            "range": "stddev: 0.00009379319893776367",
            "extra": "mean: 2.0091032693151623 msec\nrounds: 453"
          },
          {
            "name": "Items Limit: (50)",
            "value": 178.75882978296727,
            "unit": "iter/sec",
            "range": "stddev: 0.00007818238211162417",
            "extra": "mean: 5.594129259036373 msec\nrounds: 166"
          },
          {
            "name": "Items Limit: (100)",
            "value": 101.06550421947702,
            "unit": "iter/sec",
            "range": "stddev: 0.00006204774102701573",
            "extra": "mean: 9.89457290816428 msec\nrounds: 98"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.820654962941305,
            "unit": "iter/sec",
            "range": "stddev: 0.003736123825558755",
            "extra": "mean: 19.297324603773024 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (250)",
            "value": 43.144278609521265,
            "unit": "iter/sec",
            "range": "stddev: 0.00013150840260231888",
            "extra": "mean: 23.17804427906962 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.941812379116016,
            "unit": "iter/sec",
            "range": "stddev: 0.007948310358052964",
            "extra": "mean: 91.39253766667031 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 641.3421947844882,
            "unit": "iter/sec",
            "range": "stddev: 0.00007238861375852829",
            "extra": "mean: 1.5592300150094325 msec\nrounds: 533"
          },
          {
            "name": "Collection",
            "value": 946.2227831478903,
            "unit": "iter/sec",
            "range": "stddev: 0.00009960116613349132",
            "extra": "mean: 1.0568335679608178 msec\nrounds: 824"
          },
          {
            "name": "Collections With Model validation",
            "value": 171.83748307665718,
            "unit": "iter/sec",
            "range": "stddev: 0.0019170998372000647",
            "extra": "mean: 5.819452089820806 msec\nrounds: 167"
          },
          {
            "name": "Collections",
            "value": 489.1725104145241,
            "unit": "iter/sec",
            "range": "stddev: 0.0001191706672077863",
            "extra": "mean: 2.0442685938189813 msec\nrounds: 453"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "27a8eddd64f0b53bf33a26923f0d0b9592d8d048",
          "message": "v2.5.1 release (#661)",
          "timestamp": "2024-04-18T13:50:41+08:00",
          "tree_id": "092b9acc26158bafcfff6b3c04ca4377a8347f7f",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/27a8eddd64f0b53bf33a26923f0d0b9592d8d048"
        },
        "date": 1713419538503,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 566.2174820300032,
            "unit": "iter/sec",
            "range": "stddev: 0.0000761216068256271",
            "extra": "mean: 1.7661058369564986 msec\nrounds: 276"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 169.97198057580118,
            "unit": "iter/sec",
            "range": "stddev: 0.0022453578200789313",
            "extra": "mean: 5.883322631250021 msec\nrounds: 160"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.95105148500656,
            "unit": "iter/sec",
            "range": "stddev: 0.00021029779485276807",
            "extra": "mean: 22.752584209302466 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.02352804997718,
            "unit": "iter/sec",
            "range": "stddev: 0.008894742531484518",
            "extra": "mean: 47.56575573913178 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.941555339319518,
            "unit": "iter/sec",
            "range": "stddev: 0.010141082420133176",
            "extra": "mean: 91.39468466666756 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.927123967155927,
            "unit": "iter/sec",
            "range": "stddev: 0.009495848153456976",
            "extra": "mean: 112.01815990000057 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.201309634914907,
            "unit": "iter/sec",
            "range": "stddev: 0.021233436275102217",
            "extra": "mean: 454.27502980000156 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 848.1132869263864,
            "unit": "iter/sec",
            "range": "stddev: 0.00008183856891232865",
            "extra": "mean: 1.179087765060326 msec\nrounds: 664"
          },
          {
            "name": "Items Limit: (10)",
            "value": 472.61772791430616,
            "unit": "iter/sec",
            "range": "stddev: 0.0002178592721905602",
            "extra": "mean: 2.115874925837139 msec\nrounds: 418"
          },
          {
            "name": "Items Limit: (50)",
            "value": 176.24692654999464,
            "unit": "iter/sec",
            "range": "stddev: 0.00008374003564089049",
            "extra": "mean: 5.673857806061302 msec\nrounds: 165"
          },
          {
            "name": "Items Limit: (100)",
            "value": 96.67374761328331,
            "unit": "iter/sec",
            "range": "stddev: 0.00021189932175801502",
            "extra": "mean: 10.344069870966669 msec\nrounds: 93"
          },
          {
            "name": "Items Limit: (200)",
            "value": 48.96010559235826,
            "unit": "iter/sec",
            "range": "stddev: 0.004036886018674905",
            "extra": "mean: 20.424792551020985 msec\nrounds: 49"
          },
          {
            "name": "Items Limit: (250)",
            "value": 40.95483406600668,
            "unit": "iter/sec",
            "range": "stddev: 0.0004531092914523019",
            "extra": "mean: 24.41714202500016 msec\nrounds: 40"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.06938812611503,
            "unit": "iter/sec",
            "range": "stddev: 0.011536101373082646",
            "extra": "mean: 99.31090027272789 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 677.5327409882236,
            "unit": "iter/sec",
            "range": "stddev: 0.00008790915844884165",
            "extra": "mean: 1.4759434334367927 msec\nrounds: 323"
          },
          {
            "name": "Collection",
            "value": 995.2872128586108,
            "unit": "iter/sec",
            "range": "stddev: 0.000139880580780971",
            "extra": "mean: 1.0047351026723768 msec\nrounds: 711"
          },
          {
            "name": "Collections With Model validation",
            "value": 167.51084771973973,
            "unit": "iter/sec",
            "range": "stddev: 0.0026057755415146567",
            "extra": "mean: 5.969762636943294 msec\nrounds: 157"
          },
          {
            "name": "Collections",
            "value": 501.8239351210624,
            "unit": "iter/sec",
            "range": "stddev: 0.0001173195750735213",
            "extra": "mean: 1.992730776699113 msec\nrounds: 412"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "1148c9db529728795c74aef722b253761638e85a",
          "message": "fix datetime validator (#662)\n\n* fix datetime validator\r\n\r\n* lint code\r\n\r\n* fix pull request #",
          "timestamp": "2024-04-18T23:03:13+08:00",
          "tree_id": "79d3e379c1a5c09b036f097f75f584a9aba78c63",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/1148c9db529728795c74aef722b253761638e85a"
        },
        "date": 1713452696728,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 555.4025391400767,
            "unit": "iter/sec",
            "range": "stddev: 0.00010392568271302197",
            "extra": "mean: 1.8004959097743567 msec\nrounds: 266"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 172.36755443035577,
            "unit": "iter/sec",
            "range": "stddev: 0.0021436506753130585",
            "extra": "mean: 5.801555886227097 msec\nrounds: 167"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.39679436311613,
            "unit": "iter/sec",
            "range": "stddev: 0.00011601071894546723",
            "extra": "mean: 22.52414874418901 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.793657279541854,
            "unit": "iter/sec",
            "range": "stddev: 0.007321477819693045",
            "extra": "mean: 45.88490986956651 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.066904024828645,
            "unit": "iter/sec",
            "range": "stddev: 0.008422800385016378",
            "extra": "mean: 90.35950774999908 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.116488806507837,
            "unit": "iter/sec",
            "range": "stddev: 0.008442969585481151",
            "extra": "mean: 109.69135389999565 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2465390827587575,
            "unit": "iter/sec",
            "range": "stddev: 0.018378371505085107",
            "extra": "mean: 445.1291355999899 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 904.0409107406301,
            "unit": "iter/sec",
            "range": "stddev: 0.00006571299013012994",
            "extra": "mean: 1.1061446314202263 msec\nrounds: 662"
          },
          {
            "name": "Items Limit: (10)",
            "value": 487.7443073784109,
            "unit": "iter/sec",
            "range": "stddev: 0.00008734524974765895",
            "extra": "mean: 2.0502545798533767 msec\nrounds: 407"
          },
          {
            "name": "Items Limit: (50)",
            "value": 178.10329970267338,
            "unit": "iter/sec",
            "range": "stddev: 0.00014334862957608786",
            "extra": "mean: 5.614719107784109 msec\nrounds: 167"
          },
          {
            "name": "Items Limit: (100)",
            "value": 93.94872978600245,
            "unit": "iter/sec",
            "range": "stddev: 0.0010947292975081856",
            "extra": "mean: 10.644103462365186 msec\nrounds: 93"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.24817224546237,
            "unit": "iter/sec",
            "range": "stddev: 0.0038171309583740795",
            "extra": "mean: 19.51289102000203 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 42.912820972483715,
            "unit": "iter/sec",
            "range": "stddev: 0.0001802924768724609",
            "extra": "mean: 23.303059023810476 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.641880419186867,
            "unit": "iter/sec",
            "range": "stddev: 0.007746112803295875",
            "extra": "mean: 93.96835527272432 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 675.9817950701427,
            "unit": "iter/sec",
            "range": "stddev: 0.00008501824062989413",
            "extra": "mean: 1.4793297797261475 msec\nrounds: 513"
          },
          {
            "name": "Collection",
            "value": 927.0818660523125,
            "unit": "iter/sec",
            "range": "stddev: 0.0009235406509568472",
            "extra": "mean: 1.0786533925619606 msec\nrounds: 726"
          },
          {
            "name": "Collections With Model validation",
            "value": 175.1484944863976,
            "unit": "iter/sec",
            "range": "stddev: 0.00006755611122101423",
            "extra": "mean: 5.7094410256416 msec\nrounds: 156"
          },
          {
            "name": "Collections",
            "value": 492.9754348836918,
            "unit": "iter/sec",
            "range": "stddev: 0.00009525639222099856",
            "extra": "mean: 2.0284986415924173 msec\nrounds: 452"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2e14348e9e9d37904b065156c8155b57de99e3b9",
          "message": "update for v2.5.2 (#663)",
          "timestamp": "2024-04-19T00:37:56+08:00",
          "tree_id": "fae5aa59e7a120f1e6e7be165563b2dcb03704d6",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/2e14348e9e9d37904b065156c8155b57de99e3b9"
        },
        "date": 1713458374018,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 535.2913615610383,
            "unit": "iter/sec",
            "range": "stddev: 0.00008961538349890665",
            "extra": "mean: 1.8681414866919572 msec\nrounds: 263"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 173.556945507975,
            "unit": "iter/sec",
            "range": "stddev: 0.002057538400891725",
            "extra": "mean: 5.761797645569013 msec\nrounds: 158"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.79196979463932,
            "unit": "iter/sec",
            "range": "stddev: 0.00381274066481049",
            "extra": "mean: 22.83523679545496 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.52564115033577,
            "unit": "iter/sec",
            "range": "stddev: 0.00532851376032312",
            "extra": "mean: 44.393852913043226 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.088104997524015,
            "unit": "iter/sec",
            "range": "stddev: 0.010601878517364983",
            "extra": "mean: 90.18673616666699 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.991586408950143,
            "unit": "iter/sec",
            "range": "stddev: 0.011034050478258086",
            "extra": "mean: 111.2150798000016 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2769964008592574,
            "unit": "iter/sec",
            "range": "stddev: 0.017842012072381574",
            "extra": "mean: 439.1750464000012 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 861.0353715944731,
            "unit": "iter/sec",
            "range": "stddev: 0.00009211883011763449",
            "extra": "mean: 1.1613924735149856 msec\nrounds: 623"
          },
          {
            "name": "Items Limit: (10)",
            "value": 513.7804583936003,
            "unit": "iter/sec",
            "range": "stddev: 0.00008761056362344506",
            "extra": "mean: 1.9463566269659747 msec\nrounds: 445"
          },
          {
            "name": "Items Limit: (50)",
            "value": 178.2010997194293,
            "unit": "iter/sec",
            "range": "stddev: 0.00005745642769125559",
            "extra": "mean: 5.611637647435741 msec\nrounds: 156"
          },
          {
            "name": "Items Limit: (100)",
            "value": 100.28027119633782,
            "unit": "iter/sec",
            "range": "stddev: 0.00006280235819346104",
            "extra": "mean: 9.972051212766559 msec\nrounds: 94"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.58919063197389,
            "unit": "iter/sec",
            "range": "stddev: 0.003754580575413912",
            "extra": "mean: 19.383905576921787 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 42.790638882995474,
            "unit": "iter/sec",
            "range": "stddev: 0.00032185349262975875",
            "extra": "mean: 23.36959732558209 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.64706666876615,
            "unit": "iter/sec",
            "range": "stddev: 0.00995565925522846",
            "extra": "mean: 93.9225827272749 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 657.6937669391083,
            "unit": "iter/sec",
            "range": "stddev: 0.00008183716342192524",
            "extra": "mean: 1.5204644627452941 msec\nrounds: 510"
          },
          {
            "name": "Collection",
            "value": 973.4383609626675,
            "unit": "iter/sec",
            "range": "stddev: 0.00007660633361168707",
            "extra": "mean: 1.0272864108324895 msec\nrounds: 757"
          },
          {
            "name": "Collections With Model validation",
            "value": 175.23712883655432,
            "unit": "iter/sec",
            "range": "stddev: 0.002204400000140352",
            "extra": "mean: 5.70655320958101 msec\nrounds: 167"
          },
          {
            "name": "Collections",
            "value": 494.1310683529314,
            "unit": "iter/sec",
            "range": "stddev: 0.00013342783053995328",
            "extra": "mean: 2.0237545542992526 msec\nrounds: 442"
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
          "id": "dddd7104865db56c59ea21d75ba939891249d4ea",
          "message": "apply datetime converter in ItemCollection endpoint model (#667)\n\n* apply datetime converter in ItemCollection endpoint model\r\n\r\n* update changelog",
          "timestamp": "2024-04-22T23:14:58+08:00",
          "tree_id": "d73d3b18687b5ccb251315abef0820da25d6200f",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/dddd7104865db56c59ea21d75ba939891249d4ea"
        },
        "date": 1713798995093,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 512.5555190278947,
            "unit": "iter/sec",
            "range": "stddev: 0.00008287889913827703",
            "extra": "mean: 1.9510081598508302 msec\nrounds: 269"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 165.46258766020347,
            "unit": "iter/sec",
            "range": "stddev: 0.003134773765045473",
            "extra": "mean: 6.04366228125004 msec\nrounds: 160"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.81354970764591,
            "unit": "iter/sec",
            "range": "stddev: 0.00033392281986613815",
            "extra": "mean: 23.357091547618477 msec\nrounds: 42"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.016078825878573,
            "unit": "iter/sec",
            "range": "stddev: 0.008004079008184537",
            "extra": "mean: 47.582615590907935 msec\nrounds: 22"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.105664985548929,
            "unit": "iter/sec",
            "range": "stddev: 0.008314167878261414",
            "extra": "mean: 90.04413525000388 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.96142062806001,
            "unit": "iter/sec",
            "range": "stddev: 0.008433336362281399",
            "extra": "mean: 111.58945009999854 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2063745642821164,
            "unit": "iter/sec",
            "range": "stddev: 0.020122505809245544",
            "extra": "mean: 453.23220100000015 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 881.1052014315732,
            "unit": "iter/sec",
            "range": "stddev: 0.0000658897852096189",
            "extra": "mean: 1.1349382552449503 msec\nrounds: 572"
          },
          {
            "name": "Items Limit: (10)",
            "value": 500.71675112443535,
            "unit": "iter/sec",
            "range": "stddev: 0.00008166759495703358",
            "extra": "mean: 1.9971370994765976 msec\nrounds: 382"
          },
          {
            "name": "Items Limit: (50)",
            "value": 170.30389678986052,
            "unit": "iter/sec",
            "range": "stddev: 0.0021777310133865107",
            "extra": "mean: 5.871856245508632 msec\nrounds: 167"
          },
          {
            "name": "Items Limit: (100)",
            "value": 97.93585598442748,
            "unit": "iter/sec",
            "range": "stddev: 0.00019908377048889574",
            "extra": "mean: 10.210764892472143 msec\nrounds: 93"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.838564777434456,
            "unit": "iter/sec",
            "range": "stddev: 0.00031646108873465816",
            "extra": "mean: 19.290657530613274 msec\nrounds: 49"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.76114917862416,
            "unit": "iter/sec",
            "range": "stddev: 0.00024351421059685515",
            "extra": "mean: 23.94570120000097 msec\nrounds: 20"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.53769693577261,
            "unit": "iter/sec",
            "range": "stddev: 0.00831909554238286",
            "extra": "mean: 94.89739609091171 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 620.2573744734029,
            "unit": "iter/sec",
            "range": "stddev: 0.00007271723506268624",
            "extra": "mean: 1.6122339550561533 msec\nrounds: 445"
          },
          {
            "name": "Collection",
            "value": 926.3399425533535,
            "unit": "iter/sec",
            "range": "stddev: 0.00008354833871035774",
            "extra": "mean: 1.0795173068362038 msec\nrounds: 629"
          },
          {
            "name": "Collections With Model validation",
            "value": 175.51797616474488,
            "unit": "iter/sec",
            "range": "stddev: 0.0001180622040111031",
            "extra": "mean: 5.697422120805329 msec\nrounds: 149"
          },
          {
            "name": "Collections",
            "value": 490.6175292178544,
            "unit": "iter/sec",
            "range": "stddev: 0.00009527995656791287",
            "extra": "mean: 2.0382475970522425 msec\nrounds: 407"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "085bcd700772ec0c952e439cf3a96a4192608c5d",
          "message": "Remove str2list converter from BaseSearchGetRequest (#668)\n\n* remove str2list converter\r\n\r\n* update changelog",
          "timestamp": "2024-04-22T23:28:09+08:00",
          "tree_id": "0733736a2b615ea299ffbe978d9cc7aa1b09e82c",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/085bcd700772ec0c952e439cf3a96a4192608c5d"
        },
        "date": 1713799789070,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 543.1763526812543,
            "unit": "iter/sec",
            "range": "stddev: 0.00010232502522538903",
            "extra": "mean: 1.8410227084882285 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.1524168117559,
            "unit": "iter/sec",
            "range": "stddev: 0.002185505025026837",
            "extra": "mean: 5.877083727269807 msec\nrounds: 154"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.76586401884218,
            "unit": "iter/sec",
            "range": "stddev: 0.00046715346610890434",
            "extra": "mean: 22.84885772092784 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.517428800177967,
            "unit": "iter/sec",
            "range": "stddev: 0.00829488294748403",
            "extra": "mean: 46.47395417391734 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.327211419839056,
            "unit": "iter/sec",
            "range": "stddev: 0.00817639943551566",
            "extra": "mean: 88.28298183333534 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.006673978066576,
            "unit": "iter/sec",
            "range": "stddev: 0.009582659148050015",
            "extra": "mean: 111.0287773750045 msec\nrounds: 8"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2798275822574956,
            "unit": "iter/sec",
            "range": "stddev: 0.015388323408188211",
            "extra": "mean: 438.629661199991 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 874.5933756530509,
            "unit": "iter/sec",
            "range": "stddev: 0.00007429100064216613",
            "extra": "mean: 1.1433884909696568 msec\nrounds: 609"
          },
          {
            "name": "Items Limit: (10)",
            "value": 496.1470492773525,
            "unit": "iter/sec",
            "range": "stddev: 0.00008608942901299266",
            "extra": "mean: 2.015531486998701 msec\nrounds: 423"
          },
          {
            "name": "Items Limit: (50)",
            "value": 181.8989122587202,
            "unit": "iter/sec",
            "range": "stddev: 0.0000713643188892616",
            "extra": "mean: 5.497558988025561 msec\nrounds: 167"
          },
          {
            "name": "Items Limit: (100)",
            "value": 96.87087485893596,
            "unit": "iter/sec",
            "range": "stddev: 0.000256679920467661",
            "extra": "mean: 10.323020221054131 msec\nrounds: 95"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.252767506624814,
            "unit": "iter/sec",
            "range": "stddev: 0.004330231541590008",
            "extra": "mean: 19.89940155769869 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.00286634637103,
            "unit": "iter/sec",
            "range": "stddev: 0.003989640949893614",
            "extra": "mean: 24.38853887805103 msec\nrounds: 41"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.091069387630572,
            "unit": "iter/sec",
            "range": "stddev: 0.011980465280544911",
            "extra": "mean: 99.09752490908245 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 645.2665399273346,
            "unit": "iter/sec",
            "range": "stddev: 0.00022490761710524532",
            "extra": "mean: 1.5497471790689983 msec\nrounds: 430"
          },
          {
            "name": "Collection",
            "value": 891.0164962303302,
            "unit": "iter/sec",
            "range": "stddev: 0.00006786405426161839",
            "extra": "mean: 1.1223136768294997 msec\nrounds: 656"
          },
          {
            "name": "Collections With Model validation",
            "value": 168.43931140916027,
            "unit": "iter/sec",
            "range": "stddev: 0.0027619968905204673",
            "extra": "mean: 5.936856376543088 msec\nrounds: 162"
          },
          {
            "name": "Collections",
            "value": 486.32283380936667,
            "unit": "iter/sec",
            "range": "stddev: 0.00010742952661900011",
            "extra": "mean: 2.0562472713176967 msec\nrounds: 387"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "cae227840ee231ecfdb9b4ef1d187142dfe534ce",
          "message": "v2.5.3 (#669)",
          "timestamp": "2024-04-23T01:11:06+08:00",
          "tree_id": "0d03a7fc81d457a3c1108f48e9d90a4bd9d3638e",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/cae227840ee231ecfdb9b4ef1d187142dfe534ce"
        },
        "date": 1713805960163,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 560.8786857136089,
            "unit": "iter/sec",
            "range": "stddev: 0.00009981154218289816",
            "extra": "mean: 1.7829167438011926 msec\nrounds: 242"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 172.48526191863573,
            "unit": "iter/sec",
            "range": "stddev: 0.0001664829350572625",
            "extra": "mean: 5.797596785235583 msec\nrounds: 149"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.23917685820128,
            "unit": "iter/sec",
            "range": "stddev: 0.0002515537674275158",
            "extra": "mean: 23.127174767443048 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 20.31022695527488,
            "unit": "iter/sec",
            "range": "stddev: 0.009809534295615485",
            "extra": "mean: 49.236278954543366 msec\nrounds: 22"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.055319866168091,
            "unit": "iter/sec",
            "range": "stddev: 0.008690633200021858",
            "extra": "mean: 90.45418966666337 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.992767301610922,
            "unit": "iter/sec",
            "range": "stddev: 0.008273594198637163",
            "extra": "mean: 111.20047550000152 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2104341605556552,
            "unit": "iter/sec",
            "range": "stddev: 0.018437406030962725",
            "extra": "mean: 452.3998125999924 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 868.0155189140496,
            "unit": "iter/sec",
            "range": "stddev: 0.00007574020709158354",
            "extra": "mean: 1.1520531352378036 msec\nrounds: 525"
          },
          {
            "name": "Items Limit: (10)",
            "value": 484.20985999452046,
            "unit": "iter/sec",
            "range": "stddev: 0.00008302657362671378",
            "extra": "mean: 2.065220233250344 msec\nrounds: 403"
          },
          {
            "name": "Items Limit: (50)",
            "value": 170.81662406399155,
            "unit": "iter/sec",
            "range": "stddev: 0.0023938975140428784",
            "extra": "mean: 5.8542311410239485 msec\nrounds: 156"
          },
          {
            "name": "Items Limit: (100)",
            "value": 94.23207748086145,
            "unit": "iter/sec",
            "range": "stddev: 0.00033510318996639375",
            "extra": "mean: 10.612097565217113 msec\nrounds: 92"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.70309777806199,
            "unit": "iter/sec",
            "range": "stddev: 0.0002860654826556518",
            "extra": "mean: 19.72266081999976 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 40.818093239407666,
            "unit": "iter/sec",
            "range": "stddev: 0.00022921024394882448",
            "extra": "mean: 24.498939578945198 msec\nrounds: 19"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 9.966341679939097,
            "unit": "iter/sec",
            "range": "stddev: 0.013319460497683554",
            "extra": "mean: 100.33771990908815 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 659.2422052540915,
            "unit": "iter/sec",
            "range": "stddev: 0.00009127576604667756",
            "extra": "mean: 1.516893172236402 msec\nrounds: 389"
          },
          {
            "name": "Collection",
            "value": 936.2087380444106,
            "unit": "iter/sec",
            "range": "stddev: 0.00008943068059162435",
            "extra": "mean: 1.068137862170395 msec\nrounds: 682"
          },
          {
            "name": "Collections With Model validation",
            "value": 174.05797716656565,
            "unit": "iter/sec",
            "range": "stddev: 0.00008752065122858182",
            "extra": "mean: 5.745212119999792 msec\nrounds: 150"
          },
          {
            "name": "Collections",
            "value": 463.8431421546991,
            "unit": "iter/sec",
            "range": "stddev: 0.0019200417527296103",
            "extra": "mean: 2.15590122849436 msec\nrounds: 372"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "0bd592e8f5c87a51011a03bbd6592d254f1a2a4f",
          "message": "return 400 for datetime errors (#670)\n\n* return HTTPException\r\n\r\n* update test\r\n\r\n* update validate interval format\r\n\r\n* update changelog\r\n\r\n* remove validate interval function\r\n\r\n* catch iso8601.ParseError",
          "timestamp": "2024-04-24T15:01:11+08:00",
          "tree_id": "75788f2e09ba77b72287072b7788ee3713436fc7",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/0bd592e8f5c87a51011a03bbd6592d254f1a2a4f"
        },
        "date": 1713942182851,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 566.9276268954881,
            "unit": "iter/sec",
            "range": "stddev: 0.00008767462503948447",
            "extra": "mean: 1.7638935775206945 msec\nrounds: 258"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 171.13889091254305,
            "unit": "iter/sec",
            "range": "stddev: 0.002520372792391589",
            "extra": "mean: 5.843207202453059 msec\nrounds: 163"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.40238462407756,
            "unit": "iter/sec",
            "range": "stddev: 0.0002339917286183333",
            "extra": "mean: 22.521312953488124 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.74494393766519,
            "unit": "iter/sec",
            "range": "stddev: 0.007973160697204358",
            "extra": "mean: 45.987701916667824 msec\nrounds: 24"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.383843937122803,
            "unit": "iter/sec",
            "range": "stddev: 0.007893358037767364",
            "extra": "mean: 87.84379033333305 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.079873587956993,
            "unit": "iter/sec",
            "range": "stddev: 0.010528397094298474",
            "extra": "mean: 110.13369187499933 msec\nrounds: 8"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.206094890069454,
            "unit": "iter/sec",
            "range": "stddev: 0.01714635738467933",
            "extra": "mean: 453.28965879999714 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 889.4324368558325,
            "unit": "iter/sec",
            "range": "stddev: 0.00006166082420577586",
            "extra": "mean: 1.1243124925092982 msec\nrounds: 534"
          },
          {
            "name": "Items Limit: (10)",
            "value": 490.78548168436186,
            "unit": "iter/sec",
            "range": "stddev: 0.00013290631351728328",
            "extra": "mean: 2.0375500851574264 msec\nrounds: 411"
          },
          {
            "name": "Items Limit: (50)",
            "value": 178.8608331423636,
            "unit": "iter/sec",
            "range": "stddev: 0.00008079078913318462",
            "extra": "mean: 5.5909389575752115 msec\nrounds: 165"
          },
          {
            "name": "Items Limit: (100)",
            "value": 99.67227581026886,
            "unit": "iter/sec",
            "range": "stddev: 0.00011187262295018277",
            "extra": "mean: 10.032880175261072 msec\nrounds: 97"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.920273082538756,
            "unit": "iter/sec",
            "range": "stddev: 0.0043014896877369225",
            "extra": "mean: 19.6385435399975 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 42.51502807041163,
            "unit": "iter/sec",
            "range": "stddev: 0.00026510356103304184",
            "extra": "mean: 23.52109466666331 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.500049589984311,
            "unit": "iter/sec",
            "range": "stddev: 0.008288164484839664",
            "extra": "mean: 95.23764544444349 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 678.8783002130496,
            "unit": "iter/sec",
            "range": "stddev: 0.00007870243584137659",
            "extra": "mean: 1.4730180647785827 msec\nrounds: 494"
          },
          {
            "name": "Collection",
            "value": 921.6824159600222,
            "unit": "iter/sec",
            "range": "stddev: 0.0000821219137120739",
            "extra": "mean: 1.0849724185726188 msec\nrounds: 743"
          },
          {
            "name": "Collections With Model validation",
            "value": 170.92921916941245,
            "unit": "iter/sec",
            "range": "stddev: 0.0026305922277442923",
            "extra": "mean: 5.850374820988761 msec\nrounds: 162"
          },
          {
            "name": "Collections",
            "value": 491.1748001925621,
            "unit": "iter/sec",
            "range": "stddev: 0.00008798705868890372",
            "extra": "mean: 2.035935067531877 msec\nrounds: 385"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "github@avbentem.dds.nl",
            "name": "Arjan",
            "username": "avbentem"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "108fc2cb27aafd7c6a58c1c4c85968292e543bc1",
          "message": "Fix PUT collections (#666)\n\nCo-authored-by: Arjan van Bentem <arjan.vanbentem@planet.com>\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-04-24T15:08:56+08:00",
          "tree_id": "f49b0f7ff46002b177cde8fda99ec289d8fb84a0",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/108fc2cb27aafd7c6a58c1c4c85968292e543bc1"
        },
        "date": 1713942640480,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 559.0992423264609,
            "unit": "iter/sec",
            "range": "stddev: 0.00008396037366434146",
            "extra": "mean: 1.7885912272728408 msec\nrounds: 308"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 174.45387088513178,
            "unit": "iter/sec",
            "range": "stddev: 0.0016501405394953566",
            "extra": "mean: 5.7321743273810455 msec\nrounds: 168"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.699647424079856,
            "unit": "iter/sec",
            "range": "stddev: 0.00010560673905903533",
            "extra": "mean: 22.371541111111686 msec\nrounds: 45"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.520017064956775,
            "unit": "iter/sec",
            "range": "stddev: 0.0042533837046851",
            "extra": "mean: 44.404939708331405 msec\nrounds: 24"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.452649402323775,
            "unit": "iter/sec",
            "range": "stddev: 0.006187365676183723",
            "extra": "mean: 87.31604058333413 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.144569842406028,
            "unit": "iter/sec",
            "range": "stddev: 0.007846408913586922",
            "extra": "mean: 109.35451500000681 msec\nrounds: 8"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2727206952669547,
            "unit": "iter/sec",
            "range": "stddev: 0.01317387638921537",
            "extra": "mean: 440.0012734000029 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 875.15890636646,
            "unit": "iter/sec",
            "range": "stddev: 0.00007213194746710429",
            "extra": "mean: 1.1426496293705828 msec\nrounds: 572"
          },
          {
            "name": "Items Limit: (10)",
            "value": 485.15685977093574,
            "unit": "iter/sec",
            "range": "stddev: 0.00010226587425906188",
            "extra": "mean: 2.061189035793794 msec\nrounds: 447"
          },
          {
            "name": "Items Limit: (50)",
            "value": 174.983477499471,
            "unit": "iter/sec",
            "range": "stddev: 0.0001238819281933791",
            "extra": "mean: 5.714825275449353 msec\nrounds: 167"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.28696071609082,
            "unit": "iter/sec",
            "range": "stddev: 0.00022150563661038478",
            "extra": "mean: 10.174289577318138 msec\nrounds: 97"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.981989031934134,
            "unit": "iter/sec",
            "range": "stddev: 0.0035926458292464694",
            "extra": "mean: 19.614770215685766 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.15747004043745,
            "unit": "iter/sec",
            "range": "stddev: 0.003065528298799769",
            "extra": "mean: 24.296925904762713 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.660306063899641,
            "unit": "iter/sec",
            "range": "stddev: 0.006300700212194621",
            "extra": "mean: 93.80593709090849 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 671.8165579845794,
            "unit": "iter/sec",
            "range": "stddev: 0.0009182015740065286",
            "extra": "mean: 1.4885015680470228 msec\nrounds: 507"
          },
          {
            "name": "Collection",
            "value": 994.7661213772152,
            "unit": "iter/sec",
            "range": "stddev: 0.00006756254634525308",
            "extra": "mean: 1.005261416236752 msec\nrounds: 776"
          },
          {
            "name": "Collections With Model validation",
            "value": 174.16467967572473,
            "unit": "iter/sec",
            "range": "stddev: 0.00005413719295842242",
            "extra": "mean: 5.741692298701945 msec\nrounds: 154"
          },
          {
            "name": "Collections",
            "value": 500.90962460646074,
            "unit": "iter/sec",
            "range": "stddev: 0.00009855617558450196",
            "extra": "mean: 1.996368108889202 msec\nrounds: 450"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jonathan.d.healy@gmail.com",
            "name": "Jonathan Healy",
            "username": "jonhealy1"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "f54227871c29cf15ae49b2ab96b28f357de60485",
          "message": "update for v2.5.4 (#672)",
          "timestamp": "2024-04-25T00:02:44+08:00",
          "tree_id": "34a3afdb4f0f801bc4355486e8c3929ce7ee6a7d",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/f54227871c29cf15ae49b2ab96b28f357de60485"
        },
        "date": 1713974666837,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 567.0264078102816,
            "unit": "iter/sec",
            "range": "stddev: 0.00008193461123344734",
            "extra": "mean: 1.7635862919714045 msec\nrounds: 274"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.1571337118226,
            "unit": "iter/sec",
            "range": "stddev: 0.001760906648158075",
            "extra": "mean: 5.876920809524188 msec\nrounds: 168"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.778449191477684,
            "unit": "iter/sec",
            "range": "stddev: 0.0035551952575586495",
            "extra": "mean: 23.376256477273603 msec\nrounds: 44"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.146348553909508,
            "unit": "iter/sec",
            "range": "stddev: 0.004739833003197861",
            "extra": "mean: 45.154170565218045 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.11990389712046,
            "unit": "iter/sec",
            "range": "stddev: 0.00891260058731145",
            "extra": "mean: 89.92883474999758 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.929088853325117,
            "unit": "iter/sec",
            "range": "stddev: 0.009540518313111028",
            "extra": "mean: 111.99350980000702 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.266829333130642,
            "unit": "iter/sec",
            "range": "stddev: 0.013066635865409678",
            "extra": "mean: 441.14481199999886 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 881.8669338998295,
            "unit": "iter/sec",
            "range": "stddev: 0.00018590023411930632",
            "extra": "mean: 1.1339579267109579 msec\nrounds: 614"
          },
          {
            "name": "Items Limit: (10)",
            "value": 481.29850596513035,
            "unit": "iter/sec",
            "range": "stddev: 0.0003167154873893093",
            "extra": "mean: 2.077712661905602 msec\nrounds: 420"
          },
          {
            "name": "Items Limit: (50)",
            "value": 176.5148330131328,
            "unit": "iter/sec",
            "range": "stddev: 0.0002018705470763654",
            "extra": "mean: 5.665246273810878 msec\nrounds: 168"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.00652150469153,
            "unit": "iter/sec",
            "range": "stddev: 0.00022213633409828994",
            "extra": "mean: 10.20340263736562 msec\nrounds: 91"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.58838956251916,
            "unit": "iter/sec",
            "range": "stddev: 0.0007066747933231377",
            "extra": "mean: 19.767381579999892 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 39.33892170940228,
            "unit": "iter/sec",
            "range": "stddev: 0.005455704302184624",
            "extra": "mean: 25.420117190476855 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 9.83673100296778,
            "unit": "iter/sec",
            "range": "stddev: 0.013003894400165212",
            "extra": "mean: 101.65978918182232 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 568.9170400532943,
            "unit": "iter/sec",
            "range": "stddev: 0.0005337820476312848",
            "extra": "mean: 1.7577255198865611 msec\nrounds: 352"
          },
          {
            "name": "Collection",
            "value": 645.6320446232729,
            "unit": "iter/sec",
            "range": "stddev: 0.0010079887082429608",
            "extra": "mean: 1.5488698374373615 msec\nrounds: 609"
          },
          {
            "name": "Collections With Model validation",
            "value": 161.69256385877856,
            "unit": "iter/sec",
            "range": "stddev: 0.000992230143031412",
            "extra": "mean: 6.184576310345321 msec\nrounds: 116"
          },
          {
            "name": "Collections",
            "value": 424.9831908350431,
            "unit": "iter/sec",
            "range": "stddev: 0.0007611501338711595",
            "extra": "mean: 2.353034241272261 msec\nrounds: 315"
          }
        ]
      }
    ]
  }
}