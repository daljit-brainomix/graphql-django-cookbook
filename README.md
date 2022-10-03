## Django & GraphQL / Graphene

#### Install dependencies

`pip install -r requirements.txt`

#### Run migrations

`python manage.py migrate`

#### Load test data 

`python ./manage.py loaddata ingredients`

#### Run server

`python manage.py runserver`

#### Visit GraphQL's GraphiQL - an in-browser tool for testing GraphQL queries

`http://127.0.0.1:8000/graphql`

```
# Get all ingredients - paste in this query and press the execute button at the top
query {
  allIngredients {
    id
    name
  }
}
```
##### Get relations
```
## we may want to get a specific categories and list all ingredients that are in that category.
query {
  categoryByName(name: "Dairy") {
    id
    name
    ingredients {
      id
      name
    }
  }
}

## We can also list all ingredients and get information for the category they are in:

query {
  allIngredients {
    id
    name
    category {
      id
      name
    }
  }
}
```
