pyenv permite instalar y administrar diferentes versiones de Python en el mismo sistema de manera fácil. Puedes cambiar entre versiones locales (por proyecto) o globales, y es compatible con entornos virtuales. La instalación de pyenv funciona en sistemas Unix y tiene opciones de instalación en Windows (a través de WSL o pyenv-win)
```
# Instalar pyenv en sistemas Unix:
curl https://pyenv.run | bash

# Agregar pyenv al PATH (si es necesario):
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
source ~/.bashrc

# Instalar una versión de Python y configurarla como predeterminada
pyenv install 3.x.x
pyenv global 3.x.x

```