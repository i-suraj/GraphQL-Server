import graphene
import books.schema
import quiz.schema


class Query(books.schema.Query, quiz.schema.Query,graphene.ObjectType):
    pass


class Mutation(quiz.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,mutation=Mutation)
