from django.db import models


class offering(models.Model):
    date = models.DateTimeField()
    member_id = models.ForeignKey('members.member', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    mode_id = models.ForeignKey('paymenttype',on_delete=models.CASCADE)
    fund_id = models.ForeignKey('fund', on_delete=models.CASCADE)

    def memberName(self):
        return ('%s, %s' (members.member.last_name, members.member.first_name))


class paymenttype(models.Model):
    payment_mode = models.CharField(max_length=20)
    def __str__(self):
        return self.payment_mode

class fund(models.Model):
    fund = models.CharField(max_length=100)
    def __str__(self):
        return self.fund


