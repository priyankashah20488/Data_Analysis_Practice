-- join tables

select student.student_name, courses.course_name,courses.duration,faculty.faculty_name
from courses
join student on student.course_id = courses.id
join faculty on faculty.course_id = courses.id;