window.BENCHMARK_DATA = {
  "lastUpdate": 1718276557175,
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
          "id": "49de0ce58d604234b29c72aeabb06aeab36f6fef",
          "message": "Patch/fix doc urls in landing (#673)\n\n* fix Documentation URL in landing page\r\n\r\n* update changelog",
          "timestamp": "2024-04-25T07:54:14+02:00",
          "tree_id": "6aa4927b660ec7a1ed56ea69dd554ad14de431fd",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/49de0ce58d604234b29c72aeabb06aeab36f6fef"
        },
        "date": 1714024555973,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 565.7820522312936,
            "unit": "iter/sec",
            "range": "stddev: 0.00009355216263258057",
            "extra": "mean: 1.767465044280331 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.24021952526266,
            "unit": "iter/sec",
            "range": "stddev: 0.0023477593558952296",
            "extra": "mean: 5.874052575758139 msec\nrounds: 165"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.20896288185699,
            "unit": "iter/sec",
            "range": "stddev: 0.004166153801627964",
            "extra": "mean: 23.69165058139436 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.119459948891237,
            "unit": "iter/sec",
            "range": "stddev: 0.008153925150764931",
            "extra": "mean: 47.3496956086938 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.917289426232765,
            "unit": "iter/sec",
            "range": "stddev: 0.009871690046937684",
            "extra": "mean: 91.59782808332768 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.716749284307605,
            "unit": "iter/sec",
            "range": "stddev: 0.01112982809377408",
            "extra": "mean: 114.72166599999127 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.180255271455799,
            "unit": "iter/sec",
            "range": "stddev: 0.023595334840663645",
            "extra": "mean: 458.66188840001314 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 889.0410370086851,
            "unit": "iter/sec",
            "range": "stddev: 0.00007026963823525076",
            "extra": "mean: 1.124807470490511 msec\nrounds: 610"
          },
          {
            "name": "Items Limit: (10)",
            "value": 505.94520042916315,
            "unit": "iter/sec",
            "range": "stddev: 0.00009247504558047261",
            "extra": "mean: 1.976498638887689 msec\nrounds: 432"
          },
          {
            "name": "Items Limit: (50)",
            "value": 176.74074946646346,
            "unit": "iter/sec",
            "range": "stddev: 0.00008956365815334685",
            "extra": "mean: 5.658004750001074 msec\nrounds: 168"
          },
          {
            "name": "Items Limit: (100)",
            "value": 97.57040509427304,
            "unit": "iter/sec",
            "range": "stddev: 0.00015257024680984124",
            "extra": "mean: 10.249009410525607 msec\nrounds: 95"
          },
          {
            "name": "Items Limit: (200)",
            "value": 50.41059098688927,
            "unit": "iter/sec",
            "range": "stddev: 0.004442794552648748",
            "extra": "mean: 19.83710130000418 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.422135609382444,
            "unit": "iter/sec",
            "range": "stddev: 0.000343762063170479",
            "extra": "mean: 24.141681380944828 msec\nrounds: 42"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.276268140386223,
            "unit": "iter/sec",
            "range": "stddev: 0.007676086206890876",
            "extra": "mean: 97.31159077777976 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 682.1636774986987,
            "unit": "iter/sec",
            "range": "stddev: 0.00008507699499859188",
            "extra": "mean: 1.4659238434780304 msec\nrounds: 460"
          },
          {
            "name": "Collection",
            "value": 988.8398871993397,
            "unit": "iter/sec",
            "range": "stddev: 0.00007073334656304221",
            "extra": "mean: 1.0112860665767323 msec\nrounds: 751"
          },
          {
            "name": "Collections With Model validation",
            "value": 172.00084098918094,
            "unit": "iter/sec",
            "range": "stddev: 0.0021079396402611957",
            "extra": "mean: 5.813925061348399 msec\nrounds: 163"
          },
          {
            "name": "Collections",
            "value": 505.1002999194182,
            "unit": "iter/sec",
            "range": "stddev: 0.00007892940350923236",
            "extra": "mean: 1.9798048034410913 msec\nrounds: 407"
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
          "id": "24fd2588975d75ddc7bb515361415b54b965d7da",
          "message": "v2.5.5 (#674)",
          "timestamp": "2024-04-25T14:05:29+08:00",
          "tree_id": "669c811571abccbea6944259208626d793dd03c9",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/24fd2588975d75ddc7bb515361415b54b965d7da"
        },
        "date": 1714025237551,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 546.7124856335984,
            "unit": "iter/sec",
            "range": "stddev: 0.00009915502429904611",
            "extra": "mean: 1.8291149850749717 msec\nrounds: 268"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 170.23878927077033,
            "unit": "iter/sec",
            "range": "stddev: 0.00243304838950311",
            "extra": "mean: 5.874101926379819 msec\nrounds: 163"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 42.65062209775746,
            "unit": "iter/sec",
            "range": "stddev: 0.004006426154545473",
            "extra": "mean: 23.446316860465657 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.197028316280605,
            "unit": "iter/sec",
            "range": "stddev: 0.005648399296436874",
            "extra": "mean: 45.05107556521614 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 10.975530243734914,
            "unit": "iter/sec",
            "range": "stddev: 0.010292346186741545",
            "extra": "mean: 91.11177116666624 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.850769231594345,
            "unit": "iter/sec",
            "range": "stddev: 0.011563583540729167",
            "extra": "mean: 112.98452980000064 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2223819956841004,
            "unit": "iter/sec",
            "range": "stddev: 0.018845804178253045",
            "extra": "mean: 449.96764820000124 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 892.4930462624172,
            "unit": "iter/sec",
            "range": "stddev: 0.00005925005213754509",
            "extra": "mean: 1.120456909090553 msec\nrounds: 605"
          },
          {
            "name": "Items Limit: (10)",
            "value": 496.1800260019336,
            "unit": "iter/sec",
            "range": "stddev: 0.00008585058851738574",
            "extra": "mean: 2.0153975323386013 msec\nrounds: 402"
          },
          {
            "name": "Items Limit: (50)",
            "value": 175.94324493184106,
            "unit": "iter/sec",
            "range": "stddev: 0.00006159924508100725",
            "extra": "mean: 5.683650999999412 msec\nrounds: 169"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.32515000131643,
            "unit": "iter/sec",
            "range": "stddev: 0.00005379654926785608",
            "extra": "mean: 10.170337904255538 msec\nrounds: 94"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.51540642034591,
            "unit": "iter/sec",
            "range": "stddev: 0.003956295829146527",
            "extra": "mean: 19.411668653846668 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 42.51505294143952,
            "unit": "iter/sec",
            "range": "stddev: 0.00011268530127273308",
            "extra": "mean: 23.521080906976778 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.360075783908247,
            "unit": "iter/sec",
            "range": "stddev: 0.00929492408937634",
            "extra": "mean: 96.52439044444507 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 649.48841463522,
            "unit": "iter/sec",
            "range": "stddev: 0.0001067966090870476",
            "extra": "mean: 1.539673345153727 msec\nrounds: 423"
          },
          {
            "name": "Collection",
            "value": 974.623106724046,
            "unit": "iter/sec",
            "range": "stddev: 0.00007991490183602091",
            "extra": "mean: 1.0260376478875533 msec\nrounds: 639"
          },
          {
            "name": "Collections With Model validation",
            "value": 172.72310052026975,
            "unit": "iter/sec",
            "range": "stddev: 0.0022596622068008325",
            "extra": "mean: 5.789613531645965 msec\nrounds: 158"
          },
          {
            "name": "Collections",
            "value": 514.393428118045,
            "unit": "iter/sec",
            "range": "stddev: 0.00005122834890286178",
            "extra": "mean: 1.944037278350524 msec\nrounds: 388"
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
          "id": "3e5fc1c74112e842bbac20de8f70ed71f01131be",
          "message": "fix AsyncBaseCoreClient urls (#675)",
          "timestamp": "2024-04-25T19:05:15+08:00",
          "tree_id": "757e3af959401b3b8921b8628ebb4d0d6196905e",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/3e5fc1c74112e842bbac20de8f70ed71f01131be"
        },
        "date": 1714043215990,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 565.1726387899511,
            "unit": "iter/sec",
            "range": "stddev: 0.0001585856396208055",
            "extra": "mean: 1.769370863637393 msec\nrounds: 264"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 169.58851181859677,
            "unit": "iter/sec",
            "range": "stddev: 0.0022973035165134667",
            "extra": "mean: 5.896625834358797 msec\nrounds: 163"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.206183578232626,
            "unit": "iter/sec",
            "range": "stddev: 0.0002513798874687181",
            "extra": "mean: 22.621269674417352 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 22.067716535214064,
            "unit": "iter/sec",
            "range": "stddev: 0.007520235100035357",
            "extra": "mean: 45.31506458333704 msec\nrounds: 24"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.48354143529633,
            "unit": "iter/sec",
            "range": "stddev: 0.007864383833050192",
            "extra": "mean: 87.08115049999776 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.171150088473683,
            "unit": "iter/sec",
            "range": "stddev: 0.00931174515811818",
            "extra": "mean: 109.03757874999798 msec\nrounds: 8"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.2742632667198817,
            "unit": "iter/sec",
            "range": "stddev: 0.014661444657702496",
            "extra": "mean: 439.70283239999617 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 843.2528243703576,
            "unit": "iter/sec",
            "range": "stddev: 0.00012117257696238999",
            "extra": "mean: 1.1858839616062749 msec\nrounds: 573"
          },
          {
            "name": "Items Limit: (10)",
            "value": 506.19804329442326,
            "unit": "iter/sec",
            "range": "stddev: 0.0000913283328677095",
            "extra": "mean: 1.97551138975534 msec\nrounds: 449"
          },
          {
            "name": "Items Limit: (50)",
            "value": 180.74035832381256,
            "unit": "iter/sec",
            "range": "stddev: 0.0001758317743115143",
            "extra": "mean: 5.532798591714698 msec\nrounds: 169"
          },
          {
            "name": "Items Limit: (100)",
            "value": 99.69819973705472,
            "unit": "iter/sec",
            "range": "stddev: 0.0002780579181424708",
            "extra": "mean: 10.03027138541531 msec\nrounds: 96"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.47279050939906,
            "unit": "iter/sec",
            "range": "stddev: 0.003884309235766814",
            "extra": "mean: 19.42774017308033 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 41.46411894560593,
            "unit": "iter/sec",
            "range": "stddev: 0.003617546787342253",
            "extra": "mean: 24.11723739534499 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.494535433861962,
            "unit": "iter/sec",
            "range": "stddev: 0.009051634826460654",
            "extra": "mean: 95.28768627274076 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 639.9592858679216,
            "unit": "iter/sec",
            "range": "stddev: 0.00015553367166541747",
            "extra": "mean: 1.5625994060603188 msec\nrounds: 495"
          },
          {
            "name": "Collection",
            "value": 933.2490751364891,
            "unit": "iter/sec",
            "range": "stddev: 0.00017614877587430656",
            "extra": "mean: 1.0715253051322322 msec\nrounds: 721"
          },
          {
            "name": "Collections With Model validation",
            "value": 177.0639744511894,
            "unit": "iter/sec",
            "range": "stddev: 0.00006307239860212442",
            "extra": "mean: 5.647676231709497 msec\nrounds: 164"
          },
          {
            "name": "Collections",
            "value": 487.6870884808422,
            "unit": "iter/sec",
            "range": "stddev: 0.0015445337956132767",
            "extra": "mean: 2.050495130217668 msec\nrounds: 407"
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
          "id": "47704ad9f906fce02c999b4156ae3f08f7570721",
          "message": "v2.5.5.post1 (#676)\n\n* 2.5.5.post1\r\n\r\n* fix version link",
          "timestamp": "2024-04-25T20:04:48+08:00",
          "tree_id": "9eafee04356e5e5a3a8f2da5561da11e6974f421",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/47704ad9f906fce02c999b4156ae3f08f7570721"
        },
        "date": 1714046788812,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 567.5373574216972,
            "unit": "iter/sec",
            "range": "stddev: 0.00008570274294958499",
            "extra": "mean: 1.761998548506068 msec\nrounds: 268"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 169.35420654282817,
            "unit": "iter/sec",
            "range": "stddev: 0.0022111613838416504",
            "extra": "mean: 5.904783946108293 msec\nrounds: 167"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 43.48576258131758,
            "unit": "iter/sec",
            "range": "stddev: 0.00025960847486716516",
            "extra": "mean: 22.99603227907107 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.05980189692512,
            "unit": "iter/sec",
            "range": "stddev: 0.008874905130452065",
            "extra": "mean: 47.48382747826356 msec\nrounds: 23"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.10417610074266,
            "unit": "iter/sec",
            "range": "stddev: 0.007868281317086147",
            "extra": "mean: 90.05620866667623 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 9.071191577800786,
            "unit": "iter/sec",
            "range": "stddev: 0.00784504053286514",
            "extra": "mean: 110.23910050000723 msec\nrounds: 10"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.1167813172792505,
            "unit": "iter/sec",
            "range": "stddev: 0.011543009530471438",
            "extra": "mean: 472.4153562000083 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 833.7123107618228,
            "unit": "iter/sec",
            "range": "stddev: 0.00008651246428357384",
            "extra": "mean: 1.1994545205722442 msec\nrounds: 559"
          },
          {
            "name": "Items Limit: (10)",
            "value": 480.6686464042685,
            "unit": "iter/sec",
            "range": "stddev: 0.0013431564013422748",
            "extra": "mean: 2.080435259259547 msec\nrounds: 405"
          },
          {
            "name": "Items Limit: (50)",
            "value": 176.3373415536073,
            "unit": "iter/sec",
            "range": "stddev: 0.00008870612408452591",
            "extra": "mean: 5.670948598802573 msec\nrounds: 167"
          },
          {
            "name": "Items Limit: (100)",
            "value": 98.33264986918789,
            "unit": "iter/sec",
            "range": "stddev: 0.00015236149357733214",
            "extra": "mean: 10.169562208791302 msec\nrounds: 91"
          },
          {
            "name": "Items Limit: (200)",
            "value": 52.65398892205785,
            "unit": "iter/sec",
            "range": "stddev: 0.0003865918060018038",
            "extra": "mean: 18.991913442308626 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 40.98133735057624,
            "unit": "iter/sec",
            "range": "stddev: 0.003820888465462798",
            "extra": "mean: 24.40135106976783 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.42805185765798,
            "unit": "iter/sec",
            "range": "stddev: 0.010055793862666593",
            "extra": "mean: 95.89518863637377 msec\nrounds: 11"
          },
          {
            "name": "Collection With Model validation",
            "value": 655.6952909744051,
            "unit": "iter/sec",
            "range": "stddev: 0.00007331645787821295",
            "extra": "mean: 1.5250986453081525 msec\nrounds: 437"
          },
          {
            "name": "Collection",
            "value": 966.0837946734896,
            "unit": "iter/sec",
            "range": "stddev: 0.00007081399473750932",
            "extra": "mean: 1.0351068980905256 msec\nrounds: 628"
          },
          {
            "name": "Collections With Model validation",
            "value": 172.36093622707477,
            "unit": "iter/sec",
            "range": "stddev: 0.0021692757558846444",
            "extra": "mean: 5.801778650601912 msec\nrounds: 166"
          },
          {
            "name": "Collections",
            "value": 490.6813062448629,
            "unit": "iter/sec",
            "range": "stddev: 0.00009905441656958051",
            "extra": "mean: 2.0379826728124297 msec\nrounds: 434"
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
          "id": "1299beac429242362aab9417ae20f9d18760bd8e",
          "message": "remove print (#677)",
          "timestamp": "2024-04-25T20:47:04+08:00",
          "tree_id": "8a08e7b3bebe505bcab711014a9345dbd4463b75",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/1299beac429242362aab9417ae20f9d18760bd8e"
        },
        "date": 1714049320104,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 542.7234042653166,
            "unit": "iter/sec",
            "range": "stddev: 0.00008699304968446448",
            "extra": "mean: 1.8425591970806892 msec\nrounds: 274"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 173.49395899547923,
            "unit": "iter/sec",
            "range": "stddev: 0.0018004688515113163",
            "extra": "mean: 5.763889450618031 msec\nrounds: 162"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 44.1616789259764,
            "unit": "iter/sec",
            "range": "stddev: 0.00017443188367684436",
            "extra": "mean: 22.644066627905957 msec\nrounds: 43"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 21.845893970200013,
            "unit": "iter/sec",
            "range": "stddev: 0.006929072838734295",
            "extra": "mean: 45.7751924166665 msec\nrounds: 24"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 11.345636361133668,
            "unit": "iter/sec",
            "range": "stddev: 0.007275407432279064",
            "extra": "mean: 88.13961316666763 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 8.959819499060227,
            "unit": "iter/sec",
            "range": "stddev: 0.01061477884770709",
            "extra": "mean: 111.60939125000091 msec\nrounds: 8"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 2.240172177267893,
            "unit": "iter/sec",
            "range": "stddev: 0.014406234053860753",
            "extra": "mean: 446.3942594000059 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 873.4384133653359,
            "unit": "iter/sec",
            "range": "stddev: 0.00007269584286373702",
            "extra": "mean: 1.1449004127801357 msec\nrounds: 579"
          },
          {
            "name": "Items Limit: (10)",
            "value": 491.54038497452814,
            "unit": "iter/sec",
            "range": "stddev: 0.00007856772984327353",
            "extra": "mean: 2.034420834112787 msec\nrounds: 428"
          },
          {
            "name": "Items Limit: (50)",
            "value": 177.8985563541976,
            "unit": "iter/sec",
            "range": "stddev: 0.00009541456468056727",
            "extra": "mean: 5.621181084848104 msec\nrounds: 165"
          },
          {
            "name": "Items Limit: (100)",
            "value": 99.75215866601859,
            "unit": "iter/sec",
            "range": "stddev: 0.00017766016637855094",
            "extra": "mean: 10.024845711340566 msec\nrounds: 97"
          },
          {
            "name": "Items Limit: (200)",
            "value": 51.49697298465359,
            "unit": "iter/sec",
            "range": "stddev: 0.0036842879896240885",
            "extra": "mean: 19.418617096154485 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (250)",
            "value": 43.20182353972157,
            "unit": "iter/sec",
            "range": "stddev: 0.0001761651915708434",
            "extra": "mean: 23.14717106977112 msec\nrounds: 43"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 10.736035016861274,
            "unit": "iter/sec",
            "range": "stddev: 0.007170670903321864",
            "extra": "mean: 93.14425655555978 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 681.0994830582503,
            "unit": "iter/sec",
            "range": "stddev: 0.00005536008378300648",
            "extra": "mean: 1.4682142989007028 msec\nrounds: 455"
          },
          {
            "name": "Collection",
            "value": 928.5314908150409,
            "unit": "iter/sec",
            "range": "stddev: 0.00007318652037004815",
            "extra": "mean: 1.0769693972599959 msec\nrounds: 730"
          },
          {
            "name": "Collections With Model validation",
            "value": 172.72293374334345,
            "unit": "iter/sec",
            "range": "stddev: 0.0020239893148309646",
            "extra": "mean: 5.7896191219513655 msec\nrounds: 164"
          },
          {
            "name": "Collections",
            "value": 508.03879361893183,
            "unit": "iter/sec",
            "range": "stddev: 0.00005889060313135593",
            "extra": "mean: 1.9683536229126568 msec\nrounds: 419"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "thomas.maschler@planet.com",
            "name": "Thomas Maschler",
            "username": "thomas-maschler"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "63cac39108962b43b224e76ccf9c01c6fa85f2a0",
          "message": "update to pydantic 2 (#625)\n\n* update to pydantic 2\r\n\r\n* update changelog\r\n\r\n* typo\r\n\r\n* add CI for Python 3.12\r\n\r\n* drop support for python 3.8\r\n\r\n* update python version for docs\r\n\r\n* update python for docs docker container\r\n\r\n* update python version in dockerfile\r\n\r\n* handle post requests\r\n\r\n* test wrapper\r\n\r\n* pass through StacBaseModel\r\n\r\n* keep py38\r\n\r\n* change install order\r\n\r\n* lint\r\n\r\n* revert back to >=3.8 in setup.py\r\n\r\n* add switch to use either TypeDict or StacPydantic Response\r\n\r\n* lint and format with ruff\r\n\r\n* remove comment\r\n\r\n* update change log\r\n\r\n* use Optional not | None\r\n\r\n* use Optional not | None\r\n\r\n* update dependencies\r\n\r\n* hard code versions and address other comments\r\n\r\n* remove response_model module, update openapi schema\r\n\r\n* add responses to transactions\r\n\r\n* do not wrap response into response_class\r\n\r\n* fix tests\r\n\r\n* update changelog, remove redundant variable\r\n\r\n* lint bench\r\n\r\n* reorder installs\r\n\r\n* do not push benchmark if not in stac-utils/stac-fastapi repo\r\n\r\n* Add text about response validation to readme.\r\n\r\n* fix warning\r\n\r\n* remove versions\r\n\r\n* fix\r\n\r\n* Update README.md\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-04-26T09:18:19+02:00",
          "tree_id": "9ed6cf23007b9ba01972ced03a2217446c85a6af",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/63cac39108962b43b224e76ccf9c01c6fa85f2a0"
        },
        "date": 1714115999097,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 819.8441900958779,
            "unit": "iter/sec",
            "range": "stddev: 0.00008488518320265134",
            "extra": "mean: 1.2197439612068892 msec\nrounds: 232"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 524.2810572210335,
            "unit": "iter/sec",
            "range": "stddev: 0.00006873372611662586",
            "extra": "mean: 1.9073738908297169 msec\nrounds: 229"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 211.75559447885183,
            "unit": "iter/sec",
            "range": "stddev: 0.004562516417429509",
            "extra": "mean: 4.72242540963833 msec\nrounds: 83"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 112.5865634167677,
            "unit": "iter/sec",
            "range": "stddev: 0.008481807388299376",
            "extra": "mean: 8.882054568965273 msec\nrounds: 58"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 56.383744466389274,
            "unit": "iter/sec",
            "range": "stddev: 0.012647233919502246",
            "extra": "mean: 17.735608187499974 msec\nrounds: 32"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 45.733758203695956,
            "unit": "iter/sec",
            "range": "stddev: 0.013887012426238072",
            "extra": "mean: 21.8656860769248 msec\nrounds: 13"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.992329899553882,
            "unit": "iter/sec",
            "range": "stddev: 0.02690205178273753",
            "extra": "mean: 90.97252439999863 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 858.197008821264,
            "unit": "iter/sec",
            "range": "stddev: 0.00009195565476843646",
            "extra": "mean: 1.1652336115381046 msec\nrounds: 520"
          },
          {
            "name": "Items Limit: (10)",
            "value": 535.0887103869725,
            "unit": "iter/sec",
            "range": "stddev: 0.00007943100661208034",
            "extra": "mean: 1.8688489975368887 msec\nrounds: 406"
          },
          {
            "name": "Items Limit: (50)",
            "value": 215.69250238407653,
            "unit": "iter/sec",
            "range": "stddev: 0.00010407497770745289",
            "extra": "mean: 4.636229766667239 msec\nrounds: 180"
          },
          {
            "name": "Items Limit: (100)",
            "value": 121.84186869038768,
            "unit": "iter/sec",
            "range": "stddev: 0.00011871403452900342",
            "extra": "mean: 8.20735934821469 msec\nrounds: 112"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.58844398004074,
            "unit": "iter/sec",
            "range": "stddev: 0.00011504776109126793",
            "extra": "mean: 15.017620779661717 msec\nrounds: 59"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.82414747407817,
            "unit": "iter/sec",
            "range": "stddev: 0.0002911833972925169",
            "extra": "mean: 18.579021627450807 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.619727378158206,
            "unit": "iter/sec",
            "range": "stddev: 0.010478436752897318",
            "extra": "mean: 73.42290871428807 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 972.4331050519801,
            "unit": "iter/sec",
            "range": "stddev: 0.00007321844195746032",
            "extra": "mean: 1.0283483715278763 msec\nrounds: 576"
          },
          {
            "name": "Collection",
            "value": 918.5760721913806,
            "unit": "iter/sec",
            "range": "stddev: 0.00005543337499620914",
            "extra": "mean: 1.0886414639719193 msec\nrounds: 569"
          },
          {
            "name": "Collections With Model validation",
            "value": 683.9577097530781,
            "unit": "iter/sec",
            "range": "stddev: 0.002672102178394492",
            "extra": "mean: 1.4620787012709004 msec\nrounds: 472"
          },
          {
            "name": "Collections",
            "value": 569.1283206088914,
            "unit": "iter/sec",
            "range": "stddev: 0.00007924937944360978",
            "extra": "mean: 1.7570729900246984 msec\nrounds: 401"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jeff@arturo.ai",
            "name": "Jeff Albrecht",
            "username": "geospatial-jeff"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "e7f82d6996af0f28574329d57f5a5e90431d66bb",
          "message": "allow user to pass middleware options (#442)\n\n* allow user to pass middleware options to stac api constructor, proxy add_middleware call\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: Pete Gadomski <pete.gadomski@gmail.com>\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-04-26T10:12:07+02:00",
          "tree_id": "e9e69d4d018840ba2943556f22ab9835bce3d07b",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/e7f82d6996af0f28574329d57f5a5e90431d66bb"
        },
        "date": 1714119219195,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 808.5303082899502,
            "unit": "iter/sec",
            "range": "stddev: 0.00009545102746479681",
            "extra": "mean: 1.2368120152663296 msec\nrounds: 262"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 554.0184950442601,
            "unit": "iter/sec",
            "range": "stddev: 0.00009631266974821096",
            "extra": "mean: 1.8049938927040885 msec\nrounds: 233"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 233.0598571097091,
            "unit": "iter/sec",
            "range": "stddev: 0.0000999517331172218",
            "extra": "mean: 4.290743212501269 msec\nrounds: 80"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 111.78910275614913,
            "unit": "iter/sec",
            "range": "stddev: 0.0082986720628056",
            "extra": "mean: 8.945415745766807 msec\nrounds: 59"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 56.999216078386794,
            "unit": "iter/sec",
            "range": "stddev: 0.013227168794239885",
            "extra": "mean: 17.544100933331684 msec\nrounds: 30"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.309870754355266,
            "unit": "iter/sec",
            "range": "stddev: 0.017420267898001794",
            "extra": "mean: 24.207289486486008 msec\nrounds: 37"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.703873273077331,
            "unit": "iter/sec",
            "range": "stddev: 0.025745715287844147",
            "extra": "mean: 93.42412549999324 msec\nrounds: 6"
          },
          {
            "name": "Items Limit: (1)",
            "value": 875.9681064688075,
            "unit": "iter/sec",
            "range": "stddev: 0.00009276629490944268",
            "extra": "mean: 1.1415940747331412 msec\nrounds: 562"
          },
          {
            "name": "Items Limit: (10)",
            "value": 554.9539955649952,
            "unit": "iter/sec",
            "range": "stddev: 0.00008540387304963514",
            "extra": "mean: 1.8019511671087367 msec\nrounds: 377"
          },
          {
            "name": "Items Limit: (50)",
            "value": 215.8939599653165,
            "unit": "iter/sec",
            "range": "stddev: 0.0001399368303929702",
            "extra": "mean: 4.631903551913405 msec\nrounds: 183"
          },
          {
            "name": "Items Limit: (100)",
            "value": 122.82809613046598,
            "unit": "iter/sec",
            "range": "stddev: 0.00011931438842957597",
            "extra": "mean: 8.141459743362109 msec\nrounds: 113"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.23266404125891,
            "unit": "iter/sec",
            "range": "stddev: 0.0001412900906486898",
            "extra": "mean: 15.098290465518053 msec\nrounds: 58"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.67084795406695,
            "unit": "iter/sec",
            "range": "stddev: 0.0008461909655837293",
            "extra": "mean: 18.63208870588049 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.339307996680386,
            "unit": "iter/sec",
            "range": "stddev: 0.011547962824047497",
            "extra": "mean: 74.9664075714317 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 973.1328658782963,
            "unit": "iter/sec",
            "range": "stddev: 0.00007425297139980332",
            "extra": "mean: 1.0276089063105014 msec\nrounds: 523"
          },
          {
            "name": "Collection",
            "value": 972.1736915572455,
            "unit": "iter/sec",
            "range": "stddev: 0.00010941405019055632",
            "extra": "mean: 1.0286227745971832 msec\nrounds: 559"
          },
          {
            "name": "Collections With Model validation",
            "value": 686.8305953794013,
            "unit": "iter/sec",
            "range": "stddev: 0.0031692417303426108",
            "extra": "mean: 1.4559630958891774 msec\nrounds: 365"
          },
          {
            "name": "Collections",
            "value": 599.7514599477108,
            "unit": "iter/sec",
            "range": "stddev: 0.00006281911871586397",
            "extra": "mean: 1.6673573418015268 msec\nrounds: 433"
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
          "id": "e4e4120ae6d1a9fe80910073af5889ae08c418f8",
          "message": "use Collection Pydantic model in PutCollection transaction (#679)\n\n* use Collection Pydantic model in PutCollection transaction\r\n\r\n* update output types",
          "timestamp": "2024-05-02T10:19:41+02:00",
          "tree_id": "b94404d8e0fa57f53c997143fffd719c32ce8655",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/e4e4120ae6d1a9fe80910073af5889ae08c418f8"
        },
        "date": 1714638083157,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 821.9883259489121,
            "unit": "iter/sec",
            "range": "stddev: 0.00008322204581373171",
            "extra": "mean: 1.2165622897935797 msec\nrounds: 245"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 549.731578629551,
            "unit": "iter/sec",
            "range": "stddev: 0.00010108991948330519",
            "extra": "mean: 1.8190695948247 msec\nrounds: 232"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 210.23251295485224,
            "unit": "iter/sec",
            "range": "stddev: 0.0038944211545421732",
            "extra": "mean: 4.7566381904722395 msec\nrounds: 84"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 111.26812235335188,
            "unit": "iter/sec",
            "range": "stddev: 0.008829249436945172",
            "extra": "mean: 8.98730003571302 msec\nrounds: 56"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 57.88537552873889,
            "unit": "iter/sec",
            "range": "stddev: 0.011335396131953697",
            "extra": "mean: 17.27552064516746 msec\nrounds: 31"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 52.92783532715557,
            "unit": "iter/sec",
            "range": "stddev: 0.00997228034971742",
            "extra": "mean: 18.893650076917694 msec\nrounds: 13"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.082095279697324,
            "unit": "iter/sec",
            "range": "stddev: 0.027790599179690685",
            "extra": "mean: 90.2356435999991 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 826.768790384227,
            "unit": "iter/sec",
            "range": "stddev: 0.00007758781837740531",
            "extra": "mean: 1.2095279981907234 msec\nrounds: 553"
          },
          {
            "name": "Items Limit: (10)",
            "value": 523.563349182721,
            "unit": "iter/sec",
            "range": "stddev: 0.00008594438672088471",
            "extra": "mean: 1.909988545915205 msec\nrounds: 392"
          },
          {
            "name": "Items Limit: (50)",
            "value": 214.57858204862092,
            "unit": "iter/sec",
            "range": "stddev: 0.00009353413256660849",
            "extra": "mean: 4.66029736263898 msec\nrounds: 182"
          },
          {
            "name": "Items Limit: (100)",
            "value": 121.25354082335492,
            "unit": "iter/sec",
            "range": "stddev: 0.00011249411713176957",
            "extra": "mean: 8.247181840708668 msec\nrounds: 113"
          },
          {
            "name": "Items Limit: (200)",
            "value": 61.31461808649878,
            "unit": "iter/sec",
            "range": "stddev: 0.006983527994224933",
            "extra": "mean: 16.309324451622015 msec\nrounds: 62"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.43603354486925,
            "unit": "iter/sec",
            "range": "stddev: 0.0005413689500098759",
            "extra": "mean: 19.07085514285334 msec\nrounds: 49"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.00639132769095,
            "unit": "iter/sec",
            "range": "stddev: 0.011284492122285857",
            "extra": "mean: 76.88527700000643 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 982.6749329794686,
            "unit": "iter/sec",
            "range": "stddev: 0.00010414447812544098",
            "extra": "mean: 1.0176305169075615 msec\nrounds: 621"
          },
          {
            "name": "Collection",
            "value": 922.3311290824786,
            "unit": "iter/sec",
            "range": "stddev: 0.00008085446296816726",
            "extra": "mean: 1.0842093131940427 msec\nrounds: 629"
          },
          {
            "name": "Collections With Model validation",
            "value": 754.8348347493974,
            "unit": "iter/sec",
            "range": "stddev: 0.00007938917672329994",
            "extra": "mean: 1.3247931255477852 msec\nrounds: 454"
          },
          {
            "name": "Collections",
            "value": 595.9735370109736,
            "unit": "iter/sec",
            "range": "stddev: 0.0000741136156141054",
            "extra": "mean: 1.6779268506037492 msec\nrounds: 415"
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
          "id": "0de6ace95acd76a4850b2ad95756926119d9fd69",
          "message": "move response class in route definitions (#683)",
          "timestamp": "2024-05-06T13:13:43+02:00",
          "tree_id": "ce65d8c96ddc348b5d70ac47c967fb301a5296ab",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/0de6ace95acd76a4850b2ad95756926119d9fd69"
        },
        "date": 1714994125738,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 771.8321239694433,
            "unit": "iter/sec",
            "range": "stddev: 0.0021335999607435593",
            "extra": "mean: 1.295618527584879 msec\nrounds: 290"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 546.7572298717197,
            "unit": "iter/sec",
            "range": "stddev: 0.00015471987412119426",
            "extra": "mean: 1.8289652982451101 msec\nrounds: 228"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 226.61135656800664,
            "unit": "iter/sec",
            "range": "stddev: 0.003918846685451725",
            "extra": "mean: 4.4128415060253054 msec\nrounds: 83"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 146.0575773575571,
            "unit": "iter/sec",
            "range": "stddev: 0.00015034200995755426",
            "extra": "mean: 6.846615000000611 msec\nrounds: 14"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 62.17220341600943,
            "unit": "iter/sec",
            "range": "stddev: 0.011091302336755371",
            "extra": "mean: 16.084358363636483 msec\nrounds: 33"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 49.083208734175166,
            "unit": "iter/sec",
            "range": "stddev: 0.013956265208619725",
            "extra": "mean: 20.3735661500005 msec\nrounds: 40"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.828069071012104,
            "unit": "iter/sec",
            "range": "stddev: 0.02701929094812828",
            "extra": "mean: 84.54465340000183 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 936.39074232479,
            "unit": "iter/sec",
            "range": "stddev: 0.000052243733273728325",
            "extra": "mean: 1.0679302504820651 msec\nrounds: 519"
          },
          {
            "name": "Items Limit: (10)",
            "value": 593.4404143982616,
            "unit": "iter/sec",
            "range": "stddev: 0.0000460600126521945",
            "extra": "mean: 1.685089144145976 msec\nrounds: 333"
          },
          {
            "name": "Items Limit: (50)",
            "value": 226.22061050534913,
            "unit": "iter/sec",
            "range": "stddev: 0.000077757989462752",
            "extra": "mean: 4.420463713567577 msec\nrounds: 199"
          },
          {
            "name": "Items Limit: (100)",
            "value": 121.72639691564547,
            "unit": "iter/sec",
            "range": "stddev: 0.005247157977289039",
            "extra": "mean: 8.215144991870455 msec\nrounds: 123"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.9164280514836,
            "unit": "iter/sec",
            "range": "stddev: 0.006680625529006309",
            "extra": "mean: 15.170724955225978 msec\nrounds: 67"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.52698778980827,
            "unit": "iter/sec",
            "range": "stddev: 0.007738770289921331",
            "extra": "mean: 18.68216466666939 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.764373587056618,
            "unit": "iter/sec",
            "range": "stddev: 0.016592817476736473",
            "extra": "mean: 72.65132653333049 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1060.9008033124737,
            "unit": "iter/sec",
            "range": "stddev: 0.00004256877986249087",
            "extra": "mean: 942.5951954015666 usec\nrounds: 435"
          },
          {
            "name": "Collection",
            "value": 975.4642240278812,
            "unit": "iter/sec",
            "range": "stddev: 0.0000765221561368927",
            "extra": "mean: 1.0251529224422047 msec\nrounds: 606"
          },
          {
            "name": "Collections With Model validation",
            "value": 718.0130321734049,
            "unit": "iter/sec",
            "range": "stddev: 0.00008251786220850332",
            "extra": "mean: 1.3927323811561312 msec\nrounds: 467"
          },
          {
            "name": "Collections",
            "value": 576.5548456037897,
            "unit": "iter/sec",
            "range": "stddev: 0.00008932467836468924",
            "extra": "mean: 1.7344403704607891 msec\nrounds: 413"
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
          "id": "b9cfe2ddc947869b087879b7e8fab5daf31da06a",
          "message": "Release/v3.0.0a0 (#685)\n\n* prepare prerelease\r\n\r\n* Bump version: 2.5.5.post1 → 3.0.0a0",
          "timestamp": "2024-05-06T18:04:31+02:00",
          "tree_id": "e39a9adc8065eca218229a77c20a04699a75f48f",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/b9cfe2ddc947869b087879b7e8fab5daf31da06a"
        },
        "date": 1715011676576,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 670.8463085839841,
            "unit": "iter/sec",
            "range": "stddev: 0.002660948987016931",
            "extra": "mean: 1.4906543975933777 msec\nrounds: 249"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 566.6071851387468,
            "unit": "iter/sec",
            "range": "stddev: 0.00013557437367325557",
            "extra": "mean: 1.7648911383909243 msec\nrounds: 224"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 248.9326972189153,
            "unit": "iter/sec",
            "range": "stddev: 0.0000895566851579267",
            "extra": "mean: 4.017150061731683 msec\nrounds: 81"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 122.22826493478752,
            "unit": "iter/sec",
            "range": "stddev: 0.007566423071205812",
            "extra": "mean: 8.181413689652965 msec\nrounds: 58"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 62.30457930036358,
            "unit": "iter/sec",
            "range": "stddev: 0.012424861936530031",
            "extra": "mean: 16.05018461290155 msec\nrounds: 31"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.14310638445259,
            "unit": "iter/sec",
            "range": "stddev: 0.018460419728368756",
            "extra": "mean: 22.653593775000047 msec\nrounds: 40"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.735572049674152,
            "unit": "iter/sec",
            "range": "stddev: 0.03431776062774762",
            "extra": "mean: 102.71610080000073 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 912.353388101076,
            "unit": "iter/sec",
            "range": "stddev: 0.00006529804807826305",
            "extra": "mean: 1.0960665165954466 msec\nrounds: 482"
          },
          {
            "name": "Items Limit: (10)",
            "value": 552.8422235401559,
            "unit": "iter/sec",
            "range": "stddev: 0.00010645344838491625",
            "extra": "mean: 1.808834342638383 msec\nrounds: 394"
          },
          {
            "name": "Items Limit: (50)",
            "value": 219.08776133810545,
            "unit": "iter/sec",
            "range": "stddev: 0.0004799641453306314",
            "extra": "mean: 4.564380930693604 msec\nrounds: 202"
          },
          {
            "name": "Items Limit: (100)",
            "value": 128.37404354319403,
            "unit": "iter/sec",
            "range": "stddev: 0.0004995238559014211",
            "extra": "mean: 7.789736713119346 msec\nrounds: 122"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.22376759420513,
            "unit": "iter/sec",
            "range": "stddev: 0.005160392288123931",
            "extra": "mean: 15.100318757574044 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 56.31632779955577,
            "unit": "iter/sec",
            "range": "stddev: 0.0009008695982464111",
            "extra": "mean: 17.756839607142997 msec\nrounds: 56"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.084471996384277,
            "unit": "iter/sec",
            "range": "stddev: 0.011166429825930782",
            "extra": "mean: 71.00017666666645 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 991.5154636050916,
            "unit": "iter/sec",
            "range": "stddev: 0.00009389965602770718",
            "extra": "mean: 1.0085571397586268 msec\nrounds: 415"
          },
          {
            "name": "Collection",
            "value": 921.1970723639503,
            "unit": "iter/sec",
            "range": "stddev: 0.00008929416085054362",
            "extra": "mean: 1.0855440491509898 msec\nrounds: 590"
          },
          {
            "name": "Collections With Model validation",
            "value": 727.0264535783461,
            "unit": "iter/sec",
            "range": "stddev: 0.00010055383102694248",
            "extra": "mean: 1.375465768925061 msec\nrounds: 502"
          },
          {
            "name": "Collections",
            "value": 550.5615911280838,
            "unit": "iter/sec",
            "range": "stddev: 0.00011987696152722694",
            "extra": "mean: 1.8163272122761611 msec\nrounds: 391"
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
          "id": "55e1dddf4164bd607801c3c2e4f8bdc00d13957e",
          "message": "use literal instead of Enum for FilterLang (#686)",
          "timestamp": "2024-05-07T14:22:03+02:00",
          "tree_id": "7397dd8337ee1983829a5132fc6ecaadb7cec774",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/55e1dddf4164bd607801c3c2e4f8bdc00d13957e"
        },
        "date": 1715084641240,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 707.9400739853028,
            "unit": "iter/sec",
            "range": "stddev: 0.002588115352121586",
            "extra": "mean: 1.412548938458258 msec\nrounds: 260"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 593.8433661428076,
            "unit": "iter/sec",
            "range": "stddev: 0.00007269897850029116",
            "extra": "mean: 1.683945728812806 msec\nrounds: 236"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 254.29273358511372,
            "unit": "iter/sec",
            "range": "stddev: 0.00007298394430297493",
            "extra": "mean: 3.9324757176566836 msec\nrounds: 85"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 121.9281821927887,
            "unit": "iter/sec",
            "range": "stddev: 0.007686506247194639",
            "extra": "mean: 8.201549322033145 msec\nrounds: 59"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 56.87727096056023,
            "unit": "iter/sec",
            "range": "stddev: 0.01489055397148171",
            "extra": "mean: 17.58171556250332 msec\nrounds: 32"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.98905064920271,
            "unit": "iter/sec",
            "range": "stddev: 0.01688886683788302",
            "extra": "mean: 22.227630625002348 msec\nrounds: 40"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.973894509618027,
            "unit": "iter/sec",
            "range": "stddev: 0.029398297953955852",
            "extra": "mean: 91.1253520000173 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 922.2835038589823,
            "unit": "iter/sec",
            "range": "stddev: 0.00007279865010943862",
            "extra": "mean: 1.0842653000035667 msec\nrounds: 550"
          },
          {
            "name": "Items Limit: (10)",
            "value": 548.46366887871,
            "unit": "iter/sec",
            "range": "stddev: 0.000067090875280746",
            "extra": "mean: 1.8232748251938362 msec\nrounds: 389"
          },
          {
            "name": "Items Limit: (50)",
            "value": 226.9996098326567,
            "unit": "iter/sec",
            "range": "stddev: 0.00012858394174618512",
            "extra": "mean: 4.405293915426535 msec\nrounds: 201"
          },
          {
            "name": "Items Limit: (100)",
            "value": 130.4750745880874,
            "unit": "iter/sec",
            "range": "stddev: 0.00011895835400122056",
            "extra": "mean: 7.664299125001624 msec\nrounds: 120"
          },
          {
            "name": "Items Limit: (200)",
            "value": 67.42986774838438,
            "unit": "iter/sec",
            "range": "stddev: 0.007082293739674403",
            "extra": "mean: 14.83022336231647 msec\nrounds: 69"
          },
          {
            "name": "Items Limit: (250)",
            "value": 58.186959926790145,
            "unit": "iter/sec",
            "range": "stddev: 0.00026145782618831426",
            "extra": "mean: 17.18598121053554 msec\nrounds: 57"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.626369921533216,
            "unit": "iter/sec",
            "range": "stddev: 0.00989550714805431",
            "extra": "mean: 68.36966419998589 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1042.616480922723,
            "unit": "iter/sec",
            "range": "stddev: 0.00006782448598379652",
            "extra": "mean: 959.1254486165353 usec\nrounds: 506"
          },
          {
            "name": "Collection",
            "value": 1018.4261940666681,
            "unit": "iter/sec",
            "range": "stddev: 0.00007783171789981882",
            "extra": "mean: 981.9071876057207 usec\nrounds: 581"
          },
          {
            "name": "Collections With Model validation",
            "value": 718.6066725950257,
            "unit": "iter/sec",
            "range": "stddev: 0.00010919241562712394",
            "extra": "mean: 1.391581846003196 msec\nrounds: 513"
          },
          {
            "name": "Collections",
            "value": 568.3739168584451,
            "unit": "iter/sec",
            "range": "stddev: 0.00010024303440758539",
            "extra": "mean: 1.7594051562521866 msec\nrounds: 416"
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
          "id": "add05de82f745a717b674ada796db0e9f7153e27",
          "message": "switch to fastapi-slim (#687)",
          "timestamp": "2024-05-07T14:25:45+02:00",
          "tree_id": "9a91a801826b0563a5678131b1fbad582ff77f0a",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/add05de82f745a717b674ada796db0e9f7153e27"
        },
        "date": 1715084850388,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 759.2284408336413,
            "unit": "iter/sec",
            "range": "stddev: 0.00006088037115849713",
            "extra": "mean: 1.317126633061834 msec\nrounds: 248"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 527.699500636444,
            "unit": "iter/sec",
            "range": "stddev: 0.00011313390990047783",
            "extra": "mean: 1.895017900896111 msec\nrounds: 222"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 209.7021213078864,
            "unit": "iter/sec",
            "range": "stddev: 0.003934217985951719",
            "extra": "mean: 4.7686689756075085 msec\nrounds: 82"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 109.36252562697041,
            "unit": "iter/sec",
            "range": "stddev: 0.008651513578268336",
            "extra": "mean: 9.143900017552129 msec\nrounds: 57"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.089787925532214,
            "unit": "iter/sec",
            "range": "stddev: 0.012947569019420395",
            "extra": "mean: 18.15218460001612 msec\nrounds: 30"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.68244034933993,
            "unit": "iter/sec",
            "range": "stddev: 0.016327668784154346",
            "extra": "mean: 23.428838459454784 msec\nrounds: 37"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.004427829615747,
            "unit": "iter/sec",
            "range": "stddev: 0.027544574121440613",
            "extra": "mean: 90.87251200000992 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 862.3349743089464,
            "unit": "iter/sec",
            "range": "stddev: 0.00008193594311452389",
            "extra": "mean: 1.159642168985869 msec\nrounds: 503"
          },
          {
            "name": "Items Limit: (10)",
            "value": 546.6857835309411,
            "unit": "iter/sec",
            "range": "stddev: 0.00010878238751252961",
            "extra": "mean: 1.8292043256387376 msec\nrounds: 390"
          },
          {
            "name": "Items Limit: (50)",
            "value": 216.99994079532377,
            "unit": "iter/sec",
            "range": "stddev: 0.00007363051638600237",
            "extra": "mean: 4.60829618816905 msec\nrounds: 186"
          },
          {
            "name": "Items Limit: (100)",
            "value": 123.14044905756661,
            "unit": "iter/sec",
            "range": "stddev: 0.00016509404183899986",
            "extra": "mean: 8.120808456143541 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 63.5028278229058,
            "unit": "iter/sec",
            "range": "stddev: 0.0052931645932395525",
            "extra": "mean: 15.74733022580917 msec\nrounds: 62"
          },
          {
            "name": "Items Limit: (250)",
            "value": 51.374960313829774,
            "unit": "iter/sec",
            "range": "stddev: 0.007514298746220899",
            "extra": "mean: 19.464735230769747 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.749937510830586,
            "unit": "iter/sec",
            "range": "stddev: 0.0010494625575070747",
            "extra": "mean: 72.7276032500015 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 988.0698950371257,
            "unit": "iter/sec",
            "range": "stddev: 0.00008002934326631196",
            "extra": "mean: 1.0120741508498505 msec\nrounds: 590"
          },
          {
            "name": "Collection",
            "value": 978.7476643508795,
            "unit": "iter/sec",
            "range": "stddev: 0.00008054542993233796",
            "extra": "mean: 1.0217138047151462 msec\nrounds: 594"
          },
          {
            "name": "Collections With Model validation",
            "value": 765.3672649798591,
            "unit": "iter/sec",
            "range": "stddev: 0.000059790260915006636",
            "extra": "mean: 1.3065622816077915 msec\nrounds: 348"
          },
          {
            "name": "Collections",
            "value": 572.6318374058205,
            "unit": "iter/sec",
            "range": "stddev: 0.00009964105967512818",
            "extra": "mean: 1.7463227412053697 msec\nrounds: 398"
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
          "id": "096c93032335d43fd45433297e804f8582c803a5",
          "message": "Remove pystac (#690)\n\n* remove pystac\r\n\r\n* update, fix changelog\r\n\r\n* fix link\r\n\r\n* Update stac_fastapi/types/stac_fastapi/types/rfc3339.py\r\n\r\nCo-authored-by: Pete Gadomski <pete.gadomski@gmail.com>\r\n\r\n---------\r\n\r\nCo-authored-by: Pete Gadomski <pete.gadomski@gmail.com>",
          "timestamp": "2024-05-09T23:17:07+08:00",
          "tree_id": "de7783b05710ac4807bda2e8d1758a18506dc415",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/096c93032335d43fd45433297e804f8582c803a5"
        },
        "date": 1715267920167,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 736.509554202854,
            "unit": "iter/sec",
            "range": "stddev: 0.0000691313227103376",
            "extra": "mean: 1.3577556384619198 msec\nrounds: 260"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 552.6707462455498,
            "unit": "iter/sec",
            "range": "stddev: 0.00008589364284525226",
            "extra": "mean: 1.8093955701351763 msec\nrounds: 221"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 214.1719216466221,
            "unit": "iter/sec",
            "range": "stddev: 0.003459049011536881",
            "extra": "mean: 4.669146134150923 msec\nrounds: 82"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 104.50234435331852,
            "unit": "iter/sec",
            "range": "stddev: 0.00929899731876007",
            "extra": "mean: 9.569163315791627 msec\nrounds: 57"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 52.31077407911798,
            "unit": "iter/sec",
            "range": "stddev: 0.014550688749318141",
            "extra": "mean: 19.116520785709262 msec\nrounds: 28"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.77674486217959,
            "unit": "iter/sec",
            "range": "stddev: 0.015326540738710622",
            "extra": "mean: 23.936762026313307 msec\nrounds: 38"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.669586587835063,
            "unit": "iter/sec",
            "range": "stddev: 0.02171243924930733",
            "extra": "mean: 85.69283859999359 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 899.3262995637913,
            "unit": "iter/sec",
            "range": "stddev: 0.00006211283947535164",
            "extra": "mean: 1.1119434631068161 msec\nrounds: 393"
          },
          {
            "name": "Items Limit: (10)",
            "value": 555.7569431174064,
            "unit": "iter/sec",
            "range": "stddev: 0.00010289212285314949",
            "extra": "mean: 1.7993477407420262 msec\nrounds: 405"
          },
          {
            "name": "Items Limit: (50)",
            "value": 200.38964212597475,
            "unit": "iter/sec",
            "range": "stddev: 0.0041210833961997425",
            "extra": "mean: 4.990277887573406 msec\nrounds: 169"
          },
          {
            "name": "Items Limit: (100)",
            "value": 121.96984248343159,
            "unit": "iter/sec",
            "range": "stddev: 0.00008918792324907998",
            "extra": "mean: 8.198747982607589 msec\nrounds: 115"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.03901113109669,
            "unit": "iter/sec",
            "range": "stddev: 0.004218509674078214",
            "extra": "mean: 15.615481600002568 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.36320781212046,
            "unit": "iter/sec",
            "range": "stddev: 0.000518505397977133",
            "extra": "mean: 18.739503133334285 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 12.863328684898535,
            "unit": "iter/sec",
            "range": "stddev: 0.017053652093788705",
            "extra": "mean: 77.74037533332982 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1037.275991776881,
            "unit": "iter/sec",
            "range": "stddev: 0.00006923188306839562",
            "extra": "mean: 964.0635741380398 usec\nrounds: 580"
          },
          {
            "name": "Collection",
            "value": 918.2101843636683,
            "unit": "iter/sec",
            "range": "stddev: 0.00006153502094377815",
            "extra": "mean: 1.0890752651507707 msec\nrounds: 396"
          },
          {
            "name": "Collections With Model validation",
            "value": 712.4518226281191,
            "unit": "iter/sec",
            "range": "stddev: 0.00009149028875095866",
            "extra": "mean: 1.4036036799108218 msec\nrounds: 453"
          },
          {
            "name": "Collections",
            "value": 565.0862669642034,
            "unit": "iter/sec",
            "range": "stddev: 0.00009979583108800697",
            "extra": "mean: 1.7696413069322512 msec\nrounds: 404"
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
          "id": "f815c236cde78a3442fe18c103f43ee1db668872",
          "message": "update conformance and spec urls (#691)",
          "timestamp": "2024-05-14T13:57:25+02:00",
          "tree_id": "68a7b2bb5e692e1720db11d863624ed709d56ad2",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/f815c236cde78a3442fe18c103f43ee1db668872"
        },
        "date": 1715687944686,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 792.4682293247944,
            "unit": "iter/sec",
            "range": "stddev: 0.00009633662093991684",
            "extra": "mean: 1.2618802407410437 msec\nrounds: 270"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 541.2871543742687,
            "unit": "iter/sec",
            "range": "stddev: 0.00008614629800601376",
            "extra": "mean: 1.8474482387375446 msec\nrounds: 222"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 182.01990399786288,
            "unit": "iter/sec",
            "range": "stddev: 0.008001950660648925",
            "extra": "mean: 5.49390466666624 msec\nrounds: 63"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 102.11386183883884,
            "unit": "iter/sec",
            "range": "stddev: 0.009339184069094798",
            "extra": "mean: 9.792989727273753 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 48.41627274866593,
            "unit": "iter/sec",
            "range": "stddev: 0.016355861276640227",
            "extra": "mean: 20.65421279310589 msec\nrounds: 29"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 36.45313289857506,
            "unit": "iter/sec",
            "range": "stddev: 0.021143688347687442",
            "extra": "mean: 27.432484411760658 msec\nrounds: 34"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.51026453407513,
            "unit": "iter/sec",
            "range": "stddev: 0.0256134565991671",
            "extra": "mean: 105.1495462000048 msec\nrounds: 5"
          },
          {
            "name": "Items Limit: (1)",
            "value": 899.0421502632285,
            "unit": "iter/sec",
            "range": "stddev: 0.00006362752461046529",
            "extra": "mean: 1.1122949015318273 msec\nrounds: 457"
          },
          {
            "name": "Items Limit: (10)",
            "value": 550.4184663262854,
            "unit": "iter/sec",
            "range": "stddev: 0.00011100466029529878",
            "extra": "mean: 1.816799510151618 msec\nrounds: 394"
          },
          {
            "name": "Items Limit: (50)",
            "value": 211.92669258859266,
            "unit": "iter/sec",
            "range": "stddev: 0.0001394836946060757",
            "extra": "mean: 4.718612779661843 msec\nrounds: 177"
          },
          {
            "name": "Items Limit: (100)",
            "value": 119.11528917712938,
            "unit": "iter/sec",
            "range": "stddev: 0.000292001932751505",
            "extra": "mean: 8.395227908257507 msec\nrounds: 109"
          },
          {
            "name": "Items Limit: (200)",
            "value": 63.952216336470265,
            "unit": "iter/sec",
            "range": "stddev: 0.00045318831486729807",
            "extra": "mean: 15.63667465000312 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.05889260832415,
            "unit": "iter/sec",
            "range": "stddev: 0.00042620978924320094",
            "extra": "mean: 19.209014058821936 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 12.986147312121963,
            "unit": "iter/sec",
            "range": "stddev: 0.010338242639861437",
            "extra": "mean: 77.00513292857433 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 958.2684800426429,
            "unit": "iter/sec",
            "range": "stddev: 0.0001072371707633814",
            "extra": "mean: 1.0435488809519229 msec\nrounds: 546"
          },
          {
            "name": "Collection",
            "value": 989.5716724346022,
            "unit": "iter/sec",
            "range": "stddev: 0.00008721077009662129",
            "extra": "mean: 1.0105382236131935 msec\nrounds: 559"
          },
          {
            "name": "Collections With Model validation",
            "value": 638.5166644018487,
            "unit": "iter/sec",
            "range": "stddev: 0.003037434477751053",
            "extra": "mean: 1.5661298377181472 msec\nrounds: 456"
          },
          {
            "name": "Collections",
            "value": 553.0881894635544,
            "unit": "iter/sec",
            "range": "stddev: 0.00009292658703628265",
            "extra": "mean: 1.808029929132838 msec\nrounds: 381"
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
          "id": "5a4d5b9c57f71ce94edc1d9f925253716195a119",
          "message": "Feature/update stac pydantic3.1.0 (#697)\n\n* update stac-pydantic dependendy\r\n\r\n* replace stac-pydantic todos\r\n\r\n* fix benchmark\r\n\r\n* replace deprecated .dict()\r\n\r\n* fix datetime interval for GET Search\r\n\r\n* update changelog",
          "timestamp": "2024-05-21T21:14:42+02:00",
          "tree_id": "2cc32927a276cdace164ee475f750bc74b505680",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/5a4d5b9c57f71ce94edc1d9f925253716195a119"
        },
        "date": 1716318975490,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 837.5511260483164,
            "unit": "iter/sec",
            "range": "stddev: 0.00007511805673152185",
            "extra": "mean: 1.1939569644161785 msec\nrounds: 281"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 533.8870004032854,
            "unit": "iter/sec",
            "range": "stddev: 0.00010156494587395753",
            "extra": "mean: 1.873055532808673 msec\nrounds: 381"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 191.1077899672577,
            "unit": "iter/sec",
            "range": "stddev: 0.00595757068866022",
            "extra": "mean: 5.2326490729202035 msec\nrounds: 192"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 101.8041706517048,
            "unit": "iter/sec",
            "range": "stddev: 0.008951684510071868",
            "extra": "mean: 9.822780280988953 msec\nrounds: 121"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 48.58517521536929,
            "unit": "iter/sec",
            "range": "stddev: 0.016009980829134268",
            "extra": "mean: 20.582410078119118 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 40.5029255034745,
            "unit": "iter/sec",
            "range": "stddev: 0.016728061073077803",
            "extra": "mean: 24.689574581821656 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.266935146109015,
            "unit": "iter/sec",
            "range": "stddev: 0.02385736750188907",
            "extra": "mean: 97.40005033332484 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 866.697004877434,
            "unit": "iter/sec",
            "range": "stddev: 0.0001000930464893565",
            "extra": "mean: 1.1538057641510109 msec\nrounds: 530"
          },
          {
            "name": "Items Limit: (10)",
            "value": 536.6650113719095,
            "unit": "iter/sec",
            "range": "stddev: 0.0001050636388795406",
            "extra": "mean: 1.8633597846143146 msec\nrounds: 390"
          },
          {
            "name": "Items Limit: (50)",
            "value": 223.63046147555562,
            "unit": "iter/sec",
            "range": "stddev: 0.0000729264064912816",
            "extra": "mean: 4.471662730568156 msec\nrounds: 193"
          },
          {
            "name": "Items Limit: (100)",
            "value": 118.66529350379066,
            "unit": "iter/sec",
            "range": "stddev: 0.0044216056760204465",
            "extra": "mean: 8.42706380672337 msec\nrounds: 119"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.02794170063831,
            "unit": "iter/sec",
            "range": "stddev: 0.0068310929397210765",
            "extra": "mean: 15.618181272724417 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.26965405067979,
            "unit": "iter/sec",
            "range": "stddev: 0.0007930781979309431",
            "extra": "mean: 18.09311125926435 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.014541688161392,
            "unit": "iter/sec",
            "range": "stddev: 0.0006836742626606606",
            "extra": "mean: 71.35445612500746 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 944.813716571686,
            "unit": "iter/sec",
            "range": "stddev: 0.00008384877401490467",
            "extra": "mean: 1.0584096975524029 msec\nrounds: 572"
          },
          {
            "name": "Collection",
            "value": 934.9912314334581,
            "unit": "iter/sec",
            "range": "stddev: 0.00009061418323244336",
            "extra": "mean: 1.069528746774315 msec\nrounds: 620"
          },
          {
            "name": "Collections With Model validation",
            "value": 676.7160979778901,
            "unit": "iter/sec",
            "range": "stddev: 0.002388560209719491",
            "extra": "mean: 1.4777245627643876 msec\nrounds: 478"
          },
          {
            "name": "Collections",
            "value": 566.3367620250679,
            "unit": "iter/sec",
            "range": "stddev: 0.0001288436323114519",
            "extra": "mean: 1.7657338655259975 msec\nrounds: 409"
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
          "id": "d2fd4a6ab3a9869d2c2b622fb84c9e9304c9aab1",
          "message": "Make `str_to_interval` not return a tuple for single-value input (#692)\n\n* Do not return tuple for single-value input\r\n\r\n* Add PR reference to changelog\r\n\r\n* update from main\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-05-22T09:25:12+02:00",
          "tree_id": "8f1a0a66b983e2a4b03f2a8acc3ef365b1c890a3",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/d2fd4a6ab3a9869d2c2b622fb84c9e9304c9aab1"
        },
        "date": 1716362804047,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 823.7237156563929,
            "unit": "iter/sec",
            "range": "stddev: 0.00006929188165142522",
            "extra": "mean: 1.2139992827608945 msec\nrounds: 290"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 522.497759279722,
            "unit": "iter/sec",
            "range": "stddev: 0.00009710074896445238",
            "extra": "mean: 1.913883805700006 msec\nrounds: 386"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 201.67476969648098,
            "unit": "iter/sec",
            "range": "stddev: 0.004924008016731242",
            "extra": "mean: 4.95847845273354 msec\nrounds: 201"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 100.47145270982506,
            "unit": "iter/sec",
            "range": "stddev: 0.009434151324184736",
            "extra": "mean: 9.953075953705312 msec\nrounds: 108"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 54.06408119894637,
            "unit": "iter/sec",
            "range": "stddev: 0.013028370437922007",
            "extra": "mean: 18.496568846147127 msec\nrounds: 13"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 37.088758474133094,
            "unit": "iter/sec",
            "range": "stddev: 0.017903699063028383",
            "extra": "mean: 26.962347653061304 msec\nrounds: 49"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.328043242469873,
            "unit": "iter/sec",
            "range": "stddev: 0.025726728499486786",
            "extra": "mean: 107.20361966667093 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 875.7842933736779,
            "unit": "iter/sec",
            "range": "stddev: 0.00006713370477700387",
            "extra": "mean: 1.141833677043717 msec\nrounds: 514"
          },
          {
            "name": "Items Limit: (10)",
            "value": 559.3095332236041,
            "unit": "iter/sec",
            "range": "stddev: 0.00010653750168226603",
            "extra": "mean: 1.7879187473105596 msec\nrounds: 372"
          },
          {
            "name": "Items Limit: (50)",
            "value": 217.8190898253867,
            "unit": "iter/sec",
            "range": "stddev: 0.00023442122229911072",
            "extra": "mean: 4.590965836840304 msec\nrounds: 190"
          },
          {
            "name": "Items Limit: (100)",
            "value": 123.43654310158537,
            "unit": "iter/sec",
            "range": "stddev: 0.00037824458835563084",
            "extra": "mean: 8.101328625000649 msec\nrounds: 112"
          },
          {
            "name": "Items Limit: (200)",
            "value": 62.98356223499865,
            "unit": "iter/sec",
            "range": "stddev: 0.005346619637811514",
            "extra": "mean: 15.877158492066377 msec\nrounds: 63"
          },
          {
            "name": "Items Limit: (250)",
            "value": 49.117412231528206,
            "unit": "iter/sec",
            "range": "stddev: 0.009016539111466243",
            "extra": "mean: 20.359378773585007 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.1401419535554,
            "unit": "iter/sec",
            "range": "stddev: 0.0004514488836296963",
            "extra": "mean: 70.72064787500665 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 991.9287192182481,
            "unit": "iter/sec",
            "range": "stddev: 0.00006565495317891322",
            "extra": "mean: 1.0081369564419034 msec\nrounds: 528"
          },
          {
            "name": "Collection",
            "value": 912.6947003161969,
            "unit": "iter/sec",
            "range": "stddev: 0.00014771274358853494",
            "extra": "mean: 1.0956566304740858 msec\nrounds: 571"
          },
          {
            "name": "Collections With Model validation",
            "value": 722.1052566496815,
            "unit": "iter/sec",
            "range": "stddev: 0.00008391717229632009",
            "extra": "mean: 1.3848396626270996 msec\nrounds: 495"
          },
          {
            "name": "Collections",
            "value": 561.9825265231575,
            "unit": "iter/sec",
            "range": "stddev: 0.00010368987953217317",
            "extra": "mean: 1.7794147554493283 msec\nrounds: 413"
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
          "id": "a6a57655430d11dfb3ed3140057d3339d04ffb0d",
          "message": "BUGFIX: invalid landing page link when `filter-extension` is enabled (#695)\n\n* add test demonstrating bug\r\n\r\n* fix",
          "timestamp": "2024-05-22T09:39:55+02:00",
          "tree_id": "7bddaf3dda6337b48c7e7a843a59f8177dbd10f7",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/a6a57655430d11dfb3ed3140057d3339d04ffb0d"
        },
        "date": 1716363693601,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 759.5226611308465,
            "unit": "iter/sec",
            "range": "stddev: 0.00008776285659263801",
            "extra": "mean: 1.3166164107745109 msec\nrounds: 297"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 545.1415590877824,
            "unit": "iter/sec",
            "range": "stddev: 0.00007413162717182715",
            "extra": "mean: 1.8343859192708756 msec\nrounds: 384"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 202.4468638461393,
            "unit": "iter/sec",
            "range": "stddev: 0.004224063141701318",
            "extra": "mean: 4.939567751269317 msec\nrounds: 197"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 100.72346136981011,
            "unit": "iter/sec",
            "range": "stddev: 0.008991213891009686",
            "extra": "mean: 9.928173499999778 msec\nrounds: 114"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 53.58122754285125,
            "unit": "iter/sec",
            "range": "stddev: 0.012132864672987392",
            "extra": "mean: 18.663252893940445 msec\nrounds: 66"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 46.37738687096318,
            "unit": "iter/sec",
            "range": "stddev: 0.011634011490617208",
            "extra": "mean: 21.562232533331855 msec\nrounds: 15"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.722409164645955,
            "unit": "iter/sec",
            "range": "stddev: 0.020848255885118776",
            "extra": "mean: 93.26262266666812 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 895.4800750793373,
            "unit": "iter/sec",
            "range": "stddev: 0.00010095906547749916",
            "extra": "mean: 1.1167194310955522 msec\nrounds: 566"
          },
          {
            "name": "Items Limit: (10)",
            "value": 552.8498926276595,
            "unit": "iter/sec",
            "range": "stddev: 0.00008823707742407236",
            "extra": "mean: 1.8088092506395637 msec\nrounds: 391"
          },
          {
            "name": "Items Limit: (50)",
            "value": 223.57340174471955,
            "unit": "iter/sec",
            "range": "stddev: 0.000060678162645887424",
            "extra": "mean: 4.472803974874522 msec\nrounds: 199"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.6100835997559,
            "unit": "iter/sec",
            "range": "stddev: 0.00012267330606925497",
            "extra": "mean: 7.898265063636115 msec\nrounds: 110"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.63510153446529,
            "unit": "iter/sec",
            "range": "stddev: 0.0049402193728615386",
            "extra": "mean: 15.471469468749444 msec\nrounds: 64"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.52061941282034,
            "unit": "iter/sec",
            "range": "stddev: 0.007010974889105113",
            "extra": "mean: 19.040141018517748 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.96799079770851,
            "unit": "iter/sec",
            "range": "stddev: 0.008801874619897494",
            "extra": "mean: 71.59225793333519 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 945.5208742251743,
            "unit": "iter/sec",
            "range": "stddev: 0.00008241261193930868",
            "extra": "mean: 1.057618110038522 msec\nrounds: 518"
          },
          {
            "name": "Collection",
            "value": 1020.4529040996716,
            "unit": "iter/sec",
            "range": "stddev: 0.00006463482273913327",
            "extra": "mean: 979.9570327866165 usec\nrounds: 549"
          },
          {
            "name": "Collections With Model validation",
            "value": 719.8064303076693,
            "unit": "iter/sec",
            "range": "stddev: 0.00008201602951697905",
            "extra": "mean: 1.3892623876290835 msec\nrounds: 485"
          },
          {
            "name": "Collections",
            "value": 594.0414114296324,
            "unit": "iter/sec",
            "range": "stddev: 0.00006509641380334133",
            "extra": "mean: 1.6833843243240891 msec\nrounds: 407"
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
          "id": "1c3546a5b449edebc7587dab289f73224847c63e",
          "message": "Release/v3.0.0a1 (#699)\n\n* update changelog\r\n\r\n* Bump version: 3.0.0a0 → 3.0.0a1",
          "timestamp": "2024-05-22T19:01:58+08:00",
          "tree_id": "fffa7d89c86a25d1c5664c1ab74a34fdfc165ded",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/1c3546a5b449edebc7587dab289f73224847c63e"
        },
        "date": 1716375815974,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 757.7435323018218,
            "unit": "iter/sec",
            "range": "stddev: 0.00008390809138571209",
            "extra": "mean: 1.3197077340432957 msec\nrounds: 282"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 521.3660360207732,
            "unit": "iter/sec",
            "range": "stddev: 0.000095629973302279",
            "extra": "mean: 1.9180382512683587 msec\nrounds: 394"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 209.57615096689815,
            "unit": "iter/sec",
            "range": "stddev: 0.004190947740384282",
            "extra": "mean: 4.771535288659571 msec\nrounds: 194"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 110.61287240467153,
            "unit": "iter/sec",
            "range": "stddev: 0.007232968349053839",
            "extra": "mean: 9.040539118643906 msec\nrounds: 118"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 57.378703286058744,
            "unit": "iter/sec",
            "range": "stddev: 0.01091483236594342",
            "extra": "mean: 17.428069000000722 msec\nrounds: 66"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 45.6874993992903,
            "unit": "iter/sec",
            "range": "stddev: 0.011829009004222528",
            "extra": "mean: 21.88782518518695 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.532760939086197,
            "unit": "iter/sec",
            "range": "stddev: 0.018484483394673422",
            "extra": "mean: 86.70950566666609 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 875.9966961807738,
            "unit": "iter/sec",
            "range": "stddev: 0.00008524924495985871",
            "extra": "mean: 1.141556816777807 msec\nrounds: 453"
          },
          {
            "name": "Items Limit: (10)",
            "value": 546.9267197238161,
            "unit": "iter/sec",
            "range": "stddev: 0.00011332227553830974",
            "extra": "mean: 1.8283985110564251 msec\nrounds: 407"
          },
          {
            "name": "Items Limit: (50)",
            "value": 221.7741819416128,
            "unit": "iter/sec",
            "range": "stddev: 0.00010775289120817251",
            "extra": "mean: 4.509091145078706 msec\nrounds: 193"
          },
          {
            "name": "Items Limit: (100)",
            "value": 125.97633872623798,
            "unit": "iter/sec",
            "range": "stddev: 0.00017664312151475424",
            "extra": "mean: 7.93799859649138 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 68.78714411198504,
            "unit": "iter/sec",
            "range": "stddev: 0.00023882765736134566",
            "extra": "mean: 14.537600200002577 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.80103865505365,
            "unit": "iter/sec",
            "range": "stddev: 0.00011456770447488445",
            "extra": "mean: 17.92081337735878 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.683010274739244,
            "unit": "iter/sec",
            "range": "stddev: 0.011368563527133982",
            "extra": "mean: 73.08333326666721 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 964.89314163525,
            "unit": "iter/sec",
            "range": "stddev: 0.00008152715618727547",
            "extra": "mean: 1.0363841930778497 msec\nrounds: 549"
          },
          {
            "name": "Collection",
            "value": 944.8106258648778,
            "unit": "iter/sec",
            "range": "stddev: 0.00007657361410862182",
            "extra": "mean: 1.0584131598695792 msec\nrounds: 613"
          },
          {
            "name": "Collections With Model validation",
            "value": 662.0676706041409,
            "unit": "iter/sec",
            "range": "stddev: 0.002428863701055058",
            "extra": "mean: 1.5104196208334624 msec\nrounds: 480"
          },
          {
            "name": "Collections",
            "value": 540.2409258432098,
            "unit": "iter/sec",
            "range": "stddev: 0.00008377404527488315",
            "extra": "mean: 1.8510260000002718 msec\nrounds: 420"
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
          "id": "a8eec23ca48d94f801420e0857f1508f53970499",
          "message": "set default value for Query attribute for `QueryExtensionPostRequest` model (#701)",
          "timestamp": "2024-05-31T17:00:03+02:00",
          "tree_id": "5768d73d82f90887e36302b1472bdec6fb18c44f",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/a8eec23ca48d94f801420e0857f1508f53970499"
        },
        "date": 1717167703643,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 804.4932670476937,
            "unit": "iter/sec",
            "range": "stddev: 0.00008556145238438874",
            "extra": "mean: 1.2430184825160455 msec\nrounds: 286"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 544.0362358159751,
            "unit": "iter/sec",
            "range": "stddev: 0.00005709840060111869",
            "extra": "mean: 1.838112857501386 msec\nrounds: 400"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 213.27298283273583,
            "unit": "iter/sec",
            "range": "stddev: 0.003609695143738117",
            "extra": "mean: 4.688826436043578 msec\nrounds: 172"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 110.14686844516001,
            "unit": "iter/sec",
            "range": "stddev: 0.006468603824650283",
            "extra": "mean: 9.078787387386148 msec\nrounds: 111"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 58.255712216277665,
            "unit": "iter/sec",
            "range": "stddev: 0.009242657036557423",
            "extra": "mean: 17.165698640631888 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 46.954827070889856,
            "unit": "iter/sec",
            "range": "stddev: 0.010331738110783924",
            "extra": "mean: 21.297064910712038 msec\nrounds: 56"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.88462043014085,
            "unit": "iter/sec",
            "range": "stddev: 0.01795276320854876",
            "extra": "mean: 84.14235909999093 msec\nrounds: 10"
          },
          {
            "name": "Items Limit: (1)",
            "value": 855.5199080029657,
            "unit": "iter/sec",
            "range": "stddev: 0.00009091704830008732",
            "extra": "mean: 1.1688798713454758 msec\nrounds: 513"
          },
          {
            "name": "Items Limit: (10)",
            "value": 533.2214390731018,
            "unit": "iter/sec",
            "range": "stddev: 0.00007344256016477172",
            "extra": "mean: 1.8753934608073877 msec\nrounds: 421"
          },
          {
            "name": "Items Limit: (50)",
            "value": 220.77605836682915,
            "unit": "iter/sec",
            "range": "stddev: 0.00008275149351454182",
            "extra": "mean: 4.529476644330954 msec\nrounds: 194"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.36877520244845,
            "unit": "iter/sec",
            "range": "stddev: 0.00008799859650832947",
            "extra": "mean: 7.913347252103655 msec\nrounds: 119"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.2111438368695,
            "unit": "iter/sec",
            "range": "stddev: 0.00554587081379335",
            "extra": "mean: 15.334802323074936 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.828392632250186,
            "unit": "iter/sec",
            "range": "stddev: 0.0002385279747329544",
            "extra": "mean: 17.912032799997426 msec\nrounds: 55"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.312022850577097,
            "unit": "iter/sec",
            "range": "stddev: 0.007996790311998177",
            "extra": "mean: 69.8713249999931 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 977.6010389549183,
            "unit": "iter/sec",
            "range": "stddev: 0.00007130910948540306",
            "extra": "mean: 1.022912169844896 msec\nrounds: 577"
          },
          {
            "name": "Collection",
            "value": 968.6775797456696,
            "unit": "iter/sec",
            "range": "stddev: 0.00008344734546147768",
            "extra": "mean: 1.032335238173422 msec\nrounds: 613"
          },
          {
            "name": "Collections With Model validation",
            "value": 660.0062855228782,
            "unit": "iter/sec",
            "range": "stddev: 0.0022729773580986504",
            "extra": "mean: 1.5151370857139153 msec\nrounds: 490"
          },
          {
            "name": "Collections",
            "value": 538.1842865682253,
            "unit": "iter/sec",
            "range": "stddev: 0.00006520530632086984",
            "extra": "mean: 1.85809958588085 msec\nrounds: 425"
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
          "id": "fc41f8fd14771641ec6adc22399a3691649aa046",
          "message": "Bump version: 3.0.0a1 → 3.0.0a2 (#702)\n\n* Bump version: 3.0.0a1 → 3.0.0a2\r\n\r\n* update changelog",
          "timestamp": "2024-05-31T17:24:13+02:00",
          "tree_id": "7c7123e58787c20c325d69573af67d484ec4cbc1",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/fc41f8fd14771641ec6adc22399a3691649aa046"
        },
        "date": 1717169143947,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 778.2433229337685,
            "unit": "iter/sec",
            "range": "stddev: 0.0001222897238716367",
            "extra": "mean: 1.2849451714282216 msec\nrounds: 280"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 535.2473295576664,
            "unit": "iter/sec",
            "range": "stddev: 0.00022498693323502676",
            "extra": "mean: 1.8682951689388339 msec\nrounds: 367"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 203.0254480047819,
            "unit": "iter/sec",
            "range": "stddev: 0.004429146914531192",
            "extra": "mean: 4.925490916667978 msec\nrounds: 192"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 105.66540041393068,
            "unit": "iter/sec",
            "range": "stddev: 0.007966350370912503",
            "extra": "mean: 9.463835807015617 msec\nrounds: 114"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 57.643092598370856,
            "unit": "iter/sec",
            "range": "stddev: 0.009704811679051004",
            "extra": "mean: 17.348132359370716 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.910153661745035,
            "unit": "iter/sec",
            "range": "stddev: 0.011948723571310504",
            "extra": "mean: 22.266679547164657 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.167141166559524,
            "unit": "iter/sec",
            "range": "stddev: 0.01752819641937838",
            "extra": "mean: 89.5484336666704 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 818.5317881675289,
            "unit": "iter/sec",
            "range": "stddev: 0.00010478781193889406",
            "extra": "mean: 1.2216996510773628 msec\nrounds: 556"
          },
          {
            "name": "Items Limit: (10)",
            "value": 567.5370100833256,
            "unit": "iter/sec",
            "range": "stddev: 0.00009251198697781119",
            "extra": "mean: 1.7619996268669424 msec\nrounds: 402"
          },
          {
            "name": "Items Limit: (50)",
            "value": 224.62457169339348,
            "unit": "iter/sec",
            "range": "stddev: 0.00014759142240970506",
            "extra": "mean: 4.4518727068068635 msec\nrounds: 191"
          },
          {
            "name": "Items Limit: (100)",
            "value": 120.24218836271511,
            "unit": "iter/sec",
            "range": "stddev: 0.004322334289641071",
            "extra": "mean: 8.316548572647916 msec\nrounds: 117"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.28793123676579,
            "unit": "iter/sec",
            "range": "stddev: 0.005515742102938185",
            "extra": "mean: 15.316766530302726 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 56.16420106201313,
            "unit": "iter/sec",
            "range": "stddev: 0.00032637658634249525",
            "extra": "mean: 17.80493590384844 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.325800668051908,
            "unit": "iter/sec",
            "range": "stddev: 0.008497983941974775",
            "extra": "mean: 69.80412635714727 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 1021.5559462669196,
            "unit": "iter/sec",
            "range": "stddev: 0.000053925526352433437",
            "extra": "mean: 978.8989077439255 usec\nrounds: 607"
          },
          {
            "name": "Collection",
            "value": 910.9262364629368,
            "unit": "iter/sec",
            "range": "stddev: 0.00005529515266601191",
            "extra": "mean: 1.0977837282225291 msec\nrounds: 574"
          },
          {
            "name": "Collections With Model validation",
            "value": 657.9304782874074,
            "unit": "iter/sec",
            "range": "stddev: 0.002160913867612993",
            "extra": "mean: 1.5199174274506926 msec\nrounds: 510"
          },
          {
            "name": "Collections",
            "value": 580.8112948462849,
            "unit": "iter/sec",
            "range": "stddev: 0.00007927974292350883",
            "extra": "mean: 1.721729602838829 msec\nrounds: 423"
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
          "id": "07c890e254e8cbcae0b251ba020e8496510d2525",
          "message": "move filter client from types to extensions (#704)\n\n* move filter client from types to extensions\r\n\r\n* update changelog",
          "timestamp": "2024-06-06T13:10:32+02:00",
          "tree_id": "ecaeb737dea6a5e95ac17a701cec63c46307a820",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/07c890e254e8cbcae0b251ba020e8496510d2525"
        },
        "date": 1717672319256,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 805.9257502768304,
            "unit": "iter/sec",
            "range": "stddev: 0.0000815650809751271",
            "extra": "mean: 1.240809093959966 msec\nrounds: 298"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 538.1245839198788,
            "unit": "iter/sec",
            "range": "stddev: 0.00007718362650300996",
            "extra": "mean: 1.8583057341771432 msec\nrounds: 395"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 211.04275503675203,
            "unit": "iter/sec",
            "range": "stddev: 0.0035866820099642034",
            "extra": "mean: 4.738376353293223 msec\nrounds: 167"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 106.68884241785156,
            "unit": "iter/sec",
            "range": "stddev: 0.007176451683014904",
            "extra": "mean: 9.373051364485294 msec\nrounds: 107"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 59.052228769050586,
            "unit": "iter/sec",
            "range": "stddev: 0.01004532104057507",
            "extra": "mean: 16.934161857140648 msec\nrounds: 14"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.41338641061674,
            "unit": "iter/sec",
            "range": "stddev: 0.014562090800653222",
            "extra": "mean: 24.14678167307854 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.703399832274163,
            "unit": "iter/sec",
            "range": "stddev: 0.019359296865119616",
            "extra": "mean: 103.05666233333316 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 900.7020761505574,
            "unit": "iter/sec",
            "range": "stddev: 0.0000828474854401416",
            "extra": "mean: 1.1102450260510381 msec\nrounds: 499"
          },
          {
            "name": "Items Limit: (10)",
            "value": 552.2276096935409,
            "unit": "iter/sec",
            "range": "stddev: 0.00011295761193079213",
            "extra": "mean: 1.8108475245468993 msec\nrounds: 387"
          },
          {
            "name": "Items Limit: (50)",
            "value": 222.1558743076539,
            "unit": "iter/sec",
            "range": "stddev: 0.00015421031326081974",
            "extra": "mean: 4.50134394652623 msec\nrounds: 187"
          },
          {
            "name": "Items Limit: (100)",
            "value": 123.77637890551284,
            "unit": "iter/sec",
            "range": "stddev: 0.00021131757567993226",
            "extra": "mean: 8.079085919643601 msec\nrounds: 112"
          },
          {
            "name": "Items Limit: (200)",
            "value": 57.459965146366486,
            "unit": "iter/sec",
            "range": "stddev: 0.004151343119886039",
            "extra": "mean: 17.403421624999638 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (250)",
            "value": 51.813499243841136,
            "unit": "iter/sec",
            "range": "stddev: 0.006795139679519819",
            "extra": "mean: 19.299989666667148 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.800612165713998,
            "unit": "iter/sec",
            "range": "stddev: 0.0013858404248395589",
            "extra": "mean: 72.4605537777797 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 1032.3621182888833,
            "unit": "iter/sec",
            "range": "stddev: 0.000056347756514201457",
            "extra": "mean: 968.652357815567 usec\nrounds: 531"
          },
          {
            "name": "Collection",
            "value": 1022.0616444083864,
            "unit": "iter/sec",
            "range": "stddev: 0.0000998874527500192",
            "extra": "mean: 978.4145657660828 usec\nrounds: 555"
          },
          {
            "name": "Collections With Model validation",
            "value": 660.1947998095535,
            "unit": "iter/sec",
            "range": "stddev: 0.0029672381062189985",
            "extra": "mean: 1.514704448275676 msec\nrounds: 493"
          },
          {
            "name": "Collections",
            "value": 558.4030967037529,
            "unit": "iter/sec",
            "range": "stddev: 0.00012015345773066376",
            "extra": "mean: 1.790821014251154 msec\nrounds: 421"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "85769594+jamesfisher-gis@users.noreply.github.com",
            "name": "James Fisher",
            "username": "jamesfisher-gis"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8075fc9af0cd5165e4b7661f1c6796cffedc30c7",
          "message": "Aggregation Extension (#684)\n\n* initial commit\r\n\r\n* aggregation extension and tests\r\n\r\n* clean up\r\n\r\n* update changelog\r\n\r\n* Search and Filter extension\r\n\r\n* AggregationCollection\r\n\r\n* AggregationCollection classes\r\n\r\n* test classes\r\n\r\n* AggregationCollection literal\r\n\r\n* aggregation post model\r\n\r\n* docstring fix\r\n\r\n* linting\r\n\r\n* TypedDict import\r\n\r\n* move aggregation client and types into extensions\r\n\r\n* linting",
          "timestamp": "2024-06-11T09:20:22+02:00",
          "tree_id": "0aeb36ff56af1816cbd93faafbbb7be147a9f188",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/8075fc9af0cd5165e4b7661f1c6796cffedc30c7"
        },
        "date": 1718090516738,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 776.7972368623347,
            "unit": "iter/sec",
            "range": "stddev: 0.0000869738881908015",
            "extra": "mean: 1.2873372259139766 msec\nrounds: 301"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 538.8222651186481,
            "unit": "iter/sec",
            "range": "stddev: 0.00006461407951851492",
            "extra": "mean: 1.8558995511809462 msec\nrounds: 381"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 200.1772963410999,
            "unit": "iter/sec",
            "range": "stddev: 0.004361361311026687",
            "extra": "mean: 4.995571517241451 msec\nrounds: 174"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 108.92844118660895,
            "unit": "iter/sec",
            "range": "stddev: 0.0066740087958487996",
            "extra": "mean: 9.180338845452368 msec\nrounds: 110"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 56.15442983820528,
            "unit": "iter/sec",
            "range": "stddev: 0.010633963331937089",
            "extra": "mean: 17.808034074626807 msec\nrounds: 67"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 43.78509598578884,
            "unit": "iter/sec",
            "range": "stddev: 0.013167438514234395",
            "extra": "mean: 22.838821692307494 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.967215917147294,
            "unit": "iter/sec",
            "range": "stddev: 0.019211956801226237",
            "extra": "mean: 91.18084366666797 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 853.4422120445689,
            "unit": "iter/sec",
            "range": "stddev: 0.00009211183512478841",
            "extra": "mean: 1.1717254969195003 msec\nrounds: 487"
          },
          {
            "name": "Items Limit: (10)",
            "value": 569.4489218808852,
            "unit": "iter/sec",
            "range": "stddev: 0.00006266596805790127",
            "extra": "mean: 1.7560837532135596 msec\nrounds: 389"
          },
          {
            "name": "Items Limit: (50)",
            "value": 218.0842573146289,
            "unit": "iter/sec",
            "range": "stddev: 0.00011223655833965867",
            "extra": "mean: 4.585383705882565 msec\nrounds: 187"
          },
          {
            "name": "Items Limit: (100)",
            "value": 124.43388028452726,
            "unit": "iter/sec",
            "range": "stddev: 0.00006790400911329208",
            "extra": "mean: 8.03639650000005 msec\nrounds: 18"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.00811756377712,
            "unit": "iter/sec",
            "range": "stddev: 0.007840530963558502",
            "extra": "mean: 15.62301842424297 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 51.75330202789119,
            "unit": "iter/sec",
            "range": "stddev: 0.00775839097521108",
            "extra": "mean: 19.32243858490564 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.48466645093138,
            "unit": "iter/sec",
            "range": "stddev: 0.010588832838833488",
            "extra": "mean: 74.15830444444775 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 983.5915154462213,
            "unit": "iter/sec",
            "range": "stddev: 0.00006830732737005142",
            "extra": "mean: 1.016682214411269 msec\nrounds: 569"
          },
          {
            "name": "Collection",
            "value": 970.3765490899203,
            "unit": "iter/sec",
            "range": "stddev: 0.00007915907977589956",
            "extra": "mean: 1.0305277893801768 msec\nrounds: 565"
          },
          {
            "name": "Collections With Model validation",
            "value": 669.6078912576796,
            "unit": "iter/sec",
            "range": "stddev: 0.002140186827355448",
            "extra": "mean: 1.4934113128830768 msec\nrounds: 489"
          },
          {
            "name": "Collections",
            "value": 553.4745504078073,
            "unit": "iter/sec",
            "range": "stddev: 0.00009864788321012124",
            "extra": "mean: 1.8067678075951041 msec\nrounds: 395"
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
          "id": "9a8ab844d9d3ceb4a258e112a4328a8ddabe27c1",
          "message": "Allow default route dependencies (#705)\n\n* Allowing for default route dependencies.\r\n\r\n* Running precommit hooks.\r\n\r\n* Adding pull request to CHANGELOG.\r\n\r\n* Update stac_fastapi/api/stac_fastapi/api/routes.py\r\n\r\nCo-authored-by: Anthony Lukach <anthonylukach@gmail.com>\r\n\r\n* Fixing indenting.\r\n\r\n---------\r\n\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>\r\nCo-authored-by: Anthony Lukach <anthonylukach@gmail.com>",
          "timestamp": "2024-06-12T09:43:31+02:00",
          "tree_id": "b3372bf9c69b85631331aa32abac1a4f93bff7d2",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/9a8ab844d9d3ceb4a258e112a4328a8ddabe27c1"
        },
        "date": 1718178306454,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 784.711910920172,
            "unit": "iter/sec",
            "range": "stddev: 0.00009864975177679023",
            "extra": "mean: 1.2743530282691593 msec\nrounds: 283"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 538.2733417408156,
            "unit": "iter/sec",
            "range": "stddev: 0.00008214749531526611",
            "extra": "mean: 1.8577921707323022 msec\nrounds: 369"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 195.9356824512214,
            "unit": "iter/sec",
            "range": "stddev: 0.004939790704409767",
            "extra": "mean: 5.10371560447624 msec\nrounds: 134"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 123.51161174343346,
            "unit": "iter/sec",
            "range": "stddev: 0.00020152549370009156",
            "extra": "mean: 8.096404750002506 msec\nrounds: 16"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 49.1836854213556,
            "unit": "iter/sec",
            "range": "stddev: 0.014198731024015889",
            "extra": "mean: 20.331945266667617 msec\nrounds: 60"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 39.87346998412979,
            "unit": "iter/sec",
            "range": "stddev: 0.015653986680161366",
            "extra": "mean: 25.079332207555908 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.508340721235841,
            "unit": "iter/sec",
            "range": "stddev: 0.026096671980396457",
            "extra": "mean: 105.17082099998889 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 820.2764939473296,
            "unit": "iter/sec",
            "range": "stddev: 0.00007151258303856105",
            "extra": "mean: 1.2191011291665887 msec\nrounds: 480"
          },
          {
            "name": "Items Limit: (10)",
            "value": 561.3010533008462,
            "unit": "iter/sec",
            "range": "stddev: 0.00011060496237968522",
            "extra": "mean: 1.781575135338326 msec\nrounds: 399"
          },
          {
            "name": "Items Limit: (50)",
            "value": 223.06732611755717,
            "unit": "iter/sec",
            "range": "stddev: 0.00011404194470806803",
            "extra": "mean: 4.482951481083325 msec\nrounds: 185"
          },
          {
            "name": "Items Limit: (100)",
            "value": 127.29074930815572,
            "unit": "iter/sec",
            "range": "stddev: 0.0001333409086129693",
            "extra": "mean: 7.856030429824239 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.90378335219933,
            "unit": "iter/sec",
            "range": "stddev: 0.0050520599563636",
            "extra": "mean: 15.40742231579192 msec\nrounds: 57"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.42579070345733,
            "unit": "iter/sec",
            "range": "stddev: 0.00737230203067408",
            "extra": "mean: 19.07458116667095 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.906065583841064,
            "unit": "iter/sec",
            "range": "stddev: 0.0011025729561861893",
            "extra": "mean: 71.91106600000552 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 1045.107401898703,
            "unit": "iter/sec",
            "range": "stddev: 0.000060719204889683046",
            "extra": "mean: 956.8394580147897 usec\nrounds: 524"
          },
          {
            "name": "Collection",
            "value": 967.3317985663747,
            "unit": "iter/sec",
            "range": "stddev: 0.00008822813860467206",
            "extra": "mean: 1.0337714540988325 msec\nrounds: 610"
          },
          {
            "name": "Collections With Model validation",
            "value": 680.9054254506236,
            "unit": "iter/sec",
            "range": "stddev: 0.002305490733279333",
            "extra": "mean: 1.4686327390300928 msec\nrounds: 433"
          },
          {
            "name": "Collections",
            "value": 564.9112131353845,
            "unit": "iter/sec",
            "range": "stddev: 0.00008858767914418646",
            "extra": "mean: 1.770189680692962 msec\nrounds: 404"
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
          "id": "d8528ae2e0d93572219869458b0157fbeeaf2ba3",
          "message": "deprecate Fields default-includes (#706)",
          "timestamp": "2024-06-13T19:01:00+08:00",
          "tree_id": "8cdfea2ec70a451084086a9ae8a87e83240630fb",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/d8528ae2e0d93572219869458b0157fbeeaf2ba3"
        },
        "date": 1718276556817,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 786.4248481478272,
            "unit": "iter/sec",
            "range": "stddev: 0.00011255832896531701",
            "extra": "mean: 1.2715773189964443 msec\nrounds: 279"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 528.0378372520472,
            "unit": "iter/sec",
            "range": "stddev: 0.0002007061740685852",
            "extra": "mean: 1.8938036811984595 msec\nrounds: 367"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 206.98691476449605,
            "unit": "iter/sec",
            "range": "stddev: 0.004839935655802468",
            "extra": "mean: 4.83122327388556 msec\nrounds: 157"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 107.38256657924742,
            "unit": "iter/sec",
            "range": "stddev: 0.007582879907948178",
            "extra": "mean: 9.3124985913054 msec\nrounds: 115"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.12233545838676,
            "unit": "iter/sec",
            "range": "stddev: 0.011433301856597267",
            "extra": "mean: 18.141466461538542 msec\nrounds: 65"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.115343036568994,
            "unit": "iter/sec",
            "range": "stddev: 0.014816825498594964",
            "extra": "mean: 23.74431567924531 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.981764660176884,
            "unit": "iter/sec",
            "range": "stddev: 0.02144307726159008",
            "extra": "mean: 100.1826865333328 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1)",
            "value": 834.564325941807,
            "unit": "iter/sec",
            "range": "stddev: 0.00009415612477424517",
            "extra": "mean: 1.198229985293822 msec\nrounds: 476"
          },
          {
            "name": "Items Limit: (10)",
            "value": 514.6691862804806,
            "unit": "iter/sec",
            "range": "stddev: 0.00257720457541149",
            "extra": "mean: 1.9429956691734553 msec\nrounds: 399"
          },
          {
            "name": "Items Limit: (50)",
            "value": 220.6852114216148,
            "unit": "iter/sec",
            "range": "stddev: 0.00009469650464895587",
            "extra": "mean: 4.531341241935417 msec\nrounds: 186"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.31802694735154,
            "unit": "iter/sec",
            "range": "stddev: 0.0001625247256346313",
            "extra": "mean: 7.916526438596076 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.15172759347116,
            "unit": "iter/sec",
            "range": "stddev: 0.0003450126324288714",
            "extra": "mean: 15.1167631803269 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.430737348318935,
            "unit": "iter/sec",
            "range": "stddev: 0.004723287232058809",
            "extra": "mean: 18.715818826922153 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.149551427204203,
            "unit": "iter/sec",
            "range": "stddev: 0.014879724317574446",
            "extra": "mean: 76.04822153333448 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1018.6730804773946,
            "unit": "iter/sec",
            "range": "stddev: 0.00007417762180530667",
            "extra": "mean: 981.6692118057703 usec\nrounds: 576"
          },
          {
            "name": "Collection",
            "value": 965.1081127617865,
            "unit": "iter/sec",
            "range": "stddev: 0.0000890992378437485",
            "extra": "mean: 1.03615334569965 msec\nrounds: 593"
          },
          {
            "name": "Collections With Model validation",
            "value": 720.432524837048,
            "unit": "iter/sec",
            "range": "stddev: 0.00007742411112296762",
            "extra": "mean: 1.3880550440531352 msec\nrounds: 454"
          },
          {
            "name": "Collections",
            "value": 548.7992358512956,
            "unit": "iter/sec",
            "range": "stddev: 0.0001452519753824247",
            "extra": "mean: 1.8221599715764967 msec\nrounds: 387"
          }
        ]
      }
    ]
  }
}