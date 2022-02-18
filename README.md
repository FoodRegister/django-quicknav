
Warning, this project is no longer maintained because it is no longer part of our product, if you are still using it in some way, please consider forking it to fix the bugs as we wont maintain a project that we no longer use.

# django-quicknav

Create an Admin Interface so that you can modify your navbar, create templates that you can switch to.

To recover the template, you just need to import the navapp.models and launch the get_actual_template function with the request, you will then get an object containing a list of item that you can gather by doing template.items.all() and that you can use in your navbar. You just need to enable the navapp app in the settings and add the admin area into the quicknav/ url as in the quicknav urls and settings. If you wanna do a bit of css and create your own admin interface area, you can say in the settings what html template you want to use. You can also use the get_authorized_items, which returns the allowed data for a user

An Item contains also information like if it is allowed for normal users or only administrators.

The actual quicknav only supports for users not for anonymous people but if you wanna get the data that isn't for admins you can just do navapp.models.NavTemplate.filter(is_active=True)[0].items.filter(is_admin=False)
