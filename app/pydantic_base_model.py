from pydantic import BaseModel as PydanticBaseModel, Extra


class BaseModel(PydanticBaseModel, extra=Extra.forbid):
    """
    Configuration class + overrides to the pydantic basemodel,
    generated types then inherit from this model.
    """

    def __iter__(self):
        """
        Enables iteration over types with a __root__ key, as described in
        https://pydantic-docs.helpmanual.io/usage/models/#custom-root-types
        """
        if self.__root__:
            yield from iter(self.__root__)
            return
        yield from self.__dict__.items()

    def __getitem__(self, item):
        """
        Enables index look ups on array types with a __root__ key, as described in
        https://pydantic-docs.helpmanual.io/usage/models/#custom-root-types
        """
        if self.__root__:
            return self.__root__[item]
        return super(self.__class__, self).__getitem__(item)
