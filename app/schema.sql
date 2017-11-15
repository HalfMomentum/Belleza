drop table if exists Users;
create table Users (
  id integer primary key autoincrement,
  email text not null,
  name text not null
);

drop table if exists Bookings;
create table Bookings (
    id integer primary key autoincrement,
    customerEmail text not null,
    bookDate date not null,
    bookTime time not null,
    now() onDate date not null
;)
