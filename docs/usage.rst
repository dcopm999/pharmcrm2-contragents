=====
Usage
=====

To use PharmCRM2 Contragents in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'contragents.apps.ContragentsConfig',
        ...
    )

Add PharmCRM2 Contragents's URL patterns:

.. code-block:: python

    from contragents import urls as contragents_urls


    urlpatterns = [
        ...
        url(r'^', include(contragents_urls)),
        ...
    ]
