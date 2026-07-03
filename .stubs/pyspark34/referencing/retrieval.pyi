from referencing import Resource as Resource
from referencing.typing import D as D, Retrieve as Retrieve, URI as URI
from typing import Callable

def to_cached_resource(cache: Callable[[Retrieve[D]], Retrieve[D]] | None = None, loads: Callable[[_T], D] = ..., from_contents: Callable[[D], Resource[D]] = ...) -> Callable[[Callable[[URI], _T]], Retrieve[D]]:
    '''
    Create a retriever which caches its return values from a simpler callable.

    Takes a function which returns things like serialized JSON (strings) and
    returns something suitable for passing to `Registry` as a retrieve
    function.

    This decorator both reduces a small bit of boilerplate for a common case
    (deserializing JSON from strings and creating `Resource` objects from the
    result) as well as makes the probable need for caching a bit easier.
    Retrievers which otherwise do expensive operations (like hitting the
    network) might otherwise be called repeatedly.

    Examples
    --------

    .. testcode::

        from referencing import Registry
        import referencing.retrieval


        @referencing.retrieval.to_cached_resource()
        def retrieve(uri: str):
            print(f"Retrieved {uri}")

            # Normally, go get some expensive JSON from the network, a file ...
            return \'\'\'
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "foo": "bar"
                }
            \'\'\'

        one = Registry(retrieve=retrieve).get_or_retrieve("urn:example:foo")
        print(one.value.contents["foo"])

        # Retrieving the same URI again reuses the same value (and thus doesn\'t
        # print another retrieval message here)
        two = Registry(retrieve=retrieve).get_or_retrieve("urn:example:foo")
        print(two.value.contents["foo"])

    .. testoutput::

        Retrieved urn:example:foo
        bar
        bar

    '''
