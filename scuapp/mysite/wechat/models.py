from django.db import models


class Tbapplication(models.Model):
    ap_number = models.AutoField(db_column='AP_Number', primary_key=True)  # Field name made lowercase.
    ap_reson = models.TextField(db_column='AP_Reson', blank=True, null=True)  # Field name made lowercase.
    ap_time = models.DateTimeField(db_column='AP_Time')  # Field name made lowercase.
    ap_abletime = models.CharField(db_column='AP_AbleTime', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ow_number = models.ForeignKey('TboutWork', models.DO_NOTHING, db_column='OW_Number')  # Field name made lowercase.
    stu = models.ForeignKey('Tbstudent', models.DO_NOTHING, db_column='Stu_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbapplication'


class Tbcompany(models.Model):
    com_number = models.AutoField(db_column='Com_Number', primary_key=True)  # Field name made lowercase.
    phone_num = models.CharField(db_column='Phone_Num', max_length=11)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    com_name = models.CharField(db_column='Com_Name', max_length=60)  # Field name made lowercase.
    com_leader = models.CharField(db_column='Com_Leader', max_length=20, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_mail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    com_address = models.CharField(db_column='Com_Address', max_length=60, null=True)  # Field name made lowercase.
    com_license = models.CharField(db_column='Com_License', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbcompany'


class TbfeedbackEr(models.Model):
    fbe_number = models.AutoField(db_column='Fbe_Number', primary_key=True)  # Field name made lowercase.
    fb_content = models.CharField(db_column='Fb_Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fb_time = models.DateTimeField(db_column='Fb_Time')  # Field name made lowercase.
    stu = models.ForeignKey('Tbstudent', models.DO_NOTHING, db_column='Stu_ID')  # Field name made lowercase.
    iw_number = models.ForeignKey('TbinWork', models.DO_NOTHING, db_column='IW_Number', blank=True, null=True)  # Field name made lowercase.
    ow_number = models.ForeignKey('TboutWork', models.DO_NOTHING, db_column='Ow_Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbfeedback_er'


class TbfeedbackStu(models.Model):
    fbs_number = models.AutoField(db_column='Fbs_Number', primary_key=True)  # Field name made lowercase.
    fb_content = models.CharField(db_column='Fb_Content', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fb_time = models.DateTimeField(db_column='Fb_Time')  # Field name made lowercase.
    iw_number1 = models.ForeignKey('TbinWork', models.DO_NOTHING, db_column='IW_Number1', blank=True, null=True)  # Field name made lowercase.
    ow_number2 = models.ForeignKey('TboutWork', models.DO_NOTHING, db_column='Ow_Number2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbfeedback_stu'


class TbinResult(models.Model):
    inr_number = models.AutoField(db_column='Inr_Number', primary_key=True)  # Field name made lowercase.
    inr_phonenum = models.CharField(db_column='Inr_Phonenum', max_length=11)  # Field name made lowercase.
    r_time = models.CharField(db_column='R_Time', max_length=60)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=60)  # Field name made lowercase.
    r_ps = models.CharField(db_column='R_Ps', max_length=200, blank=True, null=True)  # Field name made lowercase.
    in_r_time = models.DateTimeField(db_column='In_R_Time')  # Field name made lowercase.
    iw_number = models.ForeignKey('TbinWork', models.DO_NOTHING, db_column='IW_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbin_result'


class TbinWork(models.Model):
    iw_number = models.AutoField(db_column='IW_Number', primary_key=True)  # Field name made lowercase.
    iw_post = models.CharField(db_column='IW_Post', max_length=60)  # Field name made lowercase.
    iw_depart = models.CharField(db_column='IW_depart', max_length=60)  # Field name made lowercase.
    w_time = models.CharField(db_column='W_Time', max_length=60, blank=True, null=True)  # Field name made lowercase.
    w_place = models.CharField(db_column='W_Place', max_length=60, blank=True, null=True)  # Field name made lowercase.
    work = models.CharField(db_column='Work', max_length=200)  # Field name made lowercase.
    w_salary = models.CharField(db_column='W_Salary', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w_reuire = models.CharField(db_column='W_Reuire', max_length=200, blank=True, null=True)  # Field name made lowercase.
    w_amount = models.CharField(db_column='W_Amount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddl_time = models.DateTimeField(db_column='Ddl_Time')  # Field name made lowercase.
    inpub_time = models.DateTimeField(db_column='Inpub_time')  # Field name made lowercase.
    w_ps = models.CharField(db_column='W_Ps', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbin_work'


class TbinterviewApply(models.Model):
    ia_number = models.AutoField(db_column='IA_Number', primary_key=True)  # Field name made lowercase.
    ia_time = models.CharField(db_column='IA_Time', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ia_name = models.CharField(db_column='IA_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=12)  # Field name made lowercase.
    a_time = models.DateTimeField(db_column='A_Time')  # Field name made lowercase.
    ow_number = models.ForeignKey('TboutWork', models.DO_NOTHING, db_column='Ow_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbinterview_apply'


class TbinterviewNotice(models.Model):
    i_number = models.AutoField(db_column='I_Number', primary_key=True)  # Field name made lowercase.
    i_address = models.CharField(db_column='I_Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    i_time = models.DateTimeField(db_column='I_Time')  # Field name made lowercase.
    ia_number = models.PositiveIntegerField(db_column='IA_Number')  # Field name made lowercase.
    stu = models.ForeignKey('Tbstudent', models.DO_NOTHING, db_column='Stu_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbinterview_notice'


class TbinterviewResult(models.Model):
    ir_number = models.AutoField(db_column='IR_Number', primary_key=True)  # Field name made lowercase.
    ir_rtime = models.CharField(db_column='IR_Rtime', max_length=60)  # Field name made lowercase.
    ir_result = models.CharField(db_column='IR_Result', max_length=60)  # Field name made lowercase.
    ir_ps = models.CharField(db_column='IR_Ps', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ir_time = models.DateTimeField(db_column='IR_Time')  # Field name made lowercase.
    i_number = models.ForeignKey(TbinterviewNotice, models.DO_NOTHING, db_column='I_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbinterview_result'


class Tbmanager(models.Model):
    manager_id = models.CharField(db_column='Manager_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=11)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=60, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tbmanager'


class TboutWork(models.Model):
    ow_number = models.AutoField(db_column='Ow_Number', primary_key=True)  # Field name made lowercase.
    ow_post = models.CharField(db_column='Ow_Post', max_length=60)  # Field name made lowercase.
    w_time = models.CharField(db_column='W_Time', max_length=60, blank=True, null=True)  # Field name made lowercase.
    w_place = models.CharField(db_column='W_Place', max_length=60, blank=True, null=True)  # Field name made lowercase.
    work = models.CharField(db_column='Work', max_length=200)  # Field name made lowercase.
    w_salary = models.CharField(db_column='W_Salary', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w_reuire = models.CharField(db_column='W_Reuire', max_length=200, blank=True, null=True)  # Field name made lowercase.
    w_amount = models.CharField(db_column='W_Amount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddl_time = models.DateTimeField(db_column='Ddl_Time')  # Field name made lowercase.
    ipub_time = models.DateTimeField(db_column='Ipub_Time')  # Field name made lowercase.
    w_ps = models.CharField(db_column='W_Ps', max_length=200, blank=True, null=True)  # Field name made lowercase.
    com_number = models.ForeignKey(Tbcompany, models.DO_NOTHING, db_column='Com_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbout_work'


class Tbqualify(models.Model):
    com_license = models.CharField(db_column='Com_License', primary_key=True, max_length=18)  # Field name made lowercase.
    com_condition = models.CharField(db_column='Com_Condition', max_length=200, blank=True, null=True)  # Field name made lowercase.
    com_business = models.CharField(db_column='Com_Business', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbqualify'


class Tbquery(models.Model):
    q_number = models.AutoField(db_column='Q_Number', primary_key=True)  # Field name made lowercase.
    q_content = models.CharField(db_column='Q_Content', max_length=200)  # Field name made lowercase.
    q_time = models.DateTimeField(db_column='Q_Time')  # Field name made lowercase.
    q_direc = models.CharField(db_column='Q_direc', max_length=10)  # Field name made lowercase.
    com_number1 = models.ForeignKey(Tbcompany, models.DO_NOTHING, db_column='Com_Number1')  # Field name made lowercase.
    stu_id1 = models.ForeignKey('Tbstudent', models.DO_NOTHING, db_column='Stu_ID1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbquery'


class Tbresume(models.Model):
    res_id = models.AutoField(db_column='Res_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age',null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2,null=True)  # Field name made lowercase.
    res_asses = models.TextField(db_column='Res_Asses', blank=True, null=True)  # Field name made lowercase.
    res_edu = models.TextField(db_column='Res_Edu', blank=True, null=True)  # Field name made lowercase.
    res_work = models.TextField(db_column='Res_Work', blank=True, null=True)  # Field name made lowercase.
    res_proj = models.TextField(db_column='Res_Proj', blank=True, null=True)  # Field name made lowercase.
    res_extra = models.TextField(db_column='Res_extra', blank=True, null=True)  # Field name made lowercase.
    res_per = models.TextField(db_column='Res_Per', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbresume'


class Tbstudent(models.Model):
    stu_id = models.CharField(db_column='Stu_ID', primary_key=True, max_length=13)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    pov_identity = models.CharField(db_column='Pov_Identity', max_length=2, blank=True, null=True)  # Field name made lowercase.
    phonenumber_phonenumberphonenumber_phonenumber = models.CharField(db_column='PhoneNumber\r\nPhoneNumberPhoneNumber\r\nPhoneNumber', max_length=11)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', max_length=20)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_mail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=60, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='Major', max_length=60, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=6, blank=True, null=True)  # Field name made lowercase.
    res_id = models.ForeignKey(Tbresume, models.DO_NOTHING, db_column='Res_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbstudent'
