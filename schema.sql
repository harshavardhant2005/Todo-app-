create table if not exists task(
    id integer primary key autoincrement,
    title varchar not null,
    description varchar ,
    done boolean default 0
);

insert into task(title,description) values ("Welcome to the To-Do App built with Flask!","In this app, you can add new tasks, update the status of your tasks, and delete tasks once they are completed." )