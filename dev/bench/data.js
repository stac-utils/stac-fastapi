window.BENCHMARK_DATA = {
  "lastUpdate": 1712679000372,
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
      }
    ]
  }
}