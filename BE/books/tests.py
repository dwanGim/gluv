from django.test import TestCase

from books.models import Book
from books.crawlers.crawlers import AladinCrawler


class TestAladinCrawler(TestCase):
    def setUp(self) -> None:
        # 테스트 시작 전에 호출되는 메서드
        return super().setUp()

    def tearDown(self) -> None:
        # 테스트 종료 후에 호출되는 메서드
        return super().tearDown()
    
    def test_crawl(self):
        crawler = AladinCrawler()
        result = crawler.crawl()
        # API 응답이 None이 아닌지 확인
        self.assertIsNot(result.text, None)
        # print(result.text)

    def test_crawl_and_save_to_db(self):
        crawler = AladinCrawler()
        result = crawler.crawl()

        data = result.json()
        # API 응답에 'item' 키가 존재하는지 확인
        self.assertIn('item', data)

        book_items = data['item']
        
        # 도서 정보를 반복하면서 Book 모델에 저장
        for book_data in book_items:
            title = book_data.get('title', '')
            author = book_data.get('author', '')
            publisher = book_data.get('publisher', None)
            detail_url = book_data.get('link', '')
            book_image = book_data.get('cover', '')
            published_date = book_data.get('pubDate', '')
            content = book_data.get('description', None)

            Book.objects.create(
                title=title,
                author=author,
                publisher=publisher,
                detail_url=detail_url,
                book_image=book_image,
                published_date=published_date,
                content=content
            )

        # 저장된 도서의 개수와 API 응답에서 얻은 도서의 개수가 일치하는지 확인
        self.assertEqual(Book.objects.count(), len(book_items))
        # print(result.text)
