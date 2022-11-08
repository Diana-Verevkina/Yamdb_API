from reviews.models import (Category, Genre, Title, TitlesGenre, Review, User,
                            Comment)


def loading(model, row):
    if model == Category:
        columns = Category(id=row['id'], name=row['name'],
                           slug=row['slug'])
    elif model == Genre:
        columns = Genre(id=row['id'], name=row['name'],
                        slug=row['slug'])
    elif model == Title:
        columns = Title(id=row['id'], name=row['name'],
                        year=row['year'],
                        category_id=row['category'])
    elif model == TitlesGenre:
        columns = TitlesGenre(id=row['id'],
                              titles_id=row['title_id'],
                              genre_id=row['genre_id'])
    elif model == Review:
        columns = Review(
            id=row['id'], title_id=row['title_id'],
            text=row['text'], author_id=row['author'],
            score=row['score'], pub_date=row['pub_date'])
    elif model == User:
        columns = User(
            id=row['id'], username=row['username'],
            email=row['email'], role=row['role'],
            bio=row['bio'], first_name=row['first_name'],
            last_name=row['last_name'],
        )
    elif model == Comment:
        columns = Comment(
            id=row['id'], review_id=row['review_id'],
            text=row['text'], author_id=row['author'],
            pub_date=row['pub_date']
        )
    return columns
