import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import pytest

class Ratings:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """ Загружает данные из CSV """
        return pd.read_csv(self.file_path)

    def average_rating(self):
        """ Считает средний рейтинг для каждого movieId """
        return self.data.groupby("movieId")["rating"].mean()

    def top_movies(self, n=10):
        """ Возвращает n фильмов с самым высоким средним рейтингом """
        avg_ratings = self.average_rating()
        return avg_ratings.nlargest(n)

    def count_ratings(self):
        """ Подсчет количества оценок для каждого movieId """
        return self.data.groupby("movieId")["rating"].count()

    def rating_trend(self, movie_id):
        """ Анализ изменения рейтинга фильма со временем """
        movie_ratings = self.data[self.data["movieId"] == movie_id].copy() 
        movie_ratings["timestamp"] = pd.to_datetime(movie_ratings["timestamp"], unit="s")
        return movie_ratings.groupby(movie_ratings["timestamp"].dt.year)["rating"].mean()

    def most_active_users(self, n=10):
        """ Пользователи, которые оставили больше всего оценок """
        return self.data["userId"].value_counts().head(n)



class Tags:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """ Читает данные из CSV """
        return pd.read_csv(self.file_path)

    def most_common_tags(self, n=10):
        """ Возвращает n самых популярных тегов """
        return self.data["tag"].value_counts().head(n)

    def rare_tags(self, threshold=5):
        """ Фильтрация редких тегов (используемых менее threshold раз) """
        tag_counts = self.data["tag"].value_counts()
        return tag_counts[tag_counts <= threshold]



class Movies:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """ Читает данные из CSV """
        return pd.read_csv(self.file_path)

    def find_by_genre(self, genre):
        """ Находит все фильмы указанного жанра """
        return self.data[self.data["genres"].str.contains(genre, na=False)]

    def find_by_title(self, title):
        """ Ищет фильм по названию """
        return self.data[self.data["title"].str.contains(title, case=False, na=False)]

    def movies_per_year(self):
        """ Подсчёт количества фильмов по годам """
        self.data["year"] = self.data["title"].str.extract(r"\((\d{4})\)").astype(float)
        return self.data["year"].value_counts().sort_index()

class Links:
    def __init__(self, links_file_path):
        self.links_file_path = links_file_path
        self.links_data = self.load_links_data()

    def load_links_data(self):
        """ Читает CSV-файл """
        return pd.read_csv(self.links_file_path)

    def get_imdb_link(self, movie_id):
        """ Генерирует ссылку на IMDb по movieId """
        row = self.links_data[self.links_data["movieId"] == movie_id]
        if not row.empty:
            return f"https://www.imdb.com/title/tt{int(row['imdbId'].values[0]):07d}/"
        return None

    def get_tmdb_link(self, movie_id):
        """ Генерирует ссылку на TMDb по movieId """
        row = self.links_data[self.links_data["movieId"] == movie_id]
        if not row.empty:
            return f"https://www.themoviedb.org/movie/{int(row['tmdbId'].values[0])}"
        return None

    def has_external_links(self, movie_id):
        """ Проверка, есть ли у фильма ссылки на IMDb и TMDb """
        row = self.links_data[self.links_data["movieId"] == movie_id]
        return not row.empty and (pd.notna(row["imdbId"].values[0]) or pd.notna(row["tmdbId"].values[0]))

    def get_movie_info(self, movie_id):
        """ Получение названия и описания фильма с IMDb """
        imdb_link = self.get_imdb_link(movie_id)
        if imdb_link:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(imdb_link, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                title = soup.find('span', {'data-testid': 'hero__primary-text'})
                title_text = title.get_text(strip=True) if title else "Название не найдено."
                
                storyline = soup.find('span', {'data-testid': 'plot-xl'})
                storyline_text = storyline.get_text(strip=True) if storyline else "Описание не найдено."
                
                return {
                    "Title": title_text,
                    "Description": storyline_text
                }
            else:
                return {"Title": "Не удалось получить данные с IMDb.", "Description": ""}
        return {"Title": "IMDb ссылка не найдена.", "Description": ""}


class TestMovieLensAnalysis:

    @pytest.fixture

    def ratings(self):

        return Ratings("ml-latest-small/ratings.csv")


    @pytest.fixture

    def tags(self):

        return Tags("ml-latest-small/tags.csv")


    @pytest.fixture

    def movies(self):

        return Movies("ml-latest-small/movies.csv")


    @pytest.fixture

    def links(self):

        return Links("ml-latest-small/links.csv")


    # Тесты для класса Ratings

    def test_average_rating(self, ratings):

        assert isinstance(ratings.average_rating(), pd.Series)


    def test_top_movies(self, ratings):

        top_movies = ratings.top_movies(5)

        assert isinstance(top_movies, pd.Series)

        assert len(top_movies) <= 5


    def test_count_ratings(self, ratings):

        assert isinstance(ratings.count_ratings(), pd.Series)


    def test_rating_trend(self, ratings):

        trend = ratings.rating_trend(1)

        assert isinstance(trend, pd.Series)


    def test_most_active_users(self, ratings):

        active_users = ratings.most_active_users(5)

        assert isinstance(active_users, pd.Series)


    # Тесты для класса Tags

    def test_most_common_tags(self, tags):

        common_tags = tags.most_common_tags(5)

        assert isinstance(common_tags, pd.Series)

        assert len(common_tags) <= 5


    def test_rare_tags(self, tags):

        rare_tags = tags.rare_tags(threshold=5)

        assert isinstance(rare_tags, pd.Series)


    # Тесты для класса Movies

    def test_find_by_genre(self, movies):

        comedy_movies = movies.find_by_genre("Comedy")

        assert isinstance(comedy_movies, pd.DataFrame)

        assert not comedy_movies.empty


    def test_find_by_title(self, movies):

        toy_story = movies.find_by_title("Toy Story")

        assert isinstance(toy_story, pd.DataFrame)

        assert not toy_story.empty


    def test_movies_per_year(self, movies):

        movies_per_year = movies.movies_per_year()

        assert isinstance(movies_per_year, pd.Series)


    # Тесты для класса Links

    def test_get_imdb_link(self, links):

        imdb_link = links.get_imdb_link(1)

        assert isinstance(imdb_link, str)

        assert "imdb.com" in imdb_link


    def test_get_tmdb_link(self, links):

        tmdb_link = links.get_tmdb_link(1)

        assert isinstance(tmdb_link, str)

        assert "themoviedb.org" in tmdb_link


    def test_has_external_links(self, links):

        has_links = links.has_external_links(1)

        assert isinstance(has_links, bool)


    def test_get_movie_info(self, links):

        movie_info = links.get_movie_info(1)

        assert isinstance(movie_info, dict)

        assert "Title" in movie_info

        assert "Description" in movie_info

if __name__ == "__main__":
    ratings = Ratings("ml-latest-small/ratings.csv")
    tags = Tags("ml-latest-small/tags.csv")
    movies = Movies("ml-latest-small/movies.csv")
    links = Links("ml-latest-small/links.csv")

    print("Топ-10 фильмов по рейтингу:\n", ratings.top_movies(10))
    print("Топ-10 тегов:\n", tags.most_common_tags(10))
    print("Фильмы жанра 'Action':\n", movies.find_by_genre("Action"))

  ###CHOOSE ID (вручную)
    movie_ids = [1, 44]

    for movie_id in movie_ids:
        print(f"\nИнформация о фильме с ID {movie_id}:")
        movie_info = links.get_movie_info(movie_id)
        print(f"Название фильма: {movie_info['Title']}")
        print(f"Описание фильма: {movie_info['Description']}")