

ITEM_ID = "Item Id"

COLLECTION_ID = "Collection Id"
COLLECTIONS = "Array of collection Ids to search for items."

CRS = """Retrieve geometries in a specific CRS. Specified CRS must be supported by the collection. 

Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`"""

LIMIT="Limits the number of results that are included in each page of the response."

PAGING_TOKEN="Token used for paging functionality. Only use tokens as returned by the API in the `links` section of the response."

IDS = "Array of Item ids to return. All other filter parameters that further restrict the number of search results are ignored"

BBOX="""Only return items intersecting this bounding box. Mutually exclusive with `intersects`. The default sort is the shortest distance between specifed geometry centroid and the footprint centroid of skraafotos. 

Example: `10.312385559082033,55.33392904334293,10.36388397216797,55.353452174893285`

See also `bbox-crs`.
"""

BBOX_CRS="""The coordinate reference system (CRS) used by `bbox` param. The specified CRS must be supported by the server.

Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`."""

INTERSECTS="""Only return items intersecting this GeoJSON Geometry. Mutually exclusive with `bbox`. The default sort is the shortest distance between specifed geometry centroid and the footprint centroid of skraafotos. """

DATETIME="""Only return items that have a temporal property that intersects this value.

Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

Examples:
- A date-time: `2018-02-12T23:20:50Z`
- A closed interval: `2018-02-12T00:00:00Z/2018-03-18T12:31:12Z`
- Open intervals: `2018-02-12T00:00:00Z/..` or `../2018-03-18T12:31:12Z`
"""

FILTER="""A CQL filter expression for filtering items.

Supports `CQL-JSON` as defined in https://portal.ogc.org/files/96288

Example:
```
{ "gt": [ { "property": "gsd" }, "0.1" ] }
```

If filter input has a geometry, the default sort is the shortest distance between specifed geometry centroid and the footprint centroid of skraafotos. 
Remember to URL encode the CQL-JSON if using GET `/search` or `/collections/{collectionid}/items`.
"""

FILTER_LANG="The CQL filter encoding that the 'filter' value uses. This server only supports the encoding `cql-json`"

FILTER_CRS="""The coordinate reference system (CRS) used by spatial literals in the 'filter' value. The specified CRS must be supported by the server.

Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`.
"""

SORTBY="""An array of property names, prefixed by either "+" for ascending or "-" for descending. If no prefix is provided, "+" is assumed.

Example: `-gsd,-datetime`
"""

# ENDPOINTS
LANDING_PAGE="The landing page provides links to the API definition, the conformance statements and to the item collections in this dataset."
CONFORMANCECLASSES="A list of all conformance classes specified in the standards that the server conforms to."
GET_COLLECTIONS="The collections in the service."
GET_COLLECTION="The collection with id `collectionId`"
GET_ITEM_COLLECTION="Items of the collection with id `collectionId`."
GET_ITEM="The item with id `itemId` in the collection with id `collectionId`."
GET_SEARCH="Query items matching across collections. It is recommended to use the `POST` endpoint instead."
POST_SEARCH="Query items matching across collections.."

QUERYABLES="Global item properties (\"queryables\") that may be used to construct a filter expression."
COLLECTION_QUERYABLES="Item properties (\"queryables\") that may be used to construct a filter expression for items of the collection with id `collectionId`."