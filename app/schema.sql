drop table if exists Users;
create table Users (
  id integer primary key autoincrement,
  email text not null,
  name text notn null
);

drop table if exists Booking;
create table Bookings (
    id integer primary key autoincrement,
    bookDate date not null,
    bookTime time not null,
    now() onDate date not null
;)
