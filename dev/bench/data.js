window.BENCHMARK_DATA = {
  "lastUpdate": 1712735235283,
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
      }
    ]
  }
}