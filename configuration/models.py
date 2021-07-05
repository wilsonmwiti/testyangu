from django.db import models

class SystemConfiguration(models.Model):
    mpesa_environment =models.CharField(verbose_name="Mpesa Environment",max_length=350,blank=True)
    mpesa_consumer_key =models.CharField(verbose_name="Mpesa Consumer Key",max_length=350,blank=True)
    mpesa_consumer_secret = models.CharField(verbose_name="Mpesa Consumer Secret",max_length=350,blank=True)
    mpesa_shortcode = models.CharField(verbose_name="Mpesa Short Code",max_length=350,blank=True)
    mpesa_express_shortcode = models.CharField(verbose_name="Mpesa Express Short Code",max_length=350,blank=True)
    mpesa_shortcode_type = models.CharField(verbose_name="Mpesa Short Code Type",max_length=350,blank=True)
    mpesa_passkey = models.CharField(verbose_name="Mpesa Passkey",max_length=350,blank=True)
    mpesa_initiator_username = models.CharField(verbose_name="Mpesa Initiator Username",max_length=350,blank=True)
    mpesa_initiator_security_credential = models.CharField(verbose_name="Mpesa Initiator Security Credential",max_length=350,blank=True)

    class Meta(object):
        db_table=u"System configuration"
class Policy(models.Model):
    name=models.CharField(max_length=70,verbose_name="Name")

    def __str__(self):
            return str(self.name)

    class Meta:
        db_table=u"Policy type"

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
    tax=models.FloatField(verbose_name=" Premium policy holder levy in %(Tax)")

    def __str__(self):
        return str(self.tax)

    class Meta:
            db_table=u"Tax rate"            

class Benefits(models.Model):
    premium=models.ForeignKey(MaximumAmountAllowed ,verbose_name="Premium", on_delete=models.CASCADE)
    benefit=models.TextField(verbose_name="Benefit")

    class Meta:
        db_table=u"Benefits(ie a premium can have multiple benefits )"
    