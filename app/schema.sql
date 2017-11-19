drop table if exists Bookings;
create table Bookings(
    id integer primary key autoincrement,
    customerEmail text not null,
    bookDate text not null,
    bookService text not null
);
drop table if exists Services;
create table Services(
    id integer primary key,
    Service text not null
  );
insert into Services values (1,'Haircut');
insert into Services values (2,'Shave');
insert into Services values (3,'Face Wash');
insert into Services values (4,'De-Tan');
insert into Services values (5,'Waxing');
