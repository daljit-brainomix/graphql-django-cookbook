import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient

# A "Type" is an object that represents your model,
# you can tailor it to let you filter your results based on a criteria.
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        # By default DjangoObjectType will present all fields on a Model through GraphQL
        # Use fields() or exclude() - include or exclude fields.
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

    # To add and resolve any extra field not present in the model
    # extra_field = graphene.String()
    # def resolve_extra_field(self, info):
    #     return "hello!"


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            # Querying category by name
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
