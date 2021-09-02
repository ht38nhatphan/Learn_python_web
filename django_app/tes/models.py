from django.db import models
from django.contrib.auth.models import User

# create Department model, this model will be mapped to table user_register_login_department in sqlite db.
class Department(models.Model):
    # define department name and description columns, the id column will be added automatically.
    dept_name = models.CharField(max_length=1000)
    dept_desc = models.CharField(max_length=1000)

    # this function will be invoked when this model object is foreign key of other model(for example Employee model.).
    def __str__(self):
        ret = self.dept_name + ',' + self.dept_desc
        return ret

    # this is a inner class which is used to define unique index columns. You can specify multiple columns in a list or tuple.
    class Meta:
        unique_together = ['dept_name']


class MaleEmployeeManager(models.Manager):

    def get_queryset(self):
        return super(MaleEmployeeManager, self).get_queryset().filter(sex='M')

class FemaleEmployeeManager(models.Manager):

    def get_queryset(self):
        return super(FemaleEmployeeManager, self).get_queryset().filter(sex='F')


# create Employee model, this model will be mapped to table user_register_login_employee in sqlite db.
class Employee(models.Model):

    # Employee has two foreign key, user(Django built-in auth_user table) and department.
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    # support department and employee table are many to many relationship.
    dept = models.ManyToManyField(Department)

    emp_mobile = models.CharField(max_length=100)
    # should add the () after IntegerField, otherwise the emp_salary column will not be created.
    emp_salary = models.IntegerField()
    # if do not specify the auto_now=True attribute with value then this field can not be created.
    emp_onboard_date = models.DateTimeField(auto_now=True)


    # add a sex field which value is limited to a choice tuple.
    sex_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=2, choices=sex_choices, default='M')

    # the first model data manager is the default manager, if defined then Employee.objects will throw error AttributeError: type object 'Employee' has no attribute 'objects'.
    # but you had better set objects = models.Manager() because Django use objects internally widely.
    objects = models.Manager()

    # create two custom model data table level manager.
    male_employee_manager = MaleEmployeeManager()

    female_employee_manager = FemaleEmployeeManager()

    # this method will be called when other model reference Employee model as foreign key.
    def __str__(self):
        return self.user.username + ',' + str(self.emp_salary) + ',' + str(self.emp_mobile)

    class Meta:
        unique_together = ['emp_mobile']