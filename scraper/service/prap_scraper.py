import httpx
import logging

from bs4 import BeautifulSoup
from scraper.models import Article

DEFAULT_TIMEOUT = 30.0

logger = logging.getLogger(__name__)

def get_prap_data(start_url: str) -> list[Article] :
    results: list[Article] = []
    failed_articles = []
    current_url = start_url
    client = httpx.Client(timeout=DEFAULT_TIMEOUT)

    with client:
        while current_url:
            try:
                response = client.get(current_url)

                if response.status_code != 200:
                    logger.error(f"페이지 접근 중 에러 발생: {response.status_code}")
                    break

                soup = BeautifulSoup(response.text, 'html.parser')
                datas = soup.find_all('article', class_='uicore-post')

                for data in datas:
                    identifier = 'id 추출 실패'
                    try:
                        title_tag = data.find('h4', class_='uicore-post-title')
                        # 상세보기로 이동하는 link에서 칼럼 id 추출
                        link = title_tag.find_parent('a').attrs.get('href')
                        identifier = link.split('?p=')[1]

                        author_tag = data.select_one('.uicore-post-footer a[rel="author"]')

                        item = Article(
                            identifier =  identifier,
                            author = author_tag.text.strip() if author_tag else "알 수 없음",
                            title =  title_tag.text.strip(),
                            summary = data.find('p').text.strip(),
                            image =  data.find(class_='uicore-cover-img')['style'].split('(')[1].split(')')[0],
                            posted_at =  data.select_one('.uicore-post-footer.uicore-body span:nth-of-type(3)').text.strip(),
                            url = link
                        )
                        results.append(item)
                    except Exception as e:
                        logger.error(f"데이터 파싱 에러: {e}")
                        failed_articles.append(identifier)
                        continue

                has_next = soup.select_one('a.next.uicore-page-link')

                if has_next and has_next.get('href'):
                    current_url = has_next.get('href')
                else:
                    current_url = None

            except Exception as e:
                logger.error(f"요청 중 예외 발생: {e}")
                break

        if failed_articles:
            logger.warning(f"실패한 ID 목록: {', '.join(failed_articles)}")

        return results