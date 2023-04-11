import os
from django.conf import settings
from django.shortcuts import render
from math import log10
from .models import Tm90kResult, Tm90KPhenotypes
# Create your views here.
# def home_page(request):
#     render()


# Home page of the pheno
def assoc_index(request):
    return render(request, 'index.html')


def gwas(request, phecode):
    # gws = -log10(5 * 10 ** -8)
    results = Tm90kResult.objects.using('analyses').raw(f"SELECT *, POWER(10, -LOG10P) as p_value\n"
                                                        f"FROM private_dash.TM90K_LOGP_gt2 gw\n"
                                                        f"INNER JOIN private_dash.TM90K_variants\n"
                                                        f"USING(VAR_ID)\n"
                                                        f"WHERE PHECODE = '{phecode}'\n"
                                                        f"ORDER BY log10p DESC LIMIT 100"
                                                        )
    # results = Tm90KLogpGt2.objects.using('analyses').filter(phecode=phecode)
    pheno = Tm90KPhenotypes.objects.using('analyses').get(phecode=phecode)
    pheno.phecode = pheno.phecode.replace('_', '.')
    with open(os.path.join(settings.BASE_DIR, f'manhattan_plots/{phecode}.html'), 'r') as f:
        graph = f.read()
    # variants = results.objects.using('analyses').select_related('TM90K_variants')
    context = {
        'results': results,
        'phecode': phecode,
        'pheno': pheno,
        'num_vars': len(results),
        'graph': graph
        # 'variants': variants
    }
    return render(request, 'gwas.html', context)


