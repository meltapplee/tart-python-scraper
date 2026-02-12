import logging

from django.core.management import BaseCommand
from scraper.models import Column
from scraper.service.prap_scraper import get_prap_data

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("작업 시작")
        data_list = get_prap_data('https://prap.kr/?paged=1&cat=5')

        for item in data_list:
            try:
                Column.objects.update_or_create(
                    identifier=item.identifier,
                    defaults={
                        'identifier': item.identifier,
                        'title': item.title,
                        'summary': item.summary,
                        'image': item.image,
                        'date': item.date,
                    }
                )
            except Exception as e:
                logger.error(f"DB 저장 실패 ({item.identifier}): {e}")
                continue

        logger.info("작업 종료")