from django.db.models import Count, Sum
from django.utils import timezone
from novel_warehouse.views import show
from apps.novel.models import Novel, Tag
from apps.feedback.models import HistoryRelation

def homepage(request):
    # Get the start and end dates for the current month
    current_month_start = timezone.now().replace(day=1)
    current_month_end = current_month_start + timezone.timedelta(days=31)  # Assuming 31 days in a month
    context = {
        "suggest_list": [novel for novel in Novel.objects.filter(
                        historyrelation__datetime__gte=current_month_start,
                        historyrelation__datetime__lte=current_month_end
                    ).annotate(n=Count('historyrelation')).order_by('-n')[:5]],
        "rank_list": Novel.objects.all().annotate(n=Count('goodrelation')).order_by('-n')[:5],
        "save_list": Novel.objects.all().annotate(n=Count('bookcaserelation')).order_by('-n')[:5]
    }

    print(context)
    return show(request, 'home/home.html', context)
