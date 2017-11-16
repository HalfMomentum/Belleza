drop table if exists Bookings;
create table Bookings(
    id integer primary key autoincrement,
    customerEmail text not null,
    bookDate text not null,
    bookService text not null
);
