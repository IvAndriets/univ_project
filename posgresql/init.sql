DROP TABLE if exists nprl.public.staff;

CREATE TABLE nprl.public.staff
(
    id TEXT,
    name TEXT,
    second_name TEXT,
    surname TEXT,
    create_at timestamp  NOT NULL  DEFAULT current_timestamp,
    updated_at timestamp  NOT NULL  DEFAULT current_timestamp,
    PRIMARY KEY (id)
);

DROP TABLE if exists nprl.public.project;

create table nprl.public.project
(
  id text,
  name text,
  rate text,
  crate_at timestamp not null default current_timestamp,
  update_at timestamp not null default current_timestamp,
  primary key (id)
);

DROP TABLE if exists nprl.public.time;

create table nprl.public.time
(
  id text,
  staff_id text,
  project_id text,
  time text,
  crate_at timestamp not null default current_timestamp,
  primary key (id)
);