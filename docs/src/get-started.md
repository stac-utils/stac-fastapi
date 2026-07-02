# Get Started

In order to have your own _sweet_ STAC FastAPI running, follow these steps.

## Install

Our code is [available on PyPI](https://pypi.org/user/stac-utils/) for easy install:

```bash
# Create a virtual environment
python -m venv env
source ./env/bin/activate

# Install core dependencies
python -m pip install stac-fastapi.types stac-fastapi.api stac-fastapi.extensions uvicorn
```

This gets you the main code, but then, you need a backend.

## Backend

You can choose [one between all availables](./index.md#backends).

For this tutorial, let's say you want to use the [PgSTAC backend](https://github.com/stac-utils/stac-fastapi-pgstac). First, we can install it:

```bash
python -m pip install stac-fastapi.pgstac
```

Then, you need a PostgreSQL database with PgSTAC enabled. You can either rely on a pre-installed database on your machine, or use a Docker image.

=== ":simple-postgresql: Local database"

    ```bash
	# Download PgSTAC
	git clone https://github.com/stac-utils/pgstac.git
	cd pgstac/src/pgstac-migrate/

	# Install dependencies
	python -m venv env
	source ./env/bin/activate
	pip install -e .

	# Add PgSTAC structures to database
	# Note that your PostgreSQL user needs superuser permissions to do the install
	pgstac-migrate migrate -d postgres://myuser@localhost:5432/database

	# Give PgSTAC admin rights as well
	psql -d postgres://myuser@localhost:5432/database -c "GRANT pgstac_admin TO myuser"
    ```

=== ":simple-docker: Docker"

    ```bash
    # Get PgSTAC FastAPI code
	git clone https://github.com/stac-utils/stac-fastapi-pgstac.git
	cd stac-fastapi-pgstac

	# Start Docker database
	make run-database
    ```

## Running the API

In order to make API run, you need a little `.env` configuration file, let's create one:

```env
PGUSER=myuser
PGPASSWORD=mypassword
PGHOST=localhost
PGPORT=5432
PGDATABASE=database
```

!!! note
	If you're using the Docker database, make sure these settings:

	```env
    PGUSER=username
    PGPASSWORD=password
    PGDATABASE=postgis
    PGHOST=localhost
    PGPORT=5439
	```

From there, you can start the API with this command:

```bash
uvicorn stac_fastapi.pgstac.app:app --host 0.0.0.0 --port 8080
```

Your API is now running on [localhost:8080](http://localhost:8080) !

## Personalize settings

You can make the API a bit more _yours_ by changing the description settings in `.env` file:

- `STAC_FASTAPI_VERSION` (string) is the version number of your API instance (this is not the STAC version).
- `STAC FASTAPI_TITLE` (string) should be a self-explanatory title for your API.
- `STAC FASTAPI_DESCRIPTION` (string) should be a good description for your API. It can contain CommonMark.
- `STAC_FASTAPI_LANDING_ID` (string) is a unique identifier for your Landing page.

## Load data

Once you're all setup, you may want to actually offer some data. This depends on which backend you've choose to use.

For example, with _PgSTAC_, you can:

- Use [PyPgSTAC](https://stac-utils.github.io/pgstac/pypgstac/) helper CLI
- Or directly use `pgstac` functions in SQL

Let's load a demo collection and item, directly in SQL:

```sql
-- Single collection
INSERT INTO pgstac.collections (content)
SELECT jsonb_build_object(
	'type', 'Collection',
	'id', '1',
	'extent', jsonb_build_object(
		'temporal', jsonb_build_object(
			'interval', json_build_array(
				json_build_array(
					'2026-01-01',
					'2026-12-31'
				)
			)
		),
		'spatial', jsonb_build_object(
			'bbox', json_build_array(
				json_build_array(-180.0, -90.0, 180.0, 90.0)
			)
		)
	)
);

-- Single item
INSERT INTO pgstac.items_staging_upsert(content)
SELECT jsonb_build_object(
	'type', 'Feature',
	'id', '1',
	'geometry', ST_Point(-1.7, 48.7, 4326),
	'collection', '1',
	'properties', json_build_object(),
	'assets', json_build_object(
		'hd', json_build_object(
			'href', 'https://path.to/some/image',
			'roles', json_build_array('data'),
			'type', 'image/jpeg'
		)
	)
);
```

Once done, you can refresh your API and see all available collections at:

[localhost:8080/collections](http://localhost:8080/collections)

## What's next

Check out the [Development & Contributing guide](./contributing.md) for advanced topics, or the [Tips & Tricks guide](./tips-and-tricks.md) for _good to know_ stuff.
