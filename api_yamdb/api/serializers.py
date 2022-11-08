from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from reviews.models import (Category, Comment, Genre,
                            Review, Title, TitleGenre, User)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'name',
            'slug',
        )
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'name',
            'slug',
        )
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category',
        )
        model = Title

    def create(self, validated_data):
        category = self.initial_data.get('category')
        category_obj = get_object_or_404(Category, slug=category)

        title_obj = Title.objects.create(
            category=category_obj,
            **validated_data
        )

        genres = self.initial_data.getlist('genre')
        for genre in genres:
            genre_obj = get_object_or_404(Genre, slug=genre)
            title_genre_obj = TitleGenre(title=title_obj, genre=genre_obj)
            title_genre_obj.save()

        return title_obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        instance.description = validated_data.get(
            'description',
            instance.description
        )

        if self.initial_data.get('category'):
            category_obj = get_object_or_404(
                Category,
                slug=self.initial_data.get('category')
            )
            instance.category = category_obj

        if self.initial_data.getlist('genre'):
            TitleGenre.objects.filter(title=instance).delete()

            genres = self.initial_data.getlist('genre')
            for genre in genres:
                genre_obj = get_object_or_404(Genre, slug=genre)
                title_genre_obj = TitleGenre(title=instance, genre=genre_obj)
                title_genre_obj.save()

        instance.save()

        return instance

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score'))['score__avg']
        round_rating = round(rating, 0) if rating else None
        return round_rating


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = (
            'id',
            'title',
            'text',
            'author',
            'score',
            'pub_date',
        )
        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('title', 'author')
            )
        ]

    def validate(self, data):
        request = self.context['request']
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method == 'POST' and Review.objects.filter(
                title=title,
                author=request.user).exists():
            raise ValidationError(
                'Отзыв автора уже оставлен на данное произведение.')
        return data


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email')
        model = User

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError(
                'Нельзя использовать me в качестве имени пользователя'
            )
        return value


class RecieveTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=512)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User
