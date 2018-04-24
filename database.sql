create table house (
id int unsigned not null auto_increment primary key,
user_id int unsigned not null,
title varchar(20) unique,
place varchar(20) unique,
date_time varchar(20) unique,
community varchar(20) unique,
payable varchar(20) unique,
telephone varchar(20) unique,
content varchar(20) unique,
comment varchar(20) unique,
photo varchar(20)
)engine=InnoDB default charset=utf8;

create table phone (
id int unsigned not null auto_increment primary key,
user_id int unsigned not null,
title varchar(20) unique,
tags enum('xiaomi','huawei','samsung','chuizi','meizu','oppo','vivo','iphone','other') default 'other' unique,
date_time varchar(20) unique,
payable varchar(20) unique,
telephone varchar(20) unique,
content varchar(20) unique,
comment varchar(20) unique,
photo varchar(20)
)engine=InnoDB default charset=utf8;

create table book (
id int unsigned not null auto_increment primary key,
user_id int unsigned not null,
title varchar(20) unique,
tags enum('wenxue','tongshu','jiaoyu','renwen','shenghuo','kejijishu','other') default 'other' unique,
date_time varchar(20) unique,
payable varchar(20) unique,
telephone varchar(20) unique,
content varchar(20) unique,
comment varchar(20) unique,
photo varchar(20)
)engine=InnoDB default charset=utf8;

create table house_photo (
id int primary key auto_increment,
house_id int unsigned not null,
photo varchar(20),
foreign key(house_id) references house(id) on delete cascade on update no action
)engine=InnoDB default charset=utf8;

create table phone_photo (
id int primary key auto_increment,
phone_id int unsigned not null,
photo varchar(20),
constraint phone_photo foreign key(phone_id) references phone(id) on delete cascade on update no action
)engine=InnoDB default charset=utf8;

create table book_photo (
id int primary key auto_increment,
book_id int unsigned not null,
photo varchar(20),
constraint book_photo foreign key(book_id) references book(id) on delete cascade on update no action
)engine=InnoDB default charset=utf8;

create table house_comment (
id int unsigned not null primary key auto_increment,
house_id int unsigned not null,
user_id int unsigned not null,
comment varchar(20) unique,
foreign key(house_id) references house(id) on delete cascade on update cascade,
foreign key(user_id) references user(id) on delete cascade on update cascade,
unique(house_id,user_id)
)engine=InnoDB default charset=utf8;


create table roles (
id int primary key auto_increment,
name varchar(20) unique
)engine=InnoDB default charset=utf8;

create table user (
id int unsigned not null primary key auto_increment,
username varchar(20) unique,
password varchar(20) unique,
email varchar(20) unique,

roles_id int,
foreign key(roles_id) references roles(id)
)engine=InnoDB default charset=utf8;


alter table house add constraint house_user foreign key (user_id) references user(id) on delete cascade on update no action;
alter table phone add constraint phone_user foreign key (user_id) references user(id) on delete cascade on update no action;
alter table book add constraint book_user foreign key (user_id) references user(id) on delete cascade on update no action;


create table phone_comment (
id int primary key auto_increment,
phone_id int unsigned not null,
user_id int unsigned not null,
comment varchar(20) unique,
foreign key(phone_id) references phone(id) on delete cascade on update cascade,
foreign key(user_id) references user(id) on delete cascade on update cascade,
unique(phone_id,user_id)
)engine=InnoDB default charset=utf8;

create table book_comment (
id int primary key auto_increment,
book_id int unsigned not null,
user_id int unsigned not null,
comment varchar(20) unique,
foreign key(book_id) references book(id) on delete cascade on update cascade,
foreign key(user_id) references user(id) on delete cascade on update cascade,
unique(book_id,user_id)
)engine=InnoDB default charset=utf8;


-- create table house (
-- id int unsigned not null auto_increment primary key,
-- title varchar(20) unique,
-- place varchar(20) unique,
-- date_time varchar(20) unique,
-- community varchar(20) unique,
-- payable varchar(20) unique,
-- telephone varchar(20) unique,
-- content varchar(20) unique,
-- comment varchar(20) unique,
-- photo varchar(20)
-- )engine=InnoDB default charset=utf8;

-- create table phone (
-- id int unsigned not null auto_increment primary key,
-- title varchar(20) unique,
-- tags enum('xiaomi','huawei','samsung','chuizi','meizu','oppo','vivo','iphone','other') default 'other' unique,
-- date_time varchar(20) unique,
-- payable varchar(20) unique,
-- telephone varchar(20) unique,
-- content varchar(20) unique,
-- comment varchar(20) unique,
-- photo varchar(20)
-- )engine=InnoDB default charset=utf8;

-- create table book (
-- id int unsigned not null auto_increment primary key,
-- title varchar(20) unique,
-- tags enum('wenxue','tongshu','jiaoyu','renwen','shenghuo','kejijishu','other') default 'other' unique,
-- date_time varchar(20) unique,
-- payable varchar(20) unique,
-- telephone varchar(20) unique,
-- content varchar(20) unique,
-- comment varchar(20) unique,
-- photo varchar(20)
-- )engine=InnoDB default charset=utf8;

-- create table house_photo (
-- id int primary key auto_increment,
-- house_id int unsigned not null,
-- photo varchar(20),
-- foreign key(house_id) references house(id) on delete cascade on update no action
-- )engine=InnoDB default charset=utf8;

-- create table phone_photo (
-- id int primary key auto_increment,
-- phone_id int unsigned not null,
-- photo varchar(20),
-- constraint phone_photo foreign key(phone_id) references phone(id) on delete cascade on update no action
-- )engine=InnoDB default charset=utf8;

-- create table book_photo (
-- id int primary key auto_increment,
-- book_id int unsigned not null,
-- photo varchar(20),
-- constraint book_photo foreign key(book_id) references book(id) on delete cascade on update no action
-- )engine=InnoDB default charset=utf8;

-- create table house_comment (
-- id int unsigned not null primary key auto_increment,
-- house_id int unsigned not null,
-- user_id int unsigned not null,
-- comment varchar(20) unique,
-- foreign key(house_id) references house(id) on delete cascade on update cascade,
-- foreign key(user_id) references user(id) on delete cascade on update cascade,
-- unique(house_id,user_id)
-- )engine=InnoDB default charset=utf8;

-- create table phone_comment (
-- id int primary key auto_increment,
-- phone_id int unsigned not null,
-- user_id int unsigned not null,
-- comment varchar(20) unique,
-- foreign key(phone_id) references phone(id) on delete cascade on update cascade,
-- foreign key(user_id) references user(id) on delete cascade on update cascade,
-- unique(phone_id,user_id)
-- )engine=InnoDB default charset=utf8;

-- create table book_comment (
-- id int primary key auto_increment,
-- book_id int unsigned not null,
-- user_id int unsigned not null,
-- comment varchar(20) unique,
-- foreign key(book_id) references book(id) on delete cascade on update cascade,
-- foreign key(user_id) references user(id) on delete cascade on update cascade,
-- unique(book_id,user_id)
-- )engine=InnoDB default charset=utf8;






-- create table roles (
-- id int primary key auto_increment,
-- name varchar(20) unique
-- )engine=InnoDB default charset=utf8;


-- create table user (
-- id int primary key auto_increment,
-- username varchar(20) unique,
-- password varchar(20) unique,
-- email varchar(20) unique,
-- user_id int,
-- roles_id int,
-- foreign key(roles_id) references roles(id)
-- )engine=InnoDB default charset=utf8;


-- alter table house add constraint house_user foreign key (hid) references user(id) on delete cascade on update no action;
-- alter table phone add constraint phone_user foreign key (pid) references user(id) on delete cascade on update no action;
-- alter table book add constraint book_user foreign key (bid) references user(id) on delete cascade on update no action;

