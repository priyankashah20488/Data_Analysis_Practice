-- create student table

create table student(
id int not null auto_increment,
student_name varchar(25),
course_id int,
primary key (id),
foreign key (course_id) references courses(id)
);