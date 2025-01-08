window.BENCHMARK_DATA = {
  "lastUpdate": 1736342801128,
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
          "id": "51a756d904e4bab245da4a525e961d64bcbf1321",
          "message": "v3.0.0a3 (#707)",
          "timestamp": "2024-06-13T20:05:48+08:00",
          "tree_id": "989366ba3e7d23d38a04ec716857ba0535a5f7ed",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/51a756d904e4bab245da4a525e961d64bcbf1321"
        },
        "date": 1718280442250,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 797.4635834365165,
            "unit": "iter/sec",
            "range": "stddev: 0.000099993920449879",
            "extra": "mean: 1.2539757560974656 msec\nrounds: 287"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 535.3000410629239,
            "unit": "iter/sec",
            "range": "stddev: 0.00009143090349092052",
            "extra": "mean: 1.8681111961328076 msec\nrounds: 362"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 202.5207530971743,
            "unit": "iter/sec",
            "range": "stddev: 0.004519978233006873",
            "extra": "mean: 4.937765560846874 msec\nrounds: 189"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 104.10799519047562,
            "unit": "iter/sec",
            "range": "stddev: 0.007801844896994359",
            "extra": "mean: 9.60541021052613 msec\nrounds: 114"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 54.937370591476835,
            "unit": "iter/sec",
            "range": "stddev: 0.011533462046154254",
            "extra": "mean: 18.20254572131167 msec\nrounds: 61"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.77863123523791,
            "unit": "iter/sec",
            "range": "stddev: 0.013810511488982833",
            "extra": "mean: 23.37615699999941 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.774483175067884,
            "unit": "iter/sec",
            "range": "stddev: 0.020767044521309574",
            "extra": "mean: 92.81187633333508 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 836.9458735818505,
            "unit": "iter/sec",
            "range": "stddev: 0.00009464412876908152",
            "extra": "mean: 1.1948203958761778 msec\nrounds: 485"
          },
          {
            "name": "Items Limit: (10)",
            "value": 556.0213333123666,
            "unit": "iter/sec",
            "range": "stddev: 0.00009495703499175214",
            "extra": "mean: 1.798492144254133 msec\nrounds: 409"
          },
          {
            "name": "Items Limit: (50)",
            "value": 216.26761250012854,
            "unit": "iter/sec",
            "range": "stddev: 0.0000878657790598511",
            "extra": "mean: 4.623900862637976 msec\nrounds: 182"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.67551115085314,
            "unit": "iter/sec",
            "range": "stddev: 0.00007092366251381194",
            "extra": "mean: 7.894185631579077 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.03996753451746,
            "unit": "iter/sec",
            "range": "stddev: 0.004222057192898451",
            "extra": "mean: 15.375161426230548 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 51.29666503452733,
            "unit": "iter/sec",
            "range": "stddev: 0.008219984953761162",
            "extra": "mean: 19.49444470370362 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.01838752952312,
            "unit": "iter/sec",
            "range": "stddev: 0.0007163193957128863",
            "extra": "mean: 71.33488055555404 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 999.9938411927808,
            "unit": "iter/sec",
            "range": "stddev: 0.00008562322578907998",
            "extra": "mean: 1.0000061588451505 msec\nrounds: 554"
          },
          {
            "name": "Collection",
            "value": 982.0695511272747,
            "unit": "iter/sec",
            "range": "stddev: 0.00007663403216301525",
            "extra": "mean: 1.01825781977676 msec\nrounds: 627"
          },
          {
            "name": "Collections With Model validation",
            "value": 747.4543879522678,
            "unit": "iter/sec",
            "range": "stddev: 0.00006419139587635836",
            "extra": "mean: 1.3378742785089646 msec\nrounds: 456"
          },
          {
            "name": "Collections",
            "value": 568.1138096935175,
            "unit": "iter/sec",
            "range": "stddev: 0.00009066806109824665",
            "extra": "mean: 1.7602106883116846 msec\nrounds: 385"
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
          "id": "68dfbd58cabe6eedd6e607b1282376628231036e",
          "message": "fix import errors (#710)",
          "timestamp": "2024-06-14T07:14:56+02:00",
          "tree_id": "4c6c8756eb0ff002e5f08c0d5871446a323ce81f",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/68dfbd58cabe6eedd6e607b1282376628231036e"
        },
        "date": 1718342183786,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 845.69271840445,
            "unit": "iter/sec",
            "range": "stddev: 0.00008002964613877812",
            "extra": "mean: 1.182462587459282 msec\nrounds: 303"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 549.4114468088188,
            "unit": "iter/sec",
            "range": "stddev: 0.000091733192487181",
            "extra": "mean: 1.8201295328089053 msec\nrounds: 381"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 223.91794312998206,
            "unit": "iter/sec",
            "range": "stddev: 0.0034437913241800863",
            "extra": "mean: 4.465921694446391 msec\nrounds: 180"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 113.831693807642,
            "unit": "iter/sec",
            "range": "stddev: 0.00612801265923244",
            "extra": "mean: 8.784899587718035 msec\nrounds: 114"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 60.590116913520795,
            "unit": "iter/sec",
            "range": "stddev: 0.008805780532741773",
            "extra": "mean: 16.504341812498602 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 48.79535420631405,
            "unit": "iter/sec",
            "range": "stddev: 0.010660234465402072",
            "extra": "mean: 20.493754298244266 msec\nrounds: 57"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.53046464383839,
            "unit": "iter/sec",
            "range": "stddev: 0.017926418895104042",
            "extra": "mean: 86.7267738888889 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 854.7587553340247,
            "unit": "iter/sec",
            "range": "stddev: 0.0001288168891554444",
            "extra": "mean: 1.1699207451922706 msec\nrounds: 416"
          },
          {
            "name": "Items Limit: (10)",
            "value": 559.307247567266,
            "unit": "iter/sec",
            "range": "stddev: 0.00008868056964098802",
            "extra": "mean: 1.7879260537916297 msec\nrounds: 409"
          },
          {
            "name": "Items Limit: (50)",
            "value": 214.10521488296382,
            "unit": "iter/sec",
            "range": "stddev: 0.003044311845339936",
            "extra": "mean: 4.670600856437006 msec\nrounds: 202"
          },
          {
            "name": "Items Limit: (100)",
            "value": 131.3444075517689,
            "unit": "iter/sec",
            "range": "stddev: 0.00019771684847428477",
            "extra": "mean: 7.613571210527968 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 68.05927478581232,
            "unit": "iter/sec",
            "range": "stddev: 0.003649936752066587",
            "extra": "mean: 14.693074575758786 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.78793476289814,
            "unit": "iter/sec",
            "range": "stddev: 0.00556706793830642",
            "extra": "mean: 18.59152994826974 msec\nrounds: 58"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.660217614785054,
            "unit": "iter/sec",
            "range": "stddev: 0.007557420860024602",
            "extra": "mean: 68.21181146666504 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1019.3457984186698,
            "unit": "iter/sec",
            "range": "stddev: 0.00008144480613500455",
            "extra": "mean: 981.0213585530236 usec\nrounds: 608"
          },
          {
            "name": "Collection",
            "value": 932.8321937460187,
            "unit": "iter/sec",
            "range": "stddev: 0.0019513905089685022",
            "extra": "mean: 1.072004168278383 msec\nrounds: 517"
          },
          {
            "name": "Collections With Model validation",
            "value": 720.3693362401938,
            "unit": "iter/sec",
            "range": "stddev: 0.0000781286863761061",
            "extra": "mean: 1.38817679999995 msec\nrounds: 425"
          },
          {
            "name": "Collections",
            "value": 599.7506133013414,
            "unit": "iter/sec",
            "range": "stddev: 0.00007669401559364283",
            "extra": "mean: 1.667359695549916 msec\nrounds: 427"
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
          "id": "80064f77739ddc1acaafa78cb0d8a11f77ecd33e",
          "message": "add tests for FieldsExtension impact on validation (#708)\n\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-06-14T13:28:37+02:00",
          "tree_id": "f0cb0f223472e1028efca0af634d570acc452b1b",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/80064f77739ddc1acaafa78cb0d8a11f77ecd33e"
        },
        "date": 1718364614180,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 773.0742154502826,
            "unit": "iter/sec",
            "range": "stddev: 0.00009669690505346728",
            "extra": "mean: 1.2935368687953754 msec\nrounds: 282"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 535.4926413941788,
            "unit": "iter/sec",
            "range": "stddev: 0.00009848108959533863",
            "extra": "mean: 1.8674392936501532 msec\nrounds: 378"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 210.07843792554877,
            "unit": "iter/sec",
            "range": "stddev: 0.003883978418702347",
            "extra": "mean: 4.760126788235151 msec\nrounds: 170"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 105.31869239084303,
            "unit": "iter/sec",
            "range": "stddev: 0.007455566472287111",
            "extra": "mean: 9.494990654545436 msec\nrounds: 110"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 51.30306432396609,
            "unit": "iter/sec",
            "range": "stddev: 0.013837214471766493",
            "extra": "mean: 19.492013063493612 msec\nrounds: 63"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.44076998237774,
            "unit": "iter/sec",
            "range": "stddev: 0.015118213713113962",
            "extra": "mean: 24.13082576470562 msec\nrounds: 51"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.501060083747607,
            "unit": "iter/sec",
            "range": "stddev: 0.027507465761529848",
            "extra": "mean: 105.25141312500352 msec\nrounds: 8"
          },
          {
            "name": "Items Limit: (1)",
            "value": 835.2665189618576,
            "unit": "iter/sec",
            "range": "stddev: 0.00008471865575147315",
            "extra": "mean: 1.1972226556415642 msec\nrounds: 514"
          },
          {
            "name": "Items Limit: (10)",
            "value": 564.4942309834682,
            "unit": "iter/sec",
            "range": "stddev: 0.00009751947217548477",
            "extra": "mean: 1.7714972892774983 msec\nrounds: 401"
          },
          {
            "name": "Items Limit: (50)",
            "value": 219.49169547110438,
            "unit": "iter/sec",
            "range": "stddev: 0.0001239551542930883",
            "extra": "mean: 4.555981026314719 msec\nrounds: 190"
          },
          {
            "name": "Items Limit: (100)",
            "value": 117.01232120931101,
            "unit": "iter/sec",
            "range": "stddev: 0.005230534185527099",
            "extra": "mean: 8.54610856074896 msec\nrounds: 107"
          },
          {
            "name": "Items Limit: (200)",
            "value": 62.19580876348959,
            "unit": "iter/sec",
            "range": "stddev: 0.007709307491845133",
            "extra": "mean: 16.0782538225795 msec\nrounds: 62"
          },
          {
            "name": "Items Limit: (250)",
            "value": 51.80524832658335,
            "unit": "iter/sec",
            "range": "stddev: 0.007556791336499892",
            "extra": "mean: 19.30306353703665 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.011213422800889,
            "unit": "iter/sec",
            "range": "stddev: 0.0005816809186492517",
            "extra": "mean: 71.37140587500213 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 1007.8799542353038,
            "unit": "iter/sec",
            "range": "stddev: 0.00007343744649666962",
            "extra": "mean: 992.1816539735801 usec\nrounds: 604"
          },
          {
            "name": "Collection",
            "value": 963.7727432248837,
            "unit": "iter/sec",
            "range": "stddev: 0.00009495152556336905",
            "extra": "mean: 1.037589003247691 msec\nrounds: 616"
          },
          {
            "name": "Collections With Model validation",
            "value": 743.6701746184765,
            "unit": "iter/sec",
            "range": "stddev: 0.00006712679274540394",
            "extra": "mean: 1.344682137498694 msec\nrounds: 400"
          },
          {
            "name": "Collections",
            "value": 571.8830824458414,
            "unit": "iter/sec",
            "range": "stddev: 0.00013527178628410354",
            "extra": "mean: 1.7486091662708034 msec\nrounds: 421"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "64801328+captaincoordinates@users.noreply.github.com",
            "name": "Tom Christian",
            "username": "captaincoordinates"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8f400e18f361132b92f32d8e3fd62787b3276adc",
          "message": "fix(#711): changed default filter language (#712)",
          "timestamp": "2024-06-21T09:58:48+02:00",
          "tree_id": "d49629fc3005dc6b6392232e591727e787bcfe1a",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/8f400e18f361132b92f32d8e3fd62787b3276adc"
        },
        "date": 1718956820809,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 795.8124471900925,
            "unit": "iter/sec",
            "range": "stddev: 0.00009536980937499761",
            "extra": "mean: 1.256577480700216 msec\nrounds: 285"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 549.3417468838556,
            "unit": "iter/sec",
            "range": "stddev: 0.000055134567328219286",
            "extra": "mean: 1.8203604690022304 msec\nrounds: 371"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 200.30573862250043,
            "unit": "iter/sec",
            "range": "stddev: 0.005070361141634358",
            "extra": "mean: 4.992368201115879 msec\nrounds: 179"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 106.26017361465757,
            "unit": "iter/sec",
            "range": "stddev: 0.007597923525152631",
            "extra": "mean: 9.410863600001305 msec\nrounds: 110"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.8694153381758,
            "unit": "iter/sec",
            "range": "stddev: 0.011240368144580315",
            "extra": "mean: 17.898880701489926 msec\nrounds: 67"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.65343736139558,
            "unit": "iter/sec",
            "range": "stddev: 0.015288863215322624",
            "extra": "mean: 24.007622500005255 msec\nrounds: 50"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.339615164306212,
            "unit": "iter/sec",
            "range": "stddev: 0.01866654147017851",
            "extra": "mean: 88.18641422221339 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 846.2668784773164,
            "unit": "iter/sec",
            "range": "stddev: 0.0000960811943843545",
            "extra": "mean: 1.1816603313121445 msec\nrounds: 495"
          },
          {
            "name": "Items Limit: (10)",
            "value": 564.7648160146374,
            "unit": "iter/sec",
            "range": "stddev: 0.00008128848693918881",
            "extra": "mean: 1.7706485454541532 msec\nrounds: 396"
          },
          {
            "name": "Items Limit: (50)",
            "value": 221.6248892443354,
            "unit": "iter/sec",
            "range": "stddev: 0.00008857102193726342",
            "extra": "mean: 4.512128594444675 msec\nrounds: 180"
          },
          {
            "name": "Items Limit: (100)",
            "value": 123.08248792673291,
            "unit": "iter/sec",
            "range": "stddev: 0.0033671950868870053",
            "extra": "mean: 8.124632649571303 msec\nrounds: 117"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.27324680046823,
            "unit": "iter/sec",
            "range": "stddev: 0.006972962542289225",
            "extra": "mean: 15.320212323080376 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.60857266339988,
            "unit": "iter/sec",
            "range": "stddev: 0.006329975588385099",
            "extra": "mean: 18.653732981828274 msec\nrounds: 55"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.317664918591523,
            "unit": "iter/sec",
            "range": "stddev: 0.008352732294602377",
            "extra": "mean: 69.84379126665392 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1059.2801612485885,
            "unit": "iter/sec",
            "range": "stddev: 0.00005124601101340926",
            "extra": "mean: 944.0373157005847 usec\nrounds: 586"
          },
          {
            "name": "Collection",
            "value": 1022.4294329649633,
            "unit": "iter/sec",
            "range": "stddev: 0.00007010061480853452",
            "extra": "mean: 978.0626102479074 usec\nrounds: 644"
          },
          {
            "name": "Collections With Model validation",
            "value": 702.0798218152574,
            "unit": "iter/sec",
            "range": "stddev: 0.000059619514145972134",
            "extra": "mean: 1.4243394681454555 msec\nrounds: 361"
          },
          {
            "name": "Collections",
            "value": 579.1913980369125,
            "unit": "iter/sec",
            "range": "stddev: 0.00007019907585309253",
            "extra": "mean: 1.7265449787226794 msec\nrounds: 329"
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
          "id": "f311dc620d2a11df397f8d95c17e15483b9e302c",
          "message": "Remove the Filter Extension dependency from Aggregation Extension requests (#716)\n\n* aggregations type\r\n\r\n* aggregations type\r\n\r\n* remove filter extension dependency\r\n\r\n* linting\r\n\r\n* update changelog",
          "timestamp": "2024-06-25T15:43:29+02:00",
          "tree_id": "0c2f4a71930b4b80460a22cea3c9734c03591734",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/f311dc620d2a11df397f8d95c17e15483b9e302c"
        },
        "date": 1719323107635,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 838.9276643239372,
            "unit": "iter/sec",
            "range": "stddev: 0.00008410329288136536",
            "extra": "mean: 1.1919978831617926 msec\nrounds: 291"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 542.0146194474663,
            "unit": "iter/sec",
            "range": "stddev: 0.00010626421441714947",
            "extra": "mean: 1.8449686855668348 msec\nrounds: 388"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 202.78520984587914,
            "unit": "iter/sec",
            "range": "stddev: 0.004798320779618365",
            "extra": "mean: 4.931326109828326 msec\nrounds: 173"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 109.87891033830299,
            "unit": "iter/sec",
            "range": "stddev: 0.006607505260079801",
            "extra": "mean: 9.100927529415143 msec\nrounds: 119"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 53.07121547923551,
            "unit": "iter/sec",
            "range": "stddev: 0.011766303056929025",
            "extra": "mean: 18.842605939395852 msec\nrounds: 66"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 43.168129729584926,
            "unit": "iter/sec",
            "range": "stddev: 0.013708161158569628",
            "extra": "mean: 23.165238018515733 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.670630507122475,
            "unit": "iter/sec",
            "range": "stddev: 0.019564545737168947",
            "extra": "mean: 93.71517449999942 msec\nrounds: 10"
          },
          {
            "name": "Items Limit: (1)",
            "value": 938.9835326915445,
            "unit": "iter/sec",
            "range": "stddev: 0.00006536600007267036",
            "extra": "mean: 1.0649814029576803 msec\nrounds: 541"
          },
          {
            "name": "Items Limit: (10)",
            "value": 540.895905876319,
            "unit": "iter/sec",
            "range": "stddev: 0.002453247560688764",
            "extra": "mean: 1.8487845611992104 msec\nrounds: 433"
          },
          {
            "name": "Items Limit: (50)",
            "value": 220.7606184030377,
            "unit": "iter/sec",
            "range": "stddev: 0.00011634818911580904",
            "extra": "mean: 4.5297934352327385 msec\nrounds: 193"
          },
          {
            "name": "Items Limit: (100)",
            "value": 125.81227116138139,
            "unit": "iter/sec",
            "range": "stddev: 0.00008569369672663",
            "extra": "mean: 7.948350274332813 msec\nrounds: 113"
          },
          {
            "name": "Items Limit: (200)",
            "value": 67.10455977822946,
            "unit": "iter/sec",
            "range": "stddev: 0.00020151664423792486",
            "extra": "mean: 14.902116984372604 msec\nrounds: 64"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.05906519984235,
            "unit": "iter/sec",
            "range": "stddev: 0.000140237361502367",
            "extra": "mean: 18.162313442307827 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.058575226969243,
            "unit": "iter/sec",
            "range": "stddev: 0.013093966638670573",
            "extra": "mean: 76.57803264285283 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 970.357633110422,
            "unit": "iter/sec",
            "range": "stddev: 0.00008518363884665604",
            "extra": "mean: 1.0305478783060233 msec\nrounds: 567"
          },
          {
            "name": "Collection",
            "value": 998.450320817448,
            "unit": "iter/sec",
            "range": "stddev: 0.00008640279483639855",
            "extra": "mean: 1.0015520844154602 msec\nrounds: 616"
          },
          {
            "name": "Collections With Model validation",
            "value": 734.5110461195575,
            "unit": "iter/sec",
            "range": "stddev: 0.00007959410541469829",
            "extra": "mean: 1.361449913221902 msec\nrounds: 484"
          },
          {
            "name": "Collections",
            "value": 580.6737485384692,
            "unit": "iter/sec",
            "range": "stddev: 0.00009659233621241548",
            "extra": "mean: 1.722137435206873 msec\nrounds: 409"
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
          "id": "4f410eb8756e253cf224eb4ad8feb533ad2273c1",
          "message": "remove middleware stack building to avoid conflict with exception handler (#721)\n\n* remove middleware stack building to avoid conflict with exception handler\r\n\r\n* update changelog",
          "timestamp": "2024-06-27T17:59:40+02:00",
          "tree_id": "8f7b36e997150dc9ea6d74ffb073172a5a4c471b",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/4f410eb8756e253cf224eb4ad8feb533ad2273c1"
        },
        "date": 1719504083646,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 795.1562395945562,
            "unit": "iter/sec",
            "range": "stddev: 0.00009353319257685386",
            "extra": "mean: 1.2576144790235086 msec\nrounds: 286"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 533.6193284183207,
            "unit": "iter/sec",
            "range": "stddev: 0.00008918023572822772",
            "extra": "mean: 1.8739950874044593 msec\nrounds: 389"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 195.51712946031975,
            "unit": "iter/sec",
            "range": "stddev: 0.005134632384543159",
            "extra": "mean: 5.114641375721252 msec\nrounds: 173"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 102.73203729024178,
            "unit": "iter/sec",
            "range": "stddev: 0.008081102175646714",
            "extra": "mean: 9.73406180172178 msec\nrounds: 116"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 51.04857446641195,
            "unit": "iter/sec",
            "range": "stddev: 0.013485417698581484",
            "extra": "mean: 19.58918560317414 msec\nrounds: 63"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.724429123842924,
            "unit": "iter/sec",
            "range": "stddev: 0.014324700352842728",
            "extra": "mean: 23.966774884609794 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.63115457115586,
            "unit": "iter/sec",
            "range": "stddev: 0.025585148581586517",
            "extra": "mean: 103.8297114444491 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 880.0571046840923,
            "unit": "iter/sec",
            "range": "stddev: 0.00010447060371921349",
            "extra": "mean: 1.1362899005956695 msec\nrounds: 503"
          },
          {
            "name": "Items Limit: (10)",
            "value": 560.0598544700637,
            "unit": "iter/sec",
            "range": "stddev: 0.00007118585308052063",
            "extra": "mean: 1.78552344364374 msec\nrounds: 417"
          },
          {
            "name": "Items Limit: (50)",
            "value": 217.8180938162033,
            "unit": "iter/sec",
            "range": "stddev: 0.00009237892894726716",
            "extra": "mean: 4.590986829789302 msec\nrounds: 188"
          },
          {
            "name": "Items Limit: (100)",
            "value": 117.41535442612981,
            "unit": "iter/sec",
            "range": "stddev: 0.0040649640936246435",
            "extra": "mean: 8.516773678259735 msec\nrounds: 115"
          },
          {
            "name": "Items Limit: (200)",
            "value": 60.776695541556954,
            "unit": "iter/sec",
            "range": "stddev: 0.007679456968507303",
            "extra": "mean: 16.453675065572384 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 50.75696031611047,
            "unit": "iter/sec",
            "range": "stddev: 0.008141529474064574",
            "extra": "mean: 19.701731423081217 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.828270886907692,
            "unit": "iter/sec",
            "range": "stddev: 0.0006776879896365464",
            "extra": "mean: 72.31562124999869 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 982.381332157454,
            "unit": "iter/sec",
            "range": "stddev: 0.000104884909459821",
            "extra": "mean: 1.0179346525283137 msec\nrounds: 613"
          },
          {
            "name": "Collection",
            "value": 887.5307143355172,
            "unit": "iter/sec",
            "range": "stddev: 0.0027005041128544457",
            "extra": "mean: 1.1267215701359552 msec\nrounds: 442"
          },
          {
            "name": "Collections With Model validation",
            "value": 713.8126273870937,
            "unit": "iter/sec",
            "range": "stddev: 0.00009536447454067907",
            "extra": "mean: 1.4009278648662928 msec\nrounds: 481"
          },
          {
            "name": "Collections",
            "value": 568.5943059303174,
            "unit": "iter/sec",
            "range": "stddev: 0.00009158450853312026",
            "extra": "mean: 1.7587232048759778 msec\nrounds: 410"
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
          "id": "63097135d72d1afe8731b6138af1974aace477af",
          "message": "raise RuntimeError if middleware stack has already been created when initialiazing StacApi (#722)",
          "timestamp": "2024-06-27T22:19:43+02:00",
          "tree_id": "e8e80d95af192f6f669c6219cf560d62330bbf54",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/63097135d72d1afe8731b6138af1974aace477af"
        },
        "date": 1719519679964,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 763.1992805037844,
            "unit": "iter/sec",
            "range": "stddev: 0.00009586471171471295",
            "extra": "mean: 1.3102737719300581 msec\nrounds: 342"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 541.705824454638,
            "unit": "iter/sec",
            "range": "stddev: 0.00007562761827345262",
            "extra": "mean: 1.8460203949380631 msec\nrounds: 395"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 208.49820763469253,
            "unit": "iter/sec",
            "range": "stddev: 0.0032375715096467405",
            "extra": "mean: 4.796204300000934 msec\nrounds: 180"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 109.13469483090962,
            "unit": "iter/sec",
            "range": "stddev: 0.006092214136504229",
            "extra": "mean: 9.162988924368856 msec\nrounds: 119"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.16504582666668,
            "unit": "iter/sec",
            "range": "stddev: 0.010374847889844059",
            "extra": "mean: 18.127420815385275 msec\nrounds: 65"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.993542473602666,
            "unit": "iter/sec",
            "range": "stddev: 0.011110900695874244",
            "extra": "mean: 22.225411581821803 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.291424652020524,
            "unit": "iter/sec",
            "range": "stddev: 0.016906369159209036",
            "extra": "mean: 88.56278377778102 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 824.6430314491639,
            "unit": "iter/sec",
            "range": "stddev: 0.0020677341631804933",
            "extra": "mean: 1.2126459108526964 msec\nrounds: 516"
          },
          {
            "name": "Items Limit: (10)",
            "value": 545.8231540880029,
            "unit": "iter/sec",
            "range": "stddev: 0.00009691810330760281",
            "extra": "mean: 1.8320952354446478 msec\nrounds: 395"
          },
          {
            "name": "Items Limit: (50)",
            "value": 219.6679276069937,
            "unit": "iter/sec",
            "range": "stddev: 0.00010870972183338253",
            "extra": "mean: 4.5523259170956125 msec\nrounds: 193"
          },
          {
            "name": "Items Limit: (100)",
            "value": 119.9573902510958,
            "unit": "iter/sec",
            "range": "stddev: 0.0041539297408889255",
            "extra": "mean: 8.33629339473618 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.36971136932537,
            "unit": "iter/sec",
            "range": "stddev: 0.005670409782853458",
            "extra": "mean: 15.297604640629459 msec\nrounds: 64"
          },
          {
            "name": "Items Limit: (250)",
            "value": 56.09311346310055,
            "unit": "iter/sec",
            "range": "stddev: 0.00008578580187693583",
            "extra": "mean: 17.827500351853796 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.802728339299607,
            "unit": "iter/sec",
            "range": "stddev: 0.010259056725858574",
            "extra": "mean: 72.44944444445561 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 1013.3876511107957,
            "unit": "iter/sec",
            "range": "stddev: 0.00008055001715183288",
            "extra": "mean: 986.7892103321751 usec\nrounds: 542"
          },
          {
            "name": "Collection",
            "value": 993.0725928253294,
            "unit": "iter/sec",
            "range": "stddev: 0.00007259322242474158",
            "extra": "mean: 1.0069757309029763 msec\nrounds: 576"
          },
          {
            "name": "Collections With Model validation",
            "value": 684.2713499714924,
            "unit": "iter/sec",
            "range": "stddev: 0.002019337794616648",
            "extra": "mean: 1.461408548000236 msec\nrounds: 500"
          },
          {
            "name": "Collections",
            "value": 550.7440917010292,
            "unit": "iter/sec",
            "range": "stddev: 0.00009229877711359662",
            "extra": "mean: 1.815725334268041 msec\nrounds: 356"
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
          "id": "1916d44397733ff09c247c1578e113ef3f7a2501",
          "message": "Release/v3.0.0a4 (#723)\n\n* update changelog\r\n\r\n* Bump version: 3.0.0a3 → 3.0.0a4\r\n\r\n---------\r\n\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-06-28T17:55:13+02:00",
          "tree_id": "4a3e1daf58fe71eb95500fd81fbb87aafe4b3e0a",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/1916d44397733ff09c247c1578e113ef3f7a2501"
        },
        "date": 1719590206692,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 755.2026397097626,
            "unit": "iter/sec",
            "range": "stddev: 0.00010452316865009145",
            "extra": "mean: 1.3241479139748733 msec\nrounds: 279"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 523.8556703359008,
            "unit": "iter/sec",
            "range": "stddev: 0.00007979392242452709",
            "extra": "mean: 1.9089227369798085 msec\nrounds: 384"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 194.23559488714173,
            "unit": "iter/sec",
            "range": "stddev: 0.005672663060118932",
            "extra": "mean: 5.14838693999953 msec\nrounds: 150"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 104.3389104268646,
            "unit": "iter/sec",
            "range": "stddev: 0.00808522746577617",
            "extra": "mean: 9.58415221999985 msec\nrounds: 100"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 51.54470067347532,
            "unit": "iter/sec",
            "range": "stddev: 0.013772986838518797",
            "extra": "mean: 19.400636475411638 msec\nrounds: 61"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.48604472513924,
            "unit": "iter/sec",
            "range": "stddev: 0.014973731733326313",
            "extra": "mean: 24.104491200001803 msec\nrounds: 50"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.473123620986016,
            "unit": "iter/sec",
            "range": "stddev: 0.02298072981917194",
            "extra": "mean: 105.56180199999484 msec\nrounds: 14"
          },
          {
            "name": "Items Limit: (1)",
            "value": 831.3393185977799,
            "unit": "iter/sec",
            "range": "stddev: 0.00007906779555500408",
            "extra": "mean: 1.2028782683906976 msec\nrounds: 503"
          },
          {
            "name": "Items Limit: (10)",
            "value": 547.4161611038897,
            "unit": "iter/sec",
            "range": "stddev: 0.00011614744203622332",
            "extra": "mean: 1.8267637513358288 msec\nrounds: 374"
          },
          {
            "name": "Items Limit: (50)",
            "value": 203.35181188672462,
            "unit": "iter/sec",
            "range": "stddev: 0.004171014742469689",
            "extra": "mean: 4.917585885868779 msec\nrounds: 184"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.58339347573096,
            "unit": "iter/sec",
            "range": "stddev: 0.00009462268844968888",
            "extra": "mean: 7.899930413792577 msec\nrounds: 116"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.28025262777048,
            "unit": "iter/sec",
            "range": "stddev: 0.004574721067071025",
            "extra": "mean: 15.318568169489527 msec\nrounds: 59"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.70967088557845,
            "unit": "iter/sec",
            "range": "stddev: 0.0065949752370591695",
            "extra": "mean: 18.971850576923323 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.40079762994565,
            "unit": "iter/sec",
            "range": "stddev: 0.01475864437248049",
            "extra": "mean: 74.62242380001196 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 942.0233129614543,
            "unit": "iter/sec",
            "range": "stddev: 0.00007009380026866004",
            "extra": "mean: 1.0615448537640575 msec\nrounds: 465"
          },
          {
            "name": "Collection",
            "value": 1003.9934797400444,
            "unit": "iter/sec",
            "range": "stddev: 0.00004997486997927626",
            "extra": "mean: 996.0224047061755 usec\nrounds: 425"
          },
          {
            "name": "Collections With Model validation",
            "value": 724.4019321224015,
            "unit": "iter/sec",
            "range": "stddev: 0.00006833329487133664",
            "extra": "mean: 1.3804491065755897 msec\nrounds: 441"
          },
          {
            "name": "Collections",
            "value": 573.4019872707452,
            "unit": "iter/sec",
            "range": "stddev: 0.00007872844411302679",
            "extra": "mean: 1.74397721354221 msec\nrounds: 384"
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
          "id": "270e03d29e3d4369c977812de5a6e731662e4cf0",
          "message": "move pagination models to extensions submodule (#717)\n\n* move pagination models to extensions submodule\r\n\r\n* remove models from api\r\n\r\n* update changelog\r\n\r\n* update changelog\r\n\r\n---------\r\n\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-07-01T20:37:19+02:00",
          "tree_id": "dad36fe57a1bc4796076cc80df63a41b55d15116",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/270e03d29e3d4369c977812de5a6e731662e4cf0"
        },
        "date": 1719859128472,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 809.9398788994122,
            "unit": "iter/sec",
            "range": "stddev: 0.00008253165955625675",
            "extra": "mean: 1.2346595420870639 msec\nrounds: 297"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 525.5347422753155,
            "unit": "iter/sec",
            "range": "stddev: 0.00008769745298275147",
            "extra": "mean: 1.902823770832877 msec\nrounds: 384"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 200.36880961101446,
            "unit": "iter/sec",
            "range": "stddev: 0.0043904166625785964",
            "extra": "mean: 4.990796730994949 msec\nrounds: 171"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 108.99122474392563,
            "unit": "iter/sec",
            "range": "stddev: 0.006385352689163359",
            "extra": "mean: 9.175050581819733 msec\nrounds: 110"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 57.29870865837406,
            "unit": "iter/sec",
            "range": "stddev: 0.009793846811455538",
            "extra": "mean: 17.45240029687567 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 45.7507536423915,
            "unit": "iter/sec",
            "range": "stddev: 0.011205718568618473",
            "extra": "mean: 21.857563436363264 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.021764256846264,
            "unit": "iter/sec",
            "range": "stddev: 0.017178931189888082",
            "extra": "mean: 90.72957620000275 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1)",
            "value": 815.5321448070866,
            "unit": "iter/sec",
            "range": "stddev: 0.00010936381769159677",
            "extra": "mean: 1.2261932363641521 msec\nrounds: 550"
          },
          {
            "name": "Items Limit: (10)",
            "value": 568.4243901312749,
            "unit": "iter/sec",
            "range": "stddev: 0.00008314819615974816",
            "extra": "mean: 1.759248929781241 msec\nrounds: 413"
          },
          {
            "name": "Items Limit: (50)",
            "value": 222.17783731335268,
            "unit": "iter/sec",
            "range": "stddev: 0.00006282544012878668",
            "extra": "mean: 4.500898973958556 msec\nrounds: 192"
          },
          {
            "name": "Items Limit: (100)",
            "value": 124.48039030160815,
            "unit": "iter/sec",
            "range": "stddev: 0.0004443218596664219",
            "extra": "mean: 8.033393834780425 msec\nrounds: 115"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.24246624562089,
            "unit": "iter/sec",
            "range": "stddev: 0.00391454511429348",
            "extra": "mean: 15.096056301588973 msec\nrounds: 63"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.02253266757351,
            "unit": "iter/sec",
            "range": "stddev: 0.006587771159653229",
            "extra": "mean: 18.8599063396223 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.468154600971458,
            "unit": "iter/sec",
            "range": "stddev: 0.014395338767808153",
            "extra": "mean: 74.24922193333525 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 972.3874516801158,
            "unit": "iter/sec",
            "range": "stddev: 0.00007750962867553712",
            "extra": "mean: 1.0283966522523245 msec\nrounds: 555"
          },
          {
            "name": "Collection",
            "value": 1017.3089015257526,
            "unit": "iter/sec",
            "range": "stddev: 0.00005871924521461928",
            "extra": "mean: 982.9855990645586 usec\nrounds: 641"
          },
          {
            "name": "Collections With Model validation",
            "value": 732.758121195326,
            "unit": "iter/sec",
            "range": "stddev: 0.00006519903934745576",
            "extra": "mean: 1.3647068126228754 msec\nrounds: 507"
          },
          {
            "name": "Collections",
            "value": 553.1846029087545,
            "unit": "iter/sec",
            "range": "stddev: 0.00007483626224309534",
            "extra": "mean: 1.807714811189251 msec\nrounds: 429"
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
          "id": "1062ac44ad433defc765354130e4570f39402ee7",
          "message": "remove pagination extension dependency and add request model attributes (#718)\n\n* remove pagination extension dependency and add request model attributes\r\n\r\n* add migration guide\r\n\r\n---------\r\n\r\nCo-authored-by: Jonathan Healy <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-07-01T20:46:23+02:00",
          "tree_id": "7fee8c25e125288618ec50922141d083de99d5d4",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/1062ac44ad433defc765354130e4570f39402ee7"
        },
        "date": 1719859672456,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 814.0301073785708,
            "unit": "iter/sec",
            "range": "stddev: 0.0000824902143774556",
            "extra": "mean: 1.2284557916663668 msec\nrounds: 288"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 520.6546323172097,
            "unit": "iter/sec",
            "range": "stddev: 0.00008879022617429503",
            "extra": "mean: 1.920658989529067 msec\nrounds: 382"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 206.14983259153703,
            "unit": "iter/sec",
            "range": "stddev: 0.004259823495318396",
            "extra": "mean: 4.850840708570396 msec\nrounds: 175"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 112.33027733741444,
            "unit": "iter/sec",
            "range": "stddev: 0.006125393905942156",
            "extra": "mean: 8.902319336364041 msec\nrounds: 110"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 59.14744797511825,
            "unit": "iter/sec",
            "range": "stddev: 0.009044703983999201",
            "extra": "mean: 16.906900199999725 msec\nrounds: 65"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 47.21347553728896,
            "unit": "iter/sec",
            "range": "stddev: 0.010475742899061603",
            "extra": "mean: 21.18039370370447 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.25317958589185,
            "unit": "iter/sec",
            "range": "stddev: 0.016746824517421374",
            "extra": "mean: 88.86377333333446 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1)",
            "value": 847.7864068667333,
            "unit": "iter/sec",
            "range": "stddev: 0.0000816373862605844",
            "extra": "mean: 1.1795423846152722 msec\nrounds: 520"
          },
          {
            "name": "Items Limit: (10)",
            "value": 522.6863778712461,
            "unit": "iter/sec",
            "range": "stddev: 0.0002024823789951772",
            "extra": "mean: 1.9131931543207945 msec\nrounds: 324"
          },
          {
            "name": "Items Limit: (50)",
            "value": 221.79060264253954,
            "unit": "iter/sec",
            "range": "stddev: 0.00007943209303705897",
            "extra": "mean: 4.508757305699298 msec\nrounds: 193"
          },
          {
            "name": "Items Limit: (100)",
            "value": 127.69337759998693,
            "unit": "iter/sec",
            "range": "stddev: 0.00008753854640613381",
            "extra": "mean: 7.831259684684715 msec\nrounds: 111"
          },
          {
            "name": "Items Limit: (200)",
            "value": 69.08718048469369,
            "unit": "iter/sec",
            "range": "stddev: 0.00010304642718639759",
            "extra": "mean: 14.474465349205422 msec\nrounds: 63"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.97120854202652,
            "unit": "iter/sec",
            "range": "stddev: 0.00007962856833969209",
            "extra": "mean: 17.866328529410623 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.186498750374748,
            "unit": "iter/sec",
            "range": "stddev: 0.008976099762774463",
            "extra": "mean: 70.48955613333305 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 1040.0287334132151,
            "unit": "iter/sec",
            "range": "stddev: 0.000057081065249677126",
            "extra": "mean: 961.5118966166954 usec\nrounds: 532"
          },
          {
            "name": "Collection",
            "value": 1018.44512853714,
            "unit": "iter/sec",
            "range": "stddev: 0.00006122272107181981",
            "extra": "mean: 981.8889324320949 usec\nrounds: 444"
          },
          {
            "name": "Collections With Model validation",
            "value": 666.4039233201057,
            "unit": "iter/sec",
            "range": "stddev: 0.0023785913490877992",
            "extra": "mean: 1.5005914056115965 msec\nrounds: 392"
          },
          {
            "name": "Collections",
            "value": 565.4809189291253,
            "unit": "iter/sec",
            "range": "stddev: 0.00007888637229812725",
            "extra": "mean: 1.7684062654028034 msec\nrounds: 422"
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
          "id": "b3e7cd0c53d55a64bc4822703bbdac4f065a38e0",
          "message": "replace attr with dataclass + fastapi.Query() for GET models  (#714)\n\n* demonstrate issue 713\r\n\r\n* move from attr to dataclass+fastapi.Query() for GET models\r\n\r\n* update migration",
          "timestamp": "2024-07-02T22:55:29+02:00",
          "tree_id": "ed547b45d40f3cb519aaf56e24106dd0cc8958f7",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/b3e7cd0c53d55a64bc4822703bbdac4f065a38e0"
        },
        "date": 1719953813524,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 675.2419477486401,
            "unit": "iter/sec",
            "range": "stddev: 0.00008014471215802417",
            "extra": "mean: 1.4809506478887353 msec\nrounds: 284"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 489.7417723914875,
            "unit": "iter/sec",
            "range": "stddev: 0.00008807126763891022",
            "extra": "mean: 2.041892393856542 msec\nrounds: 358"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 197.66058316687747,
            "unit": "iter/sec",
            "range": "stddev: 0.004024947087910633",
            "extra": "mean: 5.059177626506026 msec\nrounds: 166"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 108.65207881305201,
            "unit": "iter/sec",
            "range": "stddev: 0.005885306937404337",
            "extra": "mean: 9.20368952830264 msec\nrounds: 106"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 56.63667725537918,
            "unit": "iter/sec",
            "range": "stddev: 0.009930427986939801",
            "extra": "mean: 17.656403031747825 msec\nrounds: 63"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 45.63916662653835,
            "unit": "iter/sec",
            "range": "stddev: 0.011176874693741321",
            "extra": "mean: 21.911004821427177 msec\nrounds: 56"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.430870434264891,
            "unit": "iter/sec",
            "range": "stddev: 0.017239391662889157",
            "extra": "mean: 87.48240177777058 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 744.938289804459,
            "unit": "iter/sec",
            "range": "stddev: 0.00008415231933214077",
            "extra": "mean: 1.342393072938287 msec\nrounds: 521"
          },
          {
            "name": "Items Limit: (10)",
            "value": 502.6400385225511,
            "unit": "iter/sec",
            "range": "stddev: 0.00030266266255802264",
            "extra": "mean: 1.9894953114745448 msec\nrounds: 366"
          },
          {
            "name": "Items Limit: (50)",
            "value": 213.8402402956879,
            "unit": "iter/sec",
            "range": "stddev: 0.00007029488872454222",
            "extra": "mean: 4.676388310344435 msec\nrounds: 174"
          },
          {
            "name": "Items Limit: (100)",
            "value": 118.2298547194253,
            "unit": "iter/sec",
            "range": "stddev: 0.004254110518589675",
            "extra": "mean: 8.458100556522961 msec\nrounds: 115"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.14175939851518,
            "unit": "iter/sec",
            "range": "stddev: 0.005854279742209457",
            "extra": "mean: 15.590467261538029 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.50538915313416,
            "unit": "iter/sec",
            "range": "stddev: 0.006245317443106356",
            "extra": "mean: 19.04566400000309 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.601263962634738,
            "unit": "iter/sec",
            "range": "stddev: 0.00022340017083552166",
            "extra": "mean: 68.48722155554772 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 953.4793863344448,
            "unit": "iter/sec",
            "range": "stddev: 0.00007629476323711522",
            "extra": "mean: 1.0487903716979126 msec\nrounds: 530"
          },
          {
            "name": "Collection",
            "value": 990.0661469112562,
            "unit": "iter/sec",
            "range": "stddev: 0.000059966646472530735",
            "extra": "mean: 1.010033524648565 msec\nrounds: 568"
          },
          {
            "name": "Collections With Model validation",
            "value": 706.3949709021681,
            "unit": "iter/sec",
            "range": "stddev: 0.002039442414677403",
            "extra": "mean: 1.4156386174760787 msec\nrounds: 515"
          },
          {
            "name": "Collections",
            "value": 572.8247345324806,
            "unit": "iter/sec",
            "range": "stddev: 0.00008735208253159796",
            "extra": "mean: 1.7457346719082667 msec\nrounds: 445"
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
          "distinct": false,
          "id": "3c58f0f6e8f26d111dd21f1ffce3442b45b54a70",
          "message": "pin minimal version for fastapi-slim (#724)",
          "timestamp": "2024-07-05T14:47:21+02:00",
          "tree_id": "2bc5bc87d09362c9217b8a1157fd448880d2b61f",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/3c58f0f6e8f26d111dd21f1ffce3442b45b54a70"
        },
        "date": 1720183836076,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 672.3839081047813,
            "unit": "iter/sec",
            "range": "stddev: 0.0000740609922166359",
            "extra": "mean: 1.487245586853284 msec\nrounds: 213"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 490.4700816331548,
            "unit": "iter/sec",
            "range": "stddev: 0.00008236907054583779",
            "extra": "mean: 2.0388603453042955 msec\nrounds: 362"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 205.10500416125223,
            "unit": "iter/sec",
            "range": "stddev: 0.00372974937250988",
            "extra": "mean: 4.875551447851591 msec\nrounds: 163"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 105.42921331372523,
            "unit": "iter/sec",
            "range": "stddev: 0.007547649141513696",
            "extra": "mean: 9.485037102802849 msec\nrounds: 107"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 60.6208733558266,
            "unit": "iter/sec",
            "range": "stddev: 0.008722723698175571",
            "extra": "mean: 16.49596821428645 msec\nrounds: 14"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.69246489562892,
            "unit": "iter/sec",
            "range": "stddev: 0.014257850752318389",
            "extra": "mean: 23.42333717307536 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.43292957525019,
            "unit": "iter/sec",
            "range": "stddev: 0.022042551053921604",
            "extra": "mean: 95.85035466665835 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 777.66834105845,
            "unit": "iter/sec",
            "range": "stddev: 0.00007507696480908442",
            "extra": "mean: 1.285895216769329 msec\nrounds: 489"
          },
          {
            "name": "Items Limit: (10)",
            "value": 513.1751403802305,
            "unit": "iter/sec",
            "range": "stddev: 0.00008679887428606168",
            "extra": "mean: 1.948652460559689 msec\nrounds: 393"
          },
          {
            "name": "Items Limit: (50)",
            "value": 210.97091900351734,
            "unit": "iter/sec",
            "range": "stddev: 0.00010346932174776722",
            "extra": "mean: 4.739989780218608 msec\nrounds: 182"
          },
          {
            "name": "Items Limit: (100)",
            "value": 121.65867854363157,
            "unit": "iter/sec",
            "range": "stddev: 0.0005576322592994993",
            "extra": "mean: 8.21971775438413 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 67.23298061276564,
            "unit": "iter/sec",
            "range": "stddev: 0.00009333728636442831",
            "extra": "mean: 14.873652646155751 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 54.76213096912159,
            "unit": "iter/sec",
            "range": "stddev: 0.00020481185536626014",
            "extra": "mean: 18.26079413461584 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.482492147069433,
            "unit": "iter/sec",
            "range": "stddev: 0.010222265835814948",
            "extra": "mean: 74.17026385714313 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 930.1910086605365,
            "unit": "iter/sec",
            "range": "stddev: 0.00009678876464135533",
            "extra": "mean: 1.075048017761414 msec\nrounds: 563"
          },
          {
            "name": "Collection",
            "value": 852.4871642457078,
            "unit": "iter/sec",
            "range": "stddev: 0.002303665620542722",
            "extra": "mean: 1.1730381898298885 msec\nrounds: 590"
          },
          {
            "name": "Collections With Model validation",
            "value": 723.3439114598065,
            "unit": "iter/sec",
            "range": "stddev: 0.00007898621968227724",
            "extra": "mean: 1.3824682618560569 msec\nrounds: 485"
          },
          {
            "name": "Collections",
            "value": 546.8722803383471,
            "unit": "iter/sec",
            "range": "stddev: 0.00010020095854415736",
            "extra": "mean: 1.828580522277167 msec\nrounds: 404"
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
          "id": "dbd04643ba871d032ed5fdf214e4a5b0dc54131d",
          "message": "remove FieldsExtension check in StacApi (#725)",
          "timestamp": "2024-07-05T14:58:16+02:00",
          "tree_id": "3e2da27353104f63557f9d0517ac4e2c8554ff23",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/dbd04643ba871d032ed5fdf214e4a5b0dc54131d"
        },
        "date": 1720184388744,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 663.0244721314024,
            "unit": "iter/sec",
            "range": "stddev: 0.00008398602683803485",
            "extra": "mean: 1.508239954982859 msec\nrounds: 311"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 470.5566927530749,
            "unit": "iter/sec",
            "range": "stddev: 0.000060737299170556876",
            "extra": "mean: 2.125142443834607 msec\nrounds: 365"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 206.25498886877293,
            "unit": "iter/sec",
            "range": "stddev: 0.003411754609723311",
            "extra": "mean: 4.848367573965627 msec\nrounds: 169"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 110.88259471693299,
            "unit": "iter/sec",
            "range": "stddev: 0.005571248616746044",
            "extra": "mean: 9.01854797457485 msec\nrounds: 118"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 59.4945970773342,
            "unit": "iter/sec",
            "range": "stddev: 0.008258364611065671",
            "extra": "mean: 16.80824896923241 msec\nrounds: 65"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 47.94384011291807,
            "unit": "iter/sec",
            "range": "stddev: 0.009244746620687277",
            "extra": "mean: 20.857736836364893 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.458183709744613,
            "unit": "iter/sec",
            "range": "stddev: 0.016525144453361843",
            "extra": "mean: 87.27386690000003 msec\nrounds: 10"
          },
          {
            "name": "Items Limit: (1)",
            "value": 792.4955208293109,
            "unit": "iter/sec",
            "range": "stddev: 0.00007439839276561364",
            "extra": "mean: 1.261836784835762 msec\nrounds: 488"
          },
          {
            "name": "Items Limit: (10)",
            "value": 487.50613936012076,
            "unit": "iter/sec",
            "range": "stddev: 0.002333374187459521",
            "extra": "mean: 2.0512562186653818 msec\nrounds: 375"
          },
          {
            "name": "Items Limit: (50)",
            "value": 209.7314290257105,
            "unit": "iter/sec",
            "range": "stddev: 0.000058376395230018667",
            "extra": "mean: 4.768002605262429 msec\nrounds: 190"
          },
          {
            "name": "Items Limit: (100)",
            "value": 120.87773950226804,
            "unit": "iter/sec",
            "range": "stddev: 0.0005695483839745554",
            "extra": "mean: 8.272821812499538 msec\nrounds: 112"
          },
          {
            "name": "Items Limit: (200)",
            "value": 67.35840717985714,
            "unit": "iter/sec",
            "range": "stddev: 0.00023731289123602844",
            "extra": "mean: 14.845956753844384 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.76247093091009,
            "unit": "iter/sec",
            "range": "stddev: 0.004059724106349606",
            "extra": "mean: 18.9528652156843 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.88061398656475,
            "unit": "iter/sec",
            "range": "stddev: 0.008708395413531203",
            "extra": "mean: 72.04292266667129 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 901.2433179892413,
            "unit": "iter/sec",
            "range": "stddev: 0.00005009178671221045",
            "extra": "mean: 1.1095782681985307 msec\nrounds: 522"
          },
          {
            "name": "Collection",
            "value": 963.3263499440853,
            "unit": "iter/sec",
            "range": "stddev: 0.00008634757273198372",
            "extra": "mean: 1.0380698089054072 msec\nrounds: 539"
          },
          {
            "name": "Collections With Model validation",
            "value": 686.9608569757786,
            "unit": "iter/sec",
            "range": "stddev: 0.0020501528314831423",
            "extra": "mean: 1.4556870160001836 msec\nrounds: 500"
          },
          {
            "name": "Collections",
            "value": 574.6968096691626,
            "unit": "iter/sec",
            "range": "stddev: 0.00008861985209384724",
            "extra": "mean: 1.7400479403664568 msec\nrounds: 436"
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
          "id": "494e485c5d619d8c800bc845c391dfdced21fb2a",
          "message": "Release/v3.0.0b1 (#727)\n\n* update changelog\r\n\r\n* Bump version: 3.0.0a4 → 3.0.0b1",
          "timestamp": "2024-07-08T11:05:05+03:00",
          "tree_id": "53ff0f8a550a26adffdd7e226e8717de495b6e1d",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/494e485c5d619d8c800bc845c391dfdced21fb2a"
        },
        "date": 1720426002962,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 719.5573322978097,
            "unit": "iter/sec",
            "range": "stddev: 0.00014860431863222668",
            "extra": "mean: 1.3897433256730696 msec\nrounds: 261"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 489.45217875402363,
            "unit": "iter/sec",
            "range": "stddev: 0.00010426446367717591",
            "extra": "mean: 2.043100518105068 msec\nrounds: 359"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 194.18838557104084,
            "unit": "iter/sec",
            "range": "stddev: 0.0052029420761788864",
            "extra": "mean: 5.1496385690593485 msec\nrounds: 181"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 104.6975989568853,
            "unit": "iter/sec",
            "range": "stddev: 0.0073859411725162305",
            "extra": "mean: 9.551317412845371 msec\nrounds: 109"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.65415408784598,
            "unit": "iter/sec",
            "range": "stddev: 0.010780585818748495",
            "extra": "mean: 17.96811067187498 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.247331727901404,
            "unit": "iter/sec",
            "range": "stddev: 0.012467681361063462",
            "extra": "mean: 22.600232849056113 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.290151780679555,
            "unit": "iter/sec",
            "range": "stddev: 0.01993200694185199",
            "extra": "mean: 88.57276850000062 msec\nrounds: 8"
          },
          {
            "name": "Items Limit: (1)",
            "value": 790.2722517738292,
            "unit": "iter/sec",
            "range": "stddev: 0.00008490206917954251",
            "extra": "mean: 1.2653867040825741 msec\nrounds: 490"
          },
          {
            "name": "Items Limit: (10)",
            "value": 484.26785620412045,
            "unit": "iter/sec",
            "range": "stddev: 0.00005777740281937841",
            "extra": "mean: 2.0649729012336033 msec\nrounds: 324"
          },
          {
            "name": "Items Limit: (50)",
            "value": 212.4757019534087,
            "unit": "iter/sec",
            "range": "stddev: 0.00008970320431845155",
            "extra": "mean: 4.706420502704249 msec\nrounds: 185"
          },
          {
            "name": "Items Limit: (100)",
            "value": 123.32089541136533,
            "unit": "iter/sec",
            "range": "stddev: 0.00008526026994646445",
            "extra": "mean: 8.108925877194363 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.65596401014068,
            "unit": "iter/sec",
            "range": "stddev: 0.0005709934447235969",
            "extra": "mean: 15.002408484376062 msec\nrounds: 64"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.97980530385836,
            "unit": "iter/sec",
            "range": "stddev: 0.00036399145326990266",
            "extra": "mean: 18.52544658823588 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.743951165603972,
            "unit": "iter/sec",
            "range": "stddev: 0.008946417019275104",
            "extra": "mean: 72.7592806428642 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 1034.6038960155859,
            "unit": "iter/sec",
            "range": "stddev: 0.00005269853515056007",
            "extra": "mean: 966.5534837546518 usec\nrounds: 554"
          },
          {
            "name": "Collection",
            "value": 994.5412892788597,
            "unit": "iter/sec",
            "range": "stddev: 0.00007637448564597573",
            "extra": "mean: 1.0054886717926999 msec\nrounds: 585"
          },
          {
            "name": "Collections With Model validation",
            "value": 720.3896110045348,
            "unit": "iter/sec",
            "range": "stddev: 0.00010828217110560214",
            "extra": "mean: 1.3881377309225316 msec\nrounds: 498"
          },
          {
            "name": "Collections",
            "value": 566.069213410975,
            "unit": "iter/sec",
            "range": "stddev: 0.00010784541924133442",
            "extra": "mean: 1.7665684271615467 msec\nrounds: 405"
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
          "id": "0885f0b401c4831fd26a4137238eb7bbaa5c2b3a",
          "message": "move back to attrs (#729)\n\n* move back to attrs\r\n\r\n* update changelog\r\n\r\n* edit tests\r\n\r\n* more doc",
          "timestamp": "2024-07-09T17:04:45+02:00",
          "tree_id": "73e423f5e0fecfd83fd6eb5fe544aceb8cbbc45a",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/0885f0b401c4831fd26a4137238eb7bbaa5c2b3a"
        },
        "date": 1720537578639,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 774.7011264479002,
            "unit": "iter/sec",
            "range": "stddev: 0.00009473667342474389",
            "extra": "mean: 1.2908203768660087 msec\nrounds: 268"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 509.3715839473105,
            "unit": "iter/sec",
            "range": "stddev: 0.00005819060861120109",
            "extra": "mean: 1.9632033499996735 msec\nrounds: 300"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 209.3311101737972,
            "unit": "iter/sec",
            "range": "stddev: 0.004286819621282547",
            "extra": "mean: 4.777120797619378 msec\nrounds: 168"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 101.94856811626828,
            "unit": "iter/sec",
            "range": "stddev: 0.00888881246182311",
            "extra": "mean: 9.808867534652766 msec\nrounds: 101"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 51.28832551402185,
            "unit": "iter/sec",
            "range": "stddev: 0.01447835123016985",
            "extra": "mean: 19.497614515151355 msec\nrounds: 66"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.02815020284028,
            "unit": "iter/sec",
            "range": "stddev: 0.015291341189255849",
            "extra": "mean: 23.793576333331455 msec\nrounds: 51"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.369882820301093,
            "unit": "iter/sec",
            "range": "stddev: 0.02160160022698133",
            "extra": "mean: 96.43310511111105 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 872.5932397164337,
            "unit": "iter/sec",
            "range": "stddev: 0.00007100394862198005",
            "extra": "mean: 1.1460093368646422 msec\nrounds: 472"
          },
          {
            "name": "Items Limit: (10)",
            "value": 529.5317283278573,
            "unit": "iter/sec",
            "range": "stddev: 0.0001319993305217779",
            "extra": "mean: 1.8884609675000519 msec\nrounds: 400"
          },
          {
            "name": "Items Limit: (50)",
            "value": 220.34556063780252,
            "unit": "iter/sec",
            "range": "stddev: 0.0001360020315973487",
            "extra": "mean: 4.538326059782843 msec\nrounds: 184"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.52665326972715,
            "unit": "iter/sec",
            "range": "stddev: 0.00008144337524660176",
            "extra": "mean: 7.903473095650596 msec\nrounds: 115"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.92577324182719,
            "unit": "iter/sec",
            "range": "stddev: 0.004550659321456323",
            "extra": "mean: 15.402203933333661 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.62939368601289,
            "unit": "iter/sec",
            "range": "stddev: 0.00009338312101881609",
            "extra": "mean: 17.976108199997043 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.243001603834397,
            "unit": "iter/sec",
            "range": "stddev: 0.0006764016047807862",
            "extra": "mean: 70.20991977777966 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 950.2675413516673,
            "unit": "iter/sec",
            "range": "stddev: 0.00009094124452481535",
            "extra": "mean: 1.0523352176983685 msec\nrounds: 565"
          },
          {
            "name": "Collection",
            "value": 969.7997754629789,
            "unit": "iter/sec",
            "range": "stddev: 0.0000878028283676809",
            "extra": "mean: 1.0311406800672889 msec\nrounds: 597"
          },
          {
            "name": "Collections With Model validation",
            "value": 644.0344285506702,
            "unit": "iter/sec",
            "range": "stddev: 0.00276437997541366",
            "extra": "mean: 1.5527120223221478 msec\nrounds: 448"
          },
          {
            "name": "Collections",
            "value": 573.8915419074169,
            "unit": "iter/sec",
            "range": "stddev: 0.00010298221310262785",
            "extra": "mean: 1.7424895245473493 msec\nrounds: 387"
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
          "id": "599742c1d4a88645a6db4c6d9b49b2323400d246",
          "message": "Bump version: 3.0.0b1 → 3.0.0b2 (#730)",
          "timestamp": "2024-07-09T18:26:11+02:00",
          "tree_id": "40a255e8396aa18aa72ea111c7d5cbb49d69877d",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/599742c1d4a88645a6db4c6d9b49b2323400d246"
        },
        "date": 1720542474324,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 735.9807424537219,
            "unit": "iter/sec",
            "range": "stddev: 0.00010033177284781507",
            "extra": "mean: 1.3587312035720547 msec\nrounds: 280"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 527.4538315037946,
            "unit": "iter/sec",
            "range": "stddev: 0.000058885150535006745",
            "extra": "mean: 1.8959005324673726 msec\nrounds: 308"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 203.23102287385507,
            "unit": "iter/sec",
            "range": "stddev: 0.004367730158633301",
            "extra": "mean: 4.920508620481122 msec\nrounds: 166"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 102.92848033592564,
            "unit": "iter/sec",
            "range": "stddev: 0.008084435702210221",
            "extra": "mean: 9.715483962614815 msec\nrounds: 107"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 52.411371552316346,
            "unit": "iter/sec",
            "range": "stddev: 0.012522328728375162",
            "extra": "mean: 19.079828868851738 msec\nrounds: 61"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 39.67541655502273,
            "unit": "iter/sec",
            "range": "stddev: 0.0158474425496431",
            "extra": "mean: 25.204524283019893 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.397060482554949,
            "unit": "iter/sec",
            "range": "stddev: 0.022750765683438243",
            "extra": "mean: 106.41625664285519 msec\nrounds: 14"
          },
          {
            "name": "Items Limit: (1)",
            "value": 822.05260587578,
            "unit": "iter/sec",
            "range": "stddev: 0.00010035664208023108",
            "extra": "mean: 1.2164671614107254 msec\nrounds: 539"
          },
          {
            "name": "Items Limit: (10)",
            "value": 524.899315620519,
            "unit": "iter/sec",
            "range": "stddev: 0.00011049951189332691",
            "extra": "mean: 1.905127269632334 msec\nrounds: 382"
          },
          {
            "name": "Items Limit: (50)",
            "value": 209.1902428399008,
            "unit": "iter/sec",
            "range": "stddev: 0.0005098249721535791",
            "extra": "mean: 4.780337679350217 msec\nrounds: 184"
          },
          {
            "name": "Items Limit: (100)",
            "value": 116.19363797580966,
            "unit": "iter/sec",
            "range": "stddev: 0.005361953192128188",
            "extra": "mean: 8.606323181035005 msec\nrounds: 116"
          },
          {
            "name": "Items Limit: (200)",
            "value": 63.92005915883081,
            "unit": "iter/sec",
            "range": "stddev: 0.006264811589900943",
            "extra": "mean: 15.644541215382244 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 54.42901666787977,
            "unit": "iter/sec",
            "range": "stddev: 0.00032732847358205616",
            "extra": "mean: 18.372553120000248 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.886135714516032,
            "unit": "iter/sec",
            "range": "stddev: 0.009043422183729928",
            "extra": "mean: 72.01427528571814 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 926.9549685542942,
            "unit": "iter/sec",
            "range": "stddev: 0.0000770132560499136",
            "extra": "mean: 1.0788010571426454 msec\nrounds: 560"
          },
          {
            "name": "Collection",
            "value": 973.2349175669872,
            "unit": "iter/sec",
            "range": "stddev: 0.00007804663672997748",
            "extra": "mean: 1.0275011530617124 msec\nrounds: 588"
          },
          {
            "name": "Collections With Model validation",
            "value": 648.4532850937538,
            "unit": "iter/sec",
            "range": "stddev: 0.0021327572299863515",
            "extra": "mean: 1.5421311341732493 msec\nrounds: 477"
          },
          {
            "name": "Collections",
            "value": 565.421180549747,
            "unit": "iter/sec",
            "range": "stddev: 0.00009533595145299489",
            "extra": "mean: 1.7685931026278874 msec\nrounds: 419"
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
          "id": "c55c2537728f4df49f5235cc49574f90f8c709b1",
          "message": "add description and examples (#734)\n\n* add description and examples\r\n\r\n* update docs\r\n\r\n* update changelog\r\n\r\n* Update stac_fastapi/extensions/stac_fastapi/extensions/core/query/request.py",
          "timestamp": "2024-07-17T11:09:34+02:00",
          "tree_id": "a6946e631b88e6e81bf0ba2e14b270fd5d60f798",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/c55c2537728f4df49f5235cc49574f90f8c709b1"
        },
        "date": 1721207472592,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 782.3258519917628,
            "unit": "iter/sec",
            "range": "stddev: 0.0000785239284964922",
            "extra": "mean: 1.2782397481229204 msec\nrounds: 266"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 524.5509122935509,
            "unit": "iter/sec",
            "range": "stddev: 0.00006231400243868418",
            "extra": "mean: 1.9063926428563271 msec\nrounds: 308"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 201.0037377870734,
            "unit": "iter/sec",
            "range": "stddev: 0.004327931701699577",
            "extra": "mean: 4.9750318626378816 msec\nrounds: 182"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 102.88575313141848,
            "unit": "iter/sec",
            "range": "stddev: 0.00815448665424392",
            "extra": "mean: 9.719518685183512 msec\nrounds: 108"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 61.54567911069334,
            "unit": "iter/sec",
            "range": "stddev: 0.008523711212090172",
            "extra": "mean: 16.248094333339697 msec\nrounds: 15"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 43.164428367250224,
            "unit": "iter/sec",
            "range": "stddev: 0.013761064320624702",
            "extra": "mean: 23.167224444439103 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.856707320943862,
            "unit": "iter/sec",
            "range": "stddev: 0.019896784731172526",
            "extra": "mean: 92.10895812498165 msec\nrounds: 8"
          },
          {
            "name": "Items Limit: (1)",
            "value": 764.6801958115097,
            "unit": "iter/sec",
            "range": "stddev: 0.0022855009759948446",
            "extra": "mean: 1.3077362346735806 msec\nrounds: 473"
          },
          {
            "name": "Items Limit: (10)",
            "value": 555.1602065178535,
            "unit": "iter/sec",
            "range": "stddev: 0.00008087953092259664",
            "extra": "mean: 1.801281843077924 msec\nrounds: 325"
          },
          {
            "name": "Items Limit: (50)",
            "value": 214.3619009966509,
            "unit": "iter/sec",
            "range": "stddev: 0.00008793734082711905",
            "extra": "mean: 4.66500807909715 msec\nrounds: 177"
          },
          {
            "name": "Items Limit: (100)",
            "value": 115.38771405197409,
            "unit": "iter/sec",
            "range": "stddev: 0.00553414779120866",
            "extra": "mean: 8.6664339285686 msec\nrounds: 112"
          },
          {
            "name": "Items Limit: (200)",
            "value": 62.23423831374321,
            "unit": "iter/sec",
            "range": "stddev: 0.0069254653773410035",
            "extra": "mean: 16.0683255245878 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 50.68522328815672,
            "unit": "iter/sec",
            "range": "stddev: 0.007771446346582265",
            "extra": "mean: 19.729616150939666 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.482588726483735,
            "unit": "iter/sec",
            "range": "stddev: 0.010985371552707466",
            "extra": "mean: 74.1697325555669 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 893.5405135561102,
            "unit": "iter/sec",
            "range": "stddev: 0.000067759739956904",
            "extra": "mean: 1.1191434353885115 msec\nrounds: 503"
          },
          {
            "name": "Collection",
            "value": 944.3092914899602,
            "unit": "iter/sec",
            "range": "stddev: 0.00006824253934255635",
            "extra": "mean: 1.058975072057344 msec\nrounds: 569"
          },
          {
            "name": "Collections With Model validation",
            "value": 662.6892908189285,
            "unit": "iter/sec",
            "range": "stddev: 0.00225513541146466",
            "extra": "mean: 1.5090028069779649 msec\nrounds: 430"
          },
          {
            "name": "Collections",
            "value": 543.8677826748097,
            "unit": "iter/sec",
            "range": "stddev: 0.00008670160345648367",
            "extra": "mean: 1.8386821794846442 msec\nrounds: 390"
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
          "id": "fe4d0dfb9812ec624b5af8bb10e32621b48e090a",
          "message": "Adding free-text extension. (#655)\n\n* Adding free-text extension.\r\n\r\n* Adding pull request to change log.\r\n\r\n* q parameter should be string for post.\r\n\r\n* Removing unneeded imports.\r\n\r\n* split free-text ext\r\n\r\n---------\r\n\r\nCo-authored-by: vincentsarago <vincent.sarago@gmail.com>",
          "timestamp": "2024-07-19T11:11:53+02:00",
          "tree_id": "6cceb8696142bc472a4c302c68c09d691ee1cbdb",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/fe4d0dfb9812ec624b5af8bb10e32621b48e090a"
        },
        "date": 1721380404265,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 741.7641338176994,
            "unit": "iter/sec",
            "range": "stddev: 0.00009066062898408873",
            "extra": "mean: 1.3481374393949412 msec\nrounds: 264"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 508.47651679435313,
            "unit": "iter/sec",
            "range": "stddev: 0.00006970032954697532",
            "extra": "mean: 1.966659161182929 msec\nrounds: 304"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 209.5279603652645,
            "unit": "iter/sec",
            "range": "stddev: 0.004099692869090613",
            "extra": "mean: 4.772632722891621 msec\nrounds: 166"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 100.59961545222443,
            "unit": "iter/sec",
            "range": "stddev: 0.008433416666121008",
            "extra": "mean: 9.940395850468317 msec\nrounds: 107"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 44.67664296001307,
            "unit": "iter/sec",
            "range": "stddev: 0.016665893098592833",
            "extra": "mean: 22.38306044827562 msec\nrounds: 58"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 36.49924430212789,
            "unit": "iter/sec",
            "range": "stddev: 0.018449710986462968",
            "extra": "mean: 27.397827519998827 msec\nrounds: 50"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.215502071531022,
            "unit": "iter/sec",
            "range": "stddev: 0.028264325631452727",
            "extra": "mean: 108.51280724999768 msec\nrounds: 8"
          },
          {
            "name": "Items Limit: (1)",
            "value": 867.6479650874059,
            "unit": "iter/sec",
            "range": "stddev: 0.00007632405012564407",
            "extra": "mean: 1.1525411690434393 msec\nrounds: 491"
          },
          {
            "name": "Items Limit: (10)",
            "value": 518.5560325168225,
            "unit": "iter/sec",
            "range": "stddev: 0.00008426649853782507",
            "extra": "mean: 1.9284319095594729 msec\nrounds: 387"
          },
          {
            "name": "Items Limit: (50)",
            "value": 213.72554343186175,
            "unit": "iter/sec",
            "range": "stddev: 0.00012665912013281428",
            "extra": "mean: 4.678897917126186 msec\nrounds: 181"
          },
          {
            "name": "Items Limit: (100)",
            "value": 117.33641123518694,
            "unit": "iter/sec",
            "range": "stddev: 0.004891816417271839",
            "extra": "mean: 8.52250370940371 msec\nrounds: 117"
          },
          {
            "name": "Items Limit: (200)",
            "value": 62.95114505698012,
            "unit": "iter/sec",
            "range": "stddev: 0.008333287972891667",
            "extra": "mean: 15.885334557375435 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.67157394171497,
            "unit": "iter/sec",
            "range": "stddev: 0.0007365900228312124",
            "extra": "mean: 18.63183667924397 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.622277293489642,
            "unit": "iter/sec",
            "range": "stddev: 0.011064111600991085",
            "extra": "mean: 73.40916488889269 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 958.7357873279481,
            "unit": "iter/sec",
            "range": "stddev: 0.00009737519830785905",
            "extra": "mean: 1.0430402340430596 msec\nrounds: 517"
          },
          {
            "name": "Collection",
            "value": 933.1133110829677,
            "unit": "iter/sec",
            "range": "stddev: 0.00008361995504738696",
            "extra": "mean: 1.0716812075474562 msec\nrounds: 530"
          },
          {
            "name": "Collections With Model validation",
            "value": 655.6112051497042,
            "unit": "iter/sec",
            "range": "stddev: 0.00326046531299241",
            "extra": "mean: 1.5252942477876916 msec\nrounds: 452"
          },
          {
            "name": "Collections",
            "value": 546.9074330665283,
            "unit": "iter/sec",
            "range": "stddev: 0.00010764230006965468",
            "extra": "mean: 1.8284629894184588 msec\nrounds: 378"
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
          "id": "4df4947b9822271b0912abe766234edb26a78a59",
          "message": "Feature/add collection search extension V2 (#736)\n\n* sketch\r\n\r\n* sketch\r\n\r\n* fix\r\n\r\n* set limit to 10\r\n\r\n* Update CHANGES.md",
          "timestamp": "2024-07-23T01:35:11+03:00",
          "tree_id": "bd5ed5a1e3ba0e0e8f642d46b14c4fb09561a5e7",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/4df4947b9822271b0912abe766234edb26a78a59"
        },
        "date": 1721687802755,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 742.1097841914473,
            "unit": "iter/sec",
            "range": "stddev: 0.0000853484269020588",
            "extra": "mean: 1.3475095212355035 msec\nrounds: 259"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 498.170107173957,
            "unit": "iter/sec",
            "range": "stddev: 0.00008209201147491718",
            "extra": "mean: 2.0073464577648936 msec\nrounds: 367"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 200.82334678597255,
            "unit": "iter/sec",
            "range": "stddev: 0.0040850371829399225",
            "extra": "mean: 4.979500720430427 msec\nrounds: 186"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 104.929679470266,
            "unit": "iter/sec",
            "range": "stddev: 0.007396100176443381",
            "extra": "mean: 9.530192077670177 msec\nrounds: 103"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 60.87724203172335,
            "unit": "iter/sec",
            "range": "stddev: 0.00919539689110736",
            "extra": "mean: 16.426499733330502 msec\nrounds: 15"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.71928845950927,
            "unit": "iter/sec",
            "range": "stddev: 0.014588945251673478",
            "extra": "mean: 23.96972807842952 msec\nrounds: 51"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.16219916575081,
            "unit": "iter/sec",
            "range": "stddev: 0.019157142865598255",
            "extra": "mean: 98.40389699999719 msec\nrounds: 8"
          },
          {
            "name": "Items Limit: (1)",
            "value": 797.3712588698071,
            "unit": "iter/sec",
            "range": "stddev: 0.000060680565722605014",
            "extra": "mean: 1.2541209491515892 msec\nrounds: 413"
          },
          {
            "name": "Items Limit: (10)",
            "value": 506.6896453440383,
            "unit": "iter/sec",
            "range": "stddev: 0.002462385066946901",
            "extra": "mean: 1.9735947027711762 msec\nrounds: 397"
          },
          {
            "name": "Items Limit: (50)",
            "value": 213.55017252869348,
            "unit": "iter/sec",
            "range": "stddev: 0.0001020636461630442",
            "extra": "mean: 4.6827403048135485 msec\nrounds: 187"
          },
          {
            "name": "Items Limit: (100)",
            "value": 123.06209314806773,
            "unit": "iter/sec",
            "range": "stddev: 0.000245254132267927",
            "extra": "mean: 8.125979124999969 msec\nrounds: 112"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.54668921135043,
            "unit": "iter/sec",
            "range": "stddev: 0.0001341647585671978",
            "extra": "mean: 15.02704359677501 msec\nrounds: 62"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.212544260486304,
            "unit": "iter/sec",
            "range": "stddev: 0.004617571361820888",
            "extra": "mean: 19.152485560003356 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.49257073419517,
            "unit": "iter/sec",
            "range": "stddev: 0.010406925766626338",
            "extra": "mean: 74.11486066666522 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 968.9525118464417,
            "unit": "iter/sec",
            "range": "stddev: 0.00006167203175983398",
            "extra": "mean: 1.0320423217587764 msec\nrounds: 432"
          },
          {
            "name": "Collection",
            "value": 921.4099558212188,
            "unit": "iter/sec",
            "range": "stddev: 0.0001034015064206017",
            "extra": "mean: 1.0852932439922867 msec\nrounds: 541"
          },
          {
            "name": "Collections With Model validation",
            "value": 709.7190943674264,
            "unit": "iter/sec",
            "range": "stddev: 0.00008088832446294599",
            "extra": "mean: 1.4090081666624756 msec\nrounds: 18"
          },
          {
            "name": "Collections",
            "value": 569.9772903563941,
            "unit": "iter/sec",
            "range": "stddev: 0.000055996105649623826",
            "extra": "mean: 1.7544558650305564 msec\nrounds: 326"
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
          "id": "69dcee0f23d4a20db2d8e30a9300c0ec35b35b9b",
          "message": "use same Limit object for collection_items and get_search request model (#738)\n\n* use same Limit object for collection_items and get_search request model\r\n\r\n* add tests",
          "timestamp": "2024-07-24T09:25:13+02:00",
          "tree_id": "2840a11af51f96851f921a3a9fbdb7551bcab6eb",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/69dcee0f23d4a20db2d8e30a9300c0ec35b35b9b"
        },
        "date": 1721806002994,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 748.269503666349,
            "unit": "iter/sec",
            "range": "stddev: 0.0000978346979633318",
            "extra": "mean: 1.3364168860286691 msec\nrounds: 272"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 530.6920413378494,
            "unit": "iter/sec",
            "range": "stddev: 0.00007768359641854143",
            "extra": "mean: 1.8843320082190183 msec\nrounds: 365"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 205.066755359047,
            "unit": "iter/sec",
            "range": "stddev: 0.0038551555072761203",
            "extra": "mean: 4.876460829787458 msec\nrounds: 188"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 103.51488600294766,
            "unit": "iter/sec",
            "range": "stddev: 0.0074671093914302645",
            "extra": "mean: 9.660446324324061 msec\nrounds: 111"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 53.70742920904122,
            "unit": "iter/sec",
            "range": "stddev: 0.011555796703694905",
            "extra": "mean: 18.619398000000675 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 43.67834487611425,
            "unit": "iter/sec",
            "range": "stddev: 0.012541508395231845",
            "extra": "mean: 22.894640418182505 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.271203811279774,
            "unit": "iter/sec",
            "range": "stddev: 0.018334754594739086",
            "extra": "mean: 88.72166777777896 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 751.1584884274191,
            "unit": "iter/sec",
            "range": "stddev: 0.0020354724555348884",
            "extra": "mean: 1.331276974708148 msec\nrounds: 514"
          },
          {
            "name": "Items Limit: (10)",
            "value": 534.609459501915,
            "unit": "iter/sec",
            "range": "stddev: 0.00009186188202200397",
            "extra": "mean: 1.8705243280425305 msec\nrounds: 378"
          },
          {
            "name": "Items Limit: (50)",
            "value": 206.71893399777923,
            "unit": "iter/sec",
            "range": "stddev: 0.0008890920950591133",
            "extra": "mean: 4.837486245990138 msec\nrounds: 187"
          },
          {
            "name": "Items Limit: (100)",
            "value": 118.27599312469602,
            "unit": "iter/sec",
            "range": "stddev: 0.004447796682817019",
            "extra": "mean: 8.454801127272887 msec\nrounds: 110"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.45700892313405,
            "unit": "iter/sec",
            "range": "stddev: 0.005744006607257417",
            "extra": "mean: 15.277202799998035 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 55.25906418369169,
            "unit": "iter/sec",
            "range": "stddev: 0.0005299830212306758",
            "extra": "mean: 18.096578629630947 msec\nrounds: 54"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.156877371576567,
            "unit": "iter/sec",
            "range": "stddev: 0.0076322388422315835",
            "extra": "mean: 70.63704613333357 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 972.8960456156689,
            "unit": "iter/sec",
            "range": "stddev: 0.00010133839661711389",
            "extra": "mean: 1.0278590446599862 msec\nrounds: 515"
          },
          {
            "name": "Collection",
            "value": 980.9030540027185,
            "unit": "iter/sec",
            "range": "stddev: 0.00006407092139748015",
            "extra": "mean: 1.0194687394634503 msec\nrounds: 522"
          },
          {
            "name": "Collections With Model validation",
            "value": 726.7444261188066,
            "unit": "iter/sec",
            "range": "stddev: 0.00007887169328317266",
            "extra": "mean: 1.3759995454530285 msec\nrounds: 484"
          },
          {
            "name": "Collections",
            "value": 573.117336761438,
            "unit": "iter/sec",
            "range": "stddev: 0.0000739868685281758",
            "extra": "mean: 1.7448433956836544 msec\nrounds: 417"
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
          "id": "4adcf0e523b83562d2807a0e500d5d8484aa6cce",
          "message": "add POST - /collections collection-search (#739)\n\n* add POST - /collections collection-search\r\n\r\n* fix",
          "timestamp": "2024-07-25T22:48:10+02:00",
          "tree_id": "af6a53ab1f86a50a7a5efc6c0eb6c42c3e9894c8",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/4adcf0e523b83562d2807a0e500d5d8484aa6cce"
        },
        "date": 1721940587475,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 727.5747930914057,
            "unit": "iter/sec",
            "range": "stddev: 0.000095290823945812",
            "extra": "mean: 1.3744291439112148 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 505.67412419803003,
            "unit": "iter/sec",
            "range": "stddev: 0.00007993018136399133",
            "extra": "mean: 1.9775581785719059 msec\nrounds: 364"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 206.04173063069607,
            "unit": "iter/sec",
            "range": "stddev: 0.004362734391972545",
            "extra": "mean: 4.853385753162667 msec\nrounds: 158"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 105.05416519219276,
            "unit": "iter/sec",
            "range": "stddev: 0.007181198040359834",
            "extra": "mean: 9.518899114285821 msec\nrounds: 105"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 54.6342241688084,
            "unit": "iter/sec",
            "range": "stddev: 0.011312302175542417",
            "extra": "mean: 18.30354535483487 msec\nrounds: 62"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.018541888837476,
            "unit": "iter/sec",
            "range": "stddev: 0.014494939824671432",
            "extra": "mean: 23.79901717307466 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.160571857073133,
            "unit": "iter/sec",
            "range": "stddev: 0.020158565902135123",
            "extra": "mean: 98.41965728571316 msec\nrounds: 14"
          },
          {
            "name": "Items Limit: (1)",
            "value": 819.198240703996,
            "unit": "iter/sec",
            "range": "stddev: 0.0000756595237704184",
            "extra": "mean: 1.2207057465609643 msec\nrounds: 509"
          },
          {
            "name": "Items Limit: (10)",
            "value": 562.4618057708847,
            "unit": "iter/sec",
            "range": "stddev: 0.00007184570847903953",
            "extra": "mean: 1.7778984986001765 msec\nrounds: 357"
          },
          {
            "name": "Items Limit: (50)",
            "value": 218.91122127356536,
            "unit": "iter/sec",
            "range": "stddev: 0.00010143954646730838",
            "extra": "mean: 4.568061857141332 msec\nrounds: 182"
          },
          {
            "name": "Items Limit: (100)",
            "value": 119.39223446120467,
            "unit": "iter/sec",
            "range": "stddev: 0.005071400785742245",
            "extra": "mean: 8.375754122643045 msec\nrounds: 106"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.08437465134158,
            "unit": "iter/sec",
            "range": "stddev: 0.006721593216272318",
            "extra": "mean: 15.60442784127356 msec\nrounds: 63"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.525137542121726,
            "unit": "iter/sec",
            "range": "stddev: 0.007021097852330143",
            "extra": "mean: 19.038503215685353 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.132866501668392,
            "unit": "iter/sec",
            "range": "stddev: 0.0010040497124031392",
            "extra": "mean: 70.75705412500355 msec\nrounds: 8"
          },
          {
            "name": "Collection With Model validation",
            "value": 962.8496979946475,
            "unit": "iter/sec",
            "range": "stddev: 0.00008857970348555058",
            "extra": "mean: 1.0385836980400225 msec\nrounds: 510"
          },
          {
            "name": "Collection",
            "value": 950.5612957718317,
            "unit": "iter/sec",
            "range": "stddev: 0.00005744229726833746",
            "extra": "mean: 1.0520100118194118 msec\nrounds: 423"
          },
          {
            "name": "Collections With Model validation",
            "value": 687.36221504652,
            "unit": "iter/sec",
            "range": "stddev: 0.0025262416627167706",
            "extra": "mean: 1.454837024948078 msec\nrounds: 481"
          },
          {
            "name": "Collections",
            "value": 566.4670764287356,
            "unit": "iter/sec",
            "range": "stddev: 0.00009541004872799558",
            "extra": "mean: 1.7653276626497902 msec\nrounds: 415"
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
          "id": "e376e3000c0231d3bbf8e12a8f7a9a254067b3c9",
          "message": "Release/v3.0.0b3 (#740)\n\n* update changelog\r\n\r\n* Bump version: 3.0.0b2 → 3.0.0b3",
          "timestamp": "2024-07-26T09:06:04+02:00",
          "tree_id": "4132782ee7b916d11b6365e58f4bc85bb8e82ee8",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/e376e3000c0231d3bbf8e12a8f7a9a254067b3c9"
        },
        "date": 1721977654757,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 707.9844192720502,
            "unit": "iter/sec",
            "range": "stddev: 0.00007755023773846485",
            "extra": "mean: 1.4124604620935022 msec\nrounds: 277"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 491.4815173762536,
            "unit": "iter/sec",
            "range": "stddev: 0.0003346843190075603",
            "extra": "mean: 2.0346645085219963 msec\nrounds: 352"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 207.17688862681297,
            "unit": "iter/sec",
            "range": "stddev: 0.003822047403143121",
            "extra": "mean: 4.826793213413377 msec\nrounds: 164"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 105.57651790973499,
            "unit": "iter/sec",
            "range": "stddev: 0.0067398575754527386",
            "extra": "mean: 9.471803198273431 msec\nrounds: 116"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.305752850353784,
            "unit": "iter/sec",
            "range": "stddev: 0.01122719976486592",
            "extra": "mean: 18.08130164516155 msec\nrounds: 62"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 45.56589791870434,
            "unit": "iter/sec",
            "range": "stddev: 0.011141853253477356",
            "extra": "mean: 21.94623711320545 msec\nrounds: 53"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.022192933432004,
            "unit": "iter/sec",
            "range": "stddev: 0.015480718315887433",
            "extra": "mean: 90.7260475333222 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1)",
            "value": 841.3423742165963,
            "unit": "iter/sec",
            "range": "stddev: 0.00006773724152819952",
            "extra": "mean: 1.188576768085805 msec\nrounds: 470"
          },
          {
            "name": "Items Limit: (10)",
            "value": 524.0705116694674,
            "unit": "iter/sec",
            "range": "stddev: 0.00006796593162699171",
            "extra": "mean: 1.9081401791038048 msec\nrounds: 402"
          },
          {
            "name": "Items Limit: (50)",
            "value": 217.1277442195678,
            "unit": "iter/sec",
            "range": "stddev: 0.00014976918640554774",
            "extra": "mean: 4.60558370186337 msec\nrounds: 161"
          },
          {
            "name": "Items Limit: (100)",
            "value": 124.22703175702323,
            "unit": "iter/sec",
            "range": "stddev: 0.00009187507424590638",
            "extra": "mean: 8.049777780700008 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 65.72516470493876,
            "unit": "iter/sec",
            "range": "stddev: 0.0036619775113235415",
            "extra": "mean: 15.214872484372144 msec\nrounds: 64"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.816944233467915,
            "unit": "iter/sec",
            "range": "stddev: 0.006292439144169765",
            "extra": "mean: 18.933317981814277 msec\nrounds: 55"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.279073927040043,
            "unit": "iter/sec",
            "range": "stddev: 0.0028072685524665217",
            "extra": "mean: 70.03255288890387 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 924.1715475247286,
            "unit": "iter/sec",
            "range": "stddev: 0.00008213863646497136",
            "extra": "mean: 1.0820501915238225 msec\nrounds: 590"
          },
          {
            "name": "Collection",
            "value": 931.7358502510992,
            "unit": "iter/sec",
            "range": "stddev: 0.00006633395132649748",
            "extra": "mean: 1.073265560974716 msec\nrounds: 533"
          },
          {
            "name": "Collections With Model validation",
            "value": 661.1257433903156,
            "unit": "iter/sec",
            "range": "stddev: 0.0022474790155563667",
            "extra": "mean: 1.5125715644831874 msec\nrounds: 473"
          },
          {
            "name": "Collections",
            "value": 563.5732763542563,
            "unit": "iter/sec",
            "range": "stddev: 0.00005854840842527963",
            "extra": "mean: 1.7743921544133159 msec\nrounds: 408"
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
          "id": "4979a89b4dc1534645388f182046955986fee669",
          "message": "3.0 release (#743)\n\n* prepare 3.0\r\n\r\n* update changelog\r\n\r\n* add 3.0.0 link to changelog\r\n\r\n* purge pre-releases from comparisons\r\n\r\n* add changelog in migration guide\r\n\r\n* fix changelog\r\n\r\n---------\r\n\r\nCo-authored-by: jonhealy1 <jonathan.d.healy@gmail.com>",
          "timestamp": "2024-08-01T11:41:10+02:00",
          "tree_id": "e76c3aee1162b24f9bd33693c70fcd186eeeffaa",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/4979a89b4dc1534645388f182046955986fee669"
        },
        "date": 1722505361811,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 718.110297045656,
            "unit": "iter/sec",
            "range": "stddev: 0.00006218330647406047",
            "extra": "mean: 1.3925437416982507 msec\nrounds: 271"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 501.8342649791383,
            "unit": "iter/sec",
            "range": "stddev: 0.00009099739174315042",
            "extra": "mean: 1.9926897579254994 msec\nrounds: 347"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 203.0347064773043,
            "unit": "iter/sec",
            "range": "stddev: 0.004355470437092051",
            "extra": "mean: 4.9252663121010904 msec\nrounds: 157"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 105.6304693201166,
            "unit": "iter/sec",
            "range": "stddev: 0.006795889561198645",
            "extra": "mean: 9.466965416668435 msec\nrounds: 108"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 55.33057294465105,
            "unit": "iter/sec",
            "range": "stddev: 0.011217805523287447",
            "extra": "mean: 18.073190765624858 msec\nrounds: 64"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.13575415138223,
            "unit": "iter/sec",
            "range": "stddev: 0.011920570079007814",
            "extra": "mean: 22.657367461538716 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.965025364205136,
            "unit": "iter/sec",
            "range": "stddev: 0.01835710309814517",
            "extra": "mean: 91.19905944444578 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 787.9931542584152,
            "unit": "iter/sec",
            "range": "stddev: 0.00007938728758900603",
            "extra": "mean: 1.2690465578233425 msec\nrounds: 441"
          },
          {
            "name": "Items Limit: (10)",
            "value": 554.0008346672118,
            "unit": "iter/sec",
            "range": "stddev: 0.00006749189132824984",
            "extra": "mean: 1.805051432098834 msec\nrounds: 405"
          },
          {
            "name": "Items Limit: (50)",
            "value": 222.22248122459746,
            "unit": "iter/sec",
            "range": "stddev: 0.0000741530028023741",
            "extra": "mean: 4.499994755208014 msec\nrounds: 192"
          },
          {
            "name": "Items Limit: (100)",
            "value": 120.38514071477994,
            "unit": "iter/sec",
            "range": "stddev: 0.004344103389010406",
            "extra": "mean: 8.306673016807197 msec\nrounds: 119"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.05484545845673,
            "unit": "iter/sec",
            "range": "stddev: 0.005919439939784724",
            "extra": "mean: 15.13893482089699 msec\nrounds: 67"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.76334305612853,
            "unit": "iter/sec",
            "range": "stddev: 0.0021655106432319315",
            "extra": "mean: 18.60003383636333 msec\nrounds: 55"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.115115292037071,
            "unit": "iter/sec",
            "range": "stddev: 0.010621003755664141",
            "extra": "mean: 70.84603839999394 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 938.3903607315907,
            "unit": "iter/sec",
            "range": "stddev: 0.00007359244258312965",
            "extra": "mean: 1.0656545951946659 msec\nrounds: 541"
          },
          {
            "name": "Collection",
            "value": 922.1566604570784,
            "unit": "iter/sec",
            "range": "stddev: 0.00006798943840767015",
            "extra": "mean: 1.0844144415812575 msec\nrounds: 582"
          },
          {
            "name": "Collections With Model validation",
            "value": 640.854327982863,
            "unit": "iter/sec",
            "range": "stddev: 0.0026280108549693",
            "extra": "mean: 1.5604170188685078 msec\nrounds: 424"
          },
          {
            "name": "Collections",
            "value": 559.0639219950317,
            "unit": "iter/sec",
            "range": "stddev: 0.0000950527057097607",
            "extra": "mean: 1.7887042262206414 msec\nrounds: 389"
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
          "id": "cf55d664edc31c0d103a9783eae8ec5c1059178f",
          "message": "revert to fastapi and update version (#746)\n\n* revert to fastapi and update version\r\n\r\n* fix makefile\r\n\r\n* Bump version: 3.0.0 → 3.0.1\r\n\r\n* Update stac_fastapi/types/setup.py\r\n\r\n* Update CHANGES.md",
          "timestamp": "2024-08-27T14:50:33+02:00",
          "tree_id": "4b588f532c34a3fc8d279ad30566d95febabf5bd",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/cf55d664edc31c0d103a9783eae8ec5c1059178f"
        },
        "date": 1724763126682,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 768.7844799846062,
            "unit": "iter/sec",
            "range": "stddev: 0.00008994613197508618",
            "extra": "mean: 1.300754666665518 msec\nrounds: 303"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 507.9278691314696,
            "unit": "iter/sec",
            "range": "stddev: 0.0000807136276986461",
            "extra": "mean: 1.9687834843753471 msec\nrounds: 384"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 206.04208965241568,
            "unit": "iter/sec",
            "range": "stddev: 0.0037456869738210856",
            "extra": "mean: 4.8533772962939645 msec\nrounds: 162"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 108.68696356952715,
            "unit": "iter/sec",
            "range": "stddev: 0.005923923354425291",
            "extra": "mean: 9.200735462264516 msec\nrounds: 106"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 58.3332263890808,
            "unit": "iter/sec",
            "range": "stddev: 0.008429017223628422",
            "extra": "mean: 17.14288857142979 msec\nrounds: 63"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 48.295527237433426,
            "unit": "iter/sec",
            "range": "stddev: 0.009536071692186917",
            "extra": "mean: 20.705851187496904 msec\nrounds: 16"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.440777836335835,
            "unit": "iter/sec",
            "range": "stddev: 0.016249963649770754",
            "extra": "mean: 87.40664439999932 msec\nrounds: 10"
          },
          {
            "name": "Items Limit: (1)",
            "value": 816.7498132661095,
            "unit": "iter/sec",
            "range": "stddev: 0.00007690374190129167",
            "extra": "mean: 1.224365140655606 msec\nrounds: 519"
          },
          {
            "name": "Items Limit: (10)",
            "value": 540.2980284176821,
            "unit": "iter/sec",
            "range": "stddev: 0.00011817313539363101",
            "extra": "mean: 1.8508303702839746 msec\nrounds: 424"
          },
          {
            "name": "Items Limit: (50)",
            "value": 213.879337075906,
            "unit": "iter/sec",
            "range": "stddev: 0.0007235669262391937",
            "extra": "mean: 4.675533474489399 msec\nrounds: 196"
          },
          {
            "name": "Items Limit: (100)",
            "value": 128.43391903182604,
            "unit": "iter/sec",
            "range": "stddev: 0.0000678496045776883",
            "extra": "mean: 7.786105162392492 msec\nrounds: 117"
          },
          {
            "name": "Items Limit: (200)",
            "value": 69.18226668395677,
            "unit": "iter/sec",
            "range": "stddev: 0.00006646863672701115",
            "extra": "mean: 14.454571206350746 msec\nrounds: 63"
          },
          {
            "name": "Items Limit: (250)",
            "value": 56.550948863424864,
            "unit": "iter/sec",
            "range": "stddev: 0.0002491312922903741",
            "extra": "mean: 17.683169249999345 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.181804581727267,
            "unit": "iter/sec",
            "range": "stddev: 0.010700101481226354",
            "extra": "mean: 70.51288813332425 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 927.507587845481,
            "unit": "iter/sec",
            "range": "stddev: 0.00007172103305714308",
            "extra": "mean: 1.0781582955271691 msec\nrounds: 626"
          },
          {
            "name": "Collection",
            "value": 931.6723130414309,
            "unit": "iter/sec",
            "range": "stddev: 0.00007245556367959532",
            "extra": "mean: 1.073338754411961 msec\nrounds: 623"
          },
          {
            "name": "Collections With Model validation",
            "value": 695.020662130534,
            "unit": "iter/sec",
            "range": "stddev: 0.00007409315967284211",
            "extra": "mean: 1.4388061456109444 msec\nrounds: 467"
          },
          {
            "name": "Collections",
            "value": 573.4844422528747,
            "unit": "iter/sec",
            "range": "stddev: 0.00009623857840720281",
            "extra": "mean: 1.7437264663564416 msec\nrounds: 431"
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
          "id": "3ae8d86741af7370e32807c7e32725c0f51a0a9c",
          "message": "add from_extensions class method to create CollectionSearch extensions classes (#745)\n\n* add from_extensions class method to create CollectionSearch extensions classes\r\n\r\n* Apply suggestions from code review\r\n\r\n* Apply suggestions from code review\r\n\r\n* fix\r\n\r\n* update makefile",
          "timestamp": "2024-09-03T12:59:01+02:00",
          "tree_id": "ef5c22bc2070c2b07f68614fc09e0be33c977bbe",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/3ae8d86741af7370e32807c7e32725c0f51a0a9c"
        },
        "date": 1725361233329,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 715.5543849896936,
            "unit": "iter/sec",
            "range": "stddev: 0.00007432797555385735",
            "extra": "mean: 1.3975178141272984 msec\nrounds: 269"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 493.7982313266242,
            "unit": "iter/sec",
            "range": "stddev: 0.00005847908414903906",
            "extra": "mean: 2.0251186346160632 msec\nrounds: 312"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 198.027791075991,
            "unit": "iter/sec",
            "range": "stddev: 0.004428759606062744",
            "extra": "mean: 5.0497962663041625 msec\nrounds: 184"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 103.10308691034751,
            "unit": "iter/sec",
            "range": "stddev: 0.007711198941404666",
            "extra": "mean: 9.69903064948523 msec\nrounds: 97"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 57.79495480098033,
            "unit": "iter/sec",
            "range": "stddev: 0.009606142189258501",
            "extra": "mean: 17.30254835294097 msec\nrounds: 17"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 48.13090301272703,
            "unit": "iter/sec",
            "range": "stddev: 0.009938276694406238",
            "extra": "mean: 20.776672312496913 msec\nrounds: 16"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.860793491450053,
            "unit": "iter/sec",
            "range": "stddev: 0.017648841742413882",
            "extra": "mean: 84.311391199995 msec\nrounds: 10"
          },
          {
            "name": "Items Limit: (1)",
            "value": 856.3688498601624,
            "unit": "iter/sec",
            "range": "stddev: 0.00006676417005986888",
            "extra": "mean: 1.1677211287674596 msec\nrounds: 365"
          },
          {
            "name": "Items Limit: (10)",
            "value": 528.8157279366201,
            "unit": "iter/sec",
            "range": "stddev: 0.00021296907142395798",
            "extra": "mean: 1.8910178861394467 msec\nrounds: 404"
          },
          {
            "name": "Items Limit: (50)",
            "value": 217.73442106915627,
            "unit": "iter/sec",
            "range": "stddev: 0.0002868646225561574",
            "extra": "mean: 4.592751091396718 msec\nrounds: 186"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.59565223474591,
            "unit": "iter/sec",
            "range": "stddev: 0.000218084612501265",
            "extra": "mean: 7.8991654322038105 msec\nrounds: 118"
          },
          {
            "name": "Items Limit: (200)",
            "value": 68.59902134287759,
            "unit": "iter/sec",
            "range": "stddev: 0.0001902324049315477",
            "extra": "mean: 14.577467439392656 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 56.07643438927399,
            "unit": "iter/sec",
            "range": "stddev: 0.0004600117222076439",
            "extra": "mean: 17.832802867924052 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 14.015653139270542,
            "unit": "iter/sec",
            "range": "stddev: 0.011079948969083086",
            "extra": "mean: 71.348797666667 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 890.2740598177132,
            "unit": "iter/sec",
            "range": "stddev: 0.002066446947365896",
            "extra": "mean: 1.1232496206895588 msec\nrounds: 522"
          },
          {
            "name": "Collection",
            "value": 958.2106350529011,
            "unit": "iter/sec",
            "range": "stddev: 0.00008325565096840313",
            "extra": "mean: 1.043611877616858 msec\nrounds: 621"
          },
          {
            "name": "Collections With Model validation",
            "value": 736.0845233968021,
            "unit": "iter/sec",
            "range": "stddev: 0.00006736028410178205",
            "extra": "mean: 1.3585396353469161 msec\nrounds: 447"
          },
          {
            "name": "Collections",
            "value": 553.1221400628325,
            "unit": "iter/sec",
            "range": "stddev: 0.00009883052369901211",
            "extra": "mean: 1.8079189523789516 msec\nrounds: 21"
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
          "id": "753341f18d6c3d0454efef52d0ff841cfa3215f7",
          "message": "Release/v3.0.2 (#752)\n\n* update changelog\r\n\r\n* Bump version: 3.0.1 → 3.0.2\r\n\r\n* update links",
          "timestamp": "2024-09-23T08:47:38+02:00",
          "tree_id": "91b644e9b3308d6b362e3b8b76195a0a486612c5",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/753341f18d6c3d0454efef52d0ff841cfa3215f7"
        },
        "date": 1727074152829,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 724.1496652669988,
            "unit": "iter/sec",
            "range": "stddev: 0.00011307772878534218",
            "extra": "mean: 1.3809300037876746 msec\nrounds: 264"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 521.4206669674757,
            "unit": "iter/sec",
            "range": "stddev: 0.00010415748437844177",
            "extra": "mean: 1.9178372921347522 msec\nrounds: 267"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 206.80425913618933,
            "unit": "iter/sec",
            "range": "stddev: 0.0053262796157431",
            "extra": "mean: 4.835490352940255 msec\nrounds: 187"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 106.35139383518415,
            "unit": "iter/sec",
            "range": "stddev: 0.009451061478320288",
            "extra": "mean: 9.402791669564097 msec\nrounds: 115"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 58.708060220615415,
            "unit": "iter/sec",
            "range": "stddev: 0.011472733058744265",
            "extra": "mean: 17.03343623076902 msec\nrounds: 13"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 43.503424035713714,
            "unit": "iter/sec",
            "range": "stddev: 0.014801228117814104",
            "extra": "mean: 22.986696384612387 msec\nrounds: 52"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.934316802071535,
            "unit": "iter/sec",
            "range": "stddev: 0.02116736395949941",
            "extra": "mean: 91.45518811111704 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 827.3567440758025,
            "unit": "iter/sec",
            "range": "stddev: 0.00009061243295886038",
            "extra": "mean: 1.208668457905723 msec\nrounds: 487"
          },
          {
            "name": "Items Limit: (10)",
            "value": 536.567765573506,
            "unit": "iter/sec",
            "range": "stddev: 0.00011065154904283986",
            "extra": "mean: 1.8636974938872044 msec\nrounds: 409"
          },
          {
            "name": "Items Limit: (50)",
            "value": 219.60303938327996,
            "unit": "iter/sec",
            "range": "stddev: 0.00009098090931543287",
            "extra": "mean: 4.553671036650221 msec\nrounds: 191"
          },
          {
            "name": "Items Limit: (100)",
            "value": 126.20848465185348,
            "unit": "iter/sec",
            "range": "stddev: 0.00020112930936494914",
            "extra": "mean: 7.923397565215232 msec\nrounds: 115"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.49364659748254,
            "unit": "iter/sec",
            "range": "stddev: 0.0005498625649131306",
            "extra": "mean: 15.505403287880364 msec\nrounds: 66"
          },
          {
            "name": "Items Limit: (250)",
            "value": 54.81074863022526,
            "unit": "iter/sec",
            "range": "stddev: 0.0004429639835625111",
            "extra": "mean: 18.244596634619807 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.350731912221974,
            "unit": "iter/sec",
            "range": "stddev: 0.013109181684509103",
            "extra": "mean: 74.902260533338 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 826.2941721244118,
            "unit": "iter/sec",
            "range": "stddev: 0.0024175003394225456",
            "extra": "mean: 1.2102227435889916 msec\nrounds: 546"
          },
          {
            "name": "Collection",
            "value": 958.1556548102676,
            "unit": "iter/sec",
            "range": "stddev: 0.00007369856151631608",
            "extra": "mean: 1.0436717614509288 msec\nrounds: 524"
          },
          {
            "name": "Collections With Model validation",
            "value": 698.6923622341486,
            "unit": "iter/sec",
            "range": "stddev: 0.00009730832864656019",
            "extra": "mean: 1.4312450715825569 msec\nrounds: 461"
          },
          {
            "name": "Collections",
            "value": 555.7521279391068,
            "unit": "iter/sec",
            "range": "stddev: 0.00007861109137269077",
            "extra": "mean: 1.7993633307501595 msec\nrounds: 387"
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
          "id": "0ce70baa48f2ae91952a30e980431a3209b5c413",
          "message": "Removed `cql2-text` in supported `filter-lang` for `FilterExtensionPostRequest` model (#755)\n\n* Removed `cql2-text` in supported `filter-lang` for `FilterExtensionPostRequest` model\r\n\r\n* update tests",
          "timestamp": "2024-10-01T16:24:12+02:00",
          "tree_id": "384dc51799fc0ae4b1dc548d299582348ebb6eeb",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/0ce70baa48f2ae91952a30e980431a3209b5c413"
        },
        "date": 1727792745797,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 673.4183642319241,
            "unit": "iter/sec",
            "range": "stddev: 0.0001247450182251377",
            "extra": "mean: 1.484960988761515 msec\nrounds: 267"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 503.19175308270326,
            "unit": "iter/sec",
            "range": "stddev: 0.00009213685591407486",
            "extra": "mean: 1.9873139690261232 msec\nrounds: 226"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 194.05376121173774,
            "unit": "iter/sec",
            "range": "stddev: 0.006658185920932306",
            "extra": "mean: 5.153211119205624 msec\nrounds: 151"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 107.55392800175453,
            "unit": "iter/sec",
            "range": "stddev: 0.0090030403803753",
            "extra": "mean: 9.29766135536851 msec\nrounds: 121"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 52.126172254157865,
            "unit": "iter/sec",
            "range": "stddev: 0.01504039031036389",
            "extra": "mean: 19.184220838702284 msec\nrounds: 62"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.230658056949224,
            "unit": "iter/sec",
            "range": "stddev: 0.01658821759415861",
            "extra": "mean: 24.253796740735137 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.823257677600685,
            "unit": "iter/sec",
            "range": "stddev: 0.02754791739390526",
            "extra": "mean: 101.79922311111038 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 814.1404520942975,
            "unit": "iter/sec",
            "range": "stddev: 0.00007491760874702047",
            "extra": "mean: 1.2282892926246285 msec\nrounds: 434"
          },
          {
            "name": "Items Limit: (10)",
            "value": 526.070070912374,
            "unit": "iter/sec",
            "range": "stddev: 0.00011189090473606162",
            "extra": "mean: 1.9008874583297992 msec\nrounds: 384"
          },
          {
            "name": "Items Limit: (50)",
            "value": 197.07183237613685,
            "unit": "iter/sec",
            "range": "stddev: 0.005474938452642172",
            "extra": "mean: 5.074291886074168 msec\nrounds: 158"
          },
          {
            "name": "Items Limit: (100)",
            "value": 112.86947766560813,
            "unit": "iter/sec",
            "range": "stddev: 0.006086350658376522",
            "extra": "mean: 8.859791155963723 msec\nrounds: 109"
          },
          {
            "name": "Items Limit: (200)",
            "value": 61.502209234690085,
            "unit": "iter/sec",
            "range": "stddev: 0.007518942176750403",
            "extra": "mean: 16.25957851666821 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.229936392976825,
            "unit": "iter/sec",
            "range": "stddev: 0.0004896545857308165",
            "extra": "mean: 19.146107942311538 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.122649581728778,
            "unit": "iter/sec",
            "range": "stddev: 0.012823397636253812",
            "extra": "mean: 76.20412278571719 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 887.7797344655438,
            "unit": "iter/sec",
            "range": "stddev: 0.00009796692734825497",
            "extra": "mean: 1.1264055273823237 msec\nrounds: 493"
          },
          {
            "name": "Collection",
            "value": 890.7022854867658,
            "unit": "iter/sec",
            "range": "stddev: 0.00010290071326743095",
            "extra": "mean: 1.1227095925250752 msec\nrounds: 562"
          },
          {
            "name": "Collections With Model validation",
            "value": 609.7822202113957,
            "unit": "iter/sec",
            "range": "stddev: 0.003444582082644517",
            "extra": "mean: 1.6399297435292979 msec\nrounds: 425"
          },
          {
            "name": "Collections",
            "value": 539.0848619400709,
            "unit": "iter/sec",
            "range": "stddev: 0.0002536583865551491",
            "extra": "mean: 1.8549955129535212 msec\nrounds: 386"
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
          "id": "ccbf496201f277be88216e199399909eab4f0412",
          "message": "add `OffsetPaginationExtension` extension (#757)",
          "timestamp": "2024-10-09T09:39:31+08:00",
          "tree_id": "0a9504cd1834e83af8a43ae4c82030ce822c282a",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/ccbf496201f277be88216e199399909eab4f0412"
        },
        "date": 1728438065936,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 746.8101421149921,
            "unit": "iter/sec",
            "range": "stddev: 0.00022171816397675655",
            "extra": "mean: 1.3390284137919788 msec\nrounds: 261"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 519.3918071494238,
            "unit": "iter/sec",
            "range": "stddev: 0.00008927308173092115",
            "extra": "mean: 1.9253287907799246 msec\nrounds: 282"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 211.93498861606173,
            "unit": "iter/sec",
            "range": "stddev: 0.004575275888386122",
            "extra": "mean: 4.718428073297445 msec\nrounds: 191"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 106.6236275603467,
            "unit": "iter/sec",
            "range": "stddev: 0.008521477421955305",
            "extra": "mean: 9.378784260871459 msec\nrounds: 115"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 57.90067586150452,
            "unit": "iter/sec",
            "range": "stddev: 0.01125555085870574",
            "extra": "mean: 17.27095556521567 msec\nrounds: 69"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 44.65307683816343,
            "unit": "iter/sec",
            "range": "stddev: 0.014403949738911681",
            "extra": "mean: 22.394873339284313 msec\nrounds: 56"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.33290006481177,
            "unit": "iter/sec",
            "range": "stddev: 0.020052078708322506",
            "extra": "mean: 88.23866744444014 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 789.9956839954252,
            "unit": "iter/sec",
            "range": "stddev: 0.00009411696904369037",
            "extra": "mean: 1.265829700413643 msec\nrounds: 484"
          },
          {
            "name": "Items Limit: (10)",
            "value": 518.1411763719743,
            "unit": "iter/sec",
            "range": "stddev: 0.00007836461984727883",
            "extra": "mean: 1.929975932432165 msec\nrounds: 370"
          },
          {
            "name": "Items Limit: (50)",
            "value": 208.04937576322988,
            "unit": "iter/sec",
            "range": "stddev: 0.0007227374788327698",
            "extra": "mean: 4.806551311829207 msec\nrounds: 186"
          },
          {
            "name": "Items Limit: (100)",
            "value": 121.86174358565,
            "unit": "iter/sec",
            "range": "stddev: 0.00025818269884548243",
            "extra": "mean: 8.20602077876191 msec\nrounds: 113"
          },
          {
            "name": "Items Limit: (200)",
            "value": 66.24596360220528,
            "unit": "iter/sec",
            "range": "stddev: 0.00018283966199339038",
            "extra": "mean: 15.09525932787112 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.34178812426273,
            "unit": "iter/sec",
            "range": "stddev: 0.004987219639244853",
            "extra": "mean: 19.105193686274845 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.411548250857226,
            "unit": "iter/sec",
            "range": "stddev: 0.010710374338228992",
            "extra": "mean: 74.56260688888644 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 904.0742854275375,
            "unit": "iter/sec",
            "range": "stddev: 0.00005984427981837568",
            "extra": "mean: 1.1061037971311165 msec\nrounds: 488"
          },
          {
            "name": "Collection",
            "value": 974.4178679436841,
            "unit": "iter/sec",
            "range": "stddev: 0.00005821620290278133",
            "extra": "mean: 1.0262537591909127 msec\nrounds: 544"
          },
          {
            "name": "Collections With Model validation",
            "value": 711.2550767806813,
            "unit": "iter/sec",
            "range": "stddev: 0.00005966357652935534",
            "extra": "mean: 1.4059653598906465 msec\nrounds: 364"
          },
          {
            "name": "Collections",
            "value": 506.7501643280679,
            "unit": "iter/sec",
            "range": "stddev: 0.0025900948957742263",
            "extra": "mean: 1.973359004877607 msec\nrounds: 410"
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
          "id": "72ec630a4e3c297f053e354bbd2352caef6940a1",
          "message": "Release/v3.0.3 (#758)\n\n* update changelog\r\n\r\n* Bump version: 3.0.2 → 3.0.3\r\n\r\n* Update CHANGES.md",
          "timestamp": "2024-10-09T14:18:18+02:00",
          "tree_id": "3db8aac1deb5c09b3f4820b43fa625988682cc60",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/72ec630a4e3c297f053e354bbd2352caef6940a1"
        },
        "date": 1728476390490,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 715.6940455978727,
            "unit": "iter/sec",
            "range": "stddev: 0.00011891513746969937",
            "extra": "mean: 1.3972451023602206 msec\nrounds: 254"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 522.5077231863568,
            "unit": "iter/sec",
            "range": "stddev: 0.00014619272727412757",
            "extra": "mean: 1.9138473090920067 msec\nrounds: 330"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 210.6934565977829,
            "unit": "iter/sec",
            "range": "stddev: 0.004660191261152495",
            "extra": "mean: 4.746231877096286 msec\nrounds: 179"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 110.50216506941425,
            "unit": "iter/sec",
            "range": "stddev: 0.008519827180891034",
            "extra": "mean: 9.049596443398453 msec\nrounds: 106"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 62.26767615258188,
            "unit": "iter/sec",
            "range": "stddev: 0.009045960657226928",
            "extra": "mean: 16.059696808815882 msec\nrounds: 68"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 46.389824664899415,
            "unit": "iter/sec",
            "range": "stddev: 0.01349059862702512",
            "extra": "mean: 21.55645138181874 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.339884313329584,
            "unit": "iter/sec",
            "range": "stddev: 0.02390234674593938",
            "extra": "mean: 96.7128808888952 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 780.7151995062794,
            "unit": "iter/sec",
            "range": "stddev: 0.00008794335312531625",
            "extra": "mean: 1.2808768173495215 msec\nrounds: 438"
          },
          {
            "name": "Items Limit: (10)",
            "value": 528.3916118147445,
            "unit": "iter/sec",
            "range": "stddev: 0.0002234325312954255",
            "extra": "mean: 1.8925357209315479 msec\nrounds: 387"
          },
          {
            "name": "Items Limit: (50)",
            "value": 217.11549055743342,
            "unit": "iter/sec",
            "range": "stddev: 0.0001289858920969564",
            "extra": "mean: 4.605843633876831 msec\nrounds: 183"
          },
          {
            "name": "Items Limit: (100)",
            "value": 117.13666368631722,
            "unit": "iter/sec",
            "range": "stddev: 0.005418520431240365",
            "extra": "mean: 8.537036727270307 msec\nrounds: 99"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.8923691271944,
            "unit": "iter/sec",
            "range": "stddev: 0.00619452382134999",
            "extra": "mean: 15.410132400004036 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 53.66326399046555,
            "unit": "iter/sec",
            "range": "stddev: 0.004306825080563903",
            "extra": "mean: 18.63472188679525 msec\nrounds: 53"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.883856655049051,
            "unit": "iter/sec",
            "range": "stddev: 0.010729396233091775",
            "extra": "mean: 72.02609655555155 msec\nrounds: 9"
          },
          {
            "name": "Collection With Model validation",
            "value": 905.2601544508502,
            "unit": "iter/sec",
            "range": "stddev: 0.000074126393732519",
            "extra": "mean: 1.1046548277678487 msec\nrounds: 569"
          },
          {
            "name": "Collection",
            "value": 898.0718050705876,
            "unit": "iter/sec",
            "range": "stddev: 0.00005949743728723718",
            "extra": "mean: 1.113496709677241 msec\nrounds: 620"
          },
          {
            "name": "Collections With Model validation",
            "value": 681.6585246111559,
            "unit": "iter/sec",
            "range": "stddev: 0.00008181109547672007",
            "extra": "mean: 1.467010187498848 msec\nrounds: 480"
          },
          {
            "name": "Collections",
            "value": 560.2483546898096,
            "unit": "iter/sec",
            "range": "stddev: 0.00009873035884071386",
            "extra": "mean: 1.7849226894270238 msec\nrounds: 454"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "committer": {
            "email": "vincent.sarago@gmail.com",
            "name": "vincentsarago",
            "username": "vincentsarago"
          },
          "distinct": true,
          "id": "8ed4e8b7e1edd6057f6f3dfedc23a9943d114d06",
          "message": "update links to pypi",
          "timestamp": "2024-10-09T14:36:57+02:00",
          "tree_id": "13e3c86e43fac2cde95a8dce0c3f8c8ffa5bcf5e",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/8ed4e8b7e1edd6057f6f3dfedc23a9943d114d06"
        },
        "date": 1728477529414,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 716.7286143866942,
            "unit": "iter/sec",
            "range": "stddev: 0.00012048701620489683",
            "extra": "mean: 1.3952282355235692 msec\nrounds: 259"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 503.51531900317815,
            "unit": "iter/sec",
            "range": "stddev: 0.0000709169934212576",
            "extra": "mean: 1.9860368935342922 msec\nrounds: 263"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 214.78823096528683,
            "unit": "iter/sec",
            "range": "stddev: 0.004255491499489767",
            "extra": "mean: 4.6557485738667665 msec\nrounds: 176"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 102.22430491302488,
            "unit": "iter/sec",
            "range": "stddev: 0.008822683575192176",
            "extra": "mean: 9.782409387384208 msec\nrounds: 111"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 48.68009793821641,
            "unit": "iter/sec",
            "range": "stddev: 0.01642370705894314",
            "extra": "mean: 20.542275844826268 msec\nrounds: 58"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 41.75428923469115,
            "unit": "iter/sec",
            "range": "stddev: 0.016038173290426984",
            "extra": "mean: 23.949635314811196 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.694768946554882,
            "unit": "iter/sec",
            "range": "stddev: 0.028888019150501414",
            "extra": "mean: 103.14840977776561 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 778.7833096017895,
            "unit": "iter/sec",
            "range": "stddev: 0.00011701904894149156",
            "extra": "mean: 1.2840542262151506 msec\nrounds: 473"
          },
          {
            "name": "Items Limit: (10)",
            "value": 515.891640975257,
            "unit": "iter/sec",
            "range": "stddev: 0.0001735274474352503",
            "extra": "mean: 1.9383915546868913 msec\nrounds: 384"
          },
          {
            "name": "Items Limit: (50)",
            "value": 190.7395628572974,
            "unit": "iter/sec",
            "range": "stddev: 0.0056151817109252366",
            "extra": "mean: 5.242750822220109 msec\nrounds: 180"
          },
          {
            "name": "Items Limit: (100)",
            "value": 110.90412560147908,
            "unit": "iter/sec",
            "range": "stddev: 0.006879786968083436",
            "extra": "mean: 9.016797117118818 msec\nrounds: 111"
          },
          {
            "name": "Items Limit: (200)",
            "value": 60.79031543809971,
            "unit": "iter/sec",
            "range": "stddev: 0.0008767832191451392",
            "extra": "mean: 16.44998866666943 msec\nrounds: 12"
          },
          {
            "name": "Items Limit: (250)",
            "value": 47.218804557809946,
            "unit": "iter/sec",
            "range": "stddev: 0.010608968092779345",
            "extra": "mean: 21.17800332652854 msec\nrounds: 49"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.184941761302234,
            "unit": "iter/sec",
            "range": "stddev: 0.0006146909379765036",
            "extra": "mean: 75.84409685714328 msec\nrounds: 7"
          },
          {
            "name": "Collection With Model validation",
            "value": 966.116261150436,
            "unit": "iter/sec",
            "range": "stddev: 0.00007128240119153832",
            "extra": "mean: 1.0350721131732281 msec\nrounds: 539"
          },
          {
            "name": "Collection",
            "value": 895.852410745873,
            "unit": "iter/sec",
            "range": "stddev: 0.00008545858647513765",
            "extra": "mean: 1.1162552983112646 msec\nrounds: 533"
          },
          {
            "name": "Collections With Model validation",
            "value": 639.4093889952966,
            "unit": "iter/sec",
            "range": "stddev: 0.0030962334397050917",
            "extra": "mean: 1.5639432532751811 msec\nrounds: 458"
          },
          {
            "name": "Collections",
            "value": 554.6808456586076,
            "unit": "iter/sec",
            "range": "stddev: 0.00009801280620575923",
            "extra": "mean: 1.802838529267469 msec\nrounds: 410"
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
          "id": "3c4ce2e0b8616d388b94a9cfb2a28e5d44ada29a",
          "message": "add numberMatched/Returned properties in model (#759)",
          "timestamp": "2024-10-11T11:27:13+02:00",
          "tree_id": "c72c72bb637b56c6e85cf81702459af0e08c2587",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/3c4ce2e0b8616d388b94a9cfb2a28e5d44ada29a"
        },
        "date": 1728638936784,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 732.4582071285761,
            "unit": "iter/sec",
            "range": "stddev: 0.00012562055473073697",
            "extra": "mean: 1.3652656086963055 msec\nrounds: 276"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 526.882666918463,
            "unit": "iter/sec",
            "range": "stddev: 0.00006366459922985452",
            "extra": "mean: 1.8979557741928026 msec\nrounds: 248"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 200.7473644248225,
            "unit": "iter/sec",
            "range": "stddev: 0.00563096866900462",
            "extra": "mean: 4.981385448646765 msec\nrounds: 185"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 100.31289682372119,
            "unit": "iter/sec",
            "range": "stddev: 0.010336320847306586",
            "extra": "mean: 9.968807916665885 msec\nrounds: 120"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 50.65090515851327,
            "unit": "iter/sec",
            "range": "stddev: 0.015667056981526158",
            "extra": "mean: 19.742983800002687 msec\nrounds: 65"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 40.72439591642806,
            "unit": "iter/sec",
            "range": "stddev: 0.017486077780785834",
            "extra": "mean: 24.55530591668283 msec\nrounds: 12"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 9.335556216398771,
            "unit": "iter/sec",
            "range": "stddev: 0.02656982160840437",
            "extra": "mean: 107.11734542858916 msec\nrounds: 7"
          },
          {
            "name": "Items Limit: (1)",
            "value": 818.3188190728399,
            "unit": "iter/sec",
            "range": "stddev: 0.000096070240525775",
            "extra": "mean: 1.2220176008331398 msec\nrounds: 481"
          },
          {
            "name": "Items Limit: (10)",
            "value": 530.2067161107705,
            "unit": "iter/sec",
            "range": "stddev: 0.00009484550143701348",
            "extra": "mean: 1.8860568333334364 msec\nrounds: 378"
          },
          {
            "name": "Items Limit: (50)",
            "value": 197.5826632218796,
            "unit": "iter/sec",
            "range": "stddev: 0.005260932762537773",
            "extra": "mean: 5.061172795697307 msec\nrounds: 186"
          },
          {
            "name": "Items Limit: (100)",
            "value": 113.96669813308061,
            "unit": "iter/sec",
            "range": "stddev: 0.006051229427690893",
            "extra": "mean: 8.774493043856419 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 59.53645862236759,
            "unit": "iter/sec",
            "range": "stddev: 0.00916365664900033",
            "extra": "mean: 16.796430676921457 msec\nrounds: 65"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.61282000656621,
            "unit": "iter/sec",
            "range": "stddev: 0.00040739189246964886",
            "extra": "mean: 19.006774392157606 msec\nrounds: 51"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.330101926195397,
            "unit": "iter/sec",
            "range": "stddev: 0.011654203725365344",
            "extra": "mean: 75.0181810714342 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 952.5298606552225,
            "unit": "iter/sec",
            "range": "stddev: 0.00010236565912152815",
            "extra": "mean: 1.049835854292404 msec\nrounds: 501"
          },
          {
            "name": "Collection",
            "value": 960.4926149734044,
            "unit": "iter/sec",
            "range": "stddev: 0.00007030551887228512",
            "extra": "mean: 1.0411324193551341 msec\nrounds: 558"
          },
          {
            "name": "Collections With Model validation",
            "value": 697.3546267745983,
            "unit": "iter/sec",
            "range": "stddev: 0.00006898348045026788",
            "extra": "mean: 1.4339906291655307 msec\nrounds: 480"
          },
          {
            "name": "Collections",
            "value": 552.9369439781915,
            "unit": "iter/sec",
            "range": "stddev: 0.000100285226695165",
            "extra": "mean: 1.8085244816621282 msec\nrounds: 409"
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
          "id": "ebb987c1e440f99d9a8c27ac431b57300ad8e7c1",
          "message": "add numberMatch and numberReturned in Collections model (#760)\n\n* add numberMatch and numberReturned in Collections model\r\n\r\n* update stac-pydantic version",
          "timestamp": "2024-10-14T15:32:23+02:00",
          "tree_id": "3a46db8d97b1f5b8e78d1e6b5c7332e9bda89f63",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/ebb987c1e440f99d9a8c27ac431b57300ad8e7c1"
        },
        "date": 1728912835910,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 784.8620130243633,
            "unit": "iter/sec",
            "range": "stddev: 0.0001020779021331461",
            "extra": "mean: 1.2741093127269985 msec\nrounds: 275"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 544.4205277426792,
            "unit": "iter/sec",
            "range": "stddev: 0.000055030786657378994",
            "extra": "mean: 1.8368153826717035 msec\nrounds: 277"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 212.12517515195933,
            "unit": "iter/sec",
            "range": "stddev: 0.004341286309291349",
            "extra": "mean: 4.7141976395948 msec\nrounds: 197"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 114.67489840152204,
            "unit": "iter/sec",
            "range": "stddev: 0.007133049699401312",
            "extra": "mean: 8.720304215998567 msec\nrounds: 125"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 59.13940005853222,
            "unit": "iter/sec",
            "range": "stddev: 0.011081433745344874",
            "extra": "mean: 16.909200955881644 msec\nrounds: 68"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 45.20373046399438,
            "unit": "iter/sec",
            "range": "stddev: 0.013904147137148245",
            "extra": "mean: 22.122068018180908 msec\nrounds: 55"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.597374311673743,
            "unit": "iter/sec",
            "range": "stddev: 0.01913309305745997",
            "extra": "mean: 86.22641411111607 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 799.6958614032127,
            "unit": "iter/sec",
            "range": "stddev: 0.00009570778399151897",
            "extra": "mean: 1.2504753972908114 msec\nrounds: 443"
          },
          {
            "name": "Items Limit: (10)",
            "value": 549.4668806656964,
            "unit": "iter/sec",
            "range": "stddev: 0.00007005175879439239",
            "extra": "mean: 1.8199459060907703 msec\nrounds: 394"
          },
          {
            "name": "Items Limit: (50)",
            "value": 219.99945783146282,
            "unit": "iter/sec",
            "range": "stddev: 0.00016221694735483043",
            "extra": "mean: 4.5454657473114315 msec\nrounds: 186"
          },
          {
            "name": "Items Limit: (100)",
            "value": 117.74807437109813,
            "unit": "iter/sec",
            "range": "stddev: 0.004872450758905183",
            "extra": "mean: 8.492707887930056 msec\nrounds: 116"
          },
          {
            "name": "Items Limit: (200)",
            "value": 67.94554969346515,
            "unit": "iter/sec",
            "range": "stddev: 0.00013596655562716866",
            "extra": "mean: 14.717667375000687 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (250)",
            "value": 52.493721561613704,
            "unit": "iter/sec",
            "range": "stddev: 0.007085806926722921",
            "extra": "mean: 19.049897211541104 msec\nrounds: 52"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 13.970742303819188,
            "unit": "iter/sec",
            "range": "stddev: 0.009608402500578359",
            "extra": "mean: 71.57815799999615 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 992.7810577214774,
            "unit": "iter/sec",
            "range": "stddev: 0.0000734880374916109",
            "extra": "mean: 1.007271434343329 msec\nrounds: 594"
          },
          {
            "name": "Collection",
            "value": 892.3140297100916,
            "unit": "iter/sec",
            "range": "stddev: 0.0023383894269480596",
            "extra": "mean: 1.1206816957981653 msec\nrounds: 595"
          },
          {
            "name": "Collections With Model validation",
            "value": 685.8164546216566,
            "unit": "iter/sec",
            "range": "stddev: 0.00010085017113926651",
            "extra": "mean: 1.4581160793986323 msec\nrounds: 466"
          },
          {
            "name": "Collections",
            "value": 572.7726485374136,
            "unit": "iter/sec",
            "range": "stddev: 0.00006626176181537628",
            "extra": "mean: 1.7458934230772365 msec\nrounds: 338"
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
          "id": "8235d919b3ab742838d628653f14a54ae694cfe6",
          "message": "update stac-version (#762)",
          "timestamp": "2024-10-15T13:20:47+02:00",
          "tree_id": "3bb379676cb1c9cd62e35b716e9d2279f05978c1",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/8235d919b3ab742838d628653f14a54ae694cfe6"
        },
        "date": 1728991349197,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 692.8658003042927,
            "unit": "iter/sec",
            "range": "stddev: 0.00011033842065483188",
            "extra": "mean: 1.4432809348662035 msec\nrounds: 261"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 505.8537856482702,
            "unit": "iter/sec",
            "range": "stddev: 0.0003360672501903728",
            "extra": "mean: 1.9768558195496417 msec\nrounds: 266"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 205.64804586502632,
            "unit": "iter/sec",
            "range": "stddev: 0.004516164113466296",
            "extra": "mean: 4.862676889506323 msec\nrounds: 181"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 102.73146996310723,
            "unit": "iter/sec",
            "range": "stddev: 0.008824012477236147",
            "extra": "mean: 9.734115557376125 msec\nrounds: 122"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 54.54196697625351,
            "unit": "iter/sec",
            "range": "stddev: 0.01323125203489931",
            "extra": "mean: 18.334505619047075 msec\nrounds: 63"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 42.811025629354305,
            "unit": "iter/sec",
            "range": "stddev: 0.015595081266995244",
            "extra": "mean: 23.358468649121278 msec\nrounds: 57"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 10.53629315384048,
            "unit": "iter/sec",
            "range": "stddev: 0.024236063182710238",
            "extra": "mean: 94.91003955556228 msec\nrounds: 9"
          },
          {
            "name": "Items Limit: (1)",
            "value": 848.5018503908877,
            "unit": "iter/sec",
            "range": "stddev: 0.00008714037262476546",
            "extra": "mean: 1.1785478128766838 msec\nrounds: 497"
          },
          {
            "name": "Items Limit: (10)",
            "value": 546.4264489837495,
            "unit": "iter/sec",
            "range": "stddev: 0.00007874172456447951",
            "extra": "mean: 1.8300724678679299 msec\nrounds: 389"
          },
          {
            "name": "Items Limit: (50)",
            "value": 218.41448913791737,
            "unit": "iter/sec",
            "range": "stddev: 0.00013776185648820102",
            "extra": "mean: 4.578450834223512 msec\nrounds: 187"
          },
          {
            "name": "Items Limit: (100)",
            "value": 116.02157184537118,
            "unit": "iter/sec",
            "range": "stddev: 0.004966856186070514",
            "extra": "mean: 8.619086813724254 msec\nrounds: 102"
          },
          {
            "name": "Items Limit: (200)",
            "value": 61.30274674123268,
            "unit": "iter/sec",
            "range": "stddev: 0.008758343876888999",
            "extra": "mean: 16.312482770488856 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (250)",
            "value": 50.72951436082937,
            "unit": "iter/sec",
            "range": "stddev: 0.006448303612156948",
            "extra": "mean: 19.712390560003996 msec\nrounds: 50"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 12.681093925810275,
            "unit": "iter/sec",
            "range": "stddev: 0.019767866524556327",
            "extra": "mean: 78.85755013332603 msec\nrounds: 15"
          },
          {
            "name": "Collection With Model validation",
            "value": 945.3583070712316,
            "unit": "iter/sec",
            "range": "stddev: 0.00008355021514084181",
            "extra": "mean: 1.0577999817847386 msec\nrounds: 549"
          },
          {
            "name": "Collection",
            "value": 908.8784503403086,
            "unit": "iter/sec",
            "range": "stddev: 0.00009923004057534733",
            "extra": "mean: 1.1002571351819082 msec\nrounds: 577"
          },
          {
            "name": "Collections With Model validation",
            "value": 669.099846978664,
            "unit": "iter/sec",
            "range": "stddev: 0.00009335875275363205",
            "extra": "mean: 1.4945452528729806 msec\nrounds: 435"
          },
          {
            "name": "Collections",
            "value": 553.6083148040431,
            "unit": "iter/sec",
            "range": "stddev: 0.00012557932770099046",
            "extra": "mean: 1.8063312512818077 msec\nrounds: 390"
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
          "id": "4491fa1ee384cd3e789e30aaa1252cdbb2ea3246",
          "message": "update CORS documentation (#764)",
          "timestamp": "2024-10-17T13:56:03+02:00",
          "tree_id": "62cbb7d3d1b5a8d8f8ebf16a51a89529ba93a7fc",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/4491fa1ee384cd3e789e30aaa1252cdbb2ea3246"
        },
        "date": 1729166257321,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 742.2336758872389,
            "unit": "iter/sec",
            "range": "stddev: 0.0001133762340437677",
            "extra": "mean: 1.3472845984852906 msec\nrounds: 264"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 541.0344296777928,
            "unit": "iter/sec",
            "range": "stddev: 0.000050948616146760736",
            "extra": "mean: 1.8483112074688839 msec\nrounds: 241"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 200.91360846714582,
            "unit": "iter/sec",
            "range": "stddev: 0.006321526370690734",
            "extra": "mean: 4.977263648935577 msec\nrounds: 188"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 96.57001131605993,
            "unit": "iter/sec",
            "range": "stddev: 0.01128495196743535",
            "extra": "mean: 10.355181555557056 msec\nrounds: 108"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 48.77697915688532,
            "unit": "iter/sec",
            "range": "stddev: 0.01621766690541393",
            "extra": "mean: 20.501474615384023 msec\nrounds: 65"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 37.73471184683318,
            "unit": "iter/sec",
            "range": "stddev: 0.01943718520288924",
            "extra": "mean: 26.50079862962895 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 8.973040052510713,
            "unit": "iter/sec",
            "range": "stddev: 0.026764894404178476",
            "extra": "mean: 111.44494999999401 msec\nrounds: 15"
          },
          {
            "name": "Items Limit: (1)",
            "value": 815.8713029785507,
            "unit": "iter/sec",
            "range": "stddev: 0.00009707371778030177",
            "extra": "mean: 1.2256835071281946 msec\nrounds: 491"
          },
          {
            "name": "Items Limit: (10)",
            "value": 531.7718871096689,
            "unit": "iter/sec",
            "range": "stddev: 0.00007819428876973671",
            "extra": "mean: 1.8805055781253948 msec\nrounds: 384"
          },
          {
            "name": "Items Limit: (50)",
            "value": 194.73333765207576,
            "unit": "iter/sec",
            "range": "stddev: 0.005555628322950753",
            "extra": "mean: 5.135227547872004 msec\nrounds: 188"
          },
          {
            "name": "Items Limit: (100)",
            "value": 110.45509226540764,
            "unit": "iter/sec",
            "range": "stddev: 0.007071013091981259",
            "extra": "mean: 9.053453122805278 msec\nrounds: 114"
          },
          {
            "name": "Items Limit: (200)",
            "value": 57.75003879840369,
            "unit": "iter/sec",
            "range": "stddev: 0.009607144700018309",
            "extra": "mean: 17.316005682538897 msec\nrounds: 63"
          },
          {
            "name": "Items Limit: (250)",
            "value": 51.48894361101517,
            "unit": "iter/sec",
            "range": "stddev: 0.00039667251956908425",
            "extra": "mean: 19.42164530612097 msec\nrounds: 49"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 12.562602149714582,
            "unit": "iter/sec",
            "range": "stddev: 0.018028863707717075",
            "extra": "mean: 79.60134278571574 msec\nrounds: 14"
          },
          {
            "name": "Collection With Model validation",
            "value": 946.3724019513985,
            "unit": "iter/sec",
            "range": "stddev: 0.0001082352836837203",
            "extra": "mean: 1.0566664855589856 msec\nrounds: 554"
          },
          {
            "name": "Collection",
            "value": 886.5314429842015,
            "unit": "iter/sec",
            "range": "stddev: 0.00009047451411313931",
            "extra": "mean: 1.1279915765128936 msec\nrounds: 562"
          },
          {
            "name": "Collections With Model validation",
            "value": 660.6688312872672,
            "unit": "iter/sec",
            "range": "stddev: 0.00008972378764649608",
            "extra": "mean: 1.513617644185771 msec\nrounds: 430"
          },
          {
            "name": "Collections",
            "value": 499.0802510285978,
            "unit": "iter/sec",
            "range": "stddev: 0.0034701634964914583",
            "extra": "mean: 2.003685775862726 msec\nrounds: 406"
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
          "id": "3a9aae60dc2149b492be3534151d33fd3791e51d",
          "message": "add python 3.13 support (#770)",
          "timestamp": "2025-01-06T14:46:24+01:00",
          "tree_id": "d7bbf46bcad6de893c560a8fe0f28cb5b895fcc9",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/3a9aae60dc2149b492be3534151d33fd3791e51d"
        },
        "date": 1736171287769,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 721.4670102324123,
            "unit": "iter/sec",
            "range": "stddev: 0.00010156668528159064",
            "extra": "mean: 1.386064762237516 msec\nrounds: 286"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 499.36236952205877,
            "unit": "iter/sec",
            "range": "stddev: 0.0003656300162177702",
            "extra": "mean: 2.002553778645962 msec\nrounds: 384"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 207.06949516535147,
            "unit": "iter/sec",
            "range": "stddev: 0.005568154371397801",
            "extra": "mean: 4.829296556701742 msec\nrounds: 194"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 123.04420286213019,
            "unit": "iter/sec",
            "range": "stddev: 0.006493756507001413",
            "extra": "mean: 8.12716061983424 msec\nrounds: 121"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 73.99181044898283,
            "unit": "iter/sec",
            "range": "stddev: 0.0007040661576074486",
            "extra": "mean: 13.515009214289973 msec\nrounds: 14"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 55.249236568153975,
            "unit": "iter/sec",
            "range": "stddev: 0.010492955729586211",
            "extra": "mean: 18.099797610170175 msec\nrounds: 59"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.893746003937911,
            "unit": "iter/sec",
            "range": "stddev: 0.025658034429044654",
            "extra": "mean: 84.07780018750266 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (1)",
            "value": 785.5609797313795,
            "unit": "iter/sec",
            "range": "stddev: 0.00021279498816891912",
            "extra": "mean: 1.2729756515426052 msec\nrounds: 551"
          },
          {
            "name": "Items Limit: (10)",
            "value": 551.3847728388339,
            "unit": "iter/sec",
            "range": "stddev: 0.00010290581587807595",
            "extra": "mean: 1.8136155535297913 msec\nrounds: 439"
          },
          {
            "name": "Items Limit: (50)",
            "value": 233.78144722240117,
            "unit": "iter/sec",
            "range": "stddev: 0.00009343925685088564",
            "extra": "mean: 4.277499399037765 msec\nrounds: 208"
          },
          {
            "name": "Items Limit: (100)",
            "value": 138.70822533862636,
            "unit": "iter/sec",
            "range": "stddev: 0.000151813401758521",
            "extra": "mean: 7.209377796873362 msec\nrounds: 128"
          },
          {
            "name": "Items Limit: (200)",
            "value": 75.532004864974,
            "unit": "iter/sec",
            "range": "stddev: 0.00032220274527974265",
            "extra": "mean: 13.23942084931634 msec\nrounds: 73"
          },
          {
            "name": "Items Limit: (250)",
            "value": 57.220140844903945,
            "unit": "iter/sec",
            "range": "stddev: 0.008254548952163971",
            "extra": "mean: 17.476363833331256 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 15.479660844538778,
            "unit": "iter/sec",
            "range": "stddev: 0.013360949359023306",
            "extra": "mean: 64.60089856250306 msec\nrounds: 16"
          },
          {
            "name": "Collection With Model validation",
            "value": 957.5555453184398,
            "unit": "iter/sec",
            "range": "stddev: 0.00008525295722659344",
            "extra": "mean: 1.0443258408236205 msec\nrounds: 534"
          },
          {
            "name": "Collection",
            "value": 931.7006107443716,
            "unit": "iter/sec",
            "range": "stddev: 0.0001669905677941115",
            "extra": "mean: 1.0733061548613363 msec\nrounds: 607"
          },
          {
            "name": "Collections With Model validation",
            "value": 686.999128162607,
            "unit": "iter/sec",
            "range": "stddev: 0.00015839420830725812",
            "extra": "mean: 1.4556059229281997 msec\nrounds: 519"
          },
          {
            "name": "Collections",
            "value": 565.3498366726163,
            "unit": "iter/sec",
            "range": "stddev: 0.00009064968743843614",
            "extra": "mean: 1.7688162888407832 msec\nrounds: 457"
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
          "id": "47eac1f6115f8ce42f13106c93477587cecb1c53",
          "message": "feature: add root_path settings to the default fastapi application (#769)",
          "timestamp": "2025-01-06T15:19:08+01:00",
          "tree_id": "bb72a2ce86473858ae1b931bca9925778f646c84",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/47eac1f6115f8ce42f13106c93477587cecb1c53"
        },
        "date": 1736173255836,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 716.8918489135242,
            "unit": "iter/sec",
            "range": "stddev: 0.00007926849909389806",
            "extra": "mean: 1.3949105454547106 msec\nrounds: 297"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 525.7728525788791,
            "unit": "iter/sec",
            "range": "stddev: 0.00008560650626725099",
            "extra": "mean: 1.9019620261774068 msec\nrounds: 382"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 210.1563795591053,
            "unit": "iter/sec",
            "range": "stddev: 0.0035585961767953178",
            "extra": "mean: 4.758361378788198 msec\nrounds: 198"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 138.91728163155585,
            "unit": "iter/sec",
            "range": "stddev: 0.00010866292040099158",
            "extra": "mean: 7.198528421051713 msec\nrounds: 19"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 70.95708648994001,
            "unit": "iter/sec",
            "range": "stddev: 0.007069410542127157",
            "extra": "mean: 14.093025086955562 msec\nrounds: 69"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 58.04245082326512,
            "unit": "iter/sec",
            "range": "stddev: 0.00832423604596729",
            "extra": "mean: 17.2287693888896 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 15.430065354273369,
            "unit": "iter/sec",
            "range": "stddev: 0.011322164501543523",
            "extra": "mean: 64.80853949999954 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (1)",
            "value": 824.8323370277152,
            "unit": "iter/sec",
            "range": "stddev: 0.00007808116560947282",
            "extra": "mean: 1.2123675989759346 msec\nrounds: 586"
          },
          {
            "name": "Items Limit: (10)",
            "value": 500.535819859818,
            "unit": "iter/sec",
            "range": "stddev: 0.0003722495053596057",
            "extra": "mean: 1.9978590149253732 msec\nrounds: 402"
          },
          {
            "name": "Items Limit: (50)",
            "value": 224.87942929177012,
            "unit": "iter/sec",
            "range": "stddev: 0.0006677106098420708",
            "extra": "mean: 4.446827364998995 msec\nrounds: 200"
          },
          {
            "name": "Items Limit: (100)",
            "value": 141.12010751914758,
            "unit": "iter/sec",
            "range": "stddev: 0.0000944916755701289",
            "extra": "mean: 7.08616240151544 msec\nrounds: 132"
          },
          {
            "name": "Items Limit: (200)",
            "value": 76.31248677467873,
            "unit": "iter/sec",
            "range": "stddev: 0.00016423300945649127",
            "extra": "mean: 13.104015375001646 msec\nrounds: 72"
          },
          {
            "name": "Items Limit: (250)",
            "value": 59.254221509242804,
            "unit": "iter/sec",
            "range": "stddev: 0.006103892176214354",
            "extra": "mean: 16.87643469999879 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 15.83000016073968,
            "unit": "iter/sec",
            "range": "stddev: 0.01156640031063667",
            "extra": "mean: 63.171193294117664 msec\nrounds: 17"
          },
          {
            "name": "Collection With Model validation",
            "value": 936.5158540291919,
            "unit": "iter/sec",
            "range": "stddev: 0.00008932282882879476",
            "extra": "mean: 1.0677875827704133 msec\nrounds: 592"
          },
          {
            "name": "Collection",
            "value": 960.1832269440047,
            "unit": "iter/sec",
            "range": "stddev: 0.00008741766140544924",
            "extra": "mean: 1.0414678906469976 msec\nrounds: 695"
          },
          {
            "name": "Collections With Model validation",
            "value": 684.2665470853843,
            "unit": "iter/sec",
            "range": "stddev: 0.00015943345731300374",
            "extra": "mean: 1.4614188056678705 msec\nrounds: 494"
          },
          {
            "name": "Collections",
            "value": 592.3956290972721,
            "unit": "iter/sec",
            "range": "stddev: 0.00020713219465117296",
            "extra": "mean: 1.688061070814887 msec\nrounds: 466"
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
          "id": "c3b15c7d0dcd6e3e4be0230050671ad31c925984",
          "message": "add more datetime tests - issue768 (#771)",
          "timestamp": "2025-01-06T18:20:19+01:00",
          "tree_id": "963a9aa5b0960ed9a762cd5855260dbd5c6e1f53",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/c3b15c7d0dcd6e3e4be0230050671ad31c925984"
        },
        "date": 1736184123918,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 720.6571609470348,
            "unit": "iter/sec",
            "range": "stddev: 0.00009865640110448804",
            "extra": "mean: 1.3876223732875608 msec\nrounds: 292"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 494.26511033998344,
            "unit": "iter/sec",
            "range": "stddev: 0.00008455855089144909",
            "extra": "mean: 2.023205723163716 msec\nrounds: 354"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 217.9131056904388,
            "unit": "iter/sec",
            "range": "stddev: 0.003704101854085014",
            "extra": "mean: 4.588985122448632 msec\nrounds: 196"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 130.54310266788636,
            "unit": "iter/sec",
            "range": "stddev: 0.0048224917694319434",
            "extra": "mean: 7.660305137254871 msec\nrounds: 102"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 73.64857402114207,
            "unit": "iter/sec",
            "range": "stddev: 0.004802808501968356",
            "extra": "mean: 13.57799540983554 msec\nrounds: 61"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 58.12136382253758,
            "unit": "iter/sec",
            "range": "stddev: 0.008403022034170964",
            "extra": "mean: 17.205377407407504 msec\nrounds: 54"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 13.435748772695836,
            "unit": "iter/sec",
            "range": "stddev: 0.015611501011768487",
            "extra": "mean: 74.42830443750204 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (1)",
            "value": 779.8973862174568,
            "unit": "iter/sec",
            "range": "stddev: 0.0001289162513568542",
            "extra": "mean: 1.2822199659496905 msec\nrounds: 558"
          },
          {
            "name": "Items Limit: (10)",
            "value": 543.7377934318539,
            "unit": "iter/sec",
            "range": "stddev: 0.0001748744247412983",
            "extra": "mean: 1.8391217459584752 msec\nrounds: 433"
          },
          {
            "name": "Items Limit: (50)",
            "value": 231.95610594055262,
            "unit": "iter/sec",
            "range": "stddev: 0.00022940901344141828",
            "extra": "mean: 4.3111604928231 msec\nrounds: 209"
          },
          {
            "name": "Items Limit: (100)",
            "value": 138.70018489073504,
            "unit": "iter/sec",
            "range": "stddev: 0.00014738326334051582",
            "extra": "mean: 7.209795724409292 msec\nrounds: 127"
          },
          {
            "name": "Items Limit: (200)",
            "value": 70.75030706457358,
            "unit": "iter/sec",
            "range": "stddev: 0.008111630444349817",
            "extra": "mean: 14.13421427397203 msec\nrounds: 73"
          },
          {
            "name": "Items Limit: (250)",
            "value": 61.44664778110187,
            "unit": "iter/sec",
            "range": "stddev: 0.0006728647079036756",
            "extra": "mean: 16.274280796609272 msec\nrounds: 59"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 15.257042334158246,
            "unit": "iter/sec",
            "range": "stddev: 0.01678586414448204",
            "extra": "mean: 65.54350299999815 msec\nrounds: 17"
          },
          {
            "name": "Collection With Model validation",
            "value": 955.2287612152874,
            "unit": "iter/sec",
            "range": "stddev: 0.00006299165206523863",
            "extra": "mean: 1.0468696511270794 msec\nrounds: 665"
          },
          {
            "name": "Collection",
            "value": 898.6605484950297,
            "unit": "iter/sec",
            "range": "stddev: 0.00013351275105545176",
            "extra": "mean: 1.1127672196967826 msec\nrounds: 660"
          },
          {
            "name": "Collections With Model validation",
            "value": 680.9367830172117,
            "unit": "iter/sec",
            "range": "stddev: 0.00016022036898690658",
            "extra": "mean: 1.4685651075699393 msec\nrounds: 502"
          },
          {
            "name": "Collections",
            "value": 591.4264332743214,
            "unit": "iter/sec",
            "range": "stddev: 0.00007949894849401441",
            "extra": "mean: 1.6908273687797275 msec\nrounds: 442"
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
          "id": "d2eb81d299c60142c4a9987e264c3779f13580e1",
          "message": "return more information when pydantic raise validation error (#772)",
          "timestamp": "2025-01-07T17:52:48+01:00",
          "tree_id": "875f5cb91c0d17efc33ba9498ddfa8dfd1521c66",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/d2eb81d299c60142c4a9987e264c3779f13580e1"
        },
        "date": 1736268878802,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 694.5909905797528,
            "unit": "iter/sec",
            "range": "stddev: 0.00008358526918614257",
            "extra": "mean: 1.4396961860466 msec\nrounds: 301"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 518.1420064337779,
            "unit": "iter/sec",
            "range": "stddev: 0.00010658555411040284",
            "extra": "mean: 1.929972840617019 msec\nrounds: 389"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 216.29967269791555,
            "unit": "iter/sec",
            "range": "stddev: 0.0034798862092646",
            "extra": "mean: 4.623215502487613 msec\nrounds: 201"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 134.2728940490044,
            "unit": "iter/sec",
            "range": "stddev: 0.0028500629524411103",
            "extra": "mean: 7.447519524194055 msec\nrounds: 124"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 69.8622130446364,
            "unit": "iter/sec",
            "range": "stddev: 0.008332337931601739",
            "extra": "mean: 14.313889532258008 msec\nrounds: 62"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 56.77909940910168,
            "unit": "iter/sec",
            "range": "stddev: 0.008427642523528386",
            "extra": "mean: 17.61211450000033 msec\nrounds: 60"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 13.119641648795897,
            "unit": "iter/sec",
            "range": "stddev: 0.0163844995529774",
            "extra": "mean: 76.22159406250084 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (1)",
            "value": 809.034810674843,
            "unit": "iter/sec",
            "range": "stddev: 0.00011148190308768185",
            "extra": "mean: 1.2360407572152137 msec\nrounds: 589"
          },
          {
            "name": "Items Limit: (10)",
            "value": 543.2874736304566,
            "unit": "iter/sec",
            "range": "stddev: 0.00008676682960562122",
            "extra": "mean: 1.8406461561088718 msec\nrounds: 442"
          },
          {
            "name": "Items Limit: (50)",
            "value": 240.4210907147762,
            "unit": "iter/sec",
            "range": "stddev: 0.00020882311060652534",
            "extra": "mean: 4.159368868292637 msec\nrounds: 205"
          },
          {
            "name": "Items Limit: (100)",
            "value": 142.3002667357672,
            "unit": "iter/sec",
            "range": "stddev: 0.00037029433875371276",
            "extra": "mean: 7.027393714284935 msec\nrounds: 133"
          },
          {
            "name": "Items Limit: (200)",
            "value": 77.31274046711656,
            "unit": "iter/sec",
            "range": "stddev: 0.00016748706093682266",
            "extra": "mean: 12.934478767122869 msec\nrounds: 73"
          },
          {
            "name": "Items Limit: (250)",
            "value": 62.0697842138322,
            "unit": "iter/sec",
            "range": "stddev: 0.0006903251397982321",
            "extra": "mean: 16.110898606558244 msec\nrounds: 61"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 15.737980881782343,
            "unit": "iter/sec",
            "range": "stddev: 0.01252957766139162",
            "extra": "mean: 63.54055247058789 msec\nrounds: 17"
          },
          {
            "name": "Collection With Model validation",
            "value": 972.5310886959071,
            "unit": "iter/sec",
            "range": "stddev: 0.0000983312821031616",
            "extra": "mean: 1.0282447642274621 msec\nrounds: 615"
          },
          {
            "name": "Collection",
            "value": 959.4224047202638,
            "unit": "iter/sec",
            "range": "stddev: 0.00011485899262883555",
            "extra": "mean: 1.0422937749630385 msec\nrounds: 671"
          },
          {
            "name": "Collections With Model validation",
            "value": 607.4450877644529,
            "unit": "iter/sec",
            "range": "stddev: 0.004248387720024561",
            "extra": "mean: 1.6462393393948507 msec\nrounds: 495"
          },
          {
            "name": "Collections",
            "value": 605.1777089766382,
            "unit": "iter/sec",
            "range": "stddev: 0.00009593615357042984",
            "extra": "mean: 1.6524071940637246 msec\nrounds: 438"
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
          "id": "d3797ef7e7d01b738cfda62bff2a937c165c8c18",
          "message": "deprecate post_request_model in `BaseCoreClient` and `AsyncBaseCoreClient` (#773)",
          "timestamp": "2025-01-08T10:20:15+01:00",
          "tree_id": "478bbb97c953045855d22d33d2c1e11ba6b4ba2e",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/d3797ef7e7d01b738cfda62bff2a937c165c8c18"
        },
        "date": 1736328121218,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 728.991110704322,
            "unit": "iter/sec",
            "range": "stddev: 0.00009091575067454557",
            "extra": "mean: 1.371758839464915 msec\nrounds: 299"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 542.3632528760144,
            "unit": "iter/sec",
            "range": "stddev: 0.00005506066057577405",
            "extra": "mean: 1.8437827317711042 msec\nrounds: 384"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 220.3814829647128,
            "unit": "iter/sec",
            "range": "stddev: 0.0036832230007954885",
            "extra": "mean: 4.537586309645255 msec\nrounds: 197"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 138.90682566146867,
            "unit": "iter/sec",
            "range": "stddev: 0.00014039786410010926",
            "extra": "mean: 7.199070277778219 msec\nrounds: 18"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 72.37730382076774,
            "unit": "iter/sec",
            "range": "stddev: 0.0068562360572856805",
            "extra": "mean: 13.816485931506374 msec\nrounds: 73"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 56.67899460321371,
            "unit": "iter/sec",
            "range": "stddev: 0.008764019355030404",
            "extra": "mean: 17.643220508772043 msec\nrounds: 57"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 14.790080828559063,
            "unit": "iter/sec",
            "range": "stddev: 0.020334080679205134",
            "extra": "mean: 67.61288268749954 msec\nrounds: 16"
          },
          {
            "name": "Items Limit: (1)",
            "value": 854.7499671809946,
            "unit": "iter/sec",
            "range": "stddev: 0.00011007359055290324",
            "extra": "mean: 1.169932773788862 msec\nrounds: 557"
          },
          {
            "name": "Items Limit: (10)",
            "value": 580.4577092420567,
            "unit": "iter/sec",
            "range": "stddev: 0.00005624801013771926",
            "extra": "mean: 1.722778393805413 msec\nrounds: 452"
          },
          {
            "name": "Items Limit: (50)",
            "value": 218.32766947123582,
            "unit": "iter/sec",
            "range": "stddev: 0.0010745413813647339",
            "extra": "mean: 4.58027149019583 msec\nrounds: 204"
          },
          {
            "name": "Items Limit: (100)",
            "value": 139.33127092449675,
            "unit": "iter/sec",
            "range": "stddev: 0.0005106469842201947",
            "extra": "mean: 7.177139728682281 msec\nrounds: 129"
          },
          {
            "name": "Items Limit: (200)",
            "value": 77.47027683561774,
            "unit": "iter/sec",
            "range": "stddev: 0.0003555338471612327",
            "extra": "mean: 12.908176410959204 msec\nrounds: 73"
          },
          {
            "name": "Items Limit: (250)",
            "value": 63.520917991025,
            "unit": "iter/sec",
            "range": "stddev: 0.00015632362131184473",
            "extra": "mean: 15.742845532259027 msec\nrounds: 62"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 16.299966058580484,
            "unit": "iter/sec",
            "range": "stddev: 0.011397000792143263",
            "extra": "mean: 61.34982100000072 msec\nrounds: 17"
          },
          {
            "name": "Collection With Model validation",
            "value": 986.1961905435717,
            "unit": "iter/sec",
            "range": "stddev: 0.00010847729008582205",
            "extra": "mean: 1.0139970216766097 msec\nrounds: 692"
          },
          {
            "name": "Collection",
            "value": 988.8024801133326,
            "unit": "iter/sec",
            "range": "stddev: 0.00007263274786772084",
            "extra": "mean: 1.0113243242324634 msec\nrounds: 586"
          },
          {
            "name": "Collections With Model validation",
            "value": 718.7318089337954,
            "unit": "iter/sec",
            "range": "stddev: 0.0000694156488297337",
            "extra": "mean: 1.391339561669676 msec\nrounds: 527"
          },
          {
            "name": "Collections",
            "value": 576.0604774338876,
            "unit": "iter/sec",
            "range": "stddev: 0.00016717163669447124",
            "extra": "mean: 1.7359288463159086 msec\nrounds: 475"
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
          "id": "362741efca4d915ffab6232ad4d833bfa469a9d9",
          "message": "Release/v3.0.4 (#774)\n\n* update changelog\r\n\r\n* Bump version: 3.0.3 → 3.0.4",
          "timestamp": "2025-01-08T14:24:47+01:00",
          "tree_id": "547a43142658d8345efdc94491d40df1370d9948",
          "url": "https://github.com/stac-utils/stac-fastapi/commit/362741efca4d915ffab6232ad4d833bfa469a9d9"
        },
        "date": 1736342800575,
        "tool": "pytest",
        "benches": [
          {
            "name": "Items With Model validation (1)",
            "value": 698.3907682393649,
            "unit": "iter/sec",
            "range": "stddev: 0.00011820205505454628",
            "extra": "mean: 1.4318631423507908 msec\nrounds: 281"
          },
          {
            "name": "Items With Model validation (10)",
            "value": 478.0739302857186,
            "unit": "iter/sec",
            "range": "stddev: 0.00013687234972885483",
            "extra": "mean: 2.091726690477255 msec\nrounds: 336"
          },
          {
            "name": "Items With Model validation (50)",
            "value": 204.54580234409204,
            "unit": "iter/sec",
            "range": "stddev: 0.00443558469142594",
            "extra": "mean: 4.888880576086207 msec\nrounds: 184"
          },
          {
            "name": "Items With Model validation (100)",
            "value": 115.17394926890545,
            "unit": "iter/sec",
            "range": "stddev: 0.006562141676206165",
            "extra": "mean: 8.682518975408435 msec\nrounds: 122"
          },
          {
            "name": "Items With Model validation (200)",
            "value": 66.16535241759159,
            "unit": "iter/sec",
            "range": "stddev: 0.008893906046551435",
            "extra": "mean: 15.113650323943968 msec\nrounds: 71"
          },
          {
            "name": "Items With Model validation (250)",
            "value": 50.54308805035835,
            "unit": "iter/sec",
            "range": "stddev: 0.011443693744605994",
            "extra": "mean: 19.78509898333982 msec\nrounds: 60"
          },
          {
            "name": "Items With Model validation (1000)",
            "value": 11.761283178648933,
            "unit": "iter/sec",
            "range": "stddev: 0.029223565388224428",
            "extra": "mean: 85.0247362307685 msec\nrounds: 13"
          },
          {
            "name": "Items Limit: (1)",
            "value": 794.6403547947476,
            "unit": "iter/sec",
            "range": "stddev: 0.00021627918197022778",
            "extra": "mean: 1.2584309291192441 msec\nrounds: 522"
          },
          {
            "name": "Items Limit: (10)",
            "value": 548.9370913990118,
            "unit": "iter/sec",
            "range": "stddev: 0.0000959247331950221",
            "extra": "mean: 1.8217023693032235 msec\nrounds: 417"
          },
          {
            "name": "Items Limit: (50)",
            "value": 231.12486898272206,
            "unit": "iter/sec",
            "range": "stddev: 0.0001231467295583131",
            "extra": "mean: 4.326665513760685 msec\nrounds: 218"
          },
          {
            "name": "Items Limit: (100)",
            "value": 132.4195853583524,
            "unit": "iter/sec",
            "range": "stddev: 0.00021308788631469927",
            "extra": "mean: 7.551752992533628 msec\nrounds: 134"
          },
          {
            "name": "Items Limit: (200)",
            "value": 64.15946455506428,
            "unit": "iter/sec",
            "range": "stddev: 0.015737362310120295",
            "extra": "mean: 15.586164986488612 msec\nrounds: 74"
          },
          {
            "name": "Items Limit: (250)",
            "value": 58.596986396258956,
            "unit": "iter/sec",
            "range": "stddev: 0.0005708262999163549",
            "extra": "mean: 17.065724049997282 msec\nrounds: 60"
          },
          {
            "name": "Items Limit: (1000)",
            "value": 15.695473365152923,
            "unit": "iter/sec",
            "range": "stddev: 0.0007099196119361164",
            "extra": "mean: 63.71263718749631 msec\nrounds: 16"
          },
          {
            "name": "Collection With Model validation",
            "value": 895.9757885841035,
            "unit": "iter/sec",
            "range": "stddev: 0.00010633904399189246",
            "extra": "mean: 1.116101587499685 msec\nrounds: 640"
          },
          {
            "name": "Collection",
            "value": 895.7818588772074,
            "unit": "iter/sec",
            "range": "stddev: 0.0001375201173145581",
            "extra": "mean: 1.1163432146900385 msec\nrounds: 531"
          },
          {
            "name": "Collections With Model validation",
            "value": 654.6550915765829,
            "unit": "iter/sec",
            "range": "stddev: 0.0002930161199534563",
            "extra": "mean: 1.5275219162990623 msec\nrounds: 454"
          },
          {
            "name": "Collections",
            "value": 574.5423271653734,
            "unit": "iter/sec",
            "range": "stddev: 0.00009783398759817853",
            "extra": "mean: 1.7405158031327512 msec\nrounds: 447"
          }
        ]
      }
    ]
  }
}