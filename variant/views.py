from statistics import mean
from django.db import connection
from django.shortcuts import render
from .models import PhewasModel, Tm90KVariants, PhewasData


# Create your views here.
def variant_index(request):
    return render(request, 'variant_index.html')


def phewas(request, variant):
    results = PhewasModel.objects.using('analyses').raw(
        f"SELECT *, POWER(10, -LOG10P) as p_value FROM private_dash.TM90K_gwas INNER JOIN private_dash.TM90K_phenotypes T90Kp\n"
        f"USING(PHECODE) WHERE VAR_ID ='{variant}'"
    )
    fig = PhewasData(variant, connection).phewas_plot()

    # phecodes = [str(x).replace('_', '.') for x in results.phecode.unique()]
    variant_info = Tm90KVariants.objects.using('analyses').get(var_id=variant)
    maf = round(mean([x.maf for x in results]), 5)
    results.p_value = [10 ** -x.log10p for x in results]
    context = {
        'results': results,
        'variant': variant_info,
        'maf': maf,
        'graph': fig.to_html(full_html=False, include_plotlyjs='cdn')
        # 'phecodes': phecodes
    }
    return render(request, 'phewas.html', context)
