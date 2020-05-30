drop table if exists univ_pr.public.position;

create table univ_pr.public.position
(
    id           text,
    name         text,
    salary       text,
    working_time int,

    primary key (id)
);

insert into univ_pr.public.position(id, name, salary, working_time)
values ('807b3702-8162-11ea-8182-f07960024c26', 'Project manager', '100', 8),
       ('807b426a-8162-11ea-8182-f07960024c26', 'Team leader', '150', 8),
       ('807b4526-8162-11ea-8182-f07960024c26', 'Programmer', '120', 8);

DROP TABLE if exists univ_pr.public.staff;

CREATE TABLE univ_pr.public.staff
(
    id          TEXT,
    name        TEXT,
    surname     TEXT,
    position_id text,
    create_at   timestamp NOT NULL DEFAULT current_timestamp,
    updated_at  timestamp NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (id),
    foreign key (position_id) references position (id) on delete restrict
);

insert into univ_pr.public.staff(id, name, surname, position_id)
VALUES ('1a9db77c-83a9-11ea-be09-f07960024c26', 'Amanah', 'Fisher', '807b3702-8162-11ea-8182-f07960024c26'),
       ('1a9e4052-83a9-11ea-be09-f07960024c26', 'Anayah', 'Christie', '807b3702-8162-11ea-8182-f07960024c26'),
       ('1a9e449e-83a9-11ea-be09-f07960024c26', 'Miya', 'Pennington', '807b426a-8162-11ea-8182-f07960024c26'),
       ('1a9e47f0-83a9-11ea-be09-f07960024c26', 'Margaux', 'Mejia', '807b426a-8162-11ea-8182-f07960024c26'),
       ('1a9e4a84-83a9-11ea-be09-f07960024c26', 'Jaidan', 'Witt', '807b4526-8162-11ea-8182-f07960024c26'),
       ('1a9e4cdc-83a9-11ea-be09-f07960024c26', 'Ria', 'Bradford', '807b4526-8162-11ea-8182-f07960024c26'),
       ('1a9e4eee-83a9-11ea-be09-f07960024c26', 'Cole', 'Kouma', '807b4526-8162-11ea-8182-f07960024c26'),
       ('1a9e50d8-83a9-11ea-be09-f07960024c26', 'Keanu', 'Halliday', '807b4526-8162-11ea-8182-f07960024c26');

DROP TABLE if exists univ_pr.public.project;

create table univ_pr.public.project
(
    id         text,
    name       text,
    create_at  timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp,
    primary key (id)
);

insert into univ_pr.public.project(id, name)
values ('18d01afa-83ab-11ea-8738-f07960024c26', 'Project_1'),
       ('18d01bd6-83ab-11ea-8738-f07960024c26', 'Project_2');

drop table if exists univ_pr.public.work_types;

create table univ_pr.public.work_types
(
    id         text,
    name       text,
    salary_mod text,
    primary key (id)
);

insert into univ_pr.public.work_types(id, name, salary_mod)
values ('c9a20896-83ad-11ea-89b5-f07960024c26', 'Standard', '100'),
       ('c9a2090e-83ad-11ea-89b5-f07960024c26', 'Vacation', '50'),
       ('c9a20990-83ad-11ea-89b5-f07960024c26', 'Hospital`s', '80');

drop table if exists univ_pr.public.month_salary_table;

create table univ_pr.public.month_salary_timesheet
(
    id           text,
    person_id    text,
    period_start text,
    period_end   text,
    create_at    timestamp not null default current_timestamp,
    primary key (id),
    foreign key (person_id) references staff (id) on delete restrict
);

insert into univ_pr.public.month_salary_timesheet(id, person_id, period_start, period_end, create_at)
values ('20c2e566-975c-11ea-a2e6-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26', '2020-04-01',
        '2020-04-30', '2020-04-01 12:00:00'),
       ('20c2e4bc-975c-11ea-a2e6-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26', '2020-04-01',
        '2020-04-30', '2020-04-01 12:00:00');


DROP TABLE if exists univ_pr.public.time_tracker;

create table univ_pr.public.time_tracker
(
    id           text,
    staff_id     text,
    project_id   text,
    work_type_id text,
    position_id  text,
    time         text,
    create_at    timestamp not null default current_timestamp,
    head_id      text,
    primary key (id),
    foreign key (project_id) references project (id) on delete RESTRICT,
    foreign key (staff_id) references staff (id) on delete RESTRICT,
    foreign key (work_type_id) references work_types (id) on delete restrict,
    foreign key (head_id) references month_salary_timesheet (id) on delete cascade
);

insert into univ_pr.public.time_tracker(id, staff_id, project_id, work_type_id, time, create_at, head_id, position_id)
values ('814572a4-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-01 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81458b54-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-02 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81458ea6-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-03 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81459158-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-06 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145932e-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-07 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('814594be-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-08 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81459644-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-09 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('814597ca-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-10 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81459964-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-13 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81459ad6-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-14 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81459db0-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-15 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('81459fd6-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-16 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a148-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-17 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a292-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-20 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a3d2-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-21 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a512-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-22 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a63e-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-23 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a76a-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-24 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a8aa-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-27 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145a9c2-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-28 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145aae4-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-29 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('8145ac06-975d-11ea-a0fc-f07960024c26', '1a9e50d8-83a9-11ea-be09-f07960024c26',
        '18d01bd6-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-30 12:00:00', '20c2e566-975c-11ea-a2e6-f07960024c26', '807b3702-8162-11ea-8182-f07960024c26'),
       ('aed392a6-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-01 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3e4b8-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-02 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3e68e-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-03 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3e814-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-06 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3e972-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-07 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3eabc-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-08 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3ebf2-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-09 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3ed0a-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-10 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3ee54-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-13 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3ef8a-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-14 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f0ac-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-15 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f1ce-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-16 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f2f0-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-17 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f41c-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-20 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f53e-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-21 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f660-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-22 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f778-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-23 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f890-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-24 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3f9da-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-27 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3fafc-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-28 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3fc14-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-29 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26'),
       ('aed3fd2c-9761-11ea-82e2-f07960024c26', '1a9db77c-83a9-11ea-be09-f07960024c26',
        '18d01afa-83ab-11ea-8738-f07960024c26', 'c9a20896-83ad-11ea-89b5-f07960024c26', '8',
        '2020-04-30 12:00:00', '20c2e4bc-975c-11ea-a2e6-f07960024c26', '807b4526-8162-11ea-8182-f07960024c26');


drop table if exists univ_pr.public.salary_table;

create table univ_pr.public.salary_table
(
    id          text,
    person_id   text,
    salary      int,
    periodStart timestamp,
    periodEnd   timestamp,
    create_at   timestamp not null default current_timestamp,
    primary key (id)
);




