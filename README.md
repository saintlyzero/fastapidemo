psql -U postgres -d demo -h localhost

### Timescale DB indexed on time
CREATE TABLE conditions (
  time        TIMESTAMPTZ       NOT NULL,
  location    TEXT              NOT NULL,
  temperature INTEGER  NULL);


### start uvicorn server
uvicorn main:app --reload