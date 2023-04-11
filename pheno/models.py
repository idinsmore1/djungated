# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tm90KLogpGt2(models.Model):
    var_id = models.CharField(db_column='VAR_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    phecode = models.CharField(db_column='PHECODE', max_length=6)  # Field name made lowercase.
    maf = models.FloatField(db_column='MAF', blank=True, null=True)  # Field name made lowercase.
    effectsize = models.FloatField(db_column='EFFECTSIZE', blank=True, null=True)  # Field name made lowercase.
    se = models.FloatField(db_column='SE', blank=True, null=True)  # Field name made lowercase.
    log10p = models.FloatField(db_column='LOG10P', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TM90K_LOGP_gt2'
        unique_together = (('var_id', 'phecode'),)


class Tm90KGwas(models.Model):
    var_id = models.CharField(db_column='VAR_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    phecode = models.CharField(db_column='PHECODE', max_length=6)  # Field name made lowercase.
    maf = models.FloatField(db_column='MAF', blank=True, null=True)  # Field name made lowercase.
    effectsize = models.FloatField(db_column='EFFECTSIZE', blank=True, null=True)  # Field name made lowercase.
    se = models.FloatField(db_column='SE', blank=True, null=True)  # Field name made lowercase.
    log10p = models.FloatField(db_column='LOG10P', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TM90K_gwas'
        unique_together = (('var_id', 'phecode'),)


class Tm90KPhenotypes(models.Model):
    phecode = models.CharField(db_column='PHECODE', primary_key=True, max_length=6)  # Field name made lowercase.
    cases = models.IntegerField()
    controls = models.IntegerField()
    phenotype = models.CharField(unique=True, max_length=119)
    phecode_exclude_range = models.CharField(max_length=34, blank=True, null=True)
    sex = models.CharField(max_length=6, blank=True, null=True)
    category_number = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'TM90K_phenotypes'


class Tm90KVariants(models.Model):
    var_id = models.CharField(db_column='VAR_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    chr = models.IntegerField(db_column='CHR', blank=True, null=True)  # Field name made lowercase.
    pos = models.IntegerField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='REF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alt = models.CharField(db_column='ALT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gene = models.CharField(db_column='GENE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    impact = models.CharField(db_column='IMPACT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    effect = models.CharField(db_column='EFFECT', max_length=57, blank=True, null=True)  # Field name made lowercase.
    hgvs_c = models.CharField(db_column='HGVS_c', max_length=16, blank=True, null=True)  # Field name made lowercase.
    hgvs_p = models.CharField(db_column='HGVS_p', max_length=17, blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='DISTANCE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TM90K_variants'

class Tm90kResult(models.Model):
    var_id = models.CharField(db_column='VAR_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    phecode = models.CharField(db_column='PHECODE', max_length=6)  # Field name made lowercase.
    maf = models.FloatField(db_column='MAF', blank=True, null=True)  # Field name made lowercase.
    effectsize = models.FloatField(db_column='EFFECTSIZE', blank=True, null=True)  # Field name made lowercase.
    se = models.FloatField(db_column='SE', blank=True, null=True)  # Field name made lowercase.
    log10p = models.FloatField(db_column='LOG10P', blank=True, null=True)  # Field name made lowercase.
    chr = models.IntegerField(db_column='CHR', blank=True, null=True)  # Field name made lowercase.
    pos = models.IntegerField(db_column='POS', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='REF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alt = models.CharField(db_column='ALT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gene = models.CharField(db_column='GENE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    impact = models.CharField(db_column='IMPACT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    effect = models.CharField(db_column='EFFECT', max_length=57, blank=True, null=True)  # Field name made lowercase.
    hgvs_c = models.CharField(db_column='HGVS_c', max_length=16, blank=True, null=True)  # Field name made lowercase.
    hgvs_p = models.CharField(db_column='HGVS_p', max_length=17, blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='DISTANCE', blank=True, null=True)  # Field name made lowercase.
    p_value = models.FloatField(blank=True, null=True)

class BariatricOutcomes(models.Model):
    chrom = models.IntegerField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=25)
    ref = models.CharField(max_length=10, blank=True, null=True)
    alt = models.CharField(max_length=10, blank=True, null=True)
    maf = models.FloatField(blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    beta = models.FloatField(blank=True, null=True)
    se = models.FloatField(blank=True, null=True)
    log10p = models.FloatField(blank=True, null=True)
    pval = models.FloatField(blank=True, null=True)
    pheno = models.CharField(max_length=25)
    genset = models.CharField(max_length=7)
    covars = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'bariatric_outcomes'
        unique_together = (('id', 'pheno', 'genset', 'covars'),)


class Exwas175KLogpGt1(models.Model):
    var_id = models.CharField(db_column='VAR_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    phecode = models.CharField(db_column='PHECODE', max_length=5)  # Field name made lowercase.
    maf = models.FloatField(db_column='MAF', blank=True, null=True)  # Field name made lowercase.
    effectsize = models.FloatField(db_column='EFFECTSIZE', blank=True, null=True)  # Field name made lowercase.
    se = models.FloatField(db_column='SE', blank=True, null=True)  # Field name made lowercase.
    log10p = models.FloatField(db_column='LOG10P', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exwas175k_logp_gt1'
        unique_together = (('var_id', 'phecode'),)


# class Fz175ImputedCanonicalVariants(models.Model):
#     id = models.CharField(max_length=85, blank=True, null=True)
#     gene = models.CharField(max_length=25, blank=True, null=True)
#     feature = models.CharField(max_length=15, blank=True, null=True)
#     feature_type = models.CharField(max_length=10, blank=True, null=True)
#     impact = models.CharField(max_length=8, blank=True, null=True)
#     consequence = models.CharField(max_length=121, blank=True, null=True)
#     rsid = models.CharField(max_length=92, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'fz175_imputed_canonical_variants'
#         unique_together = (('id', 'feature'),)
