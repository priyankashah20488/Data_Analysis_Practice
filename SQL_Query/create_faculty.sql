-- faculty table
create table faculty (
id int not null auto_increment,
faculty_name varchar(25),
course_id int,
primary key (id),
foreign key (course_id) references courses(id)
);

