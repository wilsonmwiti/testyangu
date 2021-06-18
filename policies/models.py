from django.db import models

class Policy (models.Model):
    name=models.CharField(max_length=70,verbose_name="Name")

    def __str__(self):
            return str(self.name)

    class Meta:
        db_table=u"Policy"

class PolicyFeatures(models.Model):
    name=models.ForeignKey(Policy, verbose_name=("Policy Features"), on_delete=models.CASCADE)    
    feature=models.TextField(verbose_name="Feature")
    
    class Meta:
        db_table=u"Policy Features"

class AnnualSchoolFees(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    fees=models.IntegerField(verbose_name="Fees")

    def __str__(self):
            return str(self.fees)

    class Meta:
        db_table=u"Annual school fees"

class SchoolLevel(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    school_level=models.CharField(max_length=50,verbose_name="school level")

    def __str__(self):
        return str(self.school_level)

    class Meta:
        db_table=u"School levels"

class MaximumAmountAllowed(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField(verbose_name="Amount")        
    
    def __str__(self):
        return str(self.amount)

    class Meta:
        db_table=u"Maximum premium allowed"

class PremiumRate(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    rate=models.FloatField(verbose_name="Rate in %")

    def __str__(self):
        return str(self.rate)

    class Meta:
            db_table=u"Premium rate"

class TaxRate(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    tax=models.FloatField(verbose_name="Tax in %")

    def __str__(self):
        return str(self.tax)

    class Meta:
            db_table=u"Tax rate"            

class Benefits(models.Model):
    premium=models.ForeignKey(MaximumAmountAllowed ,verbose_name="Premium", on_delete=models.CASCADE)
    benefit=models.TextField(verbose_name="Benefit")

    class Meta:
        db_table=u"Benefits(ie a premium can have multiple benefits )"