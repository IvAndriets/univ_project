DROP TABLE if exists univ_pr.public.staff;

CREATE TABLE univ_pr.public.staff
(
    id          TEXT,
    name        TEXT,
    second_name TEXT,
    surname     TEXT,
    create_at   timestamp NOT NULL DEFAULT current_timestamp,
    updated_at  timestamp NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (id)
);

DROP TABLE if exists univ_pr.public.project;

create table univ_pr.public.project
(
    id        text,
    name      text,
    rate      text,
    crate_at  timestamp not null default current_timestamp,
    update_at timestamp not null default current_timestamp,
    primary key (id)
);

DROP TABLE if exists univ_pr.public.time_tracker;

create table univ_pr.public.time_tracker
(
    id         text,
    staff_id   text,
    project_id text,
    time       text,
    crate_at   timestamp not null default current_timestamp,
    primary key (id),
    foreign key (project_id) references project (id) on delete RESTRICT,
    foreign key (staff_id) references staff (id) on delete RESTRICT
);