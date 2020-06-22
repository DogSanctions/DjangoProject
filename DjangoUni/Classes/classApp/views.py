from django.shortcuts import render
from Classes import classApp
from Classes.classApp.models import djangoClasses

class_CompSci = djangoClasses(Title='Computer Science', Course='101', Instructor='Dr.Cash',
                              Duration='2 Hours')
class_FrontEnd = djangoClasses(Title='Front End Developer', Course='205', Instructor='Mr.Lowery',
                               Duration='3 Hours')
class_BackEnd = djangoClasses(Title='Front End Developer', Course='505', Instructor='Dr.Teeth',
                              Duration='8 Hours')

class_list = [class_CompSci, class_FrontEnd, class_BackEnd]

djangoClasses.objects.bulk_create(class_list)
