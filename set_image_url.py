import os

def define_env(env):
    """
    Definir las variables y la macro para generar las URLs de las imágenes según el entorno.
    """

    # Definir las variables globales de las URLs
    env.variables.repo_url = "https://enidev911.github.io/doc_django"  # URL para GitHub Pages
    env.variables.repo_url_local = "http://127.0.0.1:5002"  # URL local para desarrollo

    # Definir la macro get_image_url
    @env.macro
    def get_image_url(path):
        # Dependiendo del entorno, devolver la URL correcta
        if os.getenv('MKDOCS_ENV') == 'local':
            return f"{env.variables.repo_url_local}/{path}"
        else:
            return f"{env.variables.repo_url}/{path}"
