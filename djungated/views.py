from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.conf import settings

from django.db import connection
from csv import writer
import os
from .utilities import SearchText
from json import load


def home(request):
    return render(request, 'home.html')


def go(request):
    query = request.GET.get('query')
    search = SearchText(query)
    if search.is_variant:
        response = redirect(f'/variant/{search.response}', variant=search.response)
    elif search.is_phenocode or search.is_phenostring:
        response = redirect(f'/pheno/{search.response}', phenocode=search.response)
    else:
        response = redirect('/')
    print(response)
    return response


def test(request):
    return render(request, 'test.html')


def download_manhattan(request, phecode):
    # phecode = phecode.replace('.', '_')
    return FileResponse(open(os.path.join(settings.BASE_DIR, f'manhattan_plots/{phecode}.html'), 'rb'))


def download_summary(request, phecode):
    # phecode = phecode.replace('.', '_')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT VAR_ID,
                       MAF                as MAF,
                       POWER(10, -LOG10P) as p_value,
                       EFFECTSIZE         as effect_size,
                       SE                 as se,
                       v.CHR              as chr,
                       v.POS              as pos,
                       v.REF              as ref,
                       v.ALT              as alt,
                       v.GENE             as gene,
                       v.IMPACT           as impact,
                       v.EFFECT           as effect,
                       v.HGVS_c,
                       v.HGVS_p,
                       v.DISTANCE         as distance
                    FROM private_dash.TM90K_LOGP_gt2 gw
                             INNER JOIN private_dash.TM90K_variants v
                                        USING (VAR_ID)
                    WHERE PHECODE = '{phecode}'
                    ORDER BY log10p DESC LIMIT 100""")
    rows = cursor.fetchall()
    # file_name = f'{phecode}_summary.csv'
    response = HttpResponse(content_type='text/csv',
                            headers={'Content-Disposition': f'attachment; filename={phecode.replace("_", ".")}_summary.csv'})
    filewriter = writer(response)
    filewriter.writerow([i[0] for i in cursor.description])
    filewriter.writerows(rows)
    # with open(os.path.join(settings.BASE_DIR, file_name), 'w') as f:
    #     summary_stats = writer(open(file_name, 'w'))
    #     summary_stats.writerows(rows)
    return response
